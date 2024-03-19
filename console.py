#!/usr/bin/python3
"""Comand Interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command Interpreter Class
    """

    prompt = '(hbnb) '
    classes = {'BaseModel'}

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

    def do_create(self, arg):
        """Create a new instance of a class

        Args:
            arg (str): The name of the class to create an instance of.
        """
        if arg == "":
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """Show details of a specific instance.

        Args:
            args (str): The class name and instance id separated by space.
        """
        if args == "" or args == None:
            print("** class name missing **")
        else:
            arg = args.split()

            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(arg) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(arg[0], arg[1])

                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
