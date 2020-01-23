# Timecard
An automated python script to fill out my timecard. Takes an excel file containing the time in, time for lunch, and time out for each day of the week to fill into a fieldglass timecard.

[Here's a video of it in action](https://www.youtube.com/watch?v=8sRkB-cHSy0&)

To do:
  1. Also fill out distek timesheet in addition to fieldglass
  2. Simplify code
  3. Add support for vacation days dropdown on the distek website?

# Requires selenium and python
$ brew install selenium-server-standalone

# Also requires openpyxl to parse excel which requires installation of pip
# After installing python run
$ python get-pip.py
# Then this to install openpyxl
$ pip install openpyxl

# Also requires chrome web driver which can be installed with brew
$ brew cask install chromedriver

