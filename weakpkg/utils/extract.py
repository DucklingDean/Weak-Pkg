from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from scrape import lastpage
from printool import waiting_animation, print_incolumn, clear_line, Color
from time   import sleep



TERMINAL_COLOR = Color()
C              = Color(False)
DV_OPTIONS     = Options()

DV_OPTIONS.add_argument("--headless")
DV_OPTIONS.add_argument("--no-sandbox")  # Overcome limited resource problems
DV_OPTIONS.add_argument("--disable-dev-shm-usage")





def p(txt:str) -> None:
    clear_line()
    print(f"\r{txt}", end="")




def wait(dv:Firefox, start:int) -> None:
    animation = waiting_animation()
    while dv.execute_script("return document.readyState;") != "complete":
        print_incolumn(start, next(animation))
        sleep(0.2)

    clear_line()





def get_totalpages() -> Firefox:
    TERMINAL_COLOR.yellow

    p("Lunching Browser...")
    dv = Firefox()#options=DV_OPTIONS)


    p("Send Resquest...")
    dv.get("https://weakpass.com/wordlists")


    p("Waiting For Response...")
    wait(dv, 24)
    TERMINAL_COLOR.white
    

    max_pages = lastpage(dv.page_source)
    print(
        "\r",
        C.bold, C.bg_bright_blue,
        "Total Pages:",
        C.reset,
        f" {max_pages}", sep=""
        
    )
    return dv




def extract_all():
    dv = get_totalpages()





    
    
    dv.close()
    

if __name__=="__main__":
    extract_all()
