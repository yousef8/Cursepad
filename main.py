import curses
import sys
import os
from file import File
from cursor import Cursor

Escape = 27
Space = 32

# wrapper function takes care of making a new stdscreen and ending it
def main(stdscr):
    # Make a new stdscreen
    if curses.has_colors:
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        head_color = curses.color_pair(1)

    curses.echo()

    # Create 3 Seperate windows
    max_y, max_x = stdscr.getmaxyx()

    head = curses.newwin(1, max_x, 0, 0)
    head.bkgd(" ", head_color)
    head.keypad(True)

    main = curses.newwin(max_y - 5, max_x, 1, 0)
    main.keypad(True)

    foot = curses.newwin(3, max_x, max_y - 3, 0)
    foot.bkgd(" ", head_color)
    foot.keypad(True)

    stdscr.refresh()
    head.refresh()
    main.refresh()
    foot.refresh()

    cursor = Cursor(main, 0, 0)
    file = File(main, foot, cursor)

    # Setting the head part
    def set_head(file_name):
        head.clear()
        head_max_y, head_max_X = head.getmaxyx()
        text = file_name + " - Cursepad"
        center_y = head_max_y // 2
        center_x = head_max_X // 2 - len(text)
        head.addstr(center_y, center_x, text)
        head.refresh()

    set_head(file.file_name)

    # Setting the foot part
    def set_foot():
        foot.clear()
        foot_max_y, foot_max_X = foot.getmaxyx()
        foot_X_quarter = foot_max_X // 4
        foot.addstr(0, 0, "Ctrl+s: Save")
        foot.addstr(0, foot_X_quarter, "Esc: Exit")
        foot.refresh()

    set_foot()

    while True:
        c = main.getch()
        cursor.far_coord()

        # Implement moving keys
        if c == curses.KEY_UP:
            cursor.up()
        elif c == curses.KEY_DOWN:
            cursor.down()
        elif c == curses.KEY_RIGHT:
            cursor.right()
        elif c == curses.KEY_LEFT:
            cursor.left()

        # Implementing deleting
        if c == 8 or c == 263:  # Backspace
            cursor.delete()

        # Saving to a file
        if c == 19:  # CTRL + S
            file.save_file()
            set_head(file.file_name)
            set_foot()

        # To exit gracefully from the Program
        if c == 27:  # ord() for ecscape charater
            sys.exit(0)


curses.wrapper(main)
