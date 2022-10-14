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
        print('Exiting ...')
        print('')
        return True

    def help_quit(self):
        """Prints info on how to use quit"""
        print('Use this command with no arguments to exit the program.\n' + \
              'Alternatively, you can enter an <EOF> character.\nSyntax: quit')
        print('')

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print('Exiting ...')
        print('')
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
            print('** class name missing **' + '\n')
            return
        elif args not in HBNBCommand.__classes:
            print('** class doesn\'t exist **' + '\n')
            return
        else:
            new_inst = HBNBCommand.__classes[args]()
            storage.save()
            print(new_inst.id + '\n')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
