# The goal of this program is to create nested directory as per the\
# input provided by the user.
# Input is in the form of startdate and enddate
# Format of the date is YYYY-MM-DD

import argparse
from datetime import datetime
import os
import touch


def valid_date(dates):
    try:
        return datetime.strptime(dates, "%Y-%m-%d").date()
    except ValueError:
        msg = "Not a valid format for date: '{0}'.".format(dates)
        raise argparse.ArgumentTypeError(msg)


def check_valid_start_end(start, end):
    if start <= end:
        return True
    else:
        return False


def check_leapyear(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def create_directory(year, month, day, option):
    if option == 'yes':
        file = ".make.txt"
        os.makedirs("{}/{}/{}".format(year, month, day), exist_ok=True)
        touch.touch(os.path.join(str(year), file))
        touch.touch(os.path.join(str(year), str(month), file))
        touch.touch(os.path.join(str(year), str(month), str(day), file))
    else:
        os.makedirs("{}/{}/{}".format(year, month, day), exist_ok=True)


def parse_year_month_day(start, end, option):
    start_year, start_month, start_day = str(start).split("-")
    end_year, end_month, end_day = str(end).split("-")
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    maxDates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year_counter = int(start_year)
    month_counter = int(start_month)
    day_counter = int(start_day)

    if start == end:
        create_directory(year_counter, months[month_counter-1], day_counter)
        return

    while year_counter <= int(end_year) and month_counter <= int(end_month):

        if month_counter == int(end_month) and day_counter < int(end_day):
            create_directory(year_counter, months[month_counter-1],day_counter, option)
            day_counter += 1
        elif month_counter == int(end_month) and day_counter == int(end_day):
            create_directory(year_counter, months[month_counter - 1],
                             day_counter, option)
            return
        else:
            create_directory(year_counter, months[month_counter-1],day_counter, option)
            day_counter += 1

        if day_counter > maxDates[month_counter-1]:
            if month_counter == 2 and check_leapyear(year_counter):
                create_directory(year_counter, months[month_counter-1],
                                 day_counter, option)

            month_counter += 1
            day_counter = 1

        if month_counter > 12:
            year_counter += 1
            month_counter = 1


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

    parser.add_argument('-o',
                        '--option',
                        help='Do you want to create a '
                             'make file inside each directory? then say yes!',
                        action='store',
                        # type="yes",
                        dest='option',
                        choices=['yes', 'no'],
                        )
    args = parser.parse_args()

    start = datetime.strptime(str(args.start_date), '%Y-%m-%d').date()
    end = datetime.strptime(str(args.end_date), '%Y-%m-%d').date()
    # if args.option:

    print(start)
    print(end)

    if check_valid_start_end(start, end):
        parse_year_month_day(start, end, args.option)
    else:
        print("Please provide a start date older to end date")


if __name__ == '__main__':
    main()
