#! /usr/bin/env python3

import argparse
from datetime import datetime
import date_directory


def create_parser():
    arg_parser = argparse.ArgumentParser(
        description='Program to create nested directory based on input. All '
                    'positional arguments are mandatory.',
        usage='__main__.py [-h/--help] start_date end_date '
              '[-o/--optional {yes,no}]'
    )

    # add positional arguments to the parser object from command line
    arg_parser.add_argument('start_date',
                            type=date_directory.valid_date,
                            help='provide start date in the MM-DD-YYYY format',
                            default=None,
                            )
    arg_parser.add_argument('end_date',
                            type=date_directory.valid_date,
                            help='provide end date in the MM-DD-YYYY format',
                            default=None,
                            )
    # add optional argument to the parser object from command line
    arg_parser.add_argument('-o',
                            '--option',
                            help='Do you want to create a '
                            'make file inside each directory? then say yes!',
                            action='store',
                            dest='option',
                            choices=['yes', 'no'],
                            default='no'
                            )
    return arg_parser


def main():
    print('\n########### welcome to the project: date-to-directory ##########')
    parser = create_parser()
    # parse arguments and store as a Namespace object within args
    args = parser.parse_args()
    # print(args)

    if date_directory.check_valid_start_end(args.start_date, args.end_date):
            date_directory.parse_year_month_day(args.start_date, args.end_date,
                                                args.option)
    else:
        print("Please provide a start date older to end date")


if __name__ == '__main__':
    main()
