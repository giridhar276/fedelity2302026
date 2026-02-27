"""requests3.py

Fetch users from the GitHub API (https://api.github.com/users) with optional
authentication. Supports pagination and safe defaults to avoid downloading the
entire GitHub user database accidentally.

Usage examples:
  python requests3.py               # fetch first 5 pages (default)
  python requests3.py --token TOKEN  # use provided token for authenticated requests
  python requests3.py --all         # attempt to fetch all pages (use with caution)

Authentication:
  - Set environment variable `GITHUB_TOKEN` or pass `--token`.

By default the script fetches `per_page` users per page and up to `max_pages`.
Set `--all` to follow pagination until no more pages (may be very large).
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Optional

import requests


def parse_args() -> argparse.Namespace:
	p = argparse.ArgumentParser(description="Fetch GitHub users (with optional auth)")
	p.add_argument("--token", help="GitHub personal access token (or set GITHUB_TOKEN env)")
	p.add_argument("--per-page", type=int, default=100, help="Users per page (max 100)")
	p.add_argument("--max-pages", type=int, default=5, help="Max pages to fetch (default 5)")
	p.add_argument("--all", action="store_true", help="Follow pagination until exhausted (dangerous)")
	p.add_argument("--output", help="Write usernames to a file instead of stdout")
	return p.parse_args()


def get_next_link(link_header: Optional[str]) -> Optional[str]:
	"""Parse Link header and return URL for rel="next" if present."""
	if not link_header:
		return None
	parts = requests.utils.parse_header_links(link_header.rstrip("\"\'"))
	for part in parts:
		if part.get("rel") == "next":
			return part.get("url")
	return None


def fetch_github_users(token: Optional[str], per_page: int = 100, max_pages: int = 5, fetch_all: bool = False):
	session = requests.Session()
	headers = {"Accept": "application/vnd.github.v3+json"}
	if token:
		headers["Authorization"] = f"token {token}"
	session.headers.update(headers)

	url = "https://api.github.com/users"
	params = {"per_page": per_page}
	page_count = 0

	while url:
		if not fetch_all and page_count >= max_pages:
			break
		try:
			resp = session.get(url, params=params, timeout=20)
		except requests.RequestException as e:
			print("Request failed:", e, file=sys.stderr)
			return

		if resp.status_code != 200:
			print(f"GitHub API returned status {resp.status_code}: {resp.text}", file=sys.stderr)
			return

		users = resp.json()
		if not isinstance(users, list):
			print("Unexpected response format", file=sys.stderr)
			return

		for u in users:
			yield u

		link = resp.headers.get("Link")
		next_url = get_next_link(link)
		url = next_url
		params = {}  # after first request, follow next_url which already has params
		page_count += 1


def main() -> int:
	args = parse_args()
	token = args.token or os.environ.get("GITHUB_TOKEN")
	if not token:
		print("Warning: no token provided — unauthenticated requests are rate-limited.")

	out = None
	if args.output:
		out = open(args.output, "w", encoding="utf-8")

	try:
		count = 0
		for user in fetch_github_users(token=token, per_page=args.per_page, max_pages=args.max_pages, fetch_all=args.all):
			login = user.get("login")
			user_id = user.get("id")
			html_url = user.get("html_url")
			line = f"{login}\t{user_id}\t{html_url}"
			# Write to output or stdout
			if out:
				out.write(line + "\n")
			else:
				print(line)
			count += 1

		print(f"Fetched {count} users.")
		return 0
	finally:
		if out:
			out.close()


if __name__ == "__main__":
	raise SystemExit(main())

