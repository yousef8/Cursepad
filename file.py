import curses


class File:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def file_name(self):
        self.stdscr.addstr(curses.LINES - 1, 0, "File name: ", curses.A_REVERSE)
        self.stdscr.move(curses.LINES - 1, 11)
        file_name = ""
        while True:
            c = self.stdscr.getch()
            if c == 10:
                file_name = self.stdscr.instr(curses.LINES - 1, 11).decode().strip()
                return file_name

    def save_file(self):
        file_name = self.file_name()

        with open(file_name, "w") as f:
            cursor_line = self.stdscr.getyx()[0]
            lines = []
            for i in range(cursor_line + 1):
                line = (
                    self.stdscr.instr(i, 0).decode().strip() + "\n"
                )  # the result of .instr() is byte coded so we transform it to string
                lines.append(line)
            f.writelines(lines)
