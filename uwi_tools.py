# MIT License

# Copyright (c) 2022 DeflateAwning

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import re, sys
from loguru import logger

logger.add(sys.stderr, format="{time} {level} {message}", filter=__file__, level="INFO")

uwi_regex = re.compile(r"(((1.{2})\s*[/_\- ]\s*)?(\d+)[\-_](\d+)[\-_](\d+)[\-_]\s*(\d+)\s*[\- ]?\s*([WE])\s*(\d)\s*M?\s*(/(\d+))?)", flags=re.IGNORECASE)

class WellLoc:
    """ Represents a well location. """
    def __init__(self, prefix, lsd, section, twp, rge, ew, mer, event):
        if prefix is not None:
            self.prefix = str(prefix)

            if len(self.prefix) == 2:
                self.prefix = '1' + self.prefix
        else:
            self.prefix = None

        self.lsd = int(lsd)
        self.section = int(section)
        self.twp = int(twp)
        self.rge = int(rge)
        self.ew = str(ew) # east or west
        self.mer = int(mer)
        
        if event is not None:
            self.event = int(event)
        else:
            self.event = None

    @classmethod
    def from_string(self_class, string): # self_class === WellLoc
        """
        Example: well_loc = WellLoc.from_string('100/12-14-019-15W7/01')
        """
        groups = uwi_regex.search(string).groups()
        return self_class(groups[2], groups[3], groups[4], groups[5], groups[6], groups[7], groups[8], groups[10])


    def get_pretty_str_main(self) -> str:
        """ Gets a string like 04-07-050-5W5, without the prefix nor the event. """
        return f"{str(self.lsd).zfill(2)}-{str(self.section).zfill(2)}-{str(self.twp).zfill(3)}-{str(self.rge).zfill(2)}{self.ew}{str(self.mer)}"

    def get_pretty_str(self, incl_prefix=True, incl_event=False) -> str:
        x = self.get_pretty_str_main()

        if self.prefix is not None and incl_prefix:
            x = f"{self.prefix}/{x}"
        if self.event is not None and incl_event:
            x = f"{x}/{str(self.event).zfill(2)}"
        return x

    def get_dict(self) -> dict:
        return {
            'prefix': self.prefix,
            'lsd': self.lsd,
            'section': self.section,
            'twp': self.twp,
            'rge': self.rge,
            'ew': self.ew,
            'mer': self.mer,
            'event': self.event,
        }

    def __eq__(self, other):
        if isinstance(other, WellLoc):
            return all([
                self.prefix == other.prefix,
                self.lsd == other.lsd,
                self.section == other.section,
                self.twp == other.twp,
                self.rge == other.rge,
                self.ew == other.ew,
                self.mer == other.mer,
                self.event == other.event
            ])
        return False

def parse_str_to_clean_uwi(in_str, incl_prefix=True, incl_event=False, value_on_error=None) -> str:
    try:
        return WellLoc.from_string(in_str).get_pretty_str(incl_prefix=incl_prefix, incl_event=incl_event)
    except:
        return value_on_error

if __name__ == '__main__':
    # just run it to ensure no syntax error
    WellLoc.from_string('100/12-14-019-15W7/01')

