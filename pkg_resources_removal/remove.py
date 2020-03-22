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


def parse_args(args):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "filenames", nargs="*", help="Filenames pre-commit believes are changed.",
    )

    return parser.parse_args(args)


def get_requirements_file_paths(files):
    fpaths = []

    for file_path in files:
        for file_name in REQUIREMENTS_FILENAMES:
            if file_name in file_path and os.path.exists(file_path):
                fpaths.append(file_path)

    return fpaths


def update_reqs(reqs_fpath):
    with open(reqs_fpath, "r+") as f:
        reqs = f.readlines()
        reqs_filtered = list(filter(lambda req: "pkg-resources" not in req, reqs))
        if len(reqs) != len(reqs_filtered):
            f.seek(0)
            f.writelines(reqs_filtered)
            f.truncate()
            os.system("git add %s" % reqs_fpath)
            print("Removed pkg-resources from %s" % reqs_fpath)


def main(argv=None):
    args = parse_args(argv)

    reqs_fpaths = get_requirements_file_paths(args.filenames)

    if reqs_fpaths:
        for reqs_fpath in reqs_fpaths:
            try:
                update_reqs(reqs_fpath)
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
