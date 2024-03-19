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
        if args == "":
            print("** class name missing **")
        else:
            arg = args.split()

            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(arg[0], arg[1])

                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, args):
        """Delete an instance from storage.

        Args:
            args (str): The class name and instance id separated by space.
        """
        if args == "":
            print("** class name missing **")
        else:
            arg = args.split()

            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(arg[0], arg[1])

                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """Print all string representation of all instances.

        Args:
            arg (str): The class name (optional).
        """
        if arg == "":
            print([str(obj) for obj in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in storage.all().values()])

    def do_update(self, args):
        """Updates an attribute of an instance of a class.

        Args:
            args (str): A string containing the class name, instance ID,
            attribute name, and value to be updated.
        """
        if args == "":
            print("** class name missing **")
        else:
            arg = args.split()

            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            elif len(arg) < 3:
                print("** attribute name missing **")
            elif len(arg) < 4:
                print("** value missing **")
            else:
                key = "{}.{}".format(arg[0], arg[1])

                if key not in storage.all():
                    print("** no instance found **")
                else:
                    obj = storage.all()[key]
                    setattr(obj, arg[2], arg[3].strip('"'))
                    obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
