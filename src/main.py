import sys
import re

def loader():
    f = open(sys.argv[1],'r')
    src = f.read()
    f.close()
    return src

def lexer(src):
    tokens = re.split('(".*?"|output|var|=|check)|\n|\s|\t| ',src)
    if '' in tokens:
        for i in range(tokens.count('')):
            tokens.remove('')
    if None in tokens:
        for qw in range(tokens.count(None)):
            tokens.remove(None)
    if ' ' in tokens:
        for r in range(tokens.count(' ')):
            tokens.remove(' ')
    if '  ' in tokens:
        for t in range(tokens.count('  ')):
            tokens.remove('  ')
    if '    ' in tokens:
        for a in range(tokens.count('    ')):
            tokens.remove('    ')
    tokens.append('pendp')
    return tokens

def parser(tokens):
    pc = 0
    varname = []
    var = {}  #var
    while tokens[pc] != 'pendp':
        if tokens[pc] == 'output':
            pc += 1
            if tokens[pc] == '(':
                pc += 1
                moji = tokens[pc].strip('"')
                pc += 1
                if tokens[pc] == ')':
                    print(moji)
                    pc += 1
                else:
                    print('output error : ")" is required at the end')
                    pc += 1
            else:
                why=tokens[pc].strip('()')
                if why.isdecimal():
                    print(why)
                    pc += 1
                elif why in varname:
                    print(var[why])
                    pc += 1
                else:
                    print('output error')
                    pc += 1
        elif tokens[pc] == 'var':
            pc += 1 #var (name) = core
            name = tokens[pc]
            pc += 1 #var name (=) core
            if tokens[pc] == '=':
                pc += 1
                core = tokens[pc]
                varname.append(name)
                try:
                    core = int(core)
                except ValueError:
                    pass
                var[name] = core
                pc += 1
            else:
                print('"=" ?')
                pc += 1
        elif tokens[pc] == 'check':
            pc += 1
            if tokens[pc] == '(':
                pc += 1
                core = tokens[pc]
                pc +=1
                if tokens[pc] == ')':
                    if type(core) == str:
                        print('String')
                        pc += 1
                    if core.isdecimal():
                        print('Int')
                        pc += 1
                    if type(core) == list:
                        print('List')
                        pc += 1
            else:
                w = tokens[pc].strip('()')
                if w in var:
                    if type(var[w]) == str:
                        print("String")
                        pc += 1
                    if type(var[w]) == int:
                        print("Int")
                        pc += 1
                    if type(var[w]) == list:
                        print('List')
                        pc +=1
        else:
            print('Syntax error')
            pc += 1






src = loader()
tokens = lexer(src)
print(tokens)
parser(tokens)
