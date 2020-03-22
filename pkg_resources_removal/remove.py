#!/usr/bin/env python

from __future__ import print_function

import argparse
import os
import subprocess
import sys


REQUIREMENTS_FILENAMES = {
    "requirements.txt",
    "requirements-test.txt",
    "requirements-dev.txt",
}


def get_requirements_file_path(files):
    for file_path in files:
        for file_name in REQUIREMENTS_FILENAMES:
            if file_name in file_path and os.path.exists(file_path):
                return file_path


def main(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "filenames", nargs="*", help="Filenames pre-commit believes are changed.",
    )

    args = parser.parse_args(argv)

    reqs_fname = get_requirements_file_path(args.filenames)

    if reqs_fname:
        try:
            with open(reqs_fname, "r+") as f:
                reqs = f.readlines()
                reqs_filtered = list(
                    filter(lambda req: "pkg-resources" not in req, reqs)
                )
                if len(reqs) != len(reqs_filtered):
                    f.seek(0)
                    f.writelines(reqs_filtered)
                    f.truncate()
                    os.system("git add %s" % reqs_fname)
                    print("Removed pkg-resources from %s" % reqs_fname)
        except IOError:
            return 1

    return 0


if __name__ == "__main__":
    argv = None

    if len(sys.argv) == 1:
        proc = subprocess.Popen(
            ["git", "diff", "--cached", "--name-only"], stdout=subprocess.PIPE
        )
        stdout, _ = proc.communicate()
        argv = stdout.decode().strip().split("\n")

    sys.exit(main(argv))
