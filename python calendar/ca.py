# import the module that we need which is calendar module
import calendar
'''
author:@jayson
twitter:@dev_jayson
'''
# import textcalendar
from calendar import TextCalendar
# Using textcalendar which is a method of calendar module
cal = TextCalendar()
# parse in the year and month
year = cal.formatyear(2022,  m=3)
# print the result
print('\n', year) 