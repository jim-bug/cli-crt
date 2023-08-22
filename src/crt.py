import argparse
from os import getcwd

def find_point(s1):
    for i in range(len(s1)):
        if s1[i] == '.':
            return i

def find_char(s1):
    for i in range(len(s1)):
        if s1[i] == '$':
            return i



def pycrt(nf, pwd, name, st):       # python creator
    NAME = name+'.py'
    for i in range(st, nf+st):
        position_point = find_point(name)
        name = f"{name[:position_point]+str(i)}.py"
        file = open(pwd+"/"+name, 'x', encoding='utf-8')
        file.write("print(\'Hello World\'")
        file.close()
        name = NAME


def jcrt(nf, pwd, name, st):       # java creator
    NAME = name+'.java'
    for i in range(st, nf+st):
        position_point = find_point(name)
        name = f"{name[:position_point]+str(i)}.java"
        file = open(pwd+"/"+name, 'x', encoding='utf-8')
        file.write("public class " + name[:position_point]+str(i) + "{\npublic static void main(string[] args){\n\n\t}\n}")
        file.close()
        name = NAME


def jcrtcou(nf, pwd, name, st):      # java course creator
    NAME = name+'.java'
    for i in range(st, nf+st):
        position_char = find_char(name)
        name = f"{name[:position_char]+str(i)+name[position_char+1:]}"
        file = open(pwd+"/"+name, 'x', encoding='utf-8')
        file.write("public class " + name[:position_char]+str(i)+name[position_char+1:-5] + "{\n\npublic static void main(string[] args){\n\n\t}\n}")
        file.close()
        name = NAME


def cppcrt(nf, pwd, name, st):      # cpp creator
    NAME = name+'.cpp'
    for i in range(st, nf+st):
        position_point = find_point(name)
        name = f"{name[:position_point]+str(i)}.cpp"
        file = open(pwd+"/"+name, 'x', encoding='utf-8')
        file.write("#include <iostream>\n\nusing namespace std\n\nint main(){\n\tcout << \'Hello World\';\n\treturn 0;\n}")
        file.close()
        name = NAME


def CrtNormal(nf, pwd, name, st):
    NAME = name
    for i in range(st, nf+st):
        position_point = find_point(name)
        name = f"{name[:position_point]+str(i)}.txt"
        file = open(pwd+"/"+name, 'x', encoding='utf-8')
        file.close()
        name = NAME



def main():
    pars = argparse.ArgumentParser(
        prog='crt',
        usage='%(prog)s [option] [arguments]',
        description="CLI Creator Coding-Files",
        epilog='''
        The crt command can create a number of files that user wants. The file can be indexed for example if I want create 10 file with python extensions and the index starts to 5, I write crt pycrt -nf 10 -st 5.
        Somefiles that it will be create with option: pycrt, cppcrt, jcrt, jcrtcou it will have built-in a main structure of code in that language.

        By Jim_Bug :)
        '''
    )
    pars.add_argument(
        "operation",
        nargs='?',
        default='CrtNormal',
        choices=['pycrt', 'jcrt', 'jcrtcou', 'cppcrt', 'CrtNormal'],
    )      # definisco le opzioni del comando crt
    # L'opzione nargs serve per far si che l'argomento può essere lasciato vuoto in modo tale da far entrare in gioco
    # il parametro default che contiene il valore di default
    pars.add_argument(
        "-nf",
        type=int,
        default=1,
        help="Number of file to create(optional value: 1)"
    )     # definisco ogni caratteristica delle opzioni
    pars.add_argument(
        "-st",
        type=int,
        default=0,
        help="start number of file(optional value: 0)"
    )
    pars.add_argument(
        "-pwd",
        type=str,
        default=getcwd(),
        help=f"pwd where to create file(optional value: {getcwd()})"
    )
    pars.add_argument(
        "-nm",
        type=str,
        default='file',
        help="Name of file(optional value: file)"
    )
    args = pars.parse_args()
    if args.operation == 'pycrt':
        pycrt(args.nf, args.pwd, args.nm, args.st)
    elif args.operation == 'jcrt':
        jcrt(args.nf, args.pwd, args.nm, args.st)
    elif args.operation == 'jcrtcou':
        args.name = "Lezione$CorsoJava8.java"
        jcrtcou(args.nf, args.pwd, args.nm, args.st)
    elif args.operation == 'cppcrt':
        cppcrt(args.nf, args.pwd, args.nm, args.st)
    elif args.operation == 'CrtNormal':
        CrtNormal(args.nf, args.pwd, args.nm, args.st)
    print("The Operation Was Successful :)")


if __name__ == '__main__':
    main()
