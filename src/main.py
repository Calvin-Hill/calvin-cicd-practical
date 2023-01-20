""" main executable for project """

# Includes and Imports
from feature_practical import get_time

# Variables
name = "Calvin"
timezone = +2

# Functions

if __name__ == '__main__':
    _, _, time_response = get_time(name, timezone)
    print(time_response)