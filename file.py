import curses
import cursor
import os


class File:
    def __init__(self, stdscr, foot, cursor, file_name="Untitled"):
        self.stdscr = stdscr
        self.foot = foot
        self.cursor = cursor
        self.file_name = file_name

    def maxYX(self, scr):
        maxY, maxX = scr.getmaxyx()
        return maxY, maxX

    def set_file_name(self):
        maxY, maxX = self.maxYX(self.foot)
        self.foot.addstr(maxY - 1, 0, "File name: ")
        self.foot.move(maxY - 1, 11)
        self.foot.addstr(self.file_name)
        while True:
            c = self.foot.getch()
            if c == 10:
                self.file_name = self.foot.instr(maxY - 1, 11).decode().strip()
                return self.file_name

    def save_file(self):
        file_name = self.set_file_name()

        with open(file_name, "w") as f:
            maxY = self.cursor.far_y + 1
            lines = []
            for i in range(maxY):
                line = (
                    self.stdscr.instr(i, 0).decode().rstrip() + "\n"
                )  # the result of .instr() is byte coded so we transform it to string
                lines.append(line)
            f.writelines(lines)
