# USIU-A Fundamentals of Web Design (APT1040)

## A Few Notes
The repository when implemented will display a website that is a full stack implementation of website. The frontend using the API queries the backend and displays content dynamically to the user.

 **THE WEBSITE DOES NOT RUN IF YOU COPY AND PASTE THE CODE ONLY** 

I intentionally made it neccessary for you to actually learn content for the whole semester before implementing things. Nonetheless, since it is unlikely that one knows how to use Python objects and their decorators I have covered this base adequately.

Should you fork the repository keep the code pretty. Write documentation and comments within your code exactly the way I have done. The code should remain FAANG compliant.

Moreover, ensure your commits are also logical and follow a clear well defined structure. For inspiration refer to mine. A commit history that is well done ensures that stable points are easily identified in case a crippling bug is introduced to the system. In the unfortunate yet common case that a bug arises one can easily return to the last stable state. I.e. a commit that one verified to work.

## Introduction
This repository has a backend and frontend implementation of a website for the first USIU course on Web Design.

> This repository does not aim to replace the process of learning how to build this. As a result, this code **does not work** unless you actually know how to configure things.

The technologies employed are as follows:

- Backend: Python
- Storage Method: Database, JSON
- Database: MySQL
- Frontend: HTML, CSS, JS, GO
- API: Python
- Web Framework: Flask
- ORM: SQLAlchemy
- Console: Python
- Operating System: Ubuntu 22.04 LTS / 20.04 LTS

> Feel free to use any other OS. Notwithstanding, a Debian based distribution is best (personal opinion). Windows and MacOS can work but may need more configuration. (I never bothered to be cross platform compatible).

## Backend
### Python Classes
The code implements two classes. The first class is a base model class which has generic functionality for extensibility of the code. The second class is an implementation of a generic grid object. The grid object will hold a picture link, title text and description text.

### Python Unit Tests
Have fun writing unittests should you decide extend the functionality of the website. 😃


## Storage Method
### MySQL
It is inevitable for one to actually have mysql installed to be able to use the database. The installation command is:

```bash
sudo apt update
sudo apt install mysql-server
```

To integrate with Python you will need to install mysqlclient:

```bash
sudo apt install python3-dev default-libmysqlclient-dev build-essential pkg-config
sudo pip install mysqlclient
```

### JSON
For debugging reasons I created a script that stored data in a .json file. However, I intentionally have not included the file in order to minimise the probability of someone taking the easy way out and setting the precedent of building a website with a file storage engine because it has the following core issues:

- It is an inferior method because only one request can be made at a time.
- Every request made while a process is doing I/O on the file will fail with an error.
- It does not implement data integrity. Should there be any errors in the data inputted it will be written in the JSON file without any data cleaning. A database on the other hand will yield an error ensuring that one clearly understands the error with  their input.


The file storage engine in contrast to the database engine was OS agnostic- which is a good thing. Have a blast of a time reconstructing it. 😃

>As a result it is inperative to figure out how to configure and connect to a database instance.

### SQL Set Up
A setup.sql file is present that will enable the setting up of a database, user and table. Remember to change variables for the user and the password for the code to run. So you must figure out some basic SQL code. To execute it run:

```bash
cat setup.sql | sudo mysql
```

Configure the following parameters:
- The database name
- The username
- The user password

Dummy placeholders are there to show you where to place the needed values. You may not need to alter anything else.

## Frontend
### HTML
There is an implementation of GO within the HTML structure to ensure that content is loaded dynamically. This keeps the HTML file very lightweight. This means that even if the database has 1000 places the HTML content should load reasonably quickly.

### CSS
Connected by a link in the HTML file it beautifies the web page. Feel free to make it much prettier. Nonetheless, I have implemented a grid structure with `display: flex;` to fit items based on the screen size. Moreover, the titles of places have a linear gradient effect applied to them. Finally, grid elements animate in on scroll.

### JS
The implementation is pretty much vanilla JS for speed. Feel free to migrate to fancier altenatives like next.js, react.js, node.js and bun should you want to use more complex renders and visual effects.

The JS uses an observer to check whether an object is in the view port or not. If it is, it animates it in.

## API
The Apllication Programming Interface uses the Flask CORS functionality to use the abstraction offered the Python ORM to query the database and yield a .json file with all the content needed.


## Web Framework
Flask is the framework of choice. It is simple to implement and direct. Install using:

```bash
pip install flask
```

It will install other dependencies also.

## ORM
SQLAlchemy provides abstraction which means that one need not write SQL code to query the database. Install using:

```bash
pip install sqlalchemy
```

## Console
The console is built using Python and allows testing of whether backend methods work. The console is immaculate and one needs not tamper with it in any shape or form.

But if you are extending functionality ensure you update the console to include the new implementations.

Excluding the BaseModel class the other class present is the Place class that holds a picture link, title and description. This fits with the aim of creating a simple implementation that shows iconic places in Africa. To create a new place from the console the following code format is to be used:

```bash
(usiu-a) create Place picture="https://images.unsplash.com/photo-1707661981342-6885666832a8?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTcxMDI3MjczMQ&ixlib=rb-4.0.3&q=80&w=1080" title="My_Awesome_Place" description="This_is_a_beautiful_place._And_it_has_history."
```

Realise that where spaces exist you will need to used underscores or else things will not work. Using a similar format one can also:

- Show a Place
- Update a Place
- Delete a Place
- Show all Places

To invoke the console to connect to the database use:

```bash
<username variable>=<user> <user password variable>=<user password> <host variable>=<host> <database variable>=<database> <storage type variable>=db ./console.py
```

To use file storage use:

```bash
./console.py
```

## Operating System
The code was tested and built on Ubuntu 22.04 and Ubuntu 20.04. The code could be backported but I would not rely on it. Should you not have access to an Ubuntu server then figure out how to make it run on Windows or MacOS. Those on MacOS do have an advantage, nonetheless.

### Windows
Four options exist:

#### Windows Subsytem for Linux (Beginners)
Should want a method that does not require dual booting use WSL. It creates a working Ubuntu (or any other Unix distribution except MacOS). It is primarily just a command line interface which really outshines a GUI for this type of development.

#### Single Ubuntu Boot (Slightly Advanced Users)
Should you have a spare machine lying around install Ubuntu on it.

#### Virtual Machine (Intermediate Advanced Users)
The machine must be fairly powerful with 16 GB RAM (recommended). 8 GB is a 50/50 scenario. The processor and GPU must also support virtualization.

#### Dual Booting (Really Advanced Users)
Should you really know what you are doing you can install Windows and Ubuntu side by side. This means Ubuntu is installed on baremetal

### MacOS
You are on a Unix distribution similar to Ubuntu. Remember to use homebrew in the place of apt; and python3 at all times.
