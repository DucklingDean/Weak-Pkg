from collections.abc import Generator
from shutil import get_terminal_size








        

def line_up() -> None:
    print("\033[A", end="")



def line_down() -> None:
    print("\033[B", end="")



def clear_line() -> None:
    print("\r"+" "*get_terminal_size().columns, end="")
    



def waiting_animation() -> Generator[str]:
    spinner = ['◐', '◓', '◑', '◒', '⬤', '⬤', '⬤', '⬤', '⬤', '⬤', '⬤', '⬤']
    #spinner = ['◴', '◷', '◶', '◵', '◴', '◷', '◶', '◵']
    #spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    while True:
        for char in spinner: yield char



def print_incolumn(column:int, txt:str, end="") -> None:
    print(f"\033[{column}G{txt}",end=end, flush=True)



class Color:
    def __init__(self, print:bool=True) -> None:
        assert type(print)==bool
        self.print = print

    def _p(self, color):
        if self.print:
            print(f"\033[{color}m", end="")
        return f"\033[{color}m"

    @property
    def reset(self):
        return self._p(0)

    @property
    def black(self):
        return self._p(30)

    @property
    def red(self):
        return self._p(31)

    @property
    def green(self):
        return self._p(32)

    @property
    def yellow(self):
        return self._p(33)

    @property
    def blue(self):
        return self._p(34)

    @property
    def magenta(self):
        return self._p(35)

    @property
    def cyan(self):
        return self._p(36)

    @property
    def white(self):
        return self._p(37)

    @property
    def bright_black(self):
        return self._p(90)

    @property
    def bright_red(self):
        return self._p(91)

    @property
    def bright_green(self):
        return self._p(92)

    @property
    def bright_yellow(self):
        return self._p(93)

    @property
    def bright_blue(self):
        return self._p(94)

    @property
    def bright_magenta(self):
        return self._p(95)

    @property
    def bright_cyan(self):
        return self._p(96)

    @property
    def bright_white(self):
        return self._p(97)

    @property
    def bold(self):
        return self._p(1)

    @property
    def underline(self):
        return self._p(4)

    # Background colors
    @property
    def bg_black(self):
        return self._p(40)

    @property
    def bg_red(self):
        return self._p(41)

    @property
    def bg_green(self):
        return self._p(42)

    @property
    def bg_yellow(self):
        return self._p(43)

    @property
    def bg_blue(self):
        return self._p(44)

    @property
    def bg_magenta(self):
        return self._p(45)

    @property
    def bg_cyan(self):
        return self._p(46)

    @property
    def bg_white(self):
        return self._p(47)

    @property
    def bg_bright_black(self):
        return self._p(100)

    @property
    def bg_bright_red(self):
        return self._p(101)

    @property
    def bg_bright_green(self):
        return self._p(102)

    @property
    def bg_bright_yellow(self):
        return self._p(103)

    @property
    def bg_bright_blue(self):
        return self._p(104)

    @property
    def bg_bright_magenta(self):
        return self._p(105)

    @property
    def bg_bright_cyan(self):
        return self._p(106)

    @property
    def bg_bright_white(self):
        return self._p(107)
