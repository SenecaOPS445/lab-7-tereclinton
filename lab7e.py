#!/usr/bin/env python3
# Student ID: 119911220

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, __str__, __repr__,
                            time_to_sec, format_time,
                            change_time, sum_times
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a string representation for the object self"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a formal string representation using '.' instead of ':'"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        return self.__str__()

    # Include other methods such as change_time, sum_times, etc.

