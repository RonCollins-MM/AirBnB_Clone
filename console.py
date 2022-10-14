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

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print('')
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
