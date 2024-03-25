#!/usr/bin/python3
import os
import unittest
from io import StringIO
from models import storage
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the FileStorage class"""

    @classmethod
    def setUp(self):
        """Set up method for the class"""
        if os.path.isfile("file.json"):
            os.rename("file.json", 'tmp.json')

        self.classes = {'BaseModel', 'User', 'State', 'City', 'Amenity',
                        'Place', 'Review'}

        for self.classname in self.classes:
            with patch('sys.stdout', new=StringIO()) as output:
                HBNBCommand().onecmd("create {}".format(self.classname))
            self.uid = output.getvalue().strip()

    @classmethod
    def tearDown(self):
        """Tear down method for the class."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("tmp.json"):
            os.rename("tmp.json", "file.json")
        pass

    def test_prompt(self):
        """_summary_
        """
        self.assertEqual('(hbnb) ', HBNBCommand.prompt)

    def test_help(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help")
        help_string = ("Documented commands (type help <topic>):\n"
                       "========================================\n"
                       "EOF  all  create  destroy  help  quit  show  update")
        self.assertEqual(output.getvalue().strip(), help_string)

    def test_emptyline(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("")
        self.assertEqual(output.getvalue(), "")

    def test_help_EOF(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help EOF")
        help_eof = "Handles the Ends Of File signal with a newline."
        self.assertEqual(output.getvalue().strip(), help_eof)

    def test_help_all(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help all")
        help_all = ("Print all string representation of all instances.\n\n"
                    "        Args:\n "
                    "           arg (str): The class name (optional).\n"
                    "            arg <class name>.all(): Retrieves all "
                    "instances of a class.")
        self.assertEqual(output.getvalue().strip(), help_all)

    def test_help_create(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help create")
        help_create = ("Create a new instance of a class.\n\n"
                       "        Args:\n "
                       "           arg (str): The name of the class to create "
                       "an instance of.\n"
                       "            arg <class name>.count(): Retrieves the "
                       "number of instances.")
        self.assertEqual(output.getvalue().strip(), help_create)

    def test_help_destroy(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help destroy")
        help_destroy = ("Delete an instance from storage.\n\n"
                        "        Args:\n "
                        "           args (str): The class name and instance "
                        "id separated by space.\n"
                        "            arg <class name>.destroy(<id>): "
                        "Destroys an instance by ID.")
        self.assertEqual(output.getvalue().strip(), help_destroy)

    def test_help_show(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help show")
        help_show = ("Show details of a specific instance.\n\n"
                     "        Args:\n "
                     "           args (str): The class name and instance id "
                     "separated by space.\n"
                     "            arg <class name>.show(<id>): Retrieves an "
                     "instance based on its ID")
        self.assertEqual(output.getvalue().strip(), help_show)

    def test_help_update(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help update")
        help_update = ("Updates an attribute of an instance of a class.\n\n"
                       "        Args:\n "
                       "           args (str): A string containing the class "
                       "name, instance ID,\n"
                       "            attribute name, and value to be updated.\n"
                       "            arg <class name>.update(<id>, "
                       "<attribute name>, <attribute value>):\n"
                       "            Update an instance based on his ID.\n"
                       "            arg <class name>.update(<id>, "
                       "<dictionary representation>):\n"
                       "            update an instance based on his ID with a "
                       "dictionary.")
        self.assertEqual(output.getvalue().strip(), help_update)

    def test_help_quit(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help quit")
        help_quit = "Command to exit the program."
        self.assertEqual(output.getvalue().strip(), help_quit)

    def test_do_create(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create {}".format(self.classname))
        self.uid = output.getvalue().strip()
        self.assertTrue(len(self.uid) > 0)

    def test_do_all(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all")
        instance_str = output.getvalue()
        self.assertIn(self.uid, instance_str)

    def test_do_all_with_arg(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all {}".format(self.classname))
        instance_str = output.getvalue()
        self.assertIn(self.uid, instance_str)

    def test_default_all(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("{}.all()".format(self.classname))
        instance_str = output.getvalue()
        self.assertIn(self.uid, instance_str)

    def test_do_all_error(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all {}".format("randomString"))
        error_msg = output.getvalue().strip()
        self.assertEqual(error_msg, "** class doesn't exist **")

    def test_default_all_error(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("{}.all()".format("randomString"))
        error_msg = output.getvalue().strip()
        self.assertEqual(error_msg, "** class doesn't exist **")

    def test_default_all_error_with_arg(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("{}.all(arg)".format(self.classname))
        error_msg = output.getvalue().strip()
        self.assertEqual(error_msg, "*** Unknown syntax: {}.all(arg)"
                         .format(self.classname))

    def test_default_count(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("{}.count()".format(self.classname))
        number = output.getvalue().strip()
        self.assertEqual(eval(number), 4)

    def test_default_count_error(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("{}.count()".format("random"))
        error_msg = output.getvalue().strip()
        self.assertEqual(error_msg, "** class doesn't exist **")

    def test_default_count_error_with_arg(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("{}.count(arg)".format(self.classname))
        error_msg = output.getvalue().strip()
        self.assertEqual(error_msg, "*** Unknown syntax: {}.count(arg)"
                         .format(self.classname))

    def test_do_show(self):
        """_summary_
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show {} {}"
                                 .format(self.classname, self.uid))
        instance_str = output.getvalue().strip()
        self.assertIn(self.uid, instance_str)
        self.assertIn(self.classname, instance_str)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
