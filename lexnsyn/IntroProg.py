
#    Nombre: IntroProg.py
#    Descripción: Una implementación del lexer y parser usando python y ply para el compliador
#    Por: Luis Fernando Lomelín Ibarra

#importar las herramientas de lex y yacc de ply

from ply import lex
import ply.yacc as yacc
import sys
import re


# Variables importantes
sem_err = False # Evitar imprmir aceptado cuando se detectan errores
#entero, bool flotante char cadena vacio nulo error
cubosem = {
           '=':{'entero':{
                          'entero':'entero',
                          'flotante': 'entero',
                          'char':'entero',
                          'bool': 'entero',
                          'cadena':'error'
                        },
                'flotante':{
                          'entero':'flotante',
                          'flotante': 'flotante',
                          'char':'flotante',
                          'bool': 'flotante',
                          'cadena':'error'
                        },
                'char':{
                          'entero':'char',
                          'flotante': 'char',
                          'char':'char',
                          'bool': 'char',
                          'cadena':'error'
                        },
                'bool':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'cadena':{
                          'entero':'error',
                          'flotante': 'error',
                          'char':'error',
                          'bool': 'error',
                          'cadena':'cadena'
                        },

                },
           '||':{
               'entero':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'flotante':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'char':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'bool':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'cadena':{
                          'entero':'error',
                          'flotante': 'error',
                          'char':'error',
                          'bool': 'error',
                          'cadena':'bool'
                        },
           },
           '&&':{
                'entero':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'flotante':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'char':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'bool':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'cadena':{
                          'entero':'error',
                          'flotante': 'error',
                          'char':'error',
                          'bool': 'error',
                          'cadena':'bool'
                        },
           },
           '<':{
                'entero':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'flotante':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'char':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'bool':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'cadena':{
                          'entero':'error',
                          'flotante': 'error',
                          'char':'error',
                          'bool': 'error',
                          'cadena':'bool'
                        },
           },
           '>':{
                'entero':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'flotante':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'char':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'bool':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'cadena':{
                          'entero':'error',
                          'flotante': 'error',
                          'char':'error',
                          'bool': 'error',
                          'cadena':'bool'
                        },
           },
           '<=':{
                'entero':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'flotante':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'char':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'bool':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'cadena':{
                          'entero':'error',
                          'flotante': 'error',
                          'char':'error',
                          'bool': 'error',
                          'cadena':'bool'
                        },
           },
           '>=':{
                'entero':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'flotante':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'char':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'bool':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'cadena':{
                          'entero':'error',
                          'flotante': 'error',
                          'char':'error',
                          'bool': 'error',
                          'cadena':'bool'
                        },
           },
           '!=':{
                'entero':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'flotante':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'char':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'bool':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'cadena':{
                          'entero':'error',
                          'flotante': 'error',
                          'char':'error',
                          'bool': 'error',
                          'cadena':'bool'
                        },
           },
           '==':{
                'entero':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'flotante':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'char':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'bool':{
                          'entero':'bool',
                          'flotante': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'cadena':{
                          'entero':'error',
                          'flotante': 'error',
                          'char':'error',
                          'bool': 'error',
                          'cadena':'bool'
                        },
           },
           '+':{
                'entero':{
                          'entero':'entero',
                          'flotante': 'flotante',
                          'char':'entero',
                          'bool': 'entero',
                          'cadena':'error'
                        },
                'flotante':{
                          'entero':'flotante',
                          'flotante': 'flotante',
                          'char':'flotante',
                          'bool': 'flotante',
                          'cadena':'error'
                        },
                'char':{
                          'entero':'entero',
                          'flotante': 'flotante',
                          'char':'entero',
                          'bool': 'entero',
                          'cadena':'error'
                        },
                'bool':{
                          'entero':'entero',
                          'flotante': 'flotante',
                          'char':'entero',
                          'bool': 'entero',
                          'cadena':'error'
                        },
                'cadena':{
                          'entero':'error',
                          'flotante': 'error',
                          'char':'error',
                          'bool': 'error',
                          'cadena':'cadena'
                        },
                'none' : {
                    'entero' : 'entero',
                    'flotante' : 'flotante',
                    'char' : 'error',
                    'bool' : 'error',
                    'cadena' : 'error'
                }
           },
           '-':{
                'entero':{
                          'entero':'entero',
                          'flotante': 'flotante',
                          'char':'entero',
                          'bool': 'entero',
                          'cadena':'error',
                        },
                'flotante':{
                          'entero':'flotante',
                          'flotante': 'flotante',
                          'char':'flotante',
                          'bool': 'flotante',
                          'cadena':'error'
                        },
                'char':{
                          'entero':'entero',
                          'flotante': 'flotante',
                          'char':'entero',
                          'bool': 'entero',
                          'cadena':'error'
                        },
                'bool':{
                          'entero':'entero',
                          'flotante': 'flotante',
                          'char':'entero',
                          'bool': 'entero',
                          'cadena':'error'
                        },
                'cadena':{
                          'entero':'error',
                          'flotante': 'error',
                          'char':'error',
                          'bool': 'error',
                          'cadena':'error'
                        },
                'none' : {
                    'entero' : 'entero',
                    'flotante' : 'flotante',
                    'char' : 'error',
                    'bool' : 'error',
                    'cadena' : 'error'
                }

           },
           '*':{
                'entero':{
                          'entero':'entero',
                          'flotante': 'flotante',
                          'char':'entero',
                          'bool': 'entero',
                          'cadena':'error'
                        },
                'flotante':{
                          'entero':'flotante',
                          'flotante': 'flotante',
                          'char':'flotante',
                          'bool': 'flotante',
                          'cadena':'error'
                        },
                'char':{
                          'entero':'entero',
                          'flotante': 'flotante',
                          'char':'entero',
                          'bool': 'entero',
                          'cadena':'error'
                        },
                'bool':{
                          'entero':'entero',
                          'flotante': 'flotante',
                          'char':'entero',
                          'bool': 'entero',
                          'cadena':'error'
                        },
                'cadena':{
                          'entero':'error',
                          'flotante': 'error',
                          'char':'error',
                          'bool': 'error',
                          'cadena':'error'
                        },
           },
           '/':{
               'entero': {
                   'entero': 'entero',
                   'flotante': 'flotante',
                   'char': 'entero',
                   'bool': 'entero',
                   'cadena': 'error'
               },
               'flotante': {
                   'entero': 'flotante',
                   'flotante': 'flotante',
                   'char': 'flotante',
                   'bool': 'flotante',
                   'cadena': 'error'
               },
               'char': {
                   'entero': 'entero',
                   'flotante': 'flotante',
                   'char': 'entero',
                   'bool': 'entero',
                   'cadena': 'error'
               },
               'bool': {
                   'entero': 'entero',
                   'flotante': 'flotante',
                   'char': 'entero',
                   'bool': 'entero',
                   'cadena': 'error'
               },
               'cadena': {
                   'entero': 'error',
                   'flotante': 'error',
                   'char': 'error',
                   'bool': 'error',
                   'cadena': 'error'
               },

           },
            'arr':{'entero':{
                          'entero':'entero',
                          'flotante': 'flotante',
                          'char':'entero',
                          'bool': 'entero',
                          'cadena':'error'
                        },
                'flotante':{
                          'entero':'flotante',
                          'flotante': 'flotante',
                          'char':'flotante',
                          'bool': 'flotante',
                          'cadena':'error'
                        },
                'char':{
                          'entero':'entero',
                          'flotante': 'flotante',
                          'char':'char',
                          'bool': 'entero',
                          'cadena':'error'
                        },
                'bool':{
                          'entero':'entero',
                          'flotante': 'flotante',
                          'char':'entero',
                          'bool': 'bool',
                          'cadena':'error'
                        },
                'cadena':{
                          'entero':'error',
                          'flotante': 'error',
                          'char':'error',
                          'bool': 'error',
                          'cadena':'cadena'
                        },
            }


           }

#Pila de Operadores
poper = ['?']
#Pila de operandos
pilaoperand = ['?']
#Pila tipos
ptipo = ['?']


#funciones especiales
special = {'leer':{'tipo':'vacio'}}

#Definir los tokens de la gramática
reserved = {'programa' :"PROGRAM",
    'funcion':"FUNCION",
    'si':"SI",
    'sino':"SINO",
    'mientras':"MIENTRAS",
    'por':"POR",
    'entero':"ENTERO",
    'flotante':"FLOTANTE",
    'char':"CHAR",
    #'cadena':"CADENA",
    'bool':"BOOL",
    'vacio':"VACIO",
    'nulo':"NULO",
    'verdadero':"CTE_BOOL",
    'falso':"CTE_BOOL",
    'principal':"PRINCIPAL",
    'leer':"LEER",
    'imprimir':"IMPRIMIR",
    'regresar' : "REGRESAR",

}

tokens=[
"CTE_INT",
"CTE_FLOAT",
"CTE_CHAR",
"CTE_STRING",
"ID",
"COLON",
"SEMICOLON",
"COMMA",
"EQ",
"EXLAM",
"OPENPAR",
"CLOSEPAR",
"GT",
"LT",
"PLUS",
"MINUS",
"MUL",
"DIV",
"OPENCUR",
"CLOSECUR",
"OPENSQU",
"CLOSESQU",
"AND",
"OR",
"DLR"] + list(reserved.values())

#Aplicar regex
#t_PROGRAM = (r"[pP][rR][oO][gG][rR][aA][mM]")
#t_IF = (r"[iI][fF]")
#t_ELSE = (r"[eE][lL][sS][eE]")
#t_PRINT = (r"[pP][rR][iI][nN][tT]")
#t_INT = (r"[iI][nN][tT]")
#t_VAR = (r"[vV][aA][rR]")
#t_FLOAT = (r"[fF][lL][oO][aA][tT]")


#t_CTE_FLOAT = (r"[0-9]+\.[0-9]+([eE][+-]?[0-9]+)?")
def t_CTE_FLOAT(t):
    r"[0-9]+\.[0-9]+([eE][+-]?[0-9]+)?"
    t.value = float(t.value)
    return t

#t_CTE_INT =(r"[0-9]+")
def t_CTE_INT(t):
    r"[0-9]+"
    t.value = int(t.value)
    return t





t_CTE_CHAR = ("\'[^\']\'")
#t_CTE_STRING = ("\"[^\"]+\"")

def t_CTE_STRING(t):
    "\"[^\"]+\""
    #print(t.value)
    return t

def t_ID(t): 
    r"[a-zA-Z]([a-zA-Z]|[0-9]|[_])*"

    t.type = reserved.get(t.value,'ID')
    #print("Recognized as ID : " + t.value + " as type "+t.type)
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
t_OPENSQU = (r"\[")
t_CLOSESQU = (r"\]")
t_AND = (r"\&\&")
t_OR = (r"\|\|")
t_EXLAM = (r"!")
t_DLR = (r"\$")
t_ignore  = ' \t'

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value) 

def t_error(t):
     print("Token Invalido '%s' en la linea %r" % (t.value[0],t.lexer.lineno) )


lexer = lex.lex()




#precedencia
precedence = (
    ('right','EQ' ),
    ( 'nonassoc', 'GT', 'LT','AND','OR'),
    ( 'left', 'PLUSMINUS' ),
    ( 'left', 'MULDIV' ),
    )

########################################################################################################

#Dir de func
dirfunc = {}
#Current scope
currscope = None
#para saber cuales parametros evualuar en llamada de funcion
funcallcurr = None

#Para generar los cuadruplos temporalmente asignar un registro de manera acendente al cuadruplo
regcount = 0

#Cuadruplos
cuadruplos = []


#Estructura del programa
def p_PROGRAMA(p):
    '''PROGRAMA : PROGRAM ID OPENCUR DECGLOB DECTODASFUNC PRINCIPAL FUNCION PRINSCOPE BLOQUE CLOSECUR '''


    global dirfunc

    #1.- Crear el directorio de funciones
    dirfunc['global'] = {'vartab':{}}
    #2.- Si se encuentran declaraciones globales se debe de crear una tabla de symbolos a nivel global
    # Este es encapsulado en la regla dirfunc

    global sem_err
    #3.- Si se encuentran funciones darlas de alta en el dir de funciones
    #print(p[5])
    if(p[5] != None):
        # 4.- Checar que no se repitan los nombres de variables globales en las funciones locales
        #print("Funciones : %r" % p[5])
        for kfun in p[5].keys():
            funvars = p[5][kfun]['vartab']
            for varnam in funvars:
                if varnam in dirfunc['global']['vartab'].keys():
                    print("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (varnam, p.lineno(5)))

                    sem_err = True
                    raise (SyntaxError(
                        "Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (varnam, p.lineno(5))))

        dirfunc.update(p[5])



    #4.- Checar si la declaración de las var locales de pricipal ya existen



    #4.- Borrar si se llega al final del programa.
    print(dirfunc)

def p_PRINSCOPE(p):
    '''PRINSCOPE : OPENCUR DECLARACIONES CLOSECUR'''
    global currscope
    global dirfunc
    currscope = 'principal'
    print('\n\n\n\n--------------------------------------------------------\nLLego a scope global\n---------------')
    if (p[2] != None):
        ks = p[2].keys()
        if dirfunc['global']['vartab'] != None:
            if len(dirfunc['global']['vartab']) > 0 :
                print('a', p[2], dirfunc['global']['vartab'])
                for k in ks:
                    if k in dirfunc['global']['vartab'].keys():
                        print(
                            "Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (
                            k, p.lineno(9)))

                        sem_err = True
                        raise (SyntaxError(
                            "Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (
                            k, p.lineno(9))))
    dirfunc['principal'] = {'vartab':p[2]}
    #dirfunc['global']['vartab'].update(p[2])
    p[0] = p[2]

###########
# Declaraciones Arreglos y variables
##########

def p_DECGLOB(p):
    '''DECGLOB : DECLARACIONES'''
    global dirfunc
    dirfunc['global'] = {'tipo': 'vacio', 'params:': None, 'vartab': p[1]}


def p_DECLARACIONES(p):
    '''DECLARACIONES : DECLARACION DECLARACIONES
                     | empty'''
    if (p[1] == None):
        p[0] = None
    else:
        vartab = {}
        vartab.update(p[1])

        if(p[2] != None):
            checkexistance = p[1].keys()
            for k in checkexistance:
                #print(p[2].keys())
                #print(k)
                if(k in p[2].keys()):
                    #print(p[2].keys())
                    print("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (k, p.lineno(2)))
                    global sem_err
                    sem_err = True
                    raise (SyntaxError("Error de Semantica la variable %r tiene una o más definicionesen la linea %r" % (k, p.lexer.lineno)))
            #print( "P[1] contiene %r y p[2] contiene %r" % (p[1].keys(),p[2].keys()))

            vartab.update(p[2])
        #knownvars.update(vartab)
        p[0] = vartab

    #Generar y regresar una tabla de variables que va  a ser ligada a una
def p_DECLARACION(p):
    '''DECLARACION : DECVAR
                   | DECARR '''
    p[0] = p[1]

def p_DECVAR(p):
    '''DECVAR : TIPO ID DVNID SEMICOLON'''
    newvars = {p[2] : {'tipo': p[1]}}
    if(p[3] != None):
        for varid in p[3]:
            if(varid in newvars):
                print("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (varid, p.lineno(3)))
                global sem_err
                sem_err = True
                raise(SyntaxError("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (varid, p.lineno(3))))
            newvars[varid] = {'tipo': p[1]}

    p[0] = newvars

def p_DVNID(p):
    '''DVNID : COMMA ID DVNID
             | empty'''
    if p[1] == None:
        p[0] = None
    else:
        vars = [p[2]]

        if(p[3] != None):
            #print("Checkin if %r is in %r" % (p[2],p[3]))
            if p[2] in p[3]:

                print("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (p[2],p.lexspan(3)))
                global sem_err
                sem_err = True
                raise (SyntaxError("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (p[2],p.lineno(3))) )
            else:
                vars = vars + p[3]
            #print(vars)
        p[0] = vars


def p_DECARR(p):
    '''DECARR : TIPO ID OPENSQU CTE_INT CLOSESQU DSEG SEMICOLON'''
    vararr = {p[2]:{'tipo':p[1], 'dims':1, 'dim1len':p[4]}}
    if(p[6] != None):
        vararr[p[2]].update(p[6])
    p[0] = vararr

def p_DSEG(p):
    '''DSEG : OPENSQU CTE_INT CLOSESQU DTER
            | empty'''
    if(p[1] == None):
        p[0] = None
    else:
        decdims = {'dims':2,'dim2len':p[2]}
        if(p[4]!=None):
            decdims.update(p[4])
        p[0] = decdims

def p_DTER(p):
    '''DTER : OPENSQU CTE_INT CLOSESQU
            | empty'''
    if (p[1] == None):
        p[0] = None
    else:
        decdims = {'dims': 3, 'dim3len': p[2]}
        p[0] = decdims

def p_TIPO(p):
    '''TIPO : ENTERO
            | FLOTANTE
            | CHAR
            | BOOL''' 
    p[0] = p[1]
#######
# Declaracion Funciones
#######

def p_DECTODASFUNC(p):
    '''DECTODASFUNC : DECFUNC DECTODASFUNC
                    | empty'''
    #print('decfuns')

    if(p[1] == None):
        p[0] = p[1]
    else:
        entfuncs = {}
        entfuncs.update(p[1])

        #Checar que las funciones no se repitan
        if (p[2] != None):
            for fu in p[1].keys():
                if fu in p[2].keys():
                    print("Error de Semantica la funcion %r tiene una o más definiciones en la linea %r" % (fu, p.lineno(2)))
                    global sem_err
                    sem_err = True
                    raise (SyntaxError("Error de Semantica la funcion %r tiene una o más definiciones en la linea %r" % (fu, p.lineno(2))))
            if not sem_err:
                entfuncs.update(p[2])

        p[0] = entfuncs



def p_DECFUNC(p):
    '''DECFUNC :  ALTADECFUN BLOQUE '''
    p[0] = p[1]

def p_ALTADECFUN(p):
    ''' ALTADECFUN : FUNCION TIPOFUN ID OPENPAR FUNPARAM CLOSEPAR OPENCUR DECLARACIONES CLOSECUR'''
    # print('Lee una dec funcion')

    entradafun = {p[3]: {'tipo': p[2]}}
    global dirfunc
    global currscope
    currscope = p[3]
    dirfunc.update({p[3]: {'tipo': p[2]}})
    vartabloc = {}
    # Si hay parametros agregarlos a la entrada de la tabla y a la tabla de variables local
    if (p[5] != None):
        vartabloc.update(p[5])
        #print('Add params to vartab')
        entradafun[p[3]].update({'vartab': vartabloc})
        entradafun[p[3]].update({'params': p[5]})
    dirfunc.update(entradafun)
    # Checar que los id de parametros no sean declarados localmente (doble def)
    #print(p[3])

    if (p[8] != None):
        # print(p[8])
        # if(len(vartabloc) > 0):
        for var in vartabloc.keys():
            if (var in p[8].keys()):
                print("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (
                var, p.lineno(8)))
                global sem_err
                sem_err = True
                raise (SyntaxError("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (
                var, p.lineno(8))))

        vartabloc.update(p[8])

    entradafun[p[3]].update({'vartab': vartabloc})
    dirfunc.update(entradafun)


    p[0] = entradafun
    # print(p[0])

def p_TIPOFUN(p):
    '''TIPOFUN : TIPO
               | VACIO'''
    #print('Llego a tipo')
    p[0] = p[1]

def p_FUNPARAM(p):
    '''FUNPARAM : PARAM
                | empty'''
    p[0] = p[1]
    #global knownvars
    #knownvars.update(p[0])

def p_PARAM(p):
    '''PARAM : TIPO ID PARAMD PARAMS '''
    funpar = {p[2] : {'tipo' : p[1]}}
    #Si tiene dims
    if(p[3] != None):
        funpar[p[2]].update(p[3])
    # hay más parametros despues de esta
    if(p[4]!=None):
        if(p[2] in p[4].keys()):
            print("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (p[2], p.lineno(4)))
            global sem_err
            sem_err = True
            raise (SyntaxError("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (p[2], p.lineno(4))))
        else:
            funpar.update(p[4])
    p[0] = funpar

def p_PARAMS(p):
    '''PARAMS : COMMA PARAM
              | empty'''
    if(p[1] != None):
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_PARAMD(p):
    '''PARAMD : OPENSQU CLOSESQU PDSEG
              | empty'''
    pdim = {'dims':1}
    if(p[1] == None):
        p[0] = p[1]
    else:

        if(p[3] != None):
            pdim.update(p[3])
        p[0] = pdim

def p_PDSEG(p):
    '''PDSEG : OPENSQU CLOSESQU PDTER
              | empty'''
    pdim = {'dims': 2}
    if (p[1] == None):
        p[0] = p[1]
    else:
        if (p[3] != None):
            pdim.update(p[3])
        p[0] = pdim

def p_PDTER(p):
    '''PDTER : OPENSQU CLOSESQU 
             | empty'''
    pdim = {'dims': 3}
    if (p[1] == None):
        p[0] = p[1]
    else:

        p[0] = pdim


######
# Declaración Bloque
######

def p_BLOQUE(p):
    '''BLOQUE : OPENCUR ESTATUTOS CLOSECUR'''
    
  
def p_ESTATUTOS(p):
    '''ESTATUTOS : ESTATUTO ESTATUTOS
                 | empty'''
    #global dirfunc
    #print('knowvars',dirfunc,'\n\n')

#######
# Declaración Estatutos
#######

def p_ESTATUTO(p):
    '''ESTATUTO : IMPRESION
                | ASIGNACION
                | EXPRESION SEMICOLON
                | CONDICION
                | BUCLE
                | RETURNF
                | LEER'''

# Impresion -------------------------  
def p_IMPRESION(p):
    '''IMPRESION : IMPRIMIR OPENPAR PRINTABLE PRINTARGS CLOSEPAR SEMICOLON'''    

def p_PRINTARGS(p):
    '''PRINTARGS : COMMA PRINTABLE PRINTARGS
                 | empty'''

def p_PRINTABLE(p):
    '''PRINTABLE : EXPRESION
                 | CTE_STRING
                 | ARR_TEX'''

# Asignacion -------------------

def p_ASIGNACION(p):
    '''ASIGNACION : ID EQ ARR_TEX SEMICOLON
        | ID ADIMS EQ EXPRESION SEMICOLON
        | ID EQ EXPRESION SEMICOLON'''
    #print('Lee asignacion')
    #Evaluar que la asignación sea correcta
    global cubosem
    global pilaoperand
    global ptipo
    global sem_err
    global dirfunc
    #Se checa que el id a asignar exista
    vartipo = None
    print(ptipo)
    print(p[3])
    if p[2] == '=':




        if (p[1] in dirfunc[currscope]['vartab'].keys()):
            vartipo = dirfunc[currscope]['vartab'][p[1]]['tipo']
            if (type(p[3]) is dict):
                print(p[3])
                if(dirfunc[currscope]['vartab'][p[1]]['dims'] != p[3]['dims']):
                    sem_err = True
                    print('La asignacion de variable %r en la linea %r no tiene las dimensiones de lo que se le esta asignando' % (p[1], p.lineno(1)))
                    raise SyntaxError('La asignacion de variable %r en la linea %r no tiene las dimensiones de lo que se le esta asignando', (p[1], p.lineno(1)))

        elif (p[1] in dirfunc['global']['vartab'].keys()):
            vartipo = dirfunc['global']['vartab'][p[1]]['tipo']
            if (type(p[3]) is dict):
                print(p[3])
                if(dirfunc['global']['vartab'][p[1]]['dims'] != p[3]['dims']):
                    sem_err = True
                    print('La asignacion de variable %r en la linea %r no tiene las dimensiones de lo que se le esta asignando' % (p[1], p.lineno(1)))
                    raise SyntaxError('La asignacion de variable %r en la linea %r no tiene las dimensiones de lo que se le esta asignando', (p[1], p.lineno(1)))
        else:

            sem_err = True
            print('La variable %r en la linea %r no ha sido declarada' % (p[1], p.lineno(1)))
            raise SyntaxError('La variable %r en la linea %r no ha sido declarada', (p[1], p.lineno(1)))



        asig = pilaoperand.pop()

        asigt = ptipo.pop()

        print('Asignando', p[1], ' = ', asig, ' tipo ', asigt)
        cuadruplos.append(('=', asig,'',p[1]))

        if (cubosem['='][vartipo][asigt] != 'error'):
            print('Cubo dice: ', cubosem['='][vartipo][asigt])
            pass
        else:

            sem_err = True
            print('Error de Semantica, el no se puede asignar %r a %r  en la linea %r' % (
            vartipo, asigt, p.lineno(1)))
            raise SyntaxError(
                'Error de Semantica, el no se puede asignar %r a %r  en la linea %r' % (
                vartipo, asigt, p.lineno(1)))


    else:
        if (p[1] in dirfunc[currscope]['vartab'].keys()):
            vartipo = dirfunc[currscope]['vartab'][p[1]]['tipo']
        elif (p[1] in dirfunc['global']['vartab'].keys()):
            vartipo = dirfunc['global']['vartab'][p[1]]['tipo']
        else:

            sem_err = True
            print('La variable %r en la linea %r no ha sido declarada' % (p[1], p.lineno(1)))
            raise SyntaxError('La variable %r en la linea %r no ha sido declarada', (p[1], p.lineno(1)))
        asig = pilaoperand.pop()

        asigt = ptipo.pop()

        print('Asignando', p[1], ' = ', asig, ' tipo ', asigt)
        cuadruplos.append(('=', asig, '', p[1]))

        if (cubosem['='][vartipo][asigt] != 'error'):
            print('Cubo dice: ',cubosem['='][vartipo][asigt])
            pass
        else:

            sem_err = True
            print('Error de Semantica, el no se puede asignar %r a %r  en la linea %r' % (vartipo, asigt, p.lineno(1)))
            raise SyntaxError(
                'Error de Semantica, el no se puede asignar %r a %r  en la linea %r' % (vartipo, asigt, p.lineno(1)))

#def p_ASIGNARR(p):
#    '''ASIGNARR : ARR_TEX SEMICOLON'''
#
#    #print( "⠄⠄⠄⠄⢠⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣿⣿⣿⣿⣆⠄⠄⠄\n⠄⠄⣼⢀⣿⣿⣿⣿⣏⡏⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣧⢻⣿⣿⣿⣿⡆⠄⠄\n⠄⠄⡟⣼⣿⣿⣿⣿⣿⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣇⢻⣿⣿⣿⣿⠄⠄\n⠄⢰⠃⣿⣿⠿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠙⠿⣿⣿⣿⣿⣿⠄⢿⣿⣿⣿⡄⠄\n⠄⢸⢠⣿⣿⣧⡙⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠈⠛⢿⣿⣿⡇⠸⣿⡿⣸⡇⠄\n⠄⠈⡆⣿⣿⣿⣿⣦⡙⠳⠄⠄⠄⠄⠄⠄⢀⣠⣤⣀⣈⠙⠃⠄⠿⢇⣿⡇⠄\n⠄⠄⡇⢿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⣠⣶⣿⣿⣿⣿⣿⣿⣷⣆⡀⣼⣿⡇⠄\n⠄⠄⢹⡘⣿⣿⣿⢿⣷⡀⠄⢀⣴⣾⣟⠉⠉⠉⠉⣽⣿⣿⣿⣿⠇⢹⣿⠃⠄\n⠄⠄⠄⢷⡘⢿⣿⣎⢻⣷⠰⣿⣿⣿⣿⣦⣀⣀⣴⣿⣿⣿⠟⢫⡾⢸⡟⠄.\n⠄⠄⠄⠄⠻⣦⡙⠿⣧⠙⢷⠙⠻⠿⢿⡿⠿⠿⠛⠋⠉⠄⠂⠘⠁⠞⠄⠄⠄\n⠄⠄⠄⠄⠄⠈⠙⠑⣠⣤⣴⡖⠄⠿⣋⣉⣉⡁⠄⢾⣦⠄⠄⠄⠄⠄⠄⠄⠄ ")
#    pass

def p_ADIMS(p):
    '''ADIMS : OPENSQU EXPRESION CLOSESQU ASEGD
             | empty'''

def p_ASEGD(p):
    '''ASEGD : OPENSQU EXPRESION CLOSESQU ATERD
             | empty'''

def p_ATERD(p):
    '''ATERD : OPENSQU EXPRESION CLOSESQU
             | empty'''
    
# Condicion ----------------------------

def p_CONDICION(p):
    'CONDICION : SI OPENPAR EXPRESION CLOSEPAR BLOQUE IFELSE'
    
    
def p_IFELSE(p):
    '''IFELSE : SINO BLOQUE
              | empty'''

# Bucles ---------------------------------

def p_BUCLE(p):
    '''BUCLE : WHILE
             | FOR'''

def p_WHILE(p):
    '''WHILE : MIENTRAS OPENPAR EXPRESION CLOSEPAR BLOQUE'''

def p_FOR(p):
    '''FOR : POR OPENPAR FORINIT EXPRESION SEMICOLON ASIGNACION CLOSEPAR BLOQUE'''

def p_FORINIT(p):
    '''FORINIT : ASIGNACION
               | empty '''

# Return ---------------------------

def p_RETURNF(p):
    '''RETURNF : REGRESAR EXPRESION SEMICOLON'''
    global currscope


#####
# Expresion
#####

def p_EXPRESION(p):
    '''EXPRESION : EXPRESIONR EXPRLOGS '''

    p[0] = 'exp'

def p_EXPERLOGS(p):
    '''EXPRLOGS : EXPRLOG'''
    global dirfunc
    global poper
    global pilaoperand
    global ptipo
    global regcount

    if (poper[-1:].pop() != None):
        if (poper[-1:].pop() == '||' or poper[-1:].pop() == '&&'):
            rop = pilaoperand.pop()
            ropt = ptipo.pop()
            lop = pilaoperand.pop()
            lopt = ptipo.pop()

            oper = poper.pop()
            if (cubosem[oper][ropt][lopt] != 'error'):
                restipo = cubosem[oper][ropt][lopt]
                print('La operacion de ', lop, oper, rop, 'resulta en ' + restipo)

                # generar cuadruplo
                cuadruplos.append((oper, rop, lop, 'res' + str(regcount)))
                pilaoperand.append('res' + str(regcount))
                regcount = regcount + 1
                ptipo.append(restipo)
            else:
                global sem_err
                sem_err = True
                print(
                    'Error de Semantica, el no se puede operacion relacional %r con %r  en la linea %r' % (
                        lopt, ropt, p.lineno(1)))
                raise SyntaxError(
                    'Error de Semantica, el no se puede operacion relacional %r con %r  en la linea %r' % (
                        lopt, ropt, p.lineno(1)))

def p_EXPRLOG(p):
    '''EXPRLOG : AND EXPRESION
               | OR EXPRESION
               | empty'''
    global poper
    if(p[1] != None):
        poper.append(p[1])
    print(poper)

def p_EXPRESIONR(p):
    '''EXPRESIONR : EXP EXPRS'''


def p_EXPRS(p):
    '''EXPRS : EXPR'''
    global dirfunc
    global poper
    global pilaoperand
    global ptipo
    global regcount
    if (poper[-1:].pop() != None):
        if (poper[-1:].pop() in ['>', '<', '<=', '>=', '==', '!=']):

            rop = pilaoperand.pop()
            ropt = ptipo.pop()
            lop = pilaoperand.pop()
            lopt = ptipo.pop()
            oper = poper.pop()
            if (cubosem[oper][ropt][lopt] != 'error'):
                restipo = cubosem[oper][ropt][lopt]
                print('La operacion de ', lop, oper, rop, 'resulta en ' + restipo)

                # generar cuadruplo
                cuadruplos.append((oper, rop, lop, 'res' + str(regcount)))

                pilaoperand.append('res' + str(regcount))
                regcount = regcount + 1
                ptipo.append(restipo)
            else:
                global sem_err
                sem_err = True
                print(
                    'Error de Semantica, el no se puede operacion relacional %r con %r  en la linea %r' % (
                        lopt, ropt, p.lineno(1)))
                raise SyntaxError(
                    'Error de Semantica, el no se puede operacion relacional %r con %r  en la linea %r' % (
                        lopt, ropt, p.lineno(1)))

def p_EXPR(p):
    '''EXPR : GT EXP
                 | LT EXP
                 | EXLAM EQ EXP
                 | EQ EQ EXP
                 | GT EQ EXP
                 | LT EQ EXP
                 | empty
                 '''
    global poper
    if(p[1] != None):
        op = p[1]
        if(p[2] == '='):
            op = op + p[2]
        if (op in ['>', '<', '<=', '>=', '==', '!=']):
            poper.append(op)

    
def p_EXP(p):
    '''EXP : TERMINO
    | TERMINOSS
            '''
    global dirfunc
    global poper
    global pilaoperand
    global ptipo
    global regcount
    # print(poper)
    # print(pilaoperand)
    # print(ptipo)
    # print(poper[-1:].pop(),'\n----')
    if poper[-1:].pop() == '+' or poper[-1:].pop() == '-':
        rop = pilaoperand.pop()
        ropt = ptipo.pop()
        lop = pilaoperand.pop()
        lopt = ptipo.pop()
        oper = poper.pop()
        if (cubosem[oper][ropt][lopt] != 'error'):
            restipo = cubosem[oper][ropt][lopt]
            print('La operacion de ', lop, oper, rop, 'resulta en ' + restipo)

            # generar cuadruplo
            cuadruplos.append((oper, rop, lop, 'res' + str(regcount)))

            pilaoperand.append('res' + str(regcount))
            regcount = regcount + 1
            ptipo.append(restipo)
        else:
            global sem_err
            sem_err = True
            print(
                'Error de Semantica, el no se puede sumar/restar %r con %r  en la linea %r' % (lopt, ropt, p.lineno(2)))
            raise SyntaxError(
                'Error de Semantica, el no se puede sumar/restar %r con %r  en la linea %r' % (lopt, ropt, p.lineno(2)))


def p_TERMINOSS(p):
    '''TERMINOSS : EXP PLUS EXP %prec PLUSMINUS
                | EXP MINUS EXP %prec PLUSMINUS
                | empty'''
    global poper
    if p[2] == '+' or p[2] == '-':
        poper.append(p[2])
    print(poper)


#def p_TERMINOS(p):
#    '''TERMINOS : PLUS EXP
#                | MINUS EXP
#                | empty'''
#    global poper
#    if p[1] == '+' or p[1] == '-':
#        poper.append(p[1])
#    print(poper)
    
    
def p_TERMINO(p):
    '''TERMINO : FACTOR
                | FACTORESS
               '''
    # if p[2] != None:
    global dirfunc
    global poper
    global pilaoperand
    global ptipo
    global regcount
    # print(poper)
    # print(pilaoperand)
    # print(ptipo)
    # print(poper[-1:].pop(), '\n----')
    if poper[-1:].pop() == '*' or poper[-1:].pop() == '/':
        rop = pilaoperand.pop()
        ropt = ptipo.pop()
        lop = pilaoperand.pop()
        lopt = ptipo.pop()
        oper = poper.pop()
        if (cubosem[oper][ropt][lopt] != 'error'):
            restipo = cubosem[oper][ropt][lopt]
            print('La operacion de ', lop, oper, rop, 'resulta en ' + restipo)
            # generar cuadruplo
            cuadruplos.append((oper, rop, lop, 'res' + str(regcount)))

            pilaoperand.append('res' + str(regcount))
            regcount = regcount + 1
            ptipo.append(restipo)
        else:
            global sem_err
            sem_err = True
            print(
                'Error de Semantica, el no se puede sumar/restar %r con %r  en la linea %r' % (lopt, ropt, p.lineno(2)))
            raise SyntaxError(
                'Error de Semantica, el no se puede sumar/restar %r con %r  en la linea %r' % (lopt, ropt, p.lineno(2)))

def p_FACTORESS(p):
    '''FACTORESS : TERMINO MUL TERMINO %prec MULDIV
                | TERMINO DIV TERMINO %prec MULDIV
                | empty'''
    global poper
    if p[2] == '*' or p[2] == '/':
        poper.append(p[2])
    print(poper)

    
#def p_FACTORES(p):
#    '''FACTORES : MUL TERMINO
#                | DIV TERMINO
#                | empty'''
#    global poper
#    if p[1] == '*' or p[1] == '/':
#        poper.append(p[1])
#    print(poper)
    
    
def p_FACTOR(p):
    '''FACTOR : SIGNOVAR VARCTE
              | OPENPAR EXPRESION CLOSEPAR'''
    if (p[1] == '('):
        p[0] = p[2]
    else:
        if(p[1] != None):
            global pilaoperand
            global ptipo
            global cuadruplos
            global regcount
            lop = pilaoperand.pop()
            lopt = ptipo.pop()
            if(cubosem[p[1]]['none'][lopt] != 'error'):
                cuadruplos.append((p[1],'',p[2],'res'+str(regcount)))
                pilaoperand.append('res'+str(regcount))
                ptipo.append(cubosem[p[1]]['none'][lopt])
            else:
                global sem_err
                sem_err = True
                print('Error de Semantica, no se le puede dar un signo a una variable que no sea un entero o flotante')
                raise SyntaxError('Error de Semantica, no se le puede dar un signo a una variable que no sea un entero o flotante')
        else:
            p[0] = p[2]

    
def p_SIGNOVAR(p):
    '''SIGNOVAR : PLUS
                | MINUS
                | empty'''
    p[0] = p[1]

#####
# LLAMADAS
#####    
 
def p_VARCTE(p):
    #'''VARCTE : ID| CTE_INT| CTE_FLOAT| CTE_STRING| CTE_BOOL| CTE_CHAR| LLAMADAFUNC| LLAMADAARR| ARR_TEX| NULO'''

    '''VARCTE : ID
                | CTE_INT
                | CTE_FLOAT
                | CTE_STRING
                | CTE_BOOL
                | CTE_CHAR
                | LLAMADAFUNC
                | LLAMADAARR
                | NULO'''

    global dirfunc
    global currscope
    global special
    global sem_err
    global poper

    #print('Para el elemento',p[1],'En el scope '+currscope+' Se encuentra la dir func así:')
    #print('dirfunc', dirfunc, '\n\n')
    pilaoperand.append(p[1])
    print('operadores ',poper)
    print('Se leyo en expresion',p[1])
    print('Pila de operandos',pilaoperand)
    if isinstance(p[1],int):

        ptipo.append('entero')
    elif isinstance(p[1],float):

        ptipo.append('flotante')
    elif p[1] == 'verdadero' or p[1] == 'falso':
        ptipo.append('bool')
    elif re.fullmatch("\"[^\"]+\"",p[1]):

        ptipo.append('cadena')
    elif re.fullmatch("\'[^\']\'",p[1]):
        ptipo.append('char')
    elif re.fullmatch(r"\$[a-zA-Z]([a-zA-Z]|[0-9]|[_])*",p[1]):
        #llamada func
        vartipo = None
        if (p[1][1:] in dirfunc.keys()):
            vartipo = dirfunc[p[1][1:]]['tipo']
        elif (p[1][1:] in special.keys()):
            vartipo = special[p[1][1:]]['tipo']
        else:
            sem_err = True
            print('La funcion %r en la linea %r no ha sido declarada' % (p[1], p.lineno(1)))
            raise SyntaxError('La funcion %r en la linea %r no ha sido declarada', (p[1], p.lineno(1)))
        ptipo.append(vartipo)
    elif re.match(r"[a-zA-Z]([a-zA-Z]|[0-9]|[_])*",p[1]):
        #print('Para el elemento', p[1], 'En el scope ' + currscope + ' Se encuentra la dir func así:')
        #print('dirfunc', dirfunc, '\n\n')
        #llamada vars
        vartipo = None
        if(p[1] in dirfunc[currscope]['vartab'].keys()):
            vartipo = dirfunc[currscope]['vartab'][p[1]]['tipo']
        elif (p[1] in dirfunc['global']['vartab'].keys()):
            vartipo = dirfunc['global']['vartab'][p[1]]['tipo']
        else:
            sem_err = True
            print('La variable %r en la linea %r no ha sido declarada'%(p[1],p.lineno(1)))
            raise SyntaxError('La variable %r en la linea %r no ha sido declarada',(p[1],p.lineno(1)))
        ptipo.append(vartipo)

    else:
        print('No se sabe que es')
        pass

    print('Pila tipos       ',ptipo,'\n----------------------------------------------------------------------------------------------------------------------------------------------\n')

    p[0] = p[1]


#LLAMADA FUNCION
def p_LLAMADAFUNC(p):
    '''LLAMADAFUNC :  DLR FID OPENPAR CALLPARAMS CLOSEPAR '''

    #llamada a funcion
    global dirfunc
    global funcallcurr
    global sem_err

    funcallcurr = p[2]
    vartipo = None

    if (p[2] in dirfunc.keys()):
        if 'params' in dirfunc[p[2]].keys():
            vartipo = dirfunc[p[2]]['params']

    elif (p[2] in special.keys()):
        if 'params' in dirfunc[p[2]].keys():
            vartipo = dirfunc[p[2]]['params']
    else:
        sem_err = True
        print('La funcion %r en la linea %r no ha sido declarada' % (p[1], p.lineno(1)))
        raise SyntaxError('La funcion %r en la linea %r no ha sido declarada', (p[1], p.lineno(1)))

    #Checar los parametros esten bien llamados
    if vartipo != None:

        if len(p[4]) != len(vartipo):
            sem_err = True
            print('La funcion %r en la linea %r no tiene los parametros correctos' % (p[1], p.lineno(1)))
            raise SyntaxError('La funcion %r en la linea %r no tiene los parametros correctos', (p[1], p.lineno(1)))
        else:

            i = 0

            for param in vartipo.values():
                print('acpapapapa',param ,p[4][i])
                if param['tipo'] != p[4][i]['tipo']:

                    sem_err = True
                    print('La funcion %r en la linea %r no tiene los parametros correctos, los tipos del argumento %r no coinciden' % (p[1], p.lineno(1),i+1))
                    raise SyntaxError('La funcion %r en la linea %r no tiene los parametros correctos, los tipos del argumento %r no coinciden', (p[1], p.lineno(1),i+1))
                else:
                    i = i+1
            print(i)





    p[0] = p[1]+p[2]

def p_FID(p):
    '''FID : ID
           | FUNID'''
    p[0] = p[1]

#-------------------------
# Aquí se van agregando los nombres de las funciones especiales del lenguaje
def p_FUNID(p):
    '''FUNID : LEER'''
    p[0] = p[1]

def p_CALLPARAMS(p):
    '''CALLPARAMS : CPARAM
                  | empty '''

    p[0] = p[1]
def p_CPARAM(p):
    ''' CPARAM : ARR_TEX CPARAMS
                | EXPRESION CPARAMS'''
    #hay que cambiar como identifica si es un arr_tex
    global ptipo
    global pilaoperand


    cfpar = []
    if type(p[1]) is dict:
        cfpar.append(p[1])
    else:
        pilaoperand.pop()
        cfpar.append({'tipo':ptipo.pop()})
    if p[2] != None:
        cfpar = cfpar + p[2]

    p[0] = cfpar



def p_CPARAMS(p):
    ''' CPARAMS : COMMA EXPRESION CPARAMS
                | COMMA ARR_TEX CPARAMS
                | empty'''
    if p[1] != None:
        global ptipo
        global pilaoperand
        cfpar = []
        if type(p[1]) is dict:
            cfpar.append(p[1])
        else:
            pilaoperand.pop()
            cfpar.append({'tipo': ptipo.pop()})
        cfpar = cfpar + p[2]
        p[0] = cfpar
    else:
        p[0] = None
#LLAMADA ARREGLO
def p_LLAMADAARR(p):
    '''LLAMADAARR : ID OPENSQU EXPRESION CLOSESQU LLSEGD'''
    global dirfunc
    global currscope
    global pilaoperand
    global ptipo
    global sem_err
    pilaoperand.pop()
    ptipo.pop()
    if (p[1] in dirfunc[currscope]['vartab'].keys()):
        if not ('dims' in dirfunc[currscope]['vartab'][p[1]].keys()):
            sem_err = True
            print('La variable %r en la linea %r no es un arreglo' % (p[1], p.lineno(1)))
            raise SyntaxError('La variable %r en la linea %r no es un arreglo', (p[1], p.lineno(1)))
    elif (p[1] in dirfunc['global']['vartab'].keys()):
        if not ('dims' in dirfunc['global']['vartab'][p[1]].keys()):
            sem_err = True
            print('La variable %r en la linea %r no es un arreglo' % (p[1], p.lineno(1)))
            raise SyntaxError('La variable %r en la linea %r no es un arreglo', (p[1], p.lineno(1)))
    else:
        sem_err = True
        print('La variable %r en la linea %r no ha sido declarada' % (p[1], p.lineno(1)))
        raise SyntaxError('La variable %r en la linea %r no ha sido declarada', (p[1], p.lineno(1)))
    p[0] = p[1]

def p_LLSEGD(p):
    '''LLSEGD : OPENSQU EXPRESION CLOSESQU LLTERD
              | empty'''
    if p[1] != None:
        global pilaoperand
        global ptipo
        pilaoperand.pop()
        ptipo.pop()
def p_LLTERD(p):
    '''LLTERD : OPENSQU EXPRESION CLOSESQU
              | empty'''
    if p[1] != None:
        global pilaoperand
        global ptipo

        pilaoperand.pop()
        ptipo.pop()



########## ARREGLO TEXTUAL
def p_ARR_TEX(p):
    '''ARR_TEX : OPENSQU ATPRIC CLOSESQU'''
    global ptipo
    global pilaoperand

    arrdim = {'dims':1}
    print('Primera dim')
    if p[2] != None:
        arrdim.update(p[2])
    ptipo.append(arrdim['tipo'])
    pilaoperand.append('arr')
    p[0] = arrdim

def p_ATPRIC(p):
    ''' ATPRIC : ATPRE ATPRISIG
               | empty'''
    newtipo = None

    global sem_err

    if p[1] != None:

        if p[2] != None:

            if (cubosem['arr'][p[1]['tipo']][p[2]['tipo']] != 'error'):
                newtipo = p[1]
                newtipo.update(p[2])
                newtipo['tipo'] = cubosem['arr'][p[1]['tipo']][p[2]['tipo']]
                p[0] = newtipo
            else:
                sem_err = True
                print('El tipo del elemento %r en la linea %r no es congruente con el tipo del arreglo' % (
                p[1], p.lineno(1)))
                raise SyntaxError('La variable %r en la linea %r no es un arreglo', (p[1], p.lineno(1)))
        else:
            p[0] = p[1]
    else:
        p[0] = None

def p_ATPRE(p):
    '''ATPRE : EXPRESION
              | ATSEGD'''
    arrdim = {}
    if type(p[1]) is not dict :
        global pilaoperand
        global ptipo
        pilaoperand.pop()

        arrdim['tipo'] = ptipo.pop()

    else:
        arrdim.update({'dims': 2})
        arrdim.update(p[1])



    p[0] = arrdim

def p_ATPRISIG(p):
    '''ATPRISIG : COMMA ATPRE ATPRISIG
                | empty'''
    newtipo = None

    global sem_err

    if p[1] != None:
        if p[3] != None:

            if (cubosem['arr'][p[2]['tipo']][p[3]['tipo']] != 'error'):
                newtipo = p[2]
                newtipo.update(p[3])
                newtipo['tipo'] = cubosem['arr'][p[2]['tipo']][p[3]['tipo']]
                p[0] = newtipo
            else:
                sem_err = True
                print('El tipo del elemento %r en la linea %r no es congruente con el tipo del arreglo' % (
                    p[1], p.lineno(1)))
                raise SyntaxError('La variable %r en la linea %r no es un arreglo', (p[2], p.lineno(2)))
        else:
            p[0] = p[2]
    else:
        p[0] = None

def p_ATSEGD(p):
    '''ATSEGD : OPENSQU ATSEGC CLOSESQU'''
    p[0] = p[2]

def p_ATSEGC(p):
    ''' ATSEGC : ATSEGE ATSEGSIG
               | empty'''
    newtipo = None

    global sem_err

    if p[1] != None:
        if p[2] != None:
            if (cubosem['arr'][p[1]['tipo']][p[2]['tipo']] != 'error'):
                newtipo = p[1]
                newtipo.update(p[2])
                newtipo['tipo'] = cubosem['arr'][p[1]['tipo']][p[2]['tipo']]
                p[0] = newtipo
            else:
                sem_err = True
                print('El tipo del elemento %r en la linea %r no es congruente con el tipo del arreglo' % (
                p[1], p.lineno(1)))
                raise SyntaxError('La variable %r en la linea %r no es un arreglo', (p[1], p.lineno(1)))
        else:
            p[0] = p[1]
    else:
        p[0] = None

def p_ATSEGE(p):
    '''ATSEGE : EXPRESION
              | ATTERD'''
    arrdim = {}
    if type(p[1]) is not dict :
        global pilaoperand
        global ptipo
        pilaoperand.pop()
        arrdim['tipo'] = ptipo.pop()
    else:
        arrdim.update(p[1])
        arrdim.update({'dims': 3})

    p[0] = arrdim

def p_ATSEGSIG(p):
    '''ATSEGSIG : COMMA ATSEGE ATSEGSIG
                | empty'''
    newtipo = None

    global sem_err

    if p[1] != None:
        if p[3] != None:
            if (cubosem['arr'][p[2]['tipo']][p[3]['tipo']] != 'error'):
                newtipo = p[2]
                newtipo.update(p[3])
                newtipo['tipo'] = cubosem['arr'][p[2]['tipo']][p[3]['tipo']]
                p[0] = newtipo
            else:
                sem_err = True
                print('El tipo del elemento %r en la linea %r no es congruente con el tipo del arreglo' % (
                    p[1], p.lineno(1)))
                raise SyntaxError('La variable %r en la linea %r no es un arreglo', (p[2], p.lineno(2)))
        else:
            p[0] = p[2]
    else:
        p[0] = None

def p_ATTERD(p):
    '''ATTERD : OPENSQU ATTERC CLOSESQU'''
    p[0] = p[2]

def p_ATTERC(p):
    ''' ATTERC : ATTERE ATTERSIG
               | empty'''
    newtipo = None

    global sem_err

    if p[1] != None:
        if p[2] != None:
            if(cubosem['arr'][p[1]['tipo']][p[2]['tipo']] != 'error'):
                newtipo = p[1]
                newtipo.update(p[2])
                newtipo['tipo'] = cubosem['arr'][p[1]['tipo']][p[2]['tipo']]
                p[0] = newtipo
            else:
                sem_err = True
                print('El tipo del elemento %r en la linea %r no es congruente con el tipo del arreglo' % (p[1], p.lineno(1)))
                raise SyntaxError('La variable %r en la linea %r no es un arreglo', (p[1], p.lineno(1)))
        else:
            p[0] = p[1]
    else:
        p[0] = None


def p_ATTERE(p):
    '''ATTERE : EXPRESION'''
    global pilaoperand
    global ptipo

    arrdim = {}

    pilaoperand.pop()
    arrdim['tipo'] = ptipo.pop()
    p[0] = arrdim

def p_ATTERSIG(p):
    '''ATTERSIG : COMMA ATTERE ATTERSIG
                | empty'''
    newtipo = None

    global sem_err

    if p[1] != None:
        if p[3] != None:
            if (cubosem['arr'][p[2]['tipo']][p[3]['tipo']] != 'error'):
                newtipo = p[2]
                newtipo.update(p[3])
                newtipo['tipo'] = cubosem['arr'][p[2]['tipo']][p[3]['tipo']]
                p[0] = newtipo
            else:
                sem_err = True
                print('El tipo del elemento %r en la linea %r no es congruente con el tipo del arreglo' % (
                p[1], p.lineno(1)))
                raise SyntaxError('La variable %r en la linea %r no es un arreglo', (p[2], p.lineno(2)))
        else:
            p[0] = p[2]
    else:
        p[0] = None

def p_empty(p):
    'empty :'
    p[0] = None
    pass

def p_error(p):
    print("Error de sintaxis con el simbolo %r en la linea %r" % (p.value,p.lexer.lineno))
    raise TypeError("Error de sintaxis con el simbolo %r en la linea %r" % (p.value,p.lexer.lineno))
    
parser = yacc.yacc( debug=1)


def cuadToTxt(cuad):
    opfile = open('cuadruplos.txt','w')
    for i in range(len(cuad)):
        opfile.write("%r %r %r %r\n" % cuad[i])


#Prueba imprimir el cubo semantico para ver si esta bien
#print(cubosem['||']['cadena']['cadena'])

'''print('\n\n\n')
print('Cubo semantico:\n')
ops =  ['OPER1','OPER2'] + list(cubosem.keys())
oper1 = list(cubosem['+'].keys())
oper2 = list(cubosem['+']['entero'].keys())

print(oper1,oper2)

print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*ops))
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
ops = list(cubosem.keys())
for op1 in oper1:
    row = [op1]
    for op2 in oper2:
        row = row + [op2]
        for op in ops:
            row.append(cubosem[op][op1][op2])
    print(
        "{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            *row))

print('\n\n\n')'''
#Leer de archivo
myFile = open(sys.argv[1])
try:
    parser.parse(myFile.read(),tracking=True)
except TypeError:

    print("No es lenguaje valido!!!!")
else:
    if(sem_err):
        print('No es lenguaje valido!!!!')
    else:
        cuadToTxt(cuadruplos)
        print('aceptado')




