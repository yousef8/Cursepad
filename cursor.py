import curses


class Cursor:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def delete(self):
        y, x = self.stdscr.getyx()

        if y > 0 and x == 0:
            self.stdscr.delch(y, x)
            last_previous_col = len(self.stdscr.instr(y - 1, 0).decode().strip())
            self.stdscr.move(y - 1, last_previous_col)
        else:
            self.stdscr.delch(y, x)
