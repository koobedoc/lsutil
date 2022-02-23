#!/usr/bin/env python3
""" Unix ls command in Python """

import stat
import argparse
import os


class lsutil:  # pylint: disable = invalid-name
    """Unix ls command in Python"""

    def __init__(self):
        self.args = argparse.Namespace(verbose=0)

    def ls(
        self,
        pathnames: list,
        one: bool = False,
        longs: bool = False,
        classify: bool = False,
        capture: list = None,
        formats: str = None,
    ):  # pylint: disable=invalid-name, too-many-arguments
        """Unix ls command clone"""
        _ = self
        if not pathnames:
            pathnames = ["."]

        if formats or longs:
            one = True

        if not formats:
            formats = "{entry.name}{classify}"
            if longs:
                formats = "{filemode} " + formats

        for name in pathnames:
            with os.scandir(name) as it:
                for entry in it:
                    classify = ""
                    if entry.is_dir():
                        classify = "/"

                    print(
                        formats.format(classify=classify, filemode=stat.filemode(entry.stat().st_mode), entry=entry),
                        end="",
                    )
                    if one:
                        print()
        if not one:
            print()

    def parse_cli(self):
        """Parse Unix command line arguments"""
        parser = argparse.ArgumentParser(description="Process some integers.")
        parser.add_argument("files", metavar="file", nargs="*", help="Files or directories")
        parser.add_argument("-l", "--longs", action="store_true", help="use a long listing format")
        parser.add_argument("-v", "--verbose", action="count", default=0, help="increase verbosity for debugging")
        parser.add_argument("-1", "--one", action="count", default=0, help="increase verbosity for debugging")
        parser.add_argument("--formats", type=str, help="Format string")

        self.args = parser.parse_args()
        if self.args.verbose:
            # print(f"lsutil ver. {__init__.__version__}, {__init__.__built__}")
            print(self.args)

    @staticmethod
    def main_cli():
        """Unix command line interface"""
        self = lsutil()
        self.parse_cli()
        self.ls(self.args.files, longs=self.args.longs, one=self.args.one, formats=self.args.formats)


if __name__ == "__main__":

    lsutil.main_cli()
