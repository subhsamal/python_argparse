######## About the Project #########

This project contains program to create directories based on input dates.
The program takes start and end dates as command line arguments and creates a
directory structure for each year, month and day in that range.
It also creates an empty .make file if user opts for this.

################# What is Argparse Module ##########

Argparse module is used to parse command line arguments required to run a
python program.
It can generate output based on the inputs provided. It is very helpful to
build interactive CLI apps in Python.

######## How to create a Virtual Environment #########

python3 -m venv <Name of the virtual environment>
Then activate it using the command:
source <Name of the virtual environment>/bin/activate

######### How to create a package ############

python_cli directory is a package. Any directory can be a package with an
__init__.py in it. Benefit of a package is code movability. A package can be
installed at any location, hence allows access to the modules even if
one is not within the local directory.

A package can have multiple subpackages and directories.

########## How to install a package ##########

A package can be install by running the following command within the directory
containing the package: pip3 install -e .

In this case I have created a shell script named install.sh containing the above
command. Install the package with ./install.sh (check for permission)

To uninstall the package, use command:
pip uninstall <package name>

########## What is setup.py #################

setup.py contains information about a package, such as package name, author,
license, version and most importantly entry point.

##### To use the package as an API ######
python3
from datetime import datetime
from python_cli import date_directory as dd
start = 'MM-DD-YYYY'
end = 'MM-DD-YYYY'
dd.parse_year_month_day(datetime.strptime(start, '%m-%d-%Y').date(),
datetime.strptime(end, '%m-%d-%Y').date(), 'yes')

dd.check_leapyear('given year')

################ Python type hinting ################
Reference: https://stackoverflow.com/questions/15300550/
python-return-return-none-and-no-return-at-all/15300733

########### How unittest.main() works ###########
Reference: http://elbenshira.com/blog/behind-pythons-unittest-main/
To run the unittest module from command line:
python3 -m unittest test/test_pythoncli.py