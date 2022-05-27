
#    Nombre: IntroProg.py
#    Descripción: Una implementación del lexer y parser usando python y ply para el compliador
#    Por: Luis Fernando Lomelín Ibarra

#importar las herramientas de lex y yacc de ply

from ply import lex
import ply.yacc as yacc
import sys
import re
import json

debugp = True
#PrintDebug
def dprint(*args,**kwargs):
    global debugp
    if debugp:
        print(*args,**kwargs)

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
special = {
    'leer':
        {
            'tipo':'flotante'
        },
}

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
    ('right', 'EQS'),
    ( 'nonassoc', 'GT', 'LT','AND','OR'),
    ('nonassoc', 'LOG'),
    ('nonassoc', 'REL'),
    ( 'left', 'PLUSMINUS' ),
    ( 'left', 'MULDIV' ),
    #('right', 'RRULE')
    )

########################################################################################################
#### Variables globales de interes para expresiones y addresses
#########################################################################################################
#Dir de func
dirfunc = {}
#Current scope
currscope = None
#para saber cuales parametros evualuar en llamada de funcion
funcallcurr = None

#Pila de Saltos
psaltos = []
cuadcount = 0

#Para generar los cuadruplos temporalmente asignar un registro de manera acendente al cuadruplo
regcount = 0

#Cuadruplos
cuadruplos = []

#Tabla constantes
ctetab = {}
objctetab = {} #Una copia para guardarlo en el obj

#Contadores de variables
tmpintcount = 0
tmpfloatcount = 0
tmpcharcount = 0
tmpboolcount = 0

glbintcount = 0
glbfloatcount = 0
glbcharcount = 0
glbboolcount = 0

cteintcount = 0
ctefloatcount = 0
ctecharcount = 0
cteboolcount = 0
ctestringcount = 0

#Contadores de arreglos
tmppointcount = 0

#Offsets de direcciones

#MAXIMOS POR VARIABLE
INTMAX = 2000
FLOATMAX = 2000
CHARMAX = 1000
BOOLMAX = 1000
POINTMAX = 2000
STRINGMAX = 1000


#Global
globalint = 1000
globalfloat = globalint + INTMAX
globalchar = globalfloat + FLOATMAX
globalbool = globalchar + CHARMAX
globalpoint = globalbool + BOOLMAX

#Local
localint = globalpoint + POINTMAX
localfloat = localint + INTMAX
localchar = localfloat + FLOATMAX
localbool = localchar + CHARMAX
localpoint = localbool + BOOLMAX


#Temporal
tempint = localpoint + POINTMAX
tempfloat = tempint + INTMAX
tempchar = tempfloat + FLOATMAX
tempbool = tempchar + CHARMAX
temppoint = tempbool + BOOLMAX


#Constantes
constint = temppoint + POINTMAX
constfloat = constint + INTMAX
constchar = constfloat + FLOATMAX
constbool = constchar + CHARMAX
conststring = constbool + BOOLMAX

#Variables pertinentes para arreglos
R = 0
atarrsize = 0
atd1 = 0
atd2 = 0
atd3 = 0

# Asociación cuadruplo con linea de código fuente
sclines = []

# Funcion para imprmir errores y parar la ejecución
def printerror(errmsg):
    global sem_err
    sem_err = True
    print(errmsg)
    raise SyntaxError(errmsg)

# Funcion par Meter valores constantes a la ctetab
def addConst(cte,tipo,line):
    # Rango de memoria constantes
    global constint
    global constfloat
    global constchar
    global constbool
    global conststring
    # Contadores constantes
    global cteintcount
    global ctefloatcount
    global ctecharcount
    global cteboolcount
    global ctestringcount
    # Maximos de variables
    global INTMAX
    global FLOATMAX
    global CHARMAX
    global BOOLMAX
    global STRINGMAX
    #Tabla const
    global ctetab
    global objctetab
    if type(cte) is not str:
        ctkey = str(cte)
    else:
        ctkey = cte
    if tipo == 'entero':
        if cteintcount < INTMAX:
            ctetab[ctkey] = constint + cteintcount
            objctetab[ctetab[ctkey]] = cte
            cteintcount += 1
            return ctetab[ctkey]
        else:
            printerror(
                "Error de Semantica: sobrepaso el limite de constantes declaradas en la linea %r" % (line))
    elif tipo == 'flotante':
        if ctefloatcount < FLOATMAX:
            ctetab[ctkey] = constint + ctefloatcount
            objctetab[ctetab[ctkey]] = cte
            ctefloatcount += 1
            return ctetab[ctkey]
        else:
            printerror(
                "Error de Semantica: sobrepaso el limite de constantes declaradas en la linea %r" % (line))
    elif tipo == 'char':
        if ctecharcount < CHARMAX:
            ctetab[cte] = constchar + ctecharcount
            objctetab[ctetab[cte]] = cte
            ctecharcount += 1
            return ctetab[ctkey]
        else:

            printerror(
                "Error de Semantica: sobrepaso el limite de constantes declaradas en la linea %r" % (line))
    elif tipo == 'bool':
        if cteboolcount < BOOLMAX:
            ctetab[cte] = constbool + cteboolcount
            if cte == 'verdadero':
                objctetab[ctetab[cte]] = True
            else:
                objctetab[ctetab[cte]] = False
            cteboolcount += 1
            return ctetab[ctkey]
        else:
            printerror(
                "Error de Semantica: sobrepaso el limite de constantes declaradas en la linea %r" % (line))
    elif tipo == 'cadena':
        if ctestringcount < STRINGMAX:
            ctetab[ctkey] = conststring + ctestringcount
            objctetab[ctetab[ctkey]] = cte
            ctestringcount += 1
            return ctetab[ctkey]
        else:

            printerror(
                "Error de Semantica: sobrepaso el limite de constantes declaradas en la linea %r" % (line))

#Asignar direcciones virtuales a la tabla de variables
def assignvirtualaddress(vartab,addressscope,linenum):
    # Rangos globales de memoria
    global globalint
    global globalfloat
    global globalchar
    global globalbool
    global globalpoint
    # Direcciones locales
    global localint
    global localfloat
    global localchar
    global localbool
    global localpoint
    # Cant. Maximas de variables
    global INTMAX
    global FLOATMAX
    global CHARMAX
    global BOOLMAX
    global POINTAYMAX

    # Contadores globales
    global glbintcount
    global glbfloatcount
    global glbcharcount
    global glbboolcount
    #
    # Contadores de variables
    intcount = 0
    floatcount = 0
    charcount = 0
    boolcount = 0

    # Contadores de arreglos
    pointcount = 0

    if addressscope == 'global':
        for k in vartab.keys():
            if('dims' in vartab[k].keys()): # Asignacion de direcciones de arreglos
                incr = vartab[k]['size']
                isArr = True
            else:
                incr = 1
                isArr = False


            if(vartab[k]['tipo'] == 'entero'): #Asignar las direcciones enteras
                if (intcount < INTMAX):
                    vartab[k]['address'] = globalint + intcount
                    intcount += incr
                    if isArr:
                        addConst(vartab[k]['address'], 'entero', linenum)
                else:
                    printerror("Error de Semantica: sobrepaso el limite de variables declaradas en la linea %r" % (linenum))

            elif (vartab[k]['tipo'] == 'flotante'):#Asignar las direcciones flotantes
                if (floatcount < FLOATMAX):
                    vartab[k]['address'] = globalfloat + floatcount
                    floatcount += incr
                    if isArr:
                        addConst(vartab[k]['address'], 'entero', linenum)
                else:
                    printerror("Error de Semantica: sobrepaso el limite de variables declaradas en la linea %r" % (linenum))

            elif (vartab[k]['tipo'] == 'char'):#Asignar las direcciones char
                if (charcount < CHARMAX):
                    vartab[k]['address'] = globalchar + charcount
                    charcount += incr
                    if isArr:
                        addConst(vartab[k]['address'], 'entero', linenum)
                else:
                    printerror("Error de Semantica: sobrepaso el limite de variables declaradas en la linea %r" % (linenum))
            elif (vartab[k]['tipo'] == 'bool'):#Asignar las direcciones char
                if (boolcount < BOOLMAX):
                    vartab[k]['address'] = globalbool + boolcount
                    boolcount += incr
                else:
                    printerror("Error de Semantica: sobrepaso el limite de variables declaradas en la linea %r" % (linenum))
    elif addressscope == 'local':
        for k in vartab.keys():
            if('dims' in vartab[k].keys()): # Asignacion de direcciones de arreglos
                incr = vartab[k]['size']
                isArr = True
            else:
                incr = 1
                isArr = False

            if(vartab[k]['tipo'] == 'entero'): #Asignar las direcciones enteras
                if (intcount < INTMAX):
                    vartab[k]['address'] = localint + intcount
                    intcount += incr
                    if isArr:
                        addConst(vartab[k]['address'], 'entero', linenum)
                else:
                    printerror("Error de Semantica: sobrepaso el limite de variables declaradas en la linea %r" % (linenum))

            elif (vartab[k]['tipo'] == 'flotante'):#Asignar las direcciones flotantes
                if (floatcount < FLOATMAX):
                    vartab[k]['address'] = localfloat + floatcount
                    floatcount += incr
                    if isArr:
                        addConst(vartab[k]['address'], 'entero', linenum)
                else:
                    printerror("Error de Semantica: sobrepaso el limite de variables declaradas en la linea %r" % (linenum))

            elif (vartab[k]['tipo'] == 'char'):#Asignar las direcciones char
                if (charcount < CHARMAX):
                    vartab[k]['address'] = localchar + charcount
                    if isArr:
                        addConst(vartab[k]['address'], 'entero', linenum)
                    charcount += incr
                else:
                    printerror("Error de Semantica: sobrepaso el limite de variables declaradas en la linea %r" % (linenum))
            elif (vartab[k]['tipo'] == 'bool'):#Asignar las direcciones char
                if (boolcount < BOOLMAX):
                    vartab[k]['address'] = localbool + boolcount
                    if isArr:
                        addConst(vartab[k]['address'], 'entero', linenum)
                    boolcount += incr
                else:
                    printerror("Error de Semantica: sobrepaso el limite de variables declaradas en la linea %r" % (linenum))
    return vartab, intcount, floatcount, charcount, boolcount




#Estructura del programa
def p_PROGRAMA(p):
    '''PROGRAMA : INITPROG ID OPENCUR DECGLOB DECTODASFUNC PRINCIPAL FUNCION PRINSCOPE BLOQUE CLOSECUR '''

    global cuadruplos
    global cuadcount
    global dirfunc



    #1.- Crear el directorio de funciones
    #dirfunc['global'] = {'vartab':{}}
    #2.- Si se encuentran declaraciones globales se debe de crear una tabla de symbolos a nivel global
    # Este es encapsulado en la regla decglob
    #if p[4] != None:
    #    dirfunc['global'].update(p[4])


    #3.- Si se encuentran funciones darlas de alta en el dir de funciones

    if(p[5] != None):
        # 4.- Checar que no se repitan los nombres de variables globales en las funciones locales
        #dprint("Funciones : %r" % p[5])
        #for kfun in p[5].keys():
        #    funvars = p[5][kfun]['vartab']
        #    for varnam in funvars:
        #        if varnam in dirfunc['global']['vartab'].keys():
        #            print("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (varnam, p.lineno(5)))
        #
        #            sem_err = True
        #            raise (SyntaxError(
        #                "Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (varnam, p.lineno(5))))

        dirfunc.update(p[5])


    #Guardar los temporales utilizadoes en prinicpal

    dirfunc[currscope]['tmpres'] = {'entero': tmpintcount, 'flotante':tmpfloatcount, 'char':tmpcharcount, 'bool': tmpboolcount, 'pointer' : tmppointcount}




    #4.- Borrar si se llega al final del programa.
    for key in dirfunc.keys():
        if 'vartab' in dirfunc[key]:
            del dirfunc[key]['vartab']
    pdirfunc = json.dumps(dirfunc,indent=4)
    dprint(pdirfunc)
    cuadruplos.append(('END','','',''))
    global sclines
    sclines.append(p.lineno(1))
    cuadcount+=1
    
    global ctetab
    pctetab = json.dumps(ctetab,indent=4)
    dprint('+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-\n',pctetab)

def p_INITPROG(p):
    ''' INITPROG : PROGRAM'''
    global cuadruplos
    global psaltos
    global cuadcount

    #Generar el go to main
    cuadruplos.append(('GOTO','',''))
    global sclines
    sclines.append(p.lineno(1))
    psaltos.append(cuadcount)
    cuadcount += 1

def p_PRINSCOPE(p):
    '''PRINSCOPE : OPENCUR DECLARACIONES CLOSECUR'''
    #Scope en el que se encuentra
    global currscope
    #Dir. de Funciones
    global dirfunc

    # Cuadruplos y su contador, pila de saltos
    global cuadcount
    global cuadruplos
    global psaltos
    init = psaltos.pop()
    cuadruplos[init] = cuadruplos[init] + (cuadcount,)

    # Contadores de variables
    intcount = 0
    floatcount = 0
    charcount = 0
    boolcount = 0

    #Reiniciar el contador local de los temporales en main
    tmpintcount = 0
    tmpfloatcount = 0
    tmpcharcount = 0
    tmpboolcount = 0
    tmppointcount = 0

    #Poner el scope correcto
    currscope = 'principal'

    dprint('\n\n\n\n--------------------------------------------------------\nLLego a scope global\n---------------')

    if (p[2] != None):
        ks = p[2].keys()
        #if dirfunc['global']['vartab'] != None:
        #    if len(dirfunc['global']['vartab']) > 0 :
        #        dprint('a', p[2], dirfunc['global']['vartab'])
        #        for k in ks:
        #            if k in dirfunc['global']['vartab'].keys():
        #                print(
        #                    "Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (
        #                    k, p.lineno(2)))
        #
        #                sem_err = True
        #                raise (SyntaxError(
        #                    "Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (
        #                    k, p.lineno(2))))

        # Switch para aumentar el contador correcto y verificación de que no se definan variables demás

        if (p[2] != None and len(p[2]) > 0):

            p[2],intcount, floatcount, charcount, boolcount = assignvirtualaddress(p[2],'local',p.lineno(1))


    dirfunc['principal'] = {'tipo': 'vacio', 'params:': None,'vartab':p[2], 'varres':{'entero': intcount, 'flotante':floatcount, 'char':charcount, 'bool': boolcount}}
    #dirfunc['global']['vartab'].update(p[2])

    p[0] = p[2]


###########
# Declaraciones Arreglos y variables
##########

def p_DECGLOB(p):
    '''DECGLOB : DECLARACIONES'''
    #Directorio de funciones
    global dirfunc

    #Contadores globales
    global glbintcount
    global glbfloatcount
    global glbcharcount
    global glbboolcount



    # Switch para aumentar el contador correcto y verificación de que no se definan variables demás
    # Contadores de variables
    intcount = 0
    floatcount = 0
    charcount = 0
    boolcount = 0

    # Contadores de arreglos
    pointcount = 0

    #dprint(p[1])
    if (p[1] != None):
        p[1], intcount, floatcount, charcount, boolcount = assignvirtualaddress(p[1],'global',p.lineno(1))

    glbintcount = intcount
    glbfloatcount = floatcount
    glbcharcount = charcount
    glbboolcount = boolcount
    if p[1] == None:
        p[1] = {}
    dirfunc['global'] = {'tipo': 'vacio', 'params:': None, 'vartab': p[1],'varres' : {'entero': intcount, 'flotante': floatcount, 'char':charcount, 'bool': boolcount}}


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
                #dprint(p[2].keys())
                #dprint(k)
                if(k in p[2].keys()):
                    #dprint(p[2].keys())
                    printerror("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (k, p.lineno(2)))
            #dprint( "P[1] contiene %r y p[2] contiene %r" % (p[1].keys(),p[2].keys()))


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
                printerror("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (varid, p.lineno(3)))
            newvars[varid] = {'tipo': p[1]}



    p[0] = newvars
# Declaración de variables simples
def p_DVNID(p):
    '''DVNID : COMMA ID DVNID
             | empty'''
    if p[1] == None:
        p[0] = None
    else:
        vars = [p[2]]

        if(p[3] != None):
            #dprint("Checkin if %r is in %r" % (p[2],p[3]))
            if p[2] in p[3]:

                printerror("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (p[2],p.lexspan(3)))
            else:
                vars = vars + p[3]
            #dprint(vars)
        p[0] = vars

#Declaración de arreglos
def p_DECARR(p):
    '''DECARR : TIPO DECARRID DPRIM DSEG SEMICOLON'''
    global R
    darrsize = 0
    vararr = {p[2]:{'tipo': p[1]}}
    vararr[p[2]].update(p[3])
    if(p[4] != None):
        vararr[p[2]]['dimlen']+=p[4]
        vararr[p[2]]['dims'] = len(vararr[p[2]]['dimlen'])
    darrsize = R
    mi = 0
    for k in range(vararr[p[2]]['dims']):
        mi += 1
        m = R / vararr[p[2]]['dimlen'][k][0]
        m = int(m)
        vararr[p[2]]['dimlen'][k][1] = m
        R = m
        if str(m) not in ctetab.keys():
            addConst(m, 'entero', p.lineno(1))
        dprint(vararr[p[2]]['dimlen'][k])
    vararr[p[2]]['dimlen'][mi-1][1] = 0
    vararr[p[2]]['size'] = darrsize
    dprint('\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+\n',vararr,'\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+')
    p[0] = vararr

def p_DPRIM(p):
    '''DPRIM : OPENSQU CTE_INT CLOSESQU '''
    global R
    if (p[2] < 0):
        printerror(
            'Error Semantico: No se pueden asignar tamaños negativos a los arreglos en la linea %r' % (p.lineno(1)))
    R = R * (p[2])
    # Agregar la cte si no esta
    global ctetab
    if p[2] not in ctetab.keys():
        addConst(p[2], 'entero', p.lineno(1))
    p[0] = {'dims': 1, 'dimlen': [[p[2],0]]}

def p_DECARRID(p):
    '''DECARRID : ID'''
    global R
    R = 1
    p[0] = p[1]

def p_DSEG(p):
    '''DSEG : OPENSQU CTE_INT CLOSESQU DTER
            | empty'''
    global R
    if(p[1] == None):
        p[0] = None
    else:
        if (p[2] < 0):
            printerror(
                'Error Semantico: No se pueden asignar tamaños negativos a los arreglos en la linea %r' % (p.lineno(1)))
        decdims = [[p[2],0]]
        R = R * p[2]
        # Agregar la cte si no la encuentra
        global ctetab
        if p[2] not in ctetab.keys():
            addConst(p[2], 'entero', p.lineno(1))
        if(p[4]!=None):
            decdims.append(p[4])
        p[0] = decdims

def p_DTER(p):
    '''DTER : OPENSQU CTE_INT CLOSESQU
            | empty'''

    global R

    if (p[1] == None):
        p[0] = None
    else:
        if (p[2] < 0):
            printerror(
                'Error Semantico: No se pueden asignar tamaños negativos a los arreglos en la linea %r' % (p.lineno(1)))

        decdims = [p[2],0]
        global ctetab
        if p[2] not in ctetab.keys():
            addConst(p[2], 'entero', p.lineno(1))
        R = R * p[2]
        p[0] = decdims
        dprint('DTER: ',p[0])


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
    #dprint('decfuns')

    if(p[1] == None):
        p[0] = p[1]
    else:
        entfuncs = {}
        entfuncs.update(p[1])

        #Checar que las funciones no se repitan
        if (p[2] != None):
            for fu in p[1].keys():
                if fu in p[2].keys():
                    printerror("Error de Semantica la funcion %r tiene una o más definiciones en la linea %r" % (fu, p.lineno(2)))

            entfuncs.update(p[2])

        p[0] = entfuncs



def p_DECFUNC(p):
    '''DECFUNC :  ALTADECFUN BLOQUE '''
    # Dir. de Funciones
    global dirfunc
    #Direcciones globales
    global tmpintcount
    global tmpfloatcount
    global tmpcharcount
    global tmpboolcount
    global tmppointcount
    # Cuadruplos y su contador
    global cuadcount
    global cuadruplos
    #Scope actual
    global currscope

    #dprint('\n\n\t\t----------------------------TEMPS DE FUNC..........................\n',{'entero': tmpintcount, 'flotante':tmpfloatcount, 'char':tmpcharcount, 'bool': tmpboolcount})

    # Guardar los recursos temporales
    p[1][currscope]['tmpres'] = {'entero': tmpintcount, 'flotante':tmpfloatcount, 'char':tmpcharcount, 'bool': tmpboolcount, 'pointer' : tmppointcount}
    dirfunc.update(p[1])
    #Generar el cuadruplo de fin de función
    cuadruplos.append(('ENDFUNC','','',''))
    global sclines
    sclines.append(p.lineno(1))
    cuadcount += 1
    p[0] = p[1]

def p_ALTADECFUN(p):
    ''' ALTADECFUN : FUNCQUAD TIPOFUN DECFUNCID OPENPAR FUNPARAM CLOSEPAR OPENCUR DECLARACIONES CLOSECUR'''
    # dprint('Lee una dec funcion')
    #Dir. de funciones
    global dirfunc

    # Rangos globales de memoria
    global globalint
    global globalfloat
    global globalchar
    global globalbool
    global globalpoint

    # Cant. Maximas de variables
    global INTMAX
    global FLOATMAX
    global CHARMAX
    global BOOLMAX
    global POINTAYMAX


    # Contadores globales
    global glbintcount
    global glbfloatcount
    global glbcharcount
    global glbboolcount

    entradafun = {p[3]: {'tipo': p[2], 'params': {}, 'inicio':p[1]}}
    address = 'res'
    #Si es de retorno generar su variable global
    if p[2] != 'vacio':

        if (p[2] == 'entero'):  # Asignar las direcciones enteras
            if (glbintcount < INTMAX):
                address = globalint + glbintcount
                glbintcount += 1
            else:

                printerror("Error de Semantica: sobrepaso el limite de funciones con retorno declaradas en la linea %r" % (p.lineno(1)))


        elif (p[2] == 'flotante'):  # Asignar las direcciones flotantes
            if (glbfloatcount < FLOATMAX):
                address = globalfloat + glbfloatcount
                glbfloatcount += 1
            else:

                printerror("Error de Semantica: sobrepaso el limite de funciones con retorno en la linea %r" % (p.lineno(1)))


        elif (p[2] == 'char'):  # Asignar las direcciones char
            if (glbcharcount < CHARMAX):
                address = globalchar + glbcharcount
                glbcharcount += 1
            else:

                printerror("Error de Semantica: sobrepaso el limite de funciones con retorno en la linea %r" % (p.lineno(1)))

        elif (p[2] == 'bool'):  # Asignar las direcciones char
            if (glbboolcount < BOOLMAX):
                address = globalbool + glbboolcount
                glbboolcount += 1
            else:

                printerror("Error de Semantica: sobrepaso el limite de funciones con retorno en la linea %r" % (p.lineno(1)))

        dirfunc['global']['vartab'].update({p[3]: {'tipo': p[2],'address':address}})


        dirfunc['global']['varres'].update({'entero': glbintcount, 'flotante':glbfloatcount, 'char':glbcharcount, 'bool': glbboolcount})

    dirfunc.update({p[3]: {'tipo': p[2]},'params':{}})
    #Agregar la dirección global de la función si hay
    if address != 'res':
        entradafun[p[3]].update({'address':address})
    vartabloc = {}

    # Si hay parametros agregarlos a la entrada de la tabla y a la tabla de variables local
    if (p[5] != None):
        aux = {}
        aux.update(p[5])
        aux.update(vartabloc)
        vartabloc = aux



        #dprint('Add params to vartab')
        entradafun[p[3]].update({'vartab': vartabloc})
        entradafun[p[3]].update({'params': p[5]})

    # Switch para aumentar el contador correcto y verificación de que no se definan variables demás
    # Contadores de variables
    intcount = 0
    floatcount = 0
    charcount = 0
    boolcount = 0

    # Contadores de arreglos
    pointcount = 0



    dirfunc.update(entradafun)
    # Checar que los id de parametros no sean declarados localmente (doble def)
    #dprint(p[3])

    if (p[8] != None):
        # dprint(p[8])
        # if(len(vartabloc) > 0):
        for var in vartabloc.keys():
            if (var in p[8].keys()):
                printerror("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (
                var, p.lineno(8)))



        vartabloc.update(p[8])
    if (vartabloc != None and len(vartabloc) > 0):
        vartabloc, intcount, floatcount, charcount, boolcount = assignvirtualaddress(vartabloc,'local',p.lineno(1))


    #dprint('\n\n\n() () () () () () () () () ()\n\n', vartabloc)
    entradafun[p[3]].update({'vartab': vartabloc, 'varres':{'entero': intcount, 'flotante':floatcount, 'char':charcount, 'bool': boolcount}})

    dirfunc.update(entradafun)

    dprint('dirfunc',dirfunc)
    p[0] = entradafun
    # dprint(p[0])

def p_DECFUNCID(p):
    '''DECFUNCID : ID'''

    #Checar que el id declarado no es una función existente
    global dirfunc
    global special

    global currscope
    global tmpintcount
    global tmpfloatcount
    global tmpcharcount
    global tmpboolcount
    global tmppointcount

    if p[1] in dirfunc.keys():

        printerror("Error de Semantica: El nombre de la función %r  en la linea %r ya fue declarado previamente" % (p[1],p.lineno(1)))

    elif p[1] in special.keys():
        printerror("Error de Semantica: El nombre de la función %r en la linea %r pertenece a una funcion especial" % (p[1], p.lineno(1)))


    tmpintcount = 0
    tmpfloatcount = 0
    tmpcharcount = 0
    tmpboolcount = 0
    tmppointcount = 0
    currscope = p[1]


    p[0] = p[1]

def p_FUNCQUAD(p):
    '''FUNCQUAD : FUNCION'''
    #dprint('inicio func')
    global cuadcount

    p[0] = cuadcount

def p_TIPOFUN(p):
    '''TIPOFUN : TIPO
               | VACIO'''
    #dprint('Llego a tipo')
    p[0] = p[1]

def p_FUNPARAM(p):
    '''FUNPARAM : PARAM
                | empty'''
    p[0] = p[1]

def p_PARAM(p):
    '''PARAM : TIPO DFID PARAMD PARAMS '''
    global R

    funpar = {p[2] : {'tipo' : p[1]}}
    #Si tiene dims
    if(p[3] != None): # si tiene dimensiones
        darrsize = R
        mi = 0
        dprint('Antes de poner las m',p[3], mi,p[3]['dims'])
        for k in range(p[3]['dims']):
            mi += 1

            m = R / p[3]['dimlen'][k][0]
            p[3]['dimlen'][k][1] = m

            R = m

        p[3]['dimlen'][mi - 1][1] = 0
        p[3]['size'] = darrsize
        dprint(p[3])
        funpar[p[2]].update(p[3])
    # hay más parametros despues de esta
    if(p[4]!=None):
        if(p[2] in p[4].keys()):
            printerror("Error de Semantica la variable %r tiene una o más definiciones en la linea %r" % (p[2], p.lineno(4)))

        else:
            funpar.update(p[4])
    p[0] = funpar

def p_DFID(p):
    '''DFID : ID'''
    global R
    R = 1
    p[0] = p[1]

def p_PARAMS(p):
    '''PARAMS : COMMA PARAM
              | empty'''
    if(p[1] != None):
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_PARAMD(p):
    '''PARAMD : OPENSQU CTE_INT CLOSESQU PDSEG
              | empty'''
    global R
    pdim = {'dims':1 , 'dimlen' : []}
    if(p[1] == None):
        p[0] = p[1]
    else:
        if(p[2] < 0):
            printerror('Error Semantico: No se pueden asignar tamaños negativos a los arreglos en la linea %r' % (p.lineno(1)))

        pdim['dimlen'] += [[p[2],0]]
        R = R * (p[2])
        global ctetab
        if p[2] not in ctetab.keys():
            addConst(p[2], 'entero', p.lineno(1))
        if(p[4] != None):
            pdim['dimlen'] += p[4]['dimlen']
            pdim['dims'] = p[4]['dims']

        p[0] = pdim

def p_PDSEG(p):
    '''PDSEG : OPENSQU CTE_INT CLOSESQU PDTER
              | empty'''
    global R
    pdim = {'dims': 2}
    if (p[1] == None):
        p[0] = p[1]
    else:
        if (p[2] < 0):
            printerror(
                'Error Semantico: No se pueden asignar tamaños negativos a los arreglos en la linea %r' % (p.lineno(1)))
        pdim['dimlen'] = [[p[2],0]]
        R = R * (p[2])
        global ctetab
        if p[2] not in ctetab.keys():
            addConst(p[2], 'entero', p.lineno(1))
        if (p[4] != None):
            pdim['dimlen']+=p[4]['dimlen']
            pdim['dims'] = p[4]['dims']
        dprint(pdim)
        p[0] = pdim

def p_PDTER(p):
    '''PDTER : OPENSQU CTE_INT CLOSESQU
             | empty'''
    pdim = {'dims': 3 , 'dimlen' : []}
    global R
    if (p[1] == None):
        p[0] = p[1]
    else:
        if (p[2] < 0):
            printerror(
                'Error Semantico: No se pueden asignar tamaños negativos a los arreglos en la linea %r' % (p.lineno(1)))
        pdim['dimlen'] += [[p[2],0]]
        global ctetab
        if p[2] not in ctetab.keys():
            addConst(p[2], 'entero', p.lineno(1))
        R = R * (p[2])
        p[0] = pdim


######
# Declaración Bloque
######

def p_BLOQUE(p):
    '''BLOQUE : OPENCUR ESTATUTOS CLOSECUR'''
  
def p_ESTATUTOS(p):
    '''ESTATUTOS : ESTATUTO ESTATUTOS
                 | empty'''


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
                '''

# Impresion -------------------------  
def p_IMPRESION(p):
    '''IMPRESION : IMPRIMIR OPENPAR PRINTABLE PRINTARGS CLOSEPAR SEMICOLON'''
    global cuadcount
    global cuadruplos

    pargs = [p[3]]
    if(p[4] != None):
        pargs = pargs + p[4]
    for prin in pargs:
        cuadruplos.append(('imprimir',prin,'',''))
        global sclines
        sclines.append(p.lineno(1))
        cuadcount+=1

def p_PRINTARGS(p):
    '''PRINTARGS : COMMA PRINTABLE PRINTARGS
                 | empty'''

    if (p[1] != None):

        pargs = [p[2]]
        if(p[3] != None):
            pargs = pargs + p[3]
        p[0] = pargs
    else:
        p[0] = None

def p_PRINTABLE(p):
    '''PRINTABLE : EXPRESION
                 | CTE_STRING'''
    global pilaoperand
    global ptipo
    #Tabla de constantes
    global ctetab
    global objctetab
    #Rango de constantes string y su contador
    global STRINGMAX
    global ctestringcount


    if type(p[1]) == str and p[1] != 'exp':
        ctkey = p[1]
        if ctkey in ctetab.keys():
            p[0] = ctetab[p[1]]
        else:
            p[0] = addConst(p[1],'cadena',p.lineno(1))


    else:
        op = pilaoperand.pop()
        ptipo.pop()
        p[0] = op


# Asignacion -------------------

def p_ASIGNACION(p):
    '''ASIGNACION : ID EQ ARR_TEX SEMICOLON %prec EQS
        | ID EQ EXPRESION SEMICOLON %prec EQS
        | ID ADIMS EQ EXPRESION SEMICOLON %prec EQS
 '''
    #dprint('Lee asignacion')
    #Evaluar que la asignación sea correcta
    #Cubo Semántico
    global cubosem
    #Pila de operandos y Pila de tipos
    global pilaoperand
    global ptipo
    #Dir de funciones
    global dirfunc
    #Cuadruplos y su contador
    global cuadruplos
    global cuadcount
    # Tabla de constantes
    global ctetab
    # Rangos de Temporales y contador de temporales
    global tmpintcount
    global tmppointcount
    global INTMAX
    global POINTMAX
    global tempint
    global temppoint
    global sclines

    #Se checa que el id a asignar exista
    vartipo = None
    addresses = None
    arrsize = 0
    dprint(ptipo)
    dprint(p[3])
    if p[2] == '=':
        #Asignación a un id por medio de una expresión o arreglo textual
        if (p[1] in dirfunc[currscope]['vartab'].keys()):
            vartipo = dirfunc[currscope]['vartab'][p[1]]['tipo']

            if ('address' in dirfunc[currscope]['vartab'][p[1]].keys()):  # Checar si se le ha asignado una address

                addresses = dirfunc[currscope]['vartab'][p[1]]['address']

            if (type(p[3]) is dict):
                dprint(p[3])
                if 'dims' not in dirfunc[currscope]['vartab'][p[1]].keys():
                    printerror('Error Semántico : La asignacion de variable %r en la linea %r no es un arreglo y por ende no se le puede asignar un arreglo' % (p[1], p.lineno(1)))
                arrsize = dirfunc[currscope]['vartab'][p[1]]['size']
                if (dirfunc[currscope]['vartab'][p[1]]['dims'] != p[3]['dims']):
                    printerror(
                        'Error Semántico : La asignacion de variable %r en la linea %r no tiene las dimensiones de lo que se le esta asignando' % (p[1], p.lineno(1)))


        elif (p[1] in dirfunc['global']['vartab'].keys()):
            vartipo = dirfunc['global']['vartab'][p[1]]['tipo']

            if ('address' in dirfunc['global']['vartab'][p[1]].keys()):  # Checar si se le ha asignado una address

                addresses = dirfunc['global']['vartab'][p[1]]['address']

            if (type(p[3]) is dict):
                dprint(p[3])
                if 'dims' not in dirfunc['global']['vartab'][p[1]].keys():
                    printerror('Error Semántico : La asignacion de variable %r en la linea %r no es un arreglo y por ende no se le puede asignar un arreglo' % (p[1], p.lineno(1)))
                arrsize = dirfunc['global']['vartab'][p[1]]['size']
                if (dirfunc['global']['vartab'][p[1]]['dims'] != p[3]['dims']):
                    printerror('La asignacion de variable %r en la linea %r no tiene las dimensiones de lo que se le esta asignando' % (p[1], p.lineno(1)))

        else:
            printerror('La variable %r en la linea %r no ha sido declarada' % (p[1], p.lineno(1)))

        ############################### Asignación por id #############################

        if type(p[3]) is str and p[3] == 'exp':



            asig = pilaoperand.pop()

            asigt = ptipo.pop()

            dprint('Asignando', p[1], ' = ', asig, ' tipo ', asigt)
            # Detectar si algun operador es una llamada de una funcion vacia
            if asigt == 'vacio':
                printerror('Error Semantico: se llamo una funcion vacia como operador en la linea %r' % (
                    p.lineno(1)))

            if (cubosem['='][vartipo][asigt] != 'error'):
                dprint('Cubo dice: ', cubosem['='][vartipo][asigt])
                # Generación de cuadruplo de asignación
                if (addresses != None):
                    cuadruplos.append(('=', asig, '', addresses))

                    sclines.append(p.lineno(1))
                    cuadcount += 1
                else:
                    cuadruplos.append(('=', asig, '', p[1]))

                    sclines.append(p.lineno(1))
                    cuadcount += 1
                p[0] = vartipo  # Se regresa al token el valor del id asignado
            else:

                printerror('Error de Semantica, el no se puede asignar %r a %r  en la linea %r' % (
                    vartipo, asigt, p.lineno(1)))

        #----------------------------ASIGNACION POR ARREGLO TEXTUAL------------------------------------------------
        else:
            dprint('\nasginación de arr\n')

            addr = addresses

            asig = pilaoperand.pop()

            asigt = ptipo.pop()

            dprint('Asignando', p[1], ' = ', asig, ' tipo ', asigt)
            # Detectar si algun operador es una llamada de una funcion vacia
            if asigt == 'vacio':

                printerror('Error Semantico: se llamo una funcion vacia como operador en la linea %r' % (
                    p.lineno(1)))


            if (cubosem['='][vartipo][asigt] != 'error'):
                dprint('Cubo dice: ', cubosem['='][vartipo][asigt])
                #Generación de cuadruplo de asignación
                #if (addresses != None):
                #    cuadruplos.append(('=', asig, '', addresses))
#
                #    sclines.append(p.lineno(1))
                #    cuadcount += 1
                #else:
                #    cuadruplos.append(('=', asig, '', p[1]))
#
                #    sclines.append(p.lineno(1))
                #    cuadcount += 1
                addr += arrsize-1
                for i in range(arrsize):
                    asig = pilaoperand.pop()
                    asigt = ptipo.pop()
                    cuadruplos.append(('=', asig, '', addr))
                    sclines.append(p.lineno(1))
                    cuadcount += 1
                    addr -= 1
                p[0] = vartipo # Se regresa al token el valor del id asignado
            else:


                printerror('Error de Semantica, el no se puede asignar %r a %r  en la linea %r' % (
                vartipo, asigt, p.lineno(1)))



    else:
        #Asignación a la llamada de un arreglo ej. N[1] = 2

        if (p[1] in dirfunc[currscope]['vartab'].keys()):
            var = dirfunc[currscope]['vartab'][p[1]]
            vartipo = dirfunc[currscope]['vartab'][p[1]]['tipo']
        elif (p[1] in dirfunc['global']['vartab'].keys()):
            var = dirfunc['global']['vartab'][p[1]]
            vartipo = dirfunc['global']['vartab'][p[1]]['tipo']
        else:
            printerror('Error Semántico: La variable %r en la linea %r no ha sido declarada' % (p[1], p.lineno(1)))
        if 'dims' not in var.keys():
            printerror('Error Semántico: La variable %r en la linea %r no es un arreglo'% (p[1], p.lineno(1)))
        si = p[2]
        dprint('subindices : ', si)
        address = None
        # Por el momento se pide que se den subindices extrictamente a las dimensiones del arreglo
        if var['dims'] != len(si):
            printerror(
                'Error Semantico: La cantidad de subindices no coincide con las dimensiones del arreglo en la linea %r' % (
                    p.lineno(1)))
        else:
            DIMS = 1
            for i in range(len(si)):
                # Verificar que el sub indice sea correcto

                cuadruplos.append(('VERIF', si[i], ctetab[str(var['dimlen'][i][0])], ''))

                sclines.append(p.lineno(1))
                cuadcount += 1

                if DIMS == len(si):
                    m = 1
                    pilaoperand.append(si[i])
                else:
                    m = var['dimlen'][i][1]

                    address = None
                    if tmpintcount < INTMAX:
                        address = tmpintcount + tempint
                        tmpintcount += 1
                    else:
                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                p.lineno(1)))
                    dprint('si = ', si[i], 'TEMPRANGE = ', temppoint, ' vardimlen = ', var['dimlen'][i], 'm = ', m,
                           'ctekeys \n', list(ctetab.keys()))
                    cuadruplos.append(('*', si[i], ctetab[str(m)], address))

                    sclines.append(p.lineno(1))
                    cuadcount += 1
                    pilaoperand.append(address)

                if DIMS > 1:
                    address = None
                    if tmpintcount < INTMAX:
                        address = tmpintcount + tempint
                        tmpintcount += 1
                    else:
                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                p.lineno(1)))
                    aux1 = pilaoperand.pop()
                    aux2 = pilaoperand.pop()
                    cuadruplos.append(('+', aux1, aux2, address))

                    sclines.append(p.lineno(1))
                    cuadcount += 1
                    pilaoperand.append(address)
                DIMS += 1
            # Crear la dir de pointer
            aux = pilaoperand.pop()
            address = None
            if tmppointcount < POINTMAX:
                address = tmppointcount + temppoint
                tmppointcount += 1
            else:
                printerror(
                    'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                        p.lineno(1)))
            cuadruplos.append(('+', aux, ctetab[str(var['address'])], '*'+str(address)))

            sclines.append(p.lineno(1))
            cuadcount += 1


        asig = pilaoperand.pop()
        asigt = ptipo.pop()
        dprint('\n\nPila Operandos: ',pilaoperand,'\nPila tipos: ',ptipo)
        dprint('\nAsignando', p[1], ' = ', asig, ' tipo ', asigt)


        if (cubosem['='][vartipo][asigt] != 'error'):
            dprint('Cubo dice: ',cubosem['='][vartipo][asigt])
            #Generación de cuadruplo de asignación
            cuadruplos.append(('=', asig, '', address))

            sclines.append(p.lineno(1))
            cuadcount += 1
            p[0] = vartipo # Se regresa al token el valor del id asignado
        else:
            printerror('Error de Semantica, el no se puede asignar %r a %r  en la linea %r' % (vartipo, asigt, p.lineno(1)))


#def p_ASIGNARR(p):
#    '''ASIGNARR : ARR_TEX SEMICOLON'''
#
#    #dprint( "⠄⠄⠄⠄⢠⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣿⣿⣿⣿⣆⠄⠄⠄\n⠄⠄⣼⢀⣿⣿⣿⣿⣏⡏⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣧⢻⣿⣿⣿⣿⡆⠄⠄\n⠄⠄⡟⣼⣿⣿⣿⣿⣿⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣇⢻⣿⣿⣿⣿⠄⠄\n⠄⢰⠃⣿⣿⠿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠙⠿⣿⣿⣿⣿⣿⠄⢿⣿⣿⣿⡄⠄\n⠄⢸⢠⣿⣿⣧⡙⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠈⠛⢿⣿⣿⡇⠸⣿⡿⣸⡇⠄\n⠄⠈⡆⣿⣿⣿⣿⣦⡙⠳⠄⠄⠄⠄⠄⠄⢀⣠⣤⣀⣈⠙⠃⠄⠿⢇⣿⡇⠄\n⠄⠄⡇⢿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⣠⣶⣿⣿⣿⣿⣿⣿⣷⣆⡀⣼⣿⡇⠄\n⠄⠄⢹⡘⣿⣿⣿⢿⣷⡀⠄⢀⣴⣾⣟⠉⠉⠉⠉⣽⣿⣿⣿⣿⠇⢹⣿⠃⠄\n⠄⠄⠄⢷⡘⢿⣿⣎⢻⣷⠰⣿⣿⣿⣿⣦⣀⣀⣴⣿⣿⣿⠟⢫⡾⢸⡟⠄.\n⠄⠄⠄⠄⠻⣦⡙⠿⣧⠙⢷⠙⠻⠿⢿⡿⠿⠿⠛⠋⠉⠄⠂⠘⠁⠞⠄⠄⠄\n⠄⠄⠄⠄⠄⠈⠙⠑⣠⣤⣴⡖⠄⠿⣋⣉⣉⡁⠄⢾⣦⠄⠄⠄⠄⠄⠄⠄⠄ ")
#    pass

def p_ADIMS(p):
    '''ADIMS : OPENSQU EXPRESION CLOSESQU ASEGD
             | empty'''
    if p[1] != None:

        global pilaoperand
        global ptipo
        etipo = ptipo.pop()
        si = []
        if etipo == 'entero':
            si.append(pilaoperand.pop())
        else:
            printerror('Error Semantico : Se esperaba que las expresiones de los subindices sean enteras en la linea %r' % (p.lineno(1)))
        if p[4] != None:
            si+= p[4]
        p[0] = si

def p_ASEGD(p):
    '''ASEGD : OPENSQU EXPRESION CLOSESQU ATERD
             | empty'''
    if p[1] != None:

        global pilaoperand
        global ptipo
        etipo = ptipo.pop()
        si = []
        if etipo == 'entero':
            si.append(pilaoperand.pop())
        else:
            printerror('Error Semantico : Se esperaba que las expresiones de los subindices sean enteras en la linea %r' % (p.lineno(1)))
        if p[4] != None:
            si+= p[4]
        p[0] = si


def p_ATERD(p):
    '''ATERD : OPENSQU EXPRESION CLOSESQU
             | empty'''
    if p[1] != None:
        global pilaoperand
        global ptipo
        etipo = ptipo.pop()
        si = []
        if etipo == 'entero':
            si.append(pilaoperand.pop())
        else:
            printerror(
                'Error Semantico : Se esperaba que las expresiones de los subindices sean enteras en la linea %r' % (
                    p.lineno(1)))
        p[0] = si
    
# Condicion ----------------------------

def p_CONDICION(p):
    'CONDICION : SI IFGTO BLOQUE IFELSE'
    global cuadruplos
    global cuadcount
    global psaltos


    endState = psaltos.pop()
    #dprint('length cuad: ', len(cuadruplos), '\npopsaltos: ', endState,'\ncount: ', cuadcount)
    cuadruplos[endState] = cuadruplos[endState] + (cuadcount,)

def p_IFGTO(p):
    '''IFGTO : OPENPAR EXPRESION CLOSEPAR '''
    global ptipo
    global pilaoperand
    global cuadruplos
    global cuadcount
    global psaltos

    tip = ptipo.pop()
    if(tip != 'bool'):
        printerror(
            'Error de Semantica, %r no es una expresion booleana en la linea %r' % (
                tip, p.lineno(1)))

    else:
        res = pilaoperand.pop()
        cuadruplos.append(('GOTOF',res,''))
        global sclines
        sclines.append(p.lineno(1))
        psaltos.append(cuadcount)
        cuadcount += 1

#Regla gramatica del if-else
def p_IFELSE(p):
    '''IFELSE : NSINO BLOQUE
              | empty'''

#Punto neuralgico del if-else
def p_BLOQIF(p):
    '''NSINO : SINO'''
    if (p[1] != None):
        global cuadruplos
        global cuadcount
        global psaltos
        # dprint('\tELSE\nlength cuad: ', len(cuadruplos),  '\ncount: ', cuadcount)
        cuadruplos.append(('GOTO', '', ''))
        global sclines
        sclines.append(p.lineno(1))
        cuadcount += 1
        falseState = psaltos.pop()
        cuadruplos[falseState] = cuadruplos[falseState] + (cuadcount,)
        # dprint('\tAFTERCUAD\nlength cuad: ', len(cuadruplos), '\npopsaltos: ', falseState, '\ncount: ', cuadcount)

        psaltos.append(cuadcount - 1)


# Bucles --------------------------------------------------------------------------------------------------------------

def p_BUCLE(p):
    '''BUCLE : WHILE
             | FOR'''

def p_WHILE(p):
    '''WHILE : NWHILE WCOND BLOQUE'''
    global cuadcount
    global cuadruplos
    global psaltos
    retState = psaltos.pop()
    condState = psaltos.pop()
    cuadruplos.append(('GOTO', '', '',condState))
    global sclines
    sclines.append(p.lineno(1))
    cuadcount += 1
    #dprint("\t\tWHILE\nCuadcuant: ", cuadcount, '\ncuadruplo:', cuadruplos[cuadcount-1],'\n\tcondState: ',cuadruplos[condState])
    #dprint('length cuad: ', len(cuadruplos), '\npopsaltos: ', endState, '\ncount: ', cuadcount)
    cuadruplos[retState] = cuadruplos[retState] + (cuadcount,)

def p_NWHILE(p):
    '''NWHILE : MIENTRAS'''
    global cuadcount
    global psaltos
    global cuadruplos

    psaltos.append(cuadcount)

def p_WCOND(p):
    '''WCOND : OPENPAR EXPRESION CLOSEPAR'''
    global cuadcount
    global cuadruplos
    global psaltos
    global pilaoperand
    global ptipo

    tip = ptipo.pop()
    if(tip != 'bool'):
        printerror('Error de Semantica, %r no es una expresion booleana en la linea %r' % (tip, p.lineno(2)))
    else:
        res = pilaoperand.pop()
        cuadruplos.append(('GOTOF',res,''))
        global sclines
        sclines.append(p.lineno(1))
        psaltos.append(cuadcount)
        cuadcount += 1

def p_FOR(p):
    '''FOR : POR OPENPAR FORINIT FORSTEP CLOSEPAR BLOQUE'''
    global cuadcount
    global cuadruplos
    global psaltos
    retState = psaltos.pop()
    condState = psaltos.pop()
    cuadruplos.append(('GOTO', '', '', condState))
    global sclines
    sclines.append(p.lineno(1))
    cuadcount += 1
    # dprint("\t\tFOR\nCuadcuant: ", cuadcount, '\ncuadruplo:', cuadruplos[cuadcount-1],'\n\tcondState: ',cuadruplos[condState])
    # dprint('length cuad: ', len(cuadruplos), '\npopsaltos: ', endState, '\ncount: ', cuadcount)
    cuadruplos[retState] = cuadruplos[retState] + (cuadcount,)

def p_FORINIT(p):
    '''FORINIT : ASIGNACION
               | empty '''
    global psaltos
    global cuadcount
    global cuadruplos

    if(p[1] != None):
        # 1.- Checar que sea una variable numeríca a utilizar
        if(p[1] not in  ['entero','flotante']):

            printerror('Error de Semantica, %r se esperaba que fuera entero en la linea %r' % (p[1], p.lineno(1)))
        else:
            #2.- Como es un while disfrazado, se mete la "migaja" a la pila antes de la expresion y el paso

            psaltos.append(cuadcount)

def p_FOREXP(p):
    '''FOREXP : EXPRESION SEMICOLON'''
    global cuadcount
    global cuadruplos
    global psaltos
    global sclines

    tipexp = ptipo.pop()
    # dprint('\t\t\t\tChecar la expresion del bool:', tipexp, '\n', pilaoperand, '\n', ptipo, '\n')
    # dprint('\t\t\tChecar la asignación: ',  tipas, '\n')
    if (tipexp not in ['bool']):
        printerror('Error de Semantica, %r no es una expresion booleana en la linea %r' % (tipexp, p.lineno(2)))

    res = pilaoperand.pop()
    cuadruplos.append(('GOTOF', res, ''))

    sclines.append(p.lineno(1))
    psaltos.append(cuadcount)
    cuadcount += 1
    cuadruplos.append(('GOTO','',''))

    sclines.append(p.lineno(1))
    psaltos.append(cuadcount)
    cuadcount+=1
    psaltos.append(cuadcount)

def p_FORSTEP(p):
    '''FORSTEP : FOREXP  ASIGNACION'''
    global cuadcount
    global cuadruplos
    global psaltos
    global pilaoperand
    global ptipo

    #dprint('\n', pilaoperand, '\n', ptipo, '\n')
    tipas = p[2]



    if (tipas not in ['entero', 'flotante']):

        printerror('Error de Semantica, %r se esperaba que fuera entero o flotante en la linea %r' % (p[1], p.lineno(1)))
    else:
        # 2.- Como es un while disfrazado, se mete la "migaja" a la pila antes de la expresion y el paso

        salasig = psaltos.pop()
        salacod = psaltos.pop()
        gtf = psaltos.pop()
        cond = psaltos.pop()

        cuadruplos.append(('GOTO','','',cond))
        global sclines
        sclines.append(p.lineno(1))

        psaltos.append(salasig)
        psaltos.append(gtf)
        cuadcount += 1
        cuadruplos[salacod] = cuadruplos[salacod] + (cuadcount,)



    # Return --------------------------------------------------------------------------------------------------------------

def p_RETURNF(p):
    '''RETURNF : REGRESAR EXPRESION SEMICOLON'''
    #dir de funciones
    global dirfunc
    #Scope actual
    global currscope
    #Pila de tipos y operandos
    global pilaoperand
    global ptipo
    #Cuadrup´los y su contador
    global cuadcount
    global cuadruplos
    #Cubo semantico
    global cubosem

    # Obtener el tipo de la funcion
    functipo = dirfunc[currscope]['tipo']

    #Evitar el retorno en funciones vacias
    if functipo == 'vacio':

        printerror('Error Semantico: se llamo return en una funcion vacia en la linea %r' % (p.lineno(1)))

    else:
        rettype = ptipo.pop();
        if (cubosem['='][functipo][rettype] != 'error'):
            dprint('Cubo dice: ',cubosem['='][functipo][rettype])
            retop = pilaoperand.pop()
            asig = dirfunc['global']['vartab'][currscope]['address']
            dprint('Se pasa retorno a variable global ',currscope,' con address ',asig)
            #Generación de cuadruplo de asignación
            cuadruplos.append(('RET', retop, '',asig ))
            global sclines
            sclines.append(p.lineno(1))
            cuadcount += 1

            p[0] = functipo # Se regresa al token el valor del id asignado
        else:
            printerror('Error de Semantica, el no se puede retornar %r en la funcion de tipo %r  en la linea %r' % (functipo, rettype, p.lineno(1)))





#####
# Expresion
#####

# Funcion para manejar la generación de cuadruplos
def expcuadgen(expopers,linenum):

    # Pila de operandos y tipos
    global poper
    global pilaoperand
    global ptipo
    #Cuadruplos
    global cuadcount
    #Rangos temporales de memoria
    global tempint
    global tempfloat
    global tempchar
    global tempbool
    #Contadores de addresses temporales
    global tmpintcount
    global tmpfloatcount
    global tmpcharcount
    global tmpboolcount
    global tmppointcount
    # Maximos de variable
    global INTMAX
    global FLOATMAX
    global CHARMAX
    global BOOLMAX
    if (poper[-1:].pop() != None):
        if (poper[-1:].pop() in expopers):
            rop = pilaoperand.pop()
            ropt = ptipo.pop()
            lop = pilaoperand.pop()
            lopt = ptipo.pop()

            # Detectar si algun operador es una llamada de una funcion vacia
            if lopt == 'vacio' or ropt == 'vacio':

                printerror('Error Semantico: se llamo una funcion vacia como operador en la linea %r' % (
                    linenum))

            if lop == 'arr' or rop == 'arr':
                printerror('Error Semantico: Se esta intentando hacer una operación de expresion sobre un arreglo textual en la linea %r, lo cual no se puede hacer' % (p.lineno(1)))

            oper = poper.pop()
            if (cubosem[oper][ropt][lopt] != 'error'):
                restipo = cubosem[oper][ropt][lopt]
                #dprint('La operacion de ', lop, oper, rop, 'resulta en ' + restipo)
                # Asegurar de guardar en el espacio temporal correspondiente
                address = 'res'
                if restipo == 'entero':
                    if tmpintcount < INTMAX:
                        address = tmpintcount + tempint
                        tmpintcount += 1
                    else:

                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                linenum))


                elif restipo == 'flotante':
                    #dprint('\t\tFloat', tmpfloatcount, FLOATMAX)
                    if tmpfloatcount < FLOATMAX:
                        address = tmpfloatcount + tempfloat
                        tmpfloatcount += 1
                    else:

                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                linenum))


                elif restipo == 'char':
                    if tmpcharcount < CHARMAX:
                        address = tmpcharcount + tempchar
                        tmpcharcount += 1
                    else:

                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                linenum))


                elif restipo == 'bool':
                    if tmpboolcount < BOOLMAX:
                        address = tmpboolcount + tempbool
                        tmpboolcount += 1
                    else:

                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                linenum))


                # generar cuadruplo
                cuadruplos.append((oper, lop, rop, address))
                global sclines
                sclines.append(linenum)
                cuadcount += 1
                pilaoperand.append(address)
                ptipo.append(restipo)
            else:
                printerror(
                    'Error de Semantica, el no se puede operacion relacional %r con %r  en la linea %r' % (
                        lopt, ropt, linenum))


def p_EXPRESION(p):
    '''EXPRESION :  EXPRESIONR
                | EXPRLOG '''
    # Generar cuadruplos
    expcuadgen(['||', '&&'], p.lineno(1))
    p[0] = 'exp'

#def p_EXPERLOGS(p):
#    '''EXPRLOGS : EXPRESIONR
#                | EXPRLOG'''
#    # ['||','&&']
#
#    #Generar cuadruplos
#    expcuadgen(['||', '&&'], p.lineno(1))

def p_EXPRLOG(p):
    '''EXPRLOG : EXPRESION AND EXPRESION %prec LOG
               | EXPRESION OR EXPRESION %prec LOG
               | empty'''
    global poper
    if(p[1] != None):
        poper.append(p[2])
    p[0] = 'expLOG'
    #dprint(poper)

def p_EXPRESIONR(p):
    '''EXPRESIONR : EXP
                | EXPR'''
    expcuadgen(['>', '<', '<=', '>=', '==', '!='], p.lineno(1))
    p[0] = 'EXPR'

#def p_EXPRS(p):
#    '''EXPRS : EXPR'''
#    # Generar cuadruplos
#    expcuadgen(['>', '<', '<=', '>=', '==', '!='], p.lineno(1))
#    p[0] = 'EXPR'

def p_EXPR(p):
    '''EXPR : EXP GT EXP %prec REL
             | EXP LT EXP %prec REL
             | EXP EXLAM EQ EXP %prec REL
             | EXP EQ EQ EXP %prec REL
             | EXP GT EQ EXP %prec REL
             | EXP LT EQ EXP %prec REL
             | empty
                 '''
    global poper
    if(p[1] != None):
        op = p[2]
        if(p[3] == '='):
            op = op + p[3]
        dprint('\n\n operaor rel : ', op)
        if (op in ['>', '<', '<=', '>=', '==', '!=']):
            poper.append(op)
    p[0] = 'expLOG'
def p_EXP(p):
    '''EXP : TERMINO
    | TERMINOSS
            '''
    # Generar cuadruplos
    expcuadgen(['+', '-'], p.lineno(1))

    p[0] = 'EXP'

def p_TERMINOSS(p):
    '''TERMINOSS : EXP PLUS EXP %prec PLUSMINUS
                | EXP MINUS EXP %prec PLUSMINUS
                | empty'''
    global poper
    if p[1] != None:
        if p[2] == '+' or p[2] == '-':
            poper.append(p[2])
    #dprint(poper)
    
def p_TERMINO(p):
    '''TERMINO : FACTOR
                | FACTORESS
               '''
    # Generar cuadruplos
    expcuadgen(['*', '/'], p.lineno(1))

    p[0] = 'Termino'

def p_FACTORESS(p):
    '''FACTORESS : TERMINO MUL TERMINO %prec MULDIV
                | TERMINO DIV TERMINO %prec MULDIV
                | empty'''
    global poper
    if p[1] != None:
        if p[2] == '*' or p[2] == '/':
            poper.append(p[2])
    #dprint(poper)
    
def p_FACTOR(p):
    '''FACTOR : SIGNOVAR VARCTE
              | OPENPAR EXPRESION CLOSEPAR'''
    if (p[1] == '('):
        p[0] = p[2]
    else:
        if(p[1] != None):
            #Pila de operandos
            global pilaoperand
            #Pila de tipos
            global ptipo
            #Cuadruplos
            global cuadruplos
            #contador de cuadruplos
            global cuadcount
            #Direcciones de temporales
            global tempint
            global tempfloat
            global tempchar
            global tempbool
            #Contadores temporales
            global tmpintcount
            global tmpfloatcount
            global tmpcharcount
            global tmpboolcount
            #maximas de variables
            global INTMAX
            global FLOATMAX
            global CHARMAX
            global BOOLMAX


            lop = pilaoperand.pop()
            lopt = ptipo.pop()
            if(cubosem[p[1]]['none'][lopt] != 'error'):
                oper = p[1]
                rop = ''
                #lop = p[2]
                restipo = cubosem[oper]['none'][lopt]

                #Detectar si algun operador es una llamada de una funcion vacia
                if lop == 'vacio' or rop == 'vacio':

                    printerror('Error Semantico: se llamo una funcion vacia como operador en la linea %r' % (
                                p.lineno(1)))


                address = 'res'
                if restipo == 'entero':
                    if tmpintcount < INTMAX:
                        address = tmpintcount + tempint
                        tmpintcount += 1
                    else:
                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                p.lineno(1)))

                elif restipo == 'flotante':
                    if tmpfloatcount < FLOATMAX:
                        address = tmpfloatcount + tempfloat
                        tmpfloatcount += 1
                    else:
                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                p.lineno(1)))

                elif restipo == 'char':
                    if tmpcharcount < CHARMAX:
                        address = tmpcharcount + tempchar
                        tmpcharcount += 1
                    else:
                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                p.lineno(1)))

                elif restipo == 'bool':
                    if tmpboolcount < BOOLMAX:
                        address = tmpboolcount + tempbool
                        tmpboolcount += 1
                    else:
                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                p.lineno(1)))

                # generar cuadruplo
                cuadruplos.append((oper, lop, rop, address))
                global sclines
                sclines.append(p.lineno(1))
                cuadcount += 1
                pilaoperand.append(address)
                ptipo.append(restipo)
            else:
                printerror('Error de Semantica, no se le puede dar un signo a una variable que no sea un entero o flotante')
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
    #Dir de funciones
    global dirfunc
    #Scope en el que se esta trabajando
    global currscope
    #Funciones espeicales
    global special
    #pila de operadores
    global poper

    #Maximos de variables
    global INTMAX
    global FLOATMAX
    global CHARMAX
    global BOOLMAX
    global STRINGMAX
    # Cuadruplos
    global cuadruplos
    # contador de cuadruplos
    global cuadcount
    # Direcciones de temporales
    global tempint
    global tempfloat
    global tempchar
    global tempbool
    # Contadores temporales
    global tmpintcount
    global tmpfloatcount
    global tmpcharcount
    global tmpboolcount
    #Ctetab
    global ctetab


    #dprint('Para el elemento',p[1],'En el scope '+currscope+' Se encuentra la dir func así:')
    #dprint('dirfunc', dirfunc, '\n\n')
    #pilaoperand.append(p[1])
    #dprint('operadores ',poper)
    #dprint('Se leyo en expresion',p[1])
    #dprint('Pila de operandos',pilaoperand)
    #dprint('-------------------------------------------------------------------------------------------------------')

    if isinstance(p[1],int): # ---------------------------- CTES INT ---------------------------------------------
        #Checar si la constante la ha encontrado antes
        ctkey = str(p[1])
        if ctkey in ctetab.keys():
            pilaoperand.append(ctetab[ctkey])
        else:
            pilaoperand.append(addConst(p[1],'entero',p.lineno(1)))


        ptipo.append('entero')
    elif isinstance(p[1],float): # ---------------------------- CTE FLOAT ---------------------------------------------
        # Checar si la constante la ha encontrado antes
        ctkey = str(p[1])
        if ctkey in ctetab.keys():
            pilaoperand.append(ctetab[ctkey])
        else:
            pilaoperand.append(addConst(p[1],'flotante',p.lineno(1)))
        ptipo.append('flotante')

    elif p[1] == 'verdadero' or p[1] == 'falso': # ---------------------------- CTES BOOL -------------------------------
        # Checar si la constante la ha encontrado antes
        if p[1] in ctetab.keys():
            pilaoperand.append(ctetab[p[1]])
        else:
            pilaoperand.append(addConst(p[1], 'bool', p.lineno(1)))

        ptipo.append('bool')
    elif re.fullmatch("\"[^\"]+\"",p[1]):# ---------------------------- CTES STRING -------------------------------------
        ctkey = p[1]
        if ctkey in ctetab.keys():
            pilaoperand.append(ctetab[ctkey])
        else:
            pilaoperand.append(addConst(p[1], 'cadena', p.lineno(1)))

        ptipo.append('cadena')


    elif re.fullmatch("\'[^\']\'",p[1]):# ---------------------------- CTES CHAR ---------------------------------------
        # Checar si la constante la ha encontrado antes
        if p[1] in ctetab:
            pilaoperand.append(ctetab[p[1]])
        else:
            pilaoperand.append(addConst(p[1],'char',p.lineno(1)))

        ptipo.append('char')


    elif re.fullmatch(r"\$[a-zA-Z]([a-zA-Z]|[0-9]|[_])*",p[1]):# ---------------------------- LLAMADA FUNC ------------------------------------
        #llamada func
        vartipo = None
        isSpecial = False
        funcadd = 'address'

        if (p[1][1:] in dirfunc.keys()):
            vartipo = dirfunc[p[1][1:]]['tipo']

            if 'address' in dirfunc[p[1][1:]].keys():
                funcadd = dirfunc[p[1][1:]]['address']
        elif (p[1][1:] in special.keys()):
            vartipo = special[p[1][1:]]['tipo']
            isSpecial = True

        else:

            printerror('La funcion %r en la linea %r no ha sido declarada' % (p[1], p.lineno(1)))


        if(isSpecial):
            pilaoperand.append(p[1])
            ptipo.append(vartipo)
        else:
            if(vartipo != 'vacio'):
                address = 'res'
                if vartipo == 'entero':
                    if tmpintcount < INTMAX:
                        address = tmpintcount + tempint
                        tmpintcount += 1
                    else:

                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                p.lineno(1)))


                elif vartipo == 'flotante':
                    if tmpfloatcount < FLOATMAX:
                        address = tmpfloatcount + tempfloat
                        tmpfloatcount += 1
                    else:

                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                p.lineno(1)))


                elif vartipo == 'char':
                    if tmpcharcount < CHARMAX:
                        address = tmpcharcount + tempchar
                        tmpcharcount += 1
                    else:

                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                p.lineno(1)))


                elif vartipo == 'bool':
                    if tmpboolcount < BOOLMAX:
                        address = tmpboolcount + tempbool
                        tmpboolcount += 1
                    else:

                        printerror(
                            'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                                p.lineno(1)))

                # generar cuadruplo
                cuadruplos.append(('=', funcadd, '', address))
                global sclines
                sclines.append(p.lineno(1))
                cuadcount += 1
                pilaoperand.append(address)
                ptipo.append(vartipo)


    elif re.match(r"[a-zA-Z]([a-zA-Z]|[0-9]|[_])*",p[1]): # ---------------------------- IDS ---------------------------------------------
        #dprint('Para el elemento', p[1], 'En el scope ' + currscope + ' Se encuentra la dir func así:')
        #dprint('dirfunc', dirfunc, '\n\n')
        #llamada vars
        vartipo = None
        address = None
        if(p[1] in dirfunc[currscope]['vartab'].keys()):
            vartipo = dirfunc[currscope]['vartab'][p[1]]['tipo']
            if('address' in dirfunc[currscope]['vartab'][p[1]].keys()):
                address = dirfunc[currscope]['vartab'][p[1]]['address']
        elif (p[1] in dirfunc['global']['vartab'].keys()):
            vartipo = dirfunc['global']['vartab'][p[1]]['tipo']
            if ('address' in dirfunc['global']['vartab'][p[1]].keys()):
                address = dirfunc['global']['vartab'][p[1]]['address']
        else:

            printerror('La variable %r en la linea %r no ha sido declarada'%(p[1],p.lineno(1)))

        if(address != None):
            pilaoperand.append(address)
        else:
            pilaoperand.append(p[1])

        ptipo.append(vartipo)

    else: #Llamada arr
        dprint('Llamada arr', pilaoperand[-1],ptipo[-1])

        pass

   # dprint('Pila tipos       ',ptipo,'\n----------------------------------------------------------------------------------------------------------------------------------------------\n')

    p[0] = p[1]


def getArrayData(addr):
    global dirfunc
    global currscope
    res = {}

    for var in dirfunc[currscope]['vartab'].values():

        if addr['address'] == var['address']:
            res['size'] = var['size']
            res['dimlen'] = var['dimlen']
            res['dims'] = var['dims']
            return res
    for var in dirfunc['global']['vartab'].values():

        if addr['address'] == var['address']:

            res['size'] = var['size']
            res['dimlen'] = var['dimlen']
            res['dims'] = var['dims']
            return res
    return res

#LLAMADA FUNCION
def p_LLAMADAFUNC(p):
    '''LLAMADAFUNC :  DLR FID OPENPAR CALLPARAMS CLOSEPAR '''

    #llamada a funcion

    #Dir de funcion
    global dirfunc
    #La llamada actual
    global funcallcurr
    #Cuadruplos y su contador
    global cuadruplos
    global cuadcount


    funcallcurr = p[2]
    vartipo = None
    funcstart = ''
    isSpecial = False

    #Generar el nuevo espacio de memoria
    cuadruplos.append(('ERA',p[2],'',''))
    global sclines
    sclines.append(p.lineno(1))
    cuadcount += 1

    if (p[2] in dirfunc.keys()):
        if 'params' in dirfunc[p[2]].keys():
            vartipo = dirfunc[p[2]]['params']
        funcstart = dirfunc[p[2]]['inicio']

    elif (p[2] in special.keys()):
        if 'params' in dirfunc[p[2]].keys():
            vartipo = dirfunc[p[2]]['params']
        isSpecial = True
    else:

        printerror('La funcion %r en la linea %r no ha sido declarada' % (p[2], p.lineno(1)))

    dprint(vartipo)
    #Checar los parametros esten bien llamados
    if vartipo != None:

        #Checar si los parametros estan vacios
        dprint('Params leídos: ', p[4], '\nParams de la func: ', vartipo)
        if len(p[4])  != len(vartipo):

            printerror('La funcion %r en la linea %r no tiene la cantidad de parametros correctos, se esperaban %r y se recibieron %r' % (p[2], p.lineno(2),len(vartipo),len(p[4])))

        else:

            i = 0

            for param in vartipo.values():
                #dprint('⠄⠄⠄⠄⢠⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣿⣿⣿⣿⣆⠄⠄⠄\n⠄⠄⣼⢀⣿⣿⣿⣿⣏⡏⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣧⢻⣿⣿⣿⣿⡆⠄⠄\n⠄⠄⡟⣼⣿⣿⣿⣿⣿⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣇⢻⣿⣿⣿⣿⠄⠄\n⠄⢰⠃⣿⣿⠿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠙⠿⣿⣿⣿⣿⣿⠄⢿⣿⣿⣿⡄⠄\n⠄⢸⢠⣿⣿⣧⡙⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠈⠛⢿⣿⣿⡇⠸⣿⡿⣸⡇⠄\n⠄⠈⡆⣿⣿⣿⣿⣦⡙⠳⠄⠄⠄⠄⠄⠄⢀⣠⣤⣀⣈⠙⠃⠄⠿⢇⣿⡇⠄\n⠄⠄⡇⢿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⣠⣶⣿⣿⣿⣿⣿⣿⣷⣆⡀⣼⣿⡇⠄\n⠄⠄⢹⡘⣿⣿⣿⢿⣷⡀⠄⢀⣴⣾⣟⠉⠉⠉⠉⣽⣿⣿⣿⣿⠇⢹⣿⠃⠄\n⠄⠄⠄⢷⡘⢿⣿⣎⢻⣷⠰⣿⣿⣿⣿⣦⣀⣀⣴⣿⣿⣿⠟⢫⡾⢸⡟⠄.\n⠄⠄⠄⠄⠻⣦⡙⠿⣧⠙⢷⠙⠻⠿⢿⡿⠿⠿⠛⠋⠉⠄⠂⠘⠁⠞⠄⠄⠄\n⠄⠄⠄⠄⠄⠈⠙⠑⣠⣤⣴⡖⠄⠿⣋⣉⣉⡁⠄⢾⣦⠄⠄⠄⠄⠄⠄⠄⠄','\nacpapapapa',param ,p[4])

                if param['tipo'] != p[4][i]['tipo']:

                    printerror('La funcion %r en la linea %r no tiene los parametros correctos, los tipos del argumento %r no coinciden. %r es diferente a %r' % (p[2], p.lineno(2),i+1,param['tipo'],p[4][i]['tipo']))
                else:


                    # Pasar el parametro nuevo
                    isArgArr = ''
                    if 'dims' in param.keys():
                        # Si es arreglo checar si se pasa un arreglo, y que las dimensiones son correctas

                        p[4][i].update(getArrayData(p[4][i]))

                        paramsIsArrayAndArgIsNot = ('dims' in param.keys() and 'dims' not in p[4][i].keys())
                        paramsIsNotArrayAndArgIs = ('dims' not in param.keys() and 'dims' in p[4][i].keys())

                        if paramsIsArrayAndArgIsNot:
                            printerror(
                                "Error Semántico: La llamada de la función {} en la linea {} esperaba un arreglo, mátriz o cubo y recibio un expresión o constante en el argumento {}".format(
                                    (p[2], p.lineno(2))))
                        if paramsIsNotArrayAndArgIs:
                            printerror(
                                "Error Semántico: La llamada de la función {} en la linea {} esperaba una expresión o constante y recibio un arreglo, mátriz o cubo en el argumento {}".format(
                                    (p[2], p.lineno(2),i)))
                        isArgArr = param['size']

                        #Checar que sean de la misma dimension
                        hasNotTheSameDims = param['dims'] != p[4][i]['dims']

                        if hasNotTheSameDims:
                            printerror("Error Semántico: La llamada de la función {} en la linea {} esperaba el argumento {} tuviera {} dimensiones. Se recibio un arreglo con {} dimensiones".format(
                                    p[2], p.lineno(2),i,param['dims'],p[4][i]['dims']))

                        #Checar que las dimensiones cuadren
                        paramsDimsAreNotEqual = param['dimlen'] != p[4][i]['dimlen'] and not isSpecial
                        if paramsDimsAreNotEqual:
                            printerror("Error Semántico: La llamada de la función {} en la linea {} esperaba que el tamaño de cada una de las dimensiones del argumento {} sean las mismas que la funcion".format(
                                    p[2], p.lineno(2),i))

                    cuadruplos.append(('PARAMETER', p[4][i]['address'], isArgArr, 'param#'+str(i)))
                    sclines.append(p.lineno(1))
                    cuadcount += 1
                    i = i+1
            dprint(i)

    cmd = 'GOTOSUB'
    if isSpecial:
        cmd = 'SPFUNC'

    cuadruplos.append((cmd, p[2], '', funcstart))
    sclines.append(p.lineno(1))
    cuadcount += 1



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

#LECTURA DE LOS PARAMETROS
def p_CALLPARAMS(p):
    '''CALLPARAMS : CPARAM
                  | empty '''

    p[0] = p[1]

def p_CPARAM(p):
    ''' CPARAM :  EXPRESION CPARAMS'''
    #hay que cambiar como identifica si es un arr_tex
    global ptipo
    global pilaoperand


    cfpar = []

    if type(p[1]) is str and p[1] == 'exp':
        if pilaoperand[-1:][0] != '?':

            cfpar.append({'tipo':ptipo.pop(),'address':pilaoperand.pop()})

    else:
        cfpar.append(p[1])

    if p[2] != None:
        cfpar = cfpar + p[2]

    p[0] = cfpar

def p_CPARAMS(p):
    ''' CPARAMS : COMMA EXPRESION CPARAMS
                | empty'''
    if p[1] != None:
        global ptipo
        global pilaoperand
        cfpar = []
        #Checar si es una expresion

        if type(p[2]) is str and p[2] == 'exp':

            if pilaoperand[-1:][0] != '?':

                cfpar.append({'tipo':ptipo.pop(),'address':pilaoperand.pop()})
        else:
            cfpar.append(p[2])
        if p[3] != None:
            cfpar = cfpar + p[3]
        p[0] = cfpar
    else:
        p[0] = None

#LLAMADA ARREGLO
def p_LLAMADAARR(p):
    '''LLAMADAARR : ID OPENSQU EXPRESION CLOSESQU LLSEGD'''
    #Dir de funciones
    global dirfunc
    #Scope en el que se trabaja
    global currscope
    #Pila de operandos y tipos
    global pilaoperand
    global ptipo
    #cuadruplos y su contador
    global cuadcount
    global cuadruplos
    #Tabla de constantes
    global ctetab
    #Rangos de Temporales y contador de temporales
    global tmpintcount
    global tmppointcount
    global INTMAX
    global POINTMAX
    global tempint
    global temppoint

    var = None

    if (p[1] in dirfunc[currscope]['vartab'].keys()):
        if not ('dims' in dirfunc[currscope]['vartab'][p[1]].keys()):

            printerror('La variable %r en la linea %r no es un arreglo' % (p[1], p.lineno(1)))
        else:
            var = dirfunc[currscope]['vartab'][p[1]]

    elif (p[1] in dirfunc['global']['vartab'].keys()):
        if not ('dims' in dirfunc['global']['vartab'][p[1]].keys()):

            printerror('La variable %r en la linea %r no es un arreglo' % (p[1], p.lineno(1)))
        else:
            var = dirfunc['global']['vartab'][p[1]]

    else:

        printerror('La variable %r en la linea %r no ha sido declarada' % (p[1], p.lineno(1)))

    etipo = ptipo.pop()
    si = []
    if etipo == 'entero':
        si.append(pilaoperand.pop())
    else:
        printerror('Error Semantico : Se esperaba que las expresiones de los subindices sean enteras en la linea %r' % (
            p.lineno(1)))

    if p[5] != None:
        si+=(p[5])
    dprint('subindices : ',si)
    #Por el momento se pide que se den subindices extrictamente a las dimensiones del arreglo
    if var['dims'] != len(si):
        printerror('Error Semantico: La cantidad de subindices no coincide con las dimensiones del arreglo en la linea %r' % (p.lineno(1)))
    else:
        DIMS = 1
        for i in range(len(si)):
            #Verificar que el sub indice sea correcto

            cuadruplos.append(('VERIF',si[i],ctetab[str(var['dimlen'][i][0])],''))
            global sclines
            sclines.append(p.lineno(1))
            cuadcount+=1

            if DIMS == len(si):
                m = 1
                pilaoperand.append(si[i])
            else:
                m = var['dimlen'][i][1]

                address = None
                if tmpintcount < INTMAX:
                    address = tmpintcount + tempint
                    tmpintcount += 1
                else:
                    printerror(
                        'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                            p.lineno(1)))
                dprint('si = ', si[i], 'TEMPRANGE = ',temppoint,' vardimlen = ', var['dimlen'][i], 'm = ',m,'ctekeys \n',list(ctetab.keys()))
                cuadruplos.append(('*',si[i],ctetab[str(m)],address))

                sclines.append(p.lineno(1))
                cuadcount += 1
                pilaoperand.append(address)

            if DIMS > 1:
                address = None
                if tmpintcount < INTMAX:
                    address = tmpintcount + tempint
                    tmpintcount += 1
                else:
                    printerror(
                        'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                            p.lineno(1)))
                aux1 = pilaoperand.pop()
                aux2 = pilaoperand.pop()
                cuadruplos.append(('+', aux1, aux2, address))

                sclines.append(p.lineno(1))
                cuadcount += 1
                pilaoperand.append(address)
            DIMS += 1
        # Crear la dir de pointer
        aux = pilaoperand.pop()
        address = None
        if tmppointcount < POINTMAX:
            address = tmppointcount + temppoint
            tmppointcount += 1
        else:
            printerror(
                'Error de Semantica, se han hecho demasiadas variables temporales en la operación en la linea %r' % (
                    p.lineno(1)))
        cuadruplos.append(('+',aux,ctetab[str(var['address'])],'*'+str(address)))

        sclines.append(p.lineno(1))
        cuadcount += 1
        dprint('Push al pointer')
        pilaoperand.append(address)
        ptipo.append(var['tipo'])
    dprint('%'+p[1]+ '  ', pilaoperand[-1])
    p[0] = '%' + p[1]

def p_LLSEGD(p):
    '''LLSEGD : OPENSQU EXPRESION CLOSESQU LLTERD
              | empty'''

    if p[1] != None:

        global pilaoperand
        global ptipo
        etipo = ptipo.pop()
        si = []
        if etipo == 'entero':
            si.append(pilaoperand.pop())
        else:
            printerror('Error Semantico : Se esperaba que las expresiones de los subindices sean enteras en la linea %r' % (p.lineno(1)))
        if p[4] != None:
            si+= p[4]
        p[0] = si



def p_LLTERD(p):
    '''LLTERD : OPENSQU EXPRESION CLOSESQU
              | empty'''
    if p[1] != None:
        global pilaoperand
        global ptipo
        etipo = ptipo.pop()
        si = []
        if etipo == 'entero':
            si.append(pilaoperand.pop())
        else:
            printerror(
                'Error Semantico : Se esperaba que las expresiones de los subindices sean enteras en la linea %r' % (
                    p.lineno(1)))
        p[0] = si


########## ARREGLO TEXTUAL
def p_ARR_TEX(p):
    '''ARR_TEX : OPENSQU ATPRIC CLOSESQU'''
    global ptipo
    global pilaoperand
    global atd1

    arrdim = {'dims':1}
    dprint('Primera dim')
    if p[2] != None:
        arrdim.update(p[2])
        dprint('ad1 = ',atd1)
        arrdim['dim1len'] = atd1
        atd1 = 0
    ptipo.append(arrdim['tipo'])
    pilaoperand.append('arr')
    dprint('\n\nArrdim final: ',arrdim,'\n\n\n')
    p[0] = arrdim

#def p_ATSEGDIME(p):
#    '''ATSEGDIME : ATELEM
#                | ATSEGDIM'''
#
#def p_ATSEGDIM(p):
#    '''ATSEGDIM : [ATELEM] ATSEGDIMS'''
#
#def p_ATSEGDIMS(p):
#    '''ATSEGDIMS : COMMA ATSEGDIM
#                | empty'''
#
#def p_ATTERDIME(p):
#    '''ATTERDIME : ATELEM
#                | ATTERDIM'''
#
#def p_ATTERDIM(p):
#    '''ATTERDIM : [ATELEM] ATTERDIMS
#                | empty'''
#
#def p_ATTERDIMS(p):
#    '''ATTERDIMS : COMMA ATTERDIM
#                | empty'''
#
#
#def p_ATELEM(p):
#    '''ATELEM : EXPRESION ATELEMS'''
#
#
#def p_ATELEMS(p):
#    '''ATELEMS : COMMA ATELEM
#                    | empty'''
#

def p_ATPRIC(p):
    ''' ATPRIC : ATPRE ATPRISIG
               | empty'''
    newtipo = None



    if p[1] != None:


        if p[2] != None :
            if p[1]['dimf'] != p[2]['dimf']:
                printerror("No se declaro correctamente el arreglo textual en la linea %r" % (p.lineno(1)))
            # checar la congruencia entre los arreglos
            if p[2]['dimf'] == 'arr':
                if p[1]['dim2len'] != p[2]['dim2len']:
                    printerror("Los tamaños de la asignacion no son consistentes en la linea %r\n" % (p.lineno(1)))
            if (cubosem['arr'][p[1]['tipo']][p[2]['tipo']] != 'error'):
                newtipo = p[1]
                newtipo.update(p[2])
                newtipo['tipo'] = cubosem['arr'][p[1]['tipo']][p[2]['tipo']]
                p[0] = newtipo
            else:

                printerror('El tipo del elemento %r en la linea %r no es congruente con el tipo del arreglo' % (
                p[1], p.lineno(1)))

        else:
            p[0] = p[1]
    else:
        p[0] = None

def p_ATPRE(p):
    '''ATPRE : EXPRESION
              | ATSEGD'''
    arrdim = {}

    global atd1

    if type(p[1]) is str and p[1] == 'exp' :
        global pilaoperand
        global ptipo
        #pilaoperand.pop()

        arrdim['tipo'] = ptipo[-1:].pop()
        arrdim['dimf'] = 'exp'
        dprint('atpre expr\n')


    else:
        arrdim.update({'dims': 2})

        arrdim.update(p[1])
        arrdim['dimf'] = 'arr'
        dprint('atpre arr')

    atd1 += 1

    p[0] = arrdim

def p_ATPRISIG(p):
    '''ATPRISIG : COMMA ATPRE ATPRISIG
                | empty'''
    newtipo = None



    if p[1] != None:
        if p[3] != None :
            if p[2]['dimf'] != p[3]['dimf']:
                printerror("No se declaro correctamente el arreglo textual en la linea %r" % (p.lineno(1)))
            # checar la congruencia entre los arreglos
            if p[2]['dimf'] == 'arr':
                if p[2]['dim2len'] != p[3]['dim2len']:
                    printerror("Los tamaños de la asignacion no son consistentes en la linea %r\n" % (p.lineno(1)))
            if (cubosem['arr'][p[2]['tipo']][p[3]['tipo']] != 'error'):
                newtipo = p[2]
                newtipo.update(p[3])
                newtipo['tipo'] = cubosem['arr'][p[2]['tipo']][p[3]['tipo']]
                p[0] = newtipo
            else:

                printerror('El tipo del elemento %r en la linea %r no es congruente con el tipo del arreglo' % (
                    p[1], p.lineno(1)))

        else:
            p[0] = p[2]
    else:
        p[0] = None

def p_ATSEGD(p):
    '''ATSEGD : OPENSQU ATSEGC CLOSESQU'''
    dprint('Segunda dim')
    global atd2
    if p[2] != None:
        dprint('-------------------------------------------- ', atd2)
        p[2]['dim2len'] = atd2
        atd2 = 0

    p[0] = p[2]

def p_ATSEGC(p):
    ''' ATSEGC : ATSEGE ATSEGSIG
               | empty'''
    newtipo = None



    if p[1] != None:
        dprint('\np[1][dimf] = ', p[1]['dimf'], '\np[2][dimf] = ', p[2])
        if p[2] != None:
            if p[1]['dimf'] != p[2]['dimf']:
                printerror("No se declaro correctamente el arreglo textual en la linea %r" % (p.lineno(1)))
            #checar la congruencia entre los arreglos
            if p[2]['dimf'] == 'arr':
                if p[1]['dim3len'] != p[2]['dim3len']:
                    printerror("Los tamaños de la asignacion no son consistentes en la linea %r\n"% (p.lineno(1)))
            if (cubosem['arr'][p[1]['tipo']][p[2]['tipo']] != 'error'):
                newtipo = p[1]
                newtipo.update(p[2])
                newtipo['tipo'] = cubosem['arr'][p[1]['tipo']][p[2]['tipo']]
                p[0] = newtipo
            else:

                printerror('El tipo del elemento %r en la linea %r no es congruente con el tipo del arreglo' % (
                p[1], p.lineno(1)))

        else:
            p[0] = p[1]
    else:
        p[0] = None

def p_ATSEGE(p):
    '''ATSEGE : EXPRESION
              | ATTERD'''
    arrdim = {}
    global atd2
    if type(p[1]) is str and p[1] == 'exp' :
        global pilaoperand
        global ptipo
        #pilaoperand.pop()
        arrdim['tipo'] = ptipo[-1:].pop()
        arrdim['dimf'] = 'exp'
        dprint('exptesion en atsege')

    else:
        arrdim.update(p[1])
        arrdim.update({'dims': 3})
        arrdim['dimf'] = 'arr'

    atd2 += 1
    p[0] = arrdim

def p_ATSEGSIG(p):
    '''ATSEGSIG : COMMA ATSEGE ATSEGSIG
                | empty'''
    newtipo = None



    if p[1] != None:

        if p[3] != None :
            if p[2]['dimf'] != p[3]['dimf']:
                printerror("No se declaro correctamente el arreglo textual en la linea %r" % (p.lineno(1)))
            #Revisar que los tamaños sean consitentes
            if p[2]['dimf'] == 'arr':
                if p[2]['dim3len'] != p[3]['dim3len']:
                    printerror("Los tamaños de la asignacion no son consistentes en la linea %r\n"% (p.lineno(1)))
            if (cubosem['arr'][p[2]['tipo']][p[3]['tipo']] != 'error'):
                newtipo = p[2]
                newtipo.update(p[3])
                newtipo['tipo'] = cubosem['arr'][p[2]['tipo']][p[3]['tipo']]
                p[0] = newtipo
            else:

                printerror('El tipo del elemento %r en la linea %r no es congruente con el tipo del arreglo' % (
                    p[1], p.lineno(1)))

        else:
            p[0] = p[2]
    else:
        p[0] = None

def p_ATTERD(p):
    '''ATTERD : OPENSQU ATTERC CLOSESQU'''
    dprint('Terdim')
    global atd3

    if p[2] != None:
        p[2]['dim3len'] = atd3
        atd3 = 0
    p[0] = p[2]

def p_ATTERC(p):
    ''' ATTERC : ATTERE ATTERSIG
               | empty'''
    newtipo = None



    if p[1] != None:
        if p[2] != None:
            if(cubosem['arr'][p[1]['tipo']][p[2]['tipo']] != 'error'):
                newtipo = p[1]
                newtipo.update(p[2])
                newtipo['tipo'] = cubosem['arr'][p[1]['tipo']][p[2]['tipo']]
                p[0] = newtipo
            else:

                printerror('El tipo del elemento %r en la linea %r no es congruente con el tipo del arreglo' % (p[1], p.lineno(1)))

        else:
            p[0] = p[1]
    else:
        p[0] = None


def p_ATTERE(p):
    '''ATTERE : EXPRESION'''
    global pilaoperand
    global ptipo
    global atd3

    arrdim = {}
    atd3 += 1
    #pilaoperand.pop()
    arrdim['tipo'] = ptipo[-1:].pop()
    arrdim['dimf'] = 'arr'
    p[0] = arrdim

def p_ATTERSIG(p):
    '''ATTERSIG : COMMA ATTERE ATTERSIG
                | empty'''
    newtipo = None



    if p[1] != None:
        if p[3] != None:
            if (cubosem['arr'][p[2]['tipo']][p[3]['tipo']] != 'error'):
                newtipo = p[2]
                newtipo.update(p[3])
                newtipo['tipo'] = cubosem['arr'][p[2]['tipo']][p[3]['tipo']]
                p[0] = newtipo
            else:

                printerror('El tipo del elemento %r en la linea %r no es congruente con el tipo del arreglo' % (
                p[1], p.lineno(1)))

        else:
            p[0] = p[2]
    else:
        p[0] = None

def p_empty(p):
    'empty :'
    p[0] = None
    pass

def p_error(p):
    dprint("Error de sintaxis con el simbolo %r en la linea %r" % (p.value,p.lexer.lineno))
    raise TypeError("Error de sintaxis con el simbolo %r en la linea %r" % (p.value,p.lexer.lineno))
    
parser = yacc.yacc( debug=1)


def cuadToTxt(cuad):
    opfile = open('cuadruplos.txt','w')
    for i in range(len(cuad)):
        opfile.write("%r : %r %r %r %r\n" % ((i,)+cuad[i]))
    opfile.close()

def genobjfile(ctes, funcs, cuad,filename):
    obj = {'ctetab':ctes,'dirfunc':funcs,'cuadruplos':cuad,'sclines':sclines}
    #wobj = json.dumps(obj)
    #open(filename + '.json', 'w').close()
    with open(filename+'.obj','w') as opfile:
        json.dump(obj,opfile)




#Prueba imprimir el cubo semantico para ver si esta bien
#dprint(cubosem['||']['cadena']['cadena'])

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
filename = sys.argv[1].split('.')[0]

try:
    parser.parse(myFile.read(),tracking=True)
except TypeError:

    print("No es lenguaje valido!!!!")
else:
    if(sem_err):
        print('No es lenguaje valido!!!!')
    else:
        cuadToTxt(cuadruplos)
        print(filename)
        genobjfile(objctetab,dirfunc,cuadruplos,filename)
        print('aceptado')




