from selectolax.parser import HTMLParser
from shutil import get_terminal_size




def lastpage(html:str) -> int:
    return int(HTMLParser(html).css("ul.pagination-list li")[-2].css_first('a').text().strip())



def wordlists_in_page(html:str) -> list[dict]:
    
    all_wordlists = []
    cards = HTMLParser(html).css(".card.is-hidden-desktop.mb-3")

    for crd in cards:

        title = crd.css_first("strong").text().strip()

        a_tags  = crd.css("a")
        td_tags = crd.css("tbody td")

        all_wordlists.append({
            "title"  :title,
            "url"    :a_tags[0].attributes.get("href"),
            "dw_link":a_tags[1].attributes.get("href"),
            "tr_link":a_tags[2].attributes.get("href"),
            "size"   :td_tags[2].text().strip(),
            "len"    :td_tags[3].text().strip(),
            "rank"   :td_tags[0].text().strip(),
        })

    return all_wordlists
