import touch
import os
from datetime import datetime
import argparse


# verify date is in the format YYYY-MM-DD
def valid_date(dates):
    try:
        return datetime.strptime(dates, "%Y-%m-%d").date()
    except ValueError:
        msg = "Not a valid format for date: '{0}'.".format(dates)
        raise argparse.ArgumentTypeError(msg)


# verify end date is same as or greater than start date
def check_valid_start_end(start, end):
    if start <= end:
        return True
    else:
        return False


# check leap year
def check_leapyear(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


# create directory based on user input. If user opts for .make file, then
# create it within each of the folders created.
def create_directory(year, month, day, option):
    if option == 'yes':
        file = ".make.txt"
        os.makedirs("{}/{}/{}".format(year, month, day), exist_ok=True)
        touch.touch(os.path.join(str(year), file))
        touch.touch(os.path.join(str(year), str(month), file))
        touch.touch(os.path.join(str(year), str(month), str(day), file))
    else:
        os.makedirs("{}/{}/{}".format(year, month, day), exist_ok=True)


# parse the year, month and day from given start and end dates. Also convert
# the MM to MONTH (i:e 01 to January)
def parse_year_month_day(start, end, option):
    start_year, start_month, start_day = str(start).split("-")
    end_year, end_month, end_day = str(end).split("-")
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    max_dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # set the year, month and day counters to the start year, month and day
    year_counter = int(start_year)
    month_counter = int(start_month)
    day_counter = int(start_day)

    if start == end:
        create_directory(year_counter, months[month_counter - 1], day_counter)
        return

    # continue the loop until year counter is not greater or with in a year
    # month counter is not greater
    while year_counter <= int(end_year) and month_counter <= int(end_month):
        # increase the day counter until it is not the end day
        if month_counter == int(end_month) and day_counter < int(end_day):
            create_directory(year_counter, months[month_counter - 1],
                             day_counter, option)
            day_counter += 1
        # when day counter is same as end date, create directory and exit.
        elif month_counter == int(end_month) and day_counter == int(end_day):
            create_directory(year_counter, months[month_counter - 1],
                             day_counter, option)
            print('############ Congratulations!! '
                  'Your directory structure is ready. ###########')
            return
        # continue the loop until the exit criteria is met
        else:
            create_directory(year_counter, months[month_counter - 1],
                             day_counter, option)
            day_counter += 1
            pass

        # create 29th day directory when it is a leap year
        if day_counter > max_dates[month_counter - 1]:
            if month_counter == 2 and check_leapyear(year_counter):
                create_directory(year_counter, months[month_counter - 1],
                                 day_counter, option)
            # increase month counter and set day to start of the month
            month_counter += 1
            day_counter = 1

        # increase year counter and set month to start of the year
        if month_counter > 12:
            year_counter += 1
            month_counter = 1
    print('######### Congratulations!! Your directory structure is ready.')
    return
