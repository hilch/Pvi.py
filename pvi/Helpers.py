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

import re
import logging
import inspect

__patternParameterPairs = re.compile(r"\s*([A-Za-z]{2}=\S*)\s*")
__logger = logging.getLogger("pvipy")

def dictFromParameterPairString( s : str ) -> dict:
    '''
    converts a string with object descriptor parameters to a dict

    Args:
        s: string with pairs of parameters, e.g. 'CN=variable EV=eds'

    Returns:
        dict
    '''
    result = dict()
    matches = __patternParameterPairs.findall(s)
    if matches:
        for m in matches: 
            token = m.split("=")
            result.update( {str.upper(token[0]):token[1]})      
    return result


def debuglog(message):
    stack = inspect.stack()
    the_class = stack[1][0].f_locals["self"].__class__.__name__
    the_method = stack[1][0].f_code.co_name
    __logger.debug( f' {the_class}.{the_method} -> {message}')

