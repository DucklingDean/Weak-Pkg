from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from scrape.utils import lastpage, wordlists_in_page
from toolkit.print import *
from time   import sleep



TERMINAL_COLOR = Color() # change the whole terminal color & style.
C              = Color(False) # it used just in printing functions.
DV_OPTIONS     = Options() # to make the browser headless.

DV_OPTIONS.add_argument("--headless")
# Overcome limited resource problems
DV_OPTIONS.add_argument("--no-sandbox")  
DV_OPTIONS.add_argument("--disable-dev-shm-usage")








   


def setup_env() -> tuple[Firefox, int]:
    """return the driver & the total pages in the website"""

    # just a simple animation works while waiting the response. 
    def wait(dv:Firefox) -> None:
        animation = waiting_animation()
        while dv.execute_script("return document.readyState;") != "complete":
            print_incolumn(2, next(animation))
            sleep(0.1)


    # i added this, so i wont type '\r [!]' & end="" every time.
    def p(txt:str) -> None:
        clear_line()
        print(f"\r[!] {txt}", end="")


    TERMINAL_COLOR.yellow
    TERMINAL_COLOR.bold

    p("Lunching Browser...")
    dv = Firefox()#options=DV_OPTIONS)


    p("Send Resquest...")
    dv.get("https://weakpass.com/wordlists")


    p("Waiting For Response...")
    wait(dv)
    TERMINAL_COLOR.reset
    

    max_pages = lastpage(dv.page_source)

    clear_line()
    print(
        "\r",
        C.bold, C.bg_green,
        "Total Pages:",
        C.reset,
        f" {max_pages}", sep=""
        
    )
    return dv, max_pages




def get_allpages_html(dv:Firefox, max_pages:int) -> list[str]:
    """extract all the wordlists in the website"""
    # first row.
    print(
        C.yellow, C.bold,
        "[!] Fetching Page:",
        C.reset, " -",
        sep=""
    )
    # second row.
    print(
        C.bright_green, C.bold,
        "[+] Scraping HTML:", 
        C.reset, " -",
        sep="", end="" 
    )

    html      = dv.page_source
    wordlists = [] # will contain processed html (dict).
    animation = waiting_animation() # the animation generator.

    for page in range(2, max_pages+1):
        dv.get(f"https://weakpass.com/wordlists?page={page}")
        
        # dynamic values
        print_incolumn(20, f"{page-1}/{max_pages}") 
        wordlists += wordlists_in_page(html) # murge the old list with the new one.
 
        line_up()
        print_incolumn(20, f"{page}/{max_pages}")
        # ---

        # waiting for the response.
        while dv.execute_script("return document.readyState;") != "complete":
            print_incolumn(2, next(animation)) # the animation
            sleep(0.1)
        line_down()

        html = dv.page_source
    # after finshing.
    else:
        wordlists += wordlists_in_page(html)
        print_incolumn(20, f"{max_pages}/{max_pages}")
        print_incolumn(2, "\u2714")
        line_up()
        print_incolumn(2, "\u2714")
        line_down()

    print(
        "\n\r",
        C.bold, C.bg_green,
        "WORDLISTS:",
        C.reset,
        f" {len(wordlists)}", sep=""
        
    )

    return wordlists




def extract_all():
    dv, max_pages = setup_env() # setup_env returns tuple.
    
    wordlists = get_allpages_html(dv, max_pages)
    

    
    dv.close()
    




if __name__=="__main__":
    extract_all()
