import curses
import sys

Escape = 27
Space = 32
# wrapper function takes care of making a new screen and ending it
def main(scr):
    # Make a new screen
    curses.echo()
    while True:
        scr.refresh()
        c = scr.getch()

        # To exit gracefully from the Program
        if c == 27:  # ord() for ecscape charater
            sys.exit(0)


curses.wrapper(main)
