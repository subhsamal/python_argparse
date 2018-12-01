# The goal of this program is to create nested directory as per the\
# input provided by the user.
# Input is in the form of startdate and enddate
# Format of the date is YYYY-MM-DD

import argparse
from datetime import datetime
import os


def valid_date(dates):
    try:
        return datetime.strptime(dates, "%Y-%m-%d").date()
    except ValueError:
        msg = "Not a valid format for date: '{0}'.".format(dates)
        raise argparse.ArgumentTypeError(msg)


def check_valid_startdate_enddate(start, end):
    if start <= end:
        return True
    else:
        return False


def create_directory(start, end):
    delta = end-start
    print (delta)

    start_year, start_month, start_day = str(start).split("-")
    end_year, end_month, end_day = str(end).split("-")

    for year in range(int(start_year), int(end_year)+1):
        os.makedirs("{}".format(year), exist_ok=True)


#     start_year, start_month, start_day = start.split("-")
#     end_year, end_month, end_day = end.split("-")
#
#     year_directory = []
#
#     path = 'Users/ssamal/Documents/Practice/Python/' \
#            'python_virtual_environment/python_argparse'
#
#     for year in range(int(start_year), int(end_year)+1):
#         for month in range(int(start_month), int(end_month)+1):


def main():
    parser = argparse.ArgumentParser(
        description='Program to create nested directory based on input'
    )

    parser.add_argument('start_date',
                        type=valid_date,
                        help='provide start date in the YYYY-MM-DD format',
                        default=None,
                        )
    parser.add_argument('end_date',
                        type=valid_date,
                        help='provide end date in the YYYY-MM-DD format',
                        default=None,
                        )
    args = parser.parse_args()

    start = datetime.strptime(str(args.start_date), '%Y-%m-%d').date()
    end = datetime.strptime(str(args.end_date), '%Y-%m-%d').date()

    print(start,"\n",end)

    if check_valid_startdate_enddate(start, end):
         create_directory(start, end)
    else:
        print("Please provide a start date older to end date")


if __name__ == '__main__':
    main()
