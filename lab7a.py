#!/usr/bin/env python3
# Student ID: 119911220

class Time:
   """Simple object type for time of the day.
      data attributes: hour, minute, second
   """
   def __init__(self, hour=12, minute=0, second=0):
       """Constructor for time object"""
       self.hour = hour
       self.minute = minute
       self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum = Time(t1.hour + t2.hour, t1.minute + t2.minute, t1.second + t2.second)

    # Handle carry for seconds to minutes
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    # Handle carry for minutes to hours
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

def valid_time(t):
    """Check for the validity of the time object attributes"""
    if any([t.hour < 0, t.hour >= 24, t.minute < 0, t.minute >= 60, t.second < 0, t.second >= 60]):
        return False
    return True

