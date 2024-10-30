from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from scrape.utils import lastpage, wordlists_in_page
from toolkit.print import *
from time   import sleep



TERMINAL_COLOR = Color()
C              = Color(False)
DV_OPTIONS     = Options()

DV_OPTIONS.add_argument("--headless")
DV_OPTIONS.add_argument("--no-sandbox")  # Overcome limited resource problems
DV_OPTIONS.add_argument("--disable-dev-shm-usage")





def p(txt:str) -> None:
    clear_line()
    print(f"\r[*] {txt}", end="")



   


def setup_env() -> tuple[Firefox, int]:
    def wait(dv:Firefox, start:int) -> None:
        animation = waiting_animation()
        while dv.execute_script("return document.readyState;") != "complete":
            print_incolumn(2, next(animation))
            sleep(0.1)
        clear_line()

    TERMINAL_COLOR.yellow

    p("Lunching Browser...")
    dv = Firefox()#options=DV_OPTIONS)


    p("Send Resquest...")
    dv.get("https://weakpass.com/wordlists")


    p("Waiting For Response...")
    wait(dv, 28)
    TERMINAL_COLOR.white
    

    max_pages = lastpage(dv.page_source)
    print(
        "\r",
        C.bold, C.bg_bright_blue,
        "Total Pages:",
        C.reset,
        f" {max_pages}", sep=""
        
    )
    return dv, max_pages




def get_allpages_html(dv:Firefox, max_pages:int) -> list[str]:
    print(
        C.yellow, C.bold,
        "[!] Fetching Page:",
        C.reset, " -",
        sep=""
    )
    print(
        C.bright_green, C.bold,
        "[+] HTML         :", 
        C.reset, " -",
        sep="" 
    )
    line_up()
    html      = dv.page_source
    wordlists = []
    animation = waiting_animation()
    for page in range(2, max_pages+1):
        dv.get(f"https://weakpass.com/wordlists?page={page}")

        print_incolumn(20, f"{page-1}/{max_pages}")
        wordlists += wordlists_in_page(html)
 
        line_up()
        print_incolumn(20, f"{page}/{max_pages}")


        while dv.execute_script("return document.readyState;") != "complete":
            print_incolumn(2, next(animation))
            sleep(0.1)

        line_down()
        html = dv.page_source
        if page == max_pages:
            wordlists += wordlists_in_page(html)
            print_incolumn(20, f"{max_pages}/{max_pages}")
            print_incolumn(2, "\u2714")
            line_up()
            print_incolumn(2, "\u2714")
            line_down()
            print()

    return wordlists




def extract_all():
    dv, max_pages = setup_env()
    
    wordlists = get_allpages_html(dv, max_pages)
    clear_line()
    print(len(wordlists))
    dv.close()
    




if __name__=="__main__":
    extract_all()
