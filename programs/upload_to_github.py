"""Upload all files from current folder to an existing GitHub repo.

Usage:
  - Set environment variable GITHUB_TOKEN with a personal access token (needs `repo` scope for private repos).
  - Run:
      python upload_to_github.py --owner OWNER --repo REPO --branch main

This script performs a safe upload using the GitHub Contents API. It supports
dry-run mode to preview actions before making requests.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path
from typing import Optional

import requests


def parse_args():
    p = argparse.ArgumentParser(description="Upload files from current folder to GitHub repo")
    p.add_argument("--owner", required=True, help="GitHub repo owner/user")
    p.add_argument("--repo", required=True, help="GitHub repository name")
    p.add_argument("--branch", default="main", help="Target branch (default: main)")
    p.add_argument("--token", help="GitHub token or set GITHUB_TOKEN env var")
    p.add_argument("--message", default="Upload files from local folder", help="Commit message")
    p.add_argument("--prefix", default="", help="Upload files under this path in repo")
    p.add_argument("--dry-run", action="store_true", help="Show actions without sending requests")
    p.add_argument("--skip", nargs="*", default=[".git", "__pycache__"], help="Paths to skip")
    return p.parse_args()


def gh_request(session: requests.Session, method: str, url: str, **kwargs):
    resp = session.request(method, url, **kwargs)
    if resp.status_code in (200, 201):
        return resp
    if resp.status_code == 404:
        return resp
    raise RuntimeError(f"GitHub API error {resp.status_code}: {resp.text}")


def upload_file(session: requests.Session, owner: str, repo: str, path_in_repo: str, content_bytes: bytes, message: str, branch: str, dry_run: bool, sha: Optional[str] = None):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path_in_repo}"
    data = {
        "message": message,
        "content": base64.b64encode(content_bytes).decode("ascii"),
        "branch": branch,
    }
    if sha:
        data["sha"] = sha

    if dry_run:
        print(f"DRY RUN: would PUT {path_in_repo} (sha={sha})")
        return None

    resp = gh_request(session, "PUT", url, json=data)
    return resp.json()


def get_file_sha(session: requests.Session, owner: str, repo: str, path_in_repo: str, branch: str) -> Optional[str]:
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path_in_repo}?ref={branch}"
    resp = session.get(url)
    if resp.status_code == 200:
        return resp.json().get("sha")
    if resp.status_code == 404:
        return None
    resp.raise_for_status()


def main():
    args = parse_args()
    token = args.token or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: set GITHUB_TOKEN environment variable or pass --token")
        return 1

    session = requests.Session()
    session.headers.update({"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"})

    root = Path.cwd()
    files_to_upload = []
    skip_set = set(args.skip)

    for p in root.rglob("*"):
        rel = p.relative_to(root)
        parts = rel.parts
        if any(part in skip_set for part in parts):
            continue
        if p.is_file():
            # skip this script itself
            if p.name == Path(__file__).name:
                continue
            files_to_upload.append(rel)

    if not files_to_upload:
        print("No files found to upload.")
        return 0

    print(f"Found {len(files_to_upload)} files to upload (dry-run={args.dry_run})")

    for rel in sorted(files_to_upload):
        local_path = root / rel
        repo_path = Path(args.prefix) / rel
        repo_path_str = str(repo_path).replace("\\", "/")

        # Read file bytes
        content = local_path.read_bytes()
        # Check existing SHA
        sha = None
        try:
            sha = get_file_sha(session, args.owner, args.repo, repo_path_str, args.branch)
        except Exception as e:
            print(f"Warning checking existing file {repo_path_str}: {e}")

        print(f"Uploading {rel} -> {repo_path_str} (exists sha={sha})")
        res = upload_file(session, args.owner, args.repo, repo_path_str, content, args.message, args.branch, args.dry_run, sha=sha)
        if res is not None:
            print("OK:", res.get("commit", {}).get("sha"))

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
