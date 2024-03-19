#!/usr/bin/python3
"""Comand Interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command Interpreter Class
    """

    prompt = '(hbnb) '

    def do_quit(self, person):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Handles the Ends Of File with a newline
        """
        print()
        return True

    def emptyline(self):
        """Handles Empty Line Command
        """
        pass

    def postloop(self):
        print


if __name__ == '__main__':
    HBNBCommand().cmdloop()
