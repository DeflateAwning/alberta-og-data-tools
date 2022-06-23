# Testing for the uwi_tools.py class

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


import uwi_tools
import unittest

class Test_WellLoc(unittest.TestCase):
    def test_test(self):
        self.assertEqual(10+3, 13)

    def test_init_eq(self):
        test_loc_1 = uwi_tools.WellLoc('100', '12', '13', '16', '36', 'W', '4', None)
        test_loc_2 = uwi_tools.WellLoc(100, 12, 13, 16, 36, 'W', 4, None)

        self.assertEqual(test_loc_1, test_loc_2)
        self.assertEqual(test_loc_1.get_dict(), test_loc_2.get_dict())

    def test_fromstr_pretty(self):
        loc1 = uwi_tools.WellLoc.from_string('100/11-04-036-11W7/01')
        loc2 = uwi_tools.WellLoc('100', '11', '4', '36', '11', 'W', '7', '01')
        
        self.assertEqual(loc1, loc2)
        self.assertEqual(loc1.get_dict(), loc2.get_dict())

    def test_tostrmain(self):
        in_str = '11-04-036-11W7'
        loc = uwi_tools.WellLoc.from_string(in_str)

        self.assertEqual(in_str, loc.get_pretty_str_main())
        
    def test_tostr_prefsuf(self):
        in_str = '100/11-04-036-11W7/01'
        loc = uwi_tools.WellLoc.from_string(in_str)

        self.assertEqual(in_str, loc.get_pretty_str(incl_event=True))
        self.assertEqual(in_str[4:], loc.get_pretty_str(incl_prefix=False, incl_event=True))

    def test_fromstr_pretty_filename(self):
        loc1 = uwi_tools.WellLoc.from_string('100 _ 11-04-036-11W7')
        loc2 = uwi_tools.WellLoc('100', '11', '4', '36', '11', 'W', '7', None)
        
        self.assertEqual(loc1, loc2)
        self.assertEqual(loc1.get_dict(), loc2.get_dict())

    def test_fromstr_extraction(self):
        loc = uwi_tools.WellLoc.from_string('some text here 100/11-04-036-11W7 some other text here')
        self.assertEqual(loc.get_pretty_str(), '100/11-04-036-11W7')

    def test_error_handler(self):
        loc1_str = uwi_tools.parse_str_to_clean_uwi('some text here 100/11-04-036-11W7/01 some other text here', incl_event=True)
        self.assertEqual('100/11-04-036-11W7/01', loc1_str)


if __name__ == '__main__':
    unittest.main()
