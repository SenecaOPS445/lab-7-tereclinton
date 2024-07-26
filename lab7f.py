#!/usr/bin/env python3
# Student ID: 119911220

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
       Function attributes: __init__, __str__, __repr__,
                            time_to_sec, format_time,
                            change_time, sum_times, __add__
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

    def __add__(self, other):
        """Overloads the '+' operator to add two Time objects."""
        total_seconds = self.time_to_sec() + other.time_to_sec()
        return sec_to_time(total_seconds)

    def time_to_sec(self):
        """Converts the current Time object to total seconds."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def format_time(self):
        """Use the __str__ method to format time."""
        return self.__str__()

    def change_time(self, seconds):
        """Modify time based on a delta in seconds."""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

def sec_to_time(seconds):
    """Convert a given number of seconds back to a Time object."""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return Time(hours, minutes, seconds)

