#!/usr/bin/env python3
""" Unix ls command in Python """

import argparse
import os


class lsutil:  # pylint: disable = invalid-name
    """ """

    def __init__(self):

        self.args = argparse.Namespace()

    def ls(
        self, pathnames: list, one: bool = False, long: bool = False, classify: bool = False, capture: list = None,
        formats: str = None
    ):  # pylint: disable=invalid-name
        """ """
        if not pathnames:
            pathnames = ["."]
        for name in pathnames:
            with os.scandir(name) as it:
                for entry in it:
                    classify = ""
                    if entry.is_dir():
                        classify = "/"
                    print(f"{entry.name}{classify}")

    def parse_cli(self):
        """Parse Unix command line arguments"""
        parser = argparse.ArgumentParser(description="Process some integers.")
        parser.add_argument("files", metavar="file", nargs="*", help="Files or directories")
        parser.add_argument(
            "--sum",
            dest="accumulate",
            action="store_const",
            const=sum,
            default=max,
            help="sum the integers (default: find the max)",
        )

        self.args = parser.parse_args()
        print(self.args)

    @staticmethod
    def main_cli():
        """ """
        self = lsutil()
        self.parse_cli()
        self.ls(self.args.files)


if __name__ == "__main__":

    lsutil.main_cli()
