#!/usr/bin/python3

"""
Module that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

 def emptyline(self):
        """Do nothing empty line."""
        pass

 def do_quit(self, arg):
        """exit the program."""
        return True

def help_quit(self):
        """Print help message"""
        print("Quit to exit the program")

 def do_EOF(self, arg):
        """EOF command to exit the program
        """
        print()
        return True

def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = line.split()
        if not args:
            print(""class does not exist "")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class name missing **")
            return
        elif class_name in storage.classes():
            object = storage.classes()[class_name]()
            object.save()
            print(object.id)
            return

 def do_destroy(self, line):
        """Deletes an instance based on a given id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        elif  args and args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        elif len(args) < 2:
            print("** instance id missing **")
            return

          else:
            obj_key = args[0] + "." + args[1]
            obj_dict = storage.all()
            if obj_key in obj_dict:
                del obj_dict[obj_key]
                storage.save()
            else:
                print("** no instance found **")
                return

     def do_count(self, line):
        """Counts the instances of a class."""
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def do_update(self, line):            

     def do_all(self, arg):
        """Prints all string representation of all instances"""
        string_list = []
        obj_dict = storage.all()
        if not arg:
            for key, value in obj_dict.items():
                string_list.append(str(value))
        else:
            if arg not in HBNBCommand.class_instructions:
                print("** class doesn't exist **")
                return
            else:
                for key, value in obj_dict.items():
                    if value.__class__.__name__ == arg:
                        string_list.append(str(value))
        print(string_list)

     def do_show(self, arg):
        """Prints the representation of an instance"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1].strip('"')
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")
            

    def do_update(self, arg):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()