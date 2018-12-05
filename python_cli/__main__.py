#! /usr/bin/python3

import argparse
from datetime import datetime
import date_directory


def main():
    print('############ welcome to the project: date-to-directory ###########')
    # print('To know how to execute the program type: '
    #     'python3 __main__.py -h/--help\n')

    # create an object of the ArgumentParser class
    parser = argparse.ArgumentParser(
        description='Program to create nested directory based on input. All '
                    'positional arguments are mandatory.',
        usage='__main__.py [-h/--help] start_date end_date '
              '[-o/--optional {yes,no}]'
    )
    # add positional arguments to the parser object from command line
    parser.add_argument('start_date',
                        type=date_directory.valid_date,
                        help='provide start date in the YYYY-MM-DD format',
                        default=None,
                        )
    parser.add_argument('end_date',
                        type=date_directory.valid_date,
                        help='provide end date in the YYYY-MM-DD format',
                        default=None,
                        )
    # add optional argument to the parser object from command line
    parser.add_argument('-o',
                        '--option',
                        help='Do you want to create a '
                             'make file inside each directory? then say yes!',
                        action='store',
                        dest='option',
                        choices=['yes', 'no'],
                        default='no'
                       )
    # parse arguments and store as a Namespace object within args
    args = parser.parse_args()

    start = datetime.strptime(str(args.start_date), '%Y-%m-%d').date()
    end = datetime.strptime(str(args.end_date), '%Y-%m-%d').date()

    # print(args.option)
    # print(end)

    if date_directory.check_valid_start_end(start, end):
            date_directory.parse_year_month_day(start, end, args.option)
    else:
        print("Please provide a start date older to end date")


if __name__ == '__main__':
    main()