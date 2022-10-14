#!/usr/bin/python3
"""
This module is the entry point for the command interpreter.
"""

from models.base_model import BaseModel
import cmd
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Implementation class for the command interpreter.

    Inherits from the inbuilt ``cmd`` module.
    The inbuilt ``cmd`` module contains the necessary tools (inherited
    attributes) to setup a custom line-oriented
    command interpreter.

    Attributes:
        prompt (str): The string to display as prompt for commands.
    """

    prompt = '(hbnb) '

    __classes = {'BaseModel' : BaseModel}

#------------------------------- Elementary functions --------------------------#
    def emptyline(self):
        """
        Method called when emptyline is entered.
        Does nothing.
        """
        pass

    def help_help(self):
        """Prints more information regarding ``help`` command"""
        print('Use this command to find out more information about other ' + \
              'commands. \nSyntax: help <command>')
        print('')

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Prints info on how to use quit"""
        print('Use this command with no arguments to exit the program.\n' + \
              'Alternatively, you can enter an <EOF> character.\nSyntax: quit')
        print('')

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print('Exiting ...')
        return True

    def help_EOF(self):
        """More info on using EOF"""
        print('Enter <EOF> character to exit program.\nAlternatively, you ' +\
              'can use "quit" command. (see <help quit>)')
        print('')

    def help_create(self):
        """Command Line info for ``create`` function"""
        print('Use this command to create an object of a class.' + \
              '\nSyntax: create <class name>\nEx: "create BaseModel"')
        print('')

    def help_show(self):
        """Command Line info for ``show`` function"""
        print('Use this command to print an object of a class based on class'+\
              'name and id of object' + \
              '\nSyntax: show <class name> <object id>')
        print('')

    def help_destroy(self):
        """Command Line info for ``destroy`` function"""
        print('Use this command to delete an object of a class based on class'+\
              'name and id of object' + \
              '\nSyntax: destroy <class name> <object id>')
        print('')




#------------------------------- Core functions ---------------------------------#

    def do_create(self, args):
        """
        Responsible for the creation of instances of Classes.

        If no arguments are passed, or if argument doesn't correspond to
        existing classes, appropriate error message is printed and function
        exits.
        Otherwise, a new instance object is created and saved to the File
        storage system. ID of created instance will be printed to Command Line.

        Args:
            args (str): The class name whose instance is to be created.
        """
        if not args:
            print('** class name missing **')
            return
        elif args not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
            return
        else:
            new_inst = HBNBCommand.__classes[args]()
            storage.save()
            print(new_inst.id)

    def do_show(self, args):
        """
        Prints a string representation of an instance based on class name and
        id.

        If class name is missing or doesn't exist, or if id is missing, or if
        instance is not found, appropriate error message is printed and
        function exits.

        Args:
            args (str): The class name and id of the instance
        """
        arg_tup = args.partition(' ')
        class_nm = arg_tup[0]
        obj_id = arg_tup[2]

        #Deal with trailing arguments if any
        if obj_id and ' ' in obj_id:
            obj_id = obj_id.partition(' ')[0]

        #Check that class name and object id are valid
        if not class_nm:
            print('** class name missing **')
            return
        if class_nm not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
            return
        if not obj_id:
            print('** instance id missing **')
            return

        #Print the object
        try:
            print(storage._FileStorage__objects[f'{class_nm}.{obj_id}'])
        except KeyError:
            print('** no instance found **')

    def do_destroy(self, args):
        """
        Deletes an instance based on class name and id.

        If class name is missing or doesn't exist, or if id is missing, or if
        instance is not found, appropriate error message is printed and
        function exits.

        Args:
            args (str): The class name and id of instance
        """
        arg_tup = args.partition(' ')
        class_nm = arg_tup[0]
        obj_id = arg_tup[2]

        #Deal with trailing arguments if any
        if obj_id and ' ' in obj_id:
            obj_id = obj_id.partition(' ')[0]

        #Check that class name and object id are valid
        if not class_nm:
            print('** class name missing **')
            return
        if class_nm not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
            return
        if not obj_id:
            print('** instance id missing **')
            return

        #Delete the object
        try:
            del(storage.all()[f'{class_nm}.{obj_id}'])
            storage.save()
        except KeyError:
            print('** no instance found **')




if __name__ == '__main__':
    HBNBCommand().cmdloop()
