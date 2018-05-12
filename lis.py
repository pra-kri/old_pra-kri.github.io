# Will attempt to run through Peter Norvig's guide to writing a LISP interpreter in Python. 
# Hopefully I'll understand something about interpreters by the end of it... I'll also try to add some of my own modifications, 
# or write the functions in a different way, to make sure I understand what is being done.





"""
General ideas:
- Parse the inputted program into small atomic bits
- Each atomic bit should mean something - either a string, a number, an expression...etc
- Using the structure of the inputted program, construct an abstract syntax tree.
- Alongside all of ths, create an 'environment'. This tells you the range of operators you can use in the program. The environment will map onto a bunch of functions/operators that are part of the original language.
- Then, start working through the Abs.Syn.Tree, and evaluate the result of the tree, using the 'environment' to see which functions you should use.
- Thats all. At a high level, evaluating a syntax tree is essentially what you do when you run a program.

- construct a tree fropm the input text
- evaluate the tree using your environment mapping

"""


# Scheme objects on the LeftHandSide, and what is used in Python to represent them (on the RHS)
Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Exp = (Atom, List)
Env = dict


# =========================================
# ======= PARSING =========================
# =========================================


def tokenize(chars: str) -> list:
    """ 
    Converts a str into a list of tokens.
    The 'str' within the function brackets tells us that the input must be a string. And the '-> list' tells us that the output will be a list.
    """
    #inserts spaces around any ( it sees
    tokenized_str = chars.replace('(', ' ( ')
    #inserts spaces around any ) it sees
    tokenized_str = tokenized_str.replace(')', ' ) ')
    # splits the str into a list. delimited by spaces
    tokenized_list = tokenized_str.split()

    #return chars.replace('(', ' ( ').replace(')', ' ) ').split()
    return tokenized_list

#TEST: testing to see if tokenize works properly
print(tokenize('woooah(aaa(zzzzzzz))'))



def atom(token :str) -> Atom:
    """ 
    Numbers will stay as numbers (either int or float).
    Any other character will become a symbol.
    """

    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)



def read_from_tokens(tokens: list) -> Exp:

    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')

    

    # creates a tree to represent the program
    # each time it sees a '(', creates a new list.
    # if it sees a '(' within another pair of brackets, then it creates a list within a list, basically.
    # Tree ----> represented by List of lists.


    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) #gets rid of the ')'
        return L
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return atom(token)



def parse(program: str) -> Exp:
    """
    Read scheme expr. from string
    """

    return read_from_tokens(tokenize(program))




program = "(begin (define r 10) (* pi (* r r)))"
print(parse(program))
# now, when we parse this, it gives us a list of lists, representing the 'abstract syntax tree'


# =========================================
# ======= ENVIRONMENTS ====================
# =========================================

# An environment is just a mapping from VARIABLE NAME --> VALUES.

import math
import operator as op 


def standard_env() -> Env:
    # dictionary. Key value pairs will represent the mapping of Varibale Name to Values
    env = Env()
    env.update(vars(math))

    # LHS = bunch of operators that should be available in LISP
    # RHS = how the LHS is implemented in Python
    env.update({

        '+':op.add,
        '-':op.sub,
        '*':op.mul,
        '/':op.truediv,
        '>':op.gt,
        '<':op.lt,
        '>=':op.ge,
        '<=':op.le,
        '=':op.eq,
        'abs':abs,
        'append':op.add,
        'apply': (lambda proc, args: proc(*args)),
        'begin': (lambda *x : x[-1]),
        'car': (lambda x: x[0]),
        'cdr': (lambda x: x[1:]),
        'cons': (lambda x,y: [x] + y),
        'eq?': op.is_,
        'expt': pow,
        'equal?': op.eq,
        'length': len,
        'list': (lambda *x: List(x)),
        'list?': (lambda x: isinstance(x, List)),
        'map': map,
        'max': max,
        'min': min,
        'not': op.not_,
        'null?': (lambda x: x == []),
        'number?': (lambda x: isinstance(x, Number)),
        'print': print,
        'procedure?': callable,
        'round': round,
        'symbol': (lambda x: isinstance(x, Symbol)),

    })

    return env
global_env = standard_env()

#print(global_env)
#print(vars(math))
#print(standard_env())


# =========================================
# ======= EVALUATION ======================
# =========================================

# Will now define the eval() function.
# eval() can process 1 of the 5 types of instances below:
# - symbol
# - number
# - conditional (i.e. 'if')
# - definition ('define' - this is similar to python's 'def')
# - procedure call (like when you call a function in python...)


def eval(x: Exp, env = global_env) -> Exp:
    """
    Evaluates an expression IN an environment.
    Note there may be different environments that would evaluate expressions slighly differently. Different env.s are kind of like different dialects (i think...?)
    """

    if isinstance(x, Symbol):
        return env[x]
        # tries to see if there is the appropriate key found in teh dictionary

    elif not isinstance(x, Number):
        return x
        # just return a number if its a number...

    elif x[0] == 'if':
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
        # implementing 'if/else' statements

    elif x[0] == 'define':
        (_, symbol, exp) = x
        env[symbol] = eval(exp, env)

    else:
        proc = eval(x[0], env)
        args = [eval(arg, env) for arg in x[1:]]
        return proc(*args)


print('aaaaaaaaaaaa')
jj = eval(parse(program))
print(jj)

print(eval(parse("(+ 4 5)")))


# TODO: eval() isnt quite working properly... need to fix this...
