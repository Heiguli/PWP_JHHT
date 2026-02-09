You should be using virtual Python environment to use this database, to not mess up with your own python environment locally installed in your PC/laptop. First the python virtual environment used was obtained by: (These are taken (copied) from the lovelace exercise 1 page, https://lovelace.oulu.fi/ohjelmoitava-web/ohjelmoitava-web/introduction-to-web-development/)

Starting with version 3.3 of Python, all the necessary tools are automatically included. In case they are not, you need to install Pip (https://pip.pypa.io/en/stable/installation/) and use it to install the venv module. In order to create a virtual environment, all you need to do is to type

python3 -m venv /path/to/the/virtualenv

on OS X and most Linux distributions you need to use python3 instead (running the above command on Python 2 will result in an error message that says "No module named venv"). The virtualenv will be a normal folder on your file system. In order to activate it in Windows, type:

c:\path\to\the\virtualenv\Scripts\activate.bat

in OS X or Linux:

source /path/to/the/virtualenv/bin/activate

After which you will see the name of your virtualenv in parenthesis in front of your command prompt. E.g. if we made an environment called "pwp-env" in the home directory, a command prompt would look like: (pwp-env) user@system:~/pwp-env$

Dependencies:
Next are the dependencies we need to be able to run this database from our virtual environment. Basically, just type in, for example, in cmd when you are IN your virtual environment the "pip install x" and you will instal depency for your virtual environment.  
- Flask==3.1.2  
  Install: `pip install Flask`  
- Flask-SQLAlchemy==3.1.1  
  Install: `pip install Flask-SQLAlchemy`  
- SQLAlchemy==2.0.46  
  Install: `pip install SQLAlchemy`  
- pysqlite3==0.6.0  
  Install: `pip install pysqlite3`

We used SQLite database and the version we used was 3.1.1.

This database might not be the FINAL FINAL version of the database, since it will probably get some little tweaks or little improvements. But the idea and ground work behind the database and how it will work is implemented and it will be the same in the final version.

To use the database locally and try it out, it is as simple, as the following:

In the folder where your virtual environment is located, create a new folder that is named to your liking. To this created folder, add the database.py file, and the populate_dp.py file. In cmd, when you are using virtual environment, locate the folder where your virtual environment is located. Then, in your cmd, type python database.py to create the test.db file. And then you can populate it with command: python populate_dp.py file. This populates the database with the data in the populate_dp.py file You can change the data to your liking. 

