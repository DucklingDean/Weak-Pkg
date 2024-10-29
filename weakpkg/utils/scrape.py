from typing import LiteralString
from selectolax.parser import HTMLParser




def lastpage(html:str) -> int:
    return int(HTMLParser(html).css("ul.pagination-list li")[-2].css_first('a').text().strip())
