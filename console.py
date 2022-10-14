#!/usr/bin/python3
"""
This module is the entry point for the command interpreter.
"""

import cmd

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
        print('')
        return True

    def help_EOF(self):
        """More info on using EOF"""
        print('Enter <EOF> character to exit program.\nAlternatively, you ' +\
              'can use "quit" command. (see <help quit>)')
        print('')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
