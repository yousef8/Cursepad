import curses
import sys
from file import File

Escape = 27
Space = 32
# wrapper function takes care of making a new screen and ending it
def main(scr):
    # Make a new screen
    curses.echo()
    file = File(scr)
    while True:
        scr.refresh()
        c = scr.getch()

        # Saving to a file
        if c == 19:  # CTRL + S
            file.save_file()

        # To exit gracefully from the Program
        if c == 27:  # ord() for ecscape charater
            sys.exit(0)


curses.wrapper(main)
