#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importar las herramientas de lex y yacc de ply

from ply import lex
import ply.yacc as yacc
import sys


# In[2]:


#Definir los tokens de la gramática
reserved = {'program' :"PROGRAM",
'if':"IF",
'else' :"ELSE",
'print' :"PRINT",
'int' :"INT",
'var' :"VAR",
'float' :"FLOAT"}

tokens=[
"CTE_INT",
"CTE_FLOAT",
"CTE_STRING",
"ID",
"COLON",
"SEMICOLON",
"COMMA",
"EQ",
"OPENPAR",
"CLOSEPAR",
"GT",
"LT",
"PLUS",
"MINUS",
"MUL",
"DIV",
"OPENCUR",
"CLOSECUR"] + list(reserved.values())

#Aplicar regex
#t_PROGRAM = (r"[pP][rR][oO][gG][rR][aA][mM]")
#t_IF = (r"[iI][fF]")
#t_ELSE = (r"[eE][lL][sS][eE]")
#t_PRINT = (r"[pP][rR][iI][nN][tT]")
#t_INT = (r"[iI][nN][tT]")
#t_VAR = (r"[vV][aA][rR]")
#t_FLOAT = (r"[fF][lL][oO][aA][tT]")

t_CTE_INT = (r"[0-9]+")
t_CTE_FLOAT = (r"[0-9]+\.[0-9]+([eE][+-]?[0-9]+)?")
t_CTE_STRING = ("\"[^\"]+\"")
def t_ID(t): 
    r"[a-zA-Z]([a-zA-Z]|[0-9])*"
    t.type =  reserved.get(t.value,'ID')
    return t
t_COLON = (":")
t_SEMICOLON = (";")
t_COMMA = (",")
t_EQ = ("=")
t_OPENPAR = ("\(")
t_CLOSEPAR = ("\)")
t_GT = ("<")
t_LT = (">")
t_PLUS = ("\+")
t_MINUS = ("\-")
t_MUL = ("\*")
t_DIV = ("/")
t_OPENCUR = ("{")
t_CLOSECUR = ("}")
t_ignore  = ' \t'
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value) 

def t_error(t):
     print("Token Invalido '%s'" % t.value[0])


lexer = lex.lex()




#precedencia
precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'MUL', 'DIV' ),
    ( 'nonassoc', 'GT', 'LT' )
)

def p_PROGRAMA(p):
    '''PROGRAMA : PROGRAM ID COLON VARS BLOQUE
                | PROGRAM ID COLON  BLOQUE'''
    
    
def p_BLOQUE(p):
    '''BLOQUE : OPENCUR ESTATUTOS CLOSECUR
              | OPENCUR ESTATUTO CLOSECUR'''
    
    
def p_VARS(p):
    'VARS : VAR ID VARCOMMA COLON TIPO SEMICOLON'
    
    
def p_VARCOMMA(p):
    '''VARCOMMA : COMMA ID VARCOMMA
                | empty'''
    
    
def p_TIPO(p):
    '''TIPO : FLOAT
            | INT'''
    
    
def p_ESTATUTOS(p):
    '''ESTATUTOS : ESTATUTO ESTATUTOS
                 | empty'''
    
    
def p_ESTATUTO(p):
    '''ESTATUTO : ASIGNACION
                | CONDICION
                | ESCRITURA'''
    
    
def p_ASIGNACION(p):
    'ASIGNACION : ID EQ EXPRESION SEMICOLON'
    
    
def p_CONDICION(p):
    'CONDICION : IF OPENPAR EXPRESION CLOSEPAR BLOQUE IFELSE SEMICOLON'
    
    
def p_IFELSE(p):
    '''IFELSE : ELSE BLOQUE
              | empty'''
    
    
def p_ESCRITURA(p):
    'ESCRITURA : PRINT OPENPAR PRINTABLE PRINTARG CLOSEPAR SEMICOLON'
    
    
def p_PRINTARG(p):
    '''PRINTARG : COMMA PRINTABLE PRINTARG
                | empty'''
    
    
def p_PRINTABLE(p):
    '''PRINTABLE : CTE_STRING
                 | EXPRESION'''
    
    
def p_EXPRESION(p):
    '''EXPRESION : EXP
                 | EXP GT EXP
                 | EXP LT EXP
                 | EXP GT LT EXP'''
    
    
def p_EXP(p):
    '''EXP : TERMINO TERMINOS
           | TERMINO '''
    
    
def p_TERMINOS(p):
    '''TERMINOS : PLUS TERMINO TERMINOS
                | MINUS TERMINO TERMINOS
                | empty'''
    
    
def p_TERMINO(p):
    '''TERMINO : FACTOR FACTORES
               | FACTOR'''
    
    
def p_FACTORES(p):
    '''FACTORES : MUL FACTOR FACTORES
                | DIV FACTOR FACTORES
                | empty'''
    
    
def p_FACTOR(p):
    '''FACTOR : SIGNOVAR VARCTE
              | OPENPAR EXPRESION CLOSEPAR'''
    
    
def p_SIGNOVAR(p):
    '''SIGNOVAR : PLUS
                | MINUS
                | empty'''
    
    
def p_VARCTE(p):
    '''VARCTE : ID
            | CTE_INT
            | CTE_FLOAT'''
    

def p_empty(p):
     'empty :'
     pass

def p_error(p):
    print("Error de sintaxis con el simbolo %r en la linea %r" % (p.value,p.lexer.lineno))
    raise TypeError("Error de sintaxis con el simbolo %r en la linea %r" % (p.value,p.lexer.lineno))
    
parser = yacc.yacc()

#Leer de archivo
myFile = open(sys.argv[1])
try:
    parser.parse(myFile.read())
except TypeError:
    print("No es lenguaje valido!!!!")
else:
    print('aceptado')




