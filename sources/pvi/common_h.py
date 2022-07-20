#
# Pvi.py
# Python connector for B&R Pvi (process visualization interface)
#
#  https://github.com/hilch/Pvi.py
# Permission is hereby granted, free of charge, 
# to any person obtaining a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from ctypes import *

# C/C++ struct tm
# struct tm
# {
#     int tm_sec; // seconds after the minute - [0,59]
#     int tm_min; // minutes after the hour - [0,59]
#     int tm_hour; // hours since midnight - [0,23]
#     int tm_mday; // day of the month - [1,31]
#     int tm_mon; // months since January - [0,11]
#     int tm_year; // years since 1900
#     int tm_wday; // days since Sunday - [0,6]
#     int tm_yday; // days since January 1 - [0,365]
#     int tm_isdst; // daylight savings time flag
# };


class struct_tm(Structure):
    _fields_ = [
        ("tm_sec", c_int32),
        ("tm_min", c_int32),
        ("tm_hour", c_int32),
        ("tm_mday", c_int32),
        ("tm_mon", c_int32),
        ("tm_year", c_int32),
        ("tm_wday", c_int32),
        ("tm_yday", c_int32),                                                
        ("tm_isdst", c_int32)
    ]
 