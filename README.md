# cli-crt
## How to create a cli-tool with python?
Well I will answer the question with my project.

## project overview
This project was born because I was going to find a way to create files quickly with cmd so I make the creator file.

The crt tool based on 4 option:
1) pycrt, python creator
2) jcrt, java creator
3) jcrtcou, java course creator(it is not necessary)
4) cppcrt, cpp creator

The crt tool use 4 argument:
1) -nf(number of files), defualt value: 1
2) -pwd(path where create the files), defualt value: the current path(os.getcwd())
3) -st(index to start of files), defualt value: 0
4) -nm(name of files), defualt value: file

In particular the 4 option create the files with built-in main structure of coding language. 

## How to do create a cli tool with python:

Startly you can install argsparse package, ![install here](https://pypi.org/project/argparse/). You have to define the options of your cli tool as normal function. 
After you have to define the main function. Inside the main function you have to create a object that it pointers to the ArgumentParser, this function will be use to add information of cli-tool.
```py
def main():
  var = argsparse.AgumentParser()
```
To add option you have to use the add_argument method:

```py
var.add_argument(names, choices=[])
```
In to the choices you have to write the option name.

Now you can use the argument:
```py
var.add_argument(name, type)
```

In my case, I used the optional argument so I did about:

```py
var.add_argument(-name, type, default=value, help='about the argument')
```

Before to install the cli-tool you can write a selection block like this:
```py
    if args.names == 'pycrt':
        pycrt(args.nf, args.pwd, args.nm, args.st)
    elif args.names == 'jcrt':
        jcrt(args.nf, args.pwd, args.nm, args.st)
    elif args.names == 'jcrtcou':
        jcrtcou(args.nf, args.pwd, args.nm, args.st)
    elif args.names == 'cppcrt':
        cppcrt(args.nf, args.pwd, args.nm, args.st)
    elif args.names == 'CrtNormal':
        CrtNormal(args.nf, args.pwd, args.nm, args.st)
```
This selection block allows to execute the function according to the typed option.

Now you can use this command:

```
python crt.py [option] [argument]
```

But if you want to use this:

```
crt [option] [argument]
```

You create new setup.py file and you have to write this:
```py
from setuptools import find_packages, setup

setup(
    name='Creator Coding-Files',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['crt=src.crt:main']    # name_command=folder.name_file:name_main_function
    }

)
```

Now you have to install your package locally:

```
pip install -e .
```

Finally you can use your cli-tool!
