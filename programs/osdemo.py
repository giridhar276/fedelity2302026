"""osdemo.py

Demonstrates frequently used functions from the `os` and `shutil` modules.
Run with: python osdemo.py

This script is safe to run: it operates in a temporary demo directory
`demo_osdir` inside the current working directory and cleans up at the end.
"""
import os
import shutil
import sys
from pathlib import Path


def main():
    cwd = Path.cwd()
    print("Current working directory:", cwd)

    demo_dir = cwd / "demo_osdir"
    # create directory (os.mkdir and os.makedirs)
    if demo_dir.exists():
        shutil.rmtree(demo_dir)
    os.mkdir(demo_dir)
    print("Created directory:", demo_dir)

    # change directory (os.chdir)
    os.chdir(demo_dir)
    print("Changed directory to:", Path.cwd())

    # create nested directories with os.makedirs
    nested = demo_dir / "a" / "b" / "c"
    os.makedirs(nested)
    print("Created nested directories:", nested)

    # list directory contents (os.listdir)
    print("Contents of demo_dir:", os.listdir(demo_dir))

    # file operations: open, write, read
    file1 = nested / "hello.txt"
    with open(file1, "w", encoding="utf-8") as f:
        f.write("Hello from osdemo!\n")
    print("Wrote file:", file1)

    # os.path utilities
    print("Is file1 a file?", os.path.isfile(file1))
    print("Is 'a' a directory?", os.path.isdir(demo_dir / "a"))
    print("Absolute path of file1:", os.path.abspath(file1))

    # join and split
    joined = os.path.join(str(nested), "hello.txt")
    head, tail = os.path.split(joined)
    print("Joined path:", joined)
    print("Head:", head, "Tail:", tail)

    # getsize
    print("Size of file1 (bytes):", os.path.getsize(file1))

    # walk the tree (os.walk)
    print("\nWalking demo_dir:")
    for root, dirs, files in os.walk(demo_dir):
        print("ROOT:", root)
        print(" DIRS:", dirs)
        print(" FILES:", files)

    # environment variables (os.environ)
    print("\nSome environment vars:")
    print("PATH exists:", "PATH" in os.environ)
    print("PYTHONPATH:", os.environ.get("PYTHONPATH"))

    # create a copy of file (shutil.copy)
    copied = demo_dir / "copied_hello.txt"
    shutil.copy(file1, copied)
    print("Copied file to:", copied)

    # rename/move (os.rename)
    renamed = demo_dir / "hello_renamed.txt"
    os.rename(copied, renamed)
    print("Renamed moved file to:", renamed)

    # permissions (os.stat)
    print("File stat for hello.txt:", os.stat(file1))

    # remove a file (os.remove / os.unlink)
    os.remove(renamed)
    print("Removed file:", renamed)

    # remove directories (os.rmdir requires empty dir)
    # remove nested directories bottom-up
    os.remove(file1)
    os.removedirs(nested)  # removes c, b, a if empty
    print("Removed nested directories and file1")

    # change back to original cwd and remove demo dir tree
    os.chdir(cwd)
    shutil.rmtree(demo_dir)
    print("Cleaned up demo directory. Back to:", Path.cwd())


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("An error occurred:", file=sys.stderr)
        raise


