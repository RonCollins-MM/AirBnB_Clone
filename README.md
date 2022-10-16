<h1> AirBnB Clone Project </h1>
<p>
This project is intended to be a hands-on learning process of building a full-scale software application that consists of:
<li>A web interface for user interaction</li>
<li>A Database Management System</li>
<li>A Server that hosts the main application</li>
<li>A debugging interface for the developer (in this case, a command line interpreter)</li>
</p>
<p>
All the components above are built in stages. The first stage is to build a small prototype of the main system - a basic command line interpreter that is able to manipulate <b><em>objects</em></b> that are stored in a JSON file storage system. This would mainly be implemented in <b>Python</b>. Next, a static webpage would be built in <b>HTML</b> and <b>CSS</b> before functionality is added with <b>Javascript</b>. After that, a proper Database management system would be set up using <b>MySQL</b>. Finally, a server would be setup using tools like <b>Puppet</b> among others.
</p>
<h2>The Command Interpreter</h2>
The command interpreter provides a shell-like environment that allows the developer to manipulate data objects and dynamically test the application without too much abstraction in between. It is built in Python.
<br>
Through the interpreter, you should be able to:

* Create a new object
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Usage

* The console can be run in both interactive and non-interactive mode.
* It prints a prompt **(hbnb)** and waits for the user for input.

### Interactive Mode

```cmd
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Non-Interactive Mode

```cmd
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Commands

Command | Description
--- | ---
`quit` | Exits the program
`EOF` | Exits the program
`create <class>` | Creates an instance of a class
`show <class> <id>` | Prints the string representation of an instance of a class based on class name and id
`destroy <class> <id>` | Deletes instance of a class based on class name and id
`all` | Prints all string representations of all instances
`all <class>` | Prints all string representations of all instances based on class name
`update <class> <id> <attribute name> "<attribute value>"` | Updates an attribute of an instance based on class name and id
`<class>.all()` | Retrieves all instances of a class
`<class>.count()` | Retrieves the number of instances of a class
`<class>.show(<id>)` | Retrieves an instance based on its id
`<class>.destroy(<id>)` | Destroys an instance based on its id

---
