import curses


class Cursor:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def coordinate(self):
        y, x = self.stdscr.getyx()
        return (y, x)

    def move(self, y, x):
        self.stdscr.move(y, x)

    def up(self):
        y, x = self.coordinate()
        if y > 0:
            y -= 1
            self.move(y, x)

    def down(self):
        y, x = self.coordinate()
        if y < self.stdscr.getmaxyx()[0] - 1:
            y += 1
            self.move(y, x)

    def right(self):
        y, x = self.coordinate()
        if x < self.stdscr.getmaxyx()[1] - 1:
            x += 1
            self.move(y, x)

    def left(self):
        y, x = self.coordinate()
        if x > 0:
            x -= 1
            self.move(y, x)

    def delete(self):
        y, x = self.stdscr.getyx()

        if y > 0 and x == 0:
            self.stdscr.delch(y, x)
            last_previous_col = len(self.stdscr.instr(y - 1, 0).decode().strip())
            self.stdscr.move(y - 1, last_previous_col)
        else:
            self.stdscr.delch(y, x)
