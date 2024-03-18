#!/usr/bin/python3
"""
Comand Line Interpreter
"""

import cmd


class HBnBCommand(cmd.Cmd):
    """
    Command Line Interpreter Class
    """

    prompt = '(hbnb) '

    def do_quit(self, person):
        """
        Command To Quit the Command Line
        """
        return True
    
    def do_EOF(self, line):
        """
        Handles the Ends Of File with a newline
        """
        print()
        return True

    def emptyline(self):
        """
        Handles Empty Line Command
        """
        pass
    
    def postloop(self):
        print

if __name__ == '__main__':
    HBnBCommand().cmdloop()
