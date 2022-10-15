#!/usr/bin/python3
"""
This module is the entry point for the command interpreter.

.. todo::
    Incoroporate RegEx into the module to reduce bulk of functions e.g.
    do_update().
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
    """

    prompt = '(hbnb) '
    """String to display as prompt to user for command"""

    __classes = {'BaseModel' : BaseModel}

    __types = {'number_rooms': int, 'number_bathrooms': int,
                'max_guest': int, 'price_by_night': int,
               'latitude': float, 'longitude': float
              }

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

    def help_all(self):
        """Command Line info for ``all`` function"""
        print('Use this command to print objects.\n' + \
              'If you specify a class name, only objects from that ' + \
              'class will be printed. ' + \
              'Otherwise, all objects will be printed.' + \
              '\nSyntax: all [class name] (class name is optional)')
        print('')

    def help_update(self):
        """Command Line info for ``update`` function"""
        print('Use this command to update object attributed.' +\
              '\nSyntax: update <class name> <object id> <att name> <att ' +\
              'value>  - To update one attribute at a time or: ' +\
              '\n\t update <class name> <object id> {"att name":"att value"' +\
              ' ...}  - To update many attributes at once')
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

    def do_all(self, args):
        """
        Prints the string representation of instances.

        If class name is given, only instances of that class are printed.
        Otherwise, all instances are printed.
        All objects are printed as strings.

        Args:
            args (str, optional): The class name whose instances are to be
            printed.
        """
        objs_as_string = []

        if args:
            args = args.split(' ')[0] #Ignore any additional args if any
            if args not in HBNBCommand.__classes:
                print('** class doesn\'t exist **')
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    objs_as_string.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                objs_as_string.append(str(v))

        print(objs_as_string)

    def do_update(self, args):
        """
        Updates instance based on class name and id by adding or updating an
        attribute and saves change to JSON.

        Example:
            ``update BaseModel 123-123-123 email "aibnb@email.com"``
            Will add attribute email to the instance of BaseModel with the
            given id.

        Only one attribute can be added at a time. Any additional are ignored
        unless they are passed as a dictionary in which case all attributes
        passed are updated.

        Example:
            ``update BaseModel 123-123-123 email "abc@mail.com" name "f_name"``
            Will only add email attribute and its value. But,
            ``update BaseModel 123-123-123 {"email":"abc@mail.com",
            "name":"f_name"}``
            Will add email and name and their values.

        If attribute name or value is missing, error message printed and
        funciton exits.
        If class name is missing, or class name doesn't exist, error message is
        printed and function exits.
        If id is missing or instance of the class name for the id doesn't
        exist, relevant error message is printed and funciton exits.
        """

        class_nm = obj_id = att_nm = att_val = kwargs = ''

        # First, process args to obtain class name and object id
        # then retrieve the Instance object
        args = args.partition(' ')
        if args[0]:
            class_nm = args[0]
        else:
            print('** class name missing **')
            return
        if class_nm not in HBNBCommand.__classes:
            print('** class name doesn\'t exist **')
            return

        args = args[2].partition(' ')
        if args[0]:
            obj_id = args[0]
        else:
            print('** instance id missing **')
            return

        # check if object exists
        if f'{class_nm}.{obj_id}' not in storage.all():
            print('** no instance found **')
            return

        # Check if attributes to be added have been passed as
        # *args or **kwargs
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            # If this line is reached, it is **kwargs. Store ALL the key/values in
            # a list
            kwargs = eval(args[2])
            args = []
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:
            # if this line is reached, it is *args. 
            args = args[2]

            # First, obtain attribute name.
            # If it is quoted, slice the string to get name
            if args and args[0] == '\"':
                end_quote = args.find('\"', 1)
                att_nm = args[1:end_quote]
                args = args[end_quote + 1:]

            args = args.partition(' ')

            # if attribute name is not set by now, it wasn't quoted. It should
            # be in the 0th index of args
            if not att_nm and args[0] != ' ':
                att_nm = args[0]

            # We have attribute name. Now let's get the value. Again, it could
            # be quoted or not
            if args[2] and args[2][0] == '\"': # if quoted
                att_val = args[2][1:args[2].find('\"', 1)]

            if not att_val and args[2]: # if not quoted
                att_val = args[2].partition(' ')[0]

            # We have attribute name and value now. Store in a list just like
            # **kwargs
            args = [att_nm, att_val]


        # At this point, args is a list that contains the attribute name and value. 
        # Now, we retrieve the object to update and do the updating work.
        obj = storage.all()[f'{class_nm}.{obj_id}']

        # Iterate through the args list to update object in a way that preserves
        # mutliple attribute names and values. (in case a dict was passed)
        for i, att_nm in enumerate(args):
            if (i % 2 == 0):
                att_val = args[i + 1]
                if not att_nm:
                    print('** attribute name missing **')
                    return
                if not att_val:
                    print('** value missing **')
                    return
                # Type cast where necessary
                if att_nm in HBNBCommand.__types:
                    att_val = HBNBCommand.__types[att_nm](att_val)

                # Update object
                obj.__dict__.update({att_nm: att_val})

        # save changes to file
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
