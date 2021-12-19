import curses
import sys
from file import File
from cursor import Cursor

Escape = 27
Space = 32
# wrapper function takes care of making a new screen and ending it
def main(scr):
    # Make a new screen
    curses.echo()
    cursor = Cursor(scr)
    file = File(scr, cursor)
    while True:
        scr.refresh()
        c = scr.getch()
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

        # To exit gracefully from the Program
        if c == 27:  # ord() for ecscape charater
            sys.exit(0)


curses.wrapper(main)
