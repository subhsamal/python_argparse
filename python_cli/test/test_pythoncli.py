from date_directory import *
import unittest


class pythoncliTest(unittest.TestCase):

    def test_valid_date(self):
        date = '12-10-2011'
        self.assertTrue(valid_date(date), msg='date is valid')

    def test_not_valid_date(self):
        date = '20-12-2018'
        try:
            valid_date(date)
            assert False
        except Exception:
            assert True

    def test_check_valid_start_end(self):
        start = datetime.strptime('11-20-2018', '%m-%d-%Y').date()
        end = datetime.strptime('11-30-2018', '%m-%d-%Y').date()
        self.assertTrue(check_valid_start_end(start, end), msg='valid start '
                                                               'and end date')

    def test_not_valid_start_end(self):
        start = datetime.strptime('10-12-2017', '%m-%d-%Y').date()
        end = datetime.strptime('10-11-2017', '%m-%d-%Y').date()
        self.assertFalse(check_valid_start_end(start, end))

    def test_leap_year(self):
        year = int(input('enter year to check leapyear: '))
        if check_leapyear(year):
            assert True
        else:
            assert False


if __name__ == '__main__':
    unittest.main()