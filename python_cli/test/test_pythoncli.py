#!/usr/bin/env python3

from python_cli.date_directory import *
import unittest


class pythoncliTest(unittest.TestCase):

    # test case should pass sine input is valid
    def test_valid_date(self):
        day = '12-10-2011'
        self.assertTrue(valid_date(day), msg='date is not valid')

    # test case should raise exception since input is not valid
    def test_not_valid_date(self):
        day = '22-12-2018'
        with self.assertRaises(Exception):
            valid_date(day)

    def test_check_valid_start_end(self):
        start = datetime.strptime('11-20-2018', '%m-%d-%Y').date()
        end = datetime.strptime('11-30-2018', '%m-%d-%Y').date()
        self.assertTrue(check_valid_start_end(start, end), msg='not valid '
                                                               'start and '
                                                               'end date')

    def test_not_valid_start_end(self):
        start = datetime.strptime('10-12-2017', '%m-%d-%Y').date()
        end = datetime.strptime('10-10-2017', '%m-%d-%Y').date()
        self.assertFalse(check_valid_start_end(start, end), msg='this is a '
                                                                'valid start'
                                                                'and end date')

    def test_leap_year(self):
        year = int(input('enter year to check leapyear: '))
        self.assertTrue(check_leapyear(year), msg='This is not a leap year')


if __name__ == '__main__':
    unittest.main()