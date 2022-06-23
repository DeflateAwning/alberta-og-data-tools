# alberta-og-data-tools
A collection of Python tools for dealing with Alberta oil and gas data, including UWIs.

While I briefly worked in the oil and gas industry in Alberta, I noticed a lack of efficiency in dealing with large lists of Unique Well Identifiers (or UWIs for short), especially when parsing lists of files, or parsing text from human-written notes. 

This library implements a `WellLoc()` class, which represents a UWI surface location or bottom hole location (with optional prefix and completion event). It also implements parsing of these UWIs from large strings of text, especially in cases where inconsistent formatting was used.

## Usage Examples
See `test_uwi_tools.py` for a list of capabilities and conversions.

Star this repo or open an issue if you want more examples!
