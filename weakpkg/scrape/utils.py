from selectolax.parser import HTMLParser
from shutil import get_terminal_size




def lastpage(html:str) -> int:
    return int(HTMLParser(html).css("ul.pagination-list li")[-2].css_first('a').text().strip())



def wordlists_in_page(html:str) -> list[dict]:
    
    all_wordlists = []
    cards = HTMLParser(html).css(".card.is-hidden-desktop.mb-3") # card is html element contains all the data of a wordlist.

    for crd in cards:

        title = crd.css_first("strong").text().strip()

        a_tags  = crd.css("a") # contains all url starts with '<a href=" ">...</a>'.
        td_tags = crd.css("tbody td") 

        all_wordlists.append({
            "title"  :title,
            "url"    :"https://www.weakpass.com"+a_tags[0].attributes.get("href").strip(), # href of the wordlist.
            "dw_link":a_tags[1].attributes.get("href"), # download url.
            "tr_link":a_tags[2].attributes.get("href"), # torrent file url.
            "size"   :td_tags[2].text().strip(), 
            "keys"   :td_tags[3].text().strip(), # keys number.
            "rank"   :td_tags[0].text().strip(), 
        })

    return all_wordlists



def wordlist_info(html:str) -> dict[str,str]:
    tree          = HTMLParser(html)
    download_btns = tree.css("div.column.is-6.mb-3")
    hashsum_elmnt = tree.css(".table.is-fullwidth tr")[:2]
    hashes        = ''
    
    # extract hashes
    for tr in hashsum_elmnt:
        hashes += ":".join(td.text().strip() for td in tr.css("td")) # name:md5:hash
        hashes += "|||"  # append "|||".
    hashes.rstrip("|||") # remove the last "|||".




    return {
        "rate"     :tree.css(".mt-4.is-size-3.has-text-weight-bold")[1].text().strip(), # crack rate.
        "comp_size":tree.css(".mb-4.is-size-3.has-text-weight-bold")[3].text().strip(), # compressed size.
        "dw_name"  :download_btns[0].text().strip(), # download file name.
        "tr_name"  :download_btns[1].text().strip(), # torrent file name.
        "hashsum"  :hashes,                         
    }
