
#    Nombre: IntroProg.py
#    Descripción: Una implementación del lexer y parser usando python y ply para el compliador
#    Por: Luis Fernando Lomelín Ibarra

#importar las herramientas de lex y yacc de ply

from ply import lex
import ply.yacc as yacc
import sys


# In[2]:


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

t_CTE_INT = (r"[0-9]+")
t_CTE_FLOAT = (r"[0-9]+\.[0-9]+([eE][+-]?[0-9]+)?")
t_CTE_CHAR = ("\'[^\']\'")
t_CTE_STRING = ("\"[^\"]+\"")
def t_ID(t): 
    r"[a-zA-Z]([a-zA-Z]|[0-9][_])*"

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
     print("Token Invalido '%s'" % t.value[0])


lexer = lex.lex()




#precedencia
precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'MUL', 'DIV' ),
    ( 'nonassoc', 'GT', 'LT' ),

)

#Estructura del programa
def p_PROGRAMA(p):
    '''PROGRAMA : PROGRAM ID OPENCUR DECLARACIONES DECTODASFUNC PRINCIPAL FUNCION OPENCUR DECLARACIONES CLOSECUR BLOQUE CLOSECUR '''
    #1.- Crear el directorio de funciones
    #dirfunc = {}
    #2.- Si se encuentran declaraciones globales se debe de crear una tabla de symbolos a nivel global
    #dirfunc['global'] = {'tipo': 'vacio', 'params:':None, 'vartab':p[4]}
    #3.- Si se encuentran funciones darlas de alta en el dir de funciones

    #4.- Borrar si se llega al final del programa.

###########
# Declaraciones Arreglos y variables
##########

def p_DECLARACIONES(p):
    '''DECLARACIONES : DECLARACION DECLARACIONES
                     | empty'''

    #Generar y regresar una tabla de variables que va  a ser ligada a una
def p_DECLARACION(p):
    '''DECLARACION : DECVAR
                   | DECARR '''

def p_DECVAR(p):
    '''DECVAR : TIPO ID DVNID SEMICOLON'''

def p_DVNID(p):
    '''DVNID : COMMA ID DVNID
             | empty'''

def p_DECARR(p):
    '''DECARR : TIPO ID OPENSQU CTE_INT CLOSESQU DSEG SEMICOLON'''

def p_DSEG(p):
    '''DSEG : OPENSQU CTE_INT CLOSESQU DTER
            | empty'''
def p_DTER(p):
    '''DTER : OPENSQU CTE_INT CLOSESQU
            | empty'''

def p_TIPO(p):
    '''TIPO : ENTERO
            | FLOTANTE
            | CHAR
            | BOOL''' 

#######
# Declaracion Funciones
#######

def p_DECTODASFUNC(p):
    '''DECTODASFUNC : DECFUNC DECTODASFUNC
                    | empty'''

def p_DECFUNC(p):
    '''DECFUNC :  FUNCION TIPOFUN ID OPENPAR FUNPARAM CLOSEPAR OPENCUR DECLARACIONES CLOSECUR BLOQUE '''
    #print('Lee una dec funcion')

def p_TIPOFUN(p):
    '''TIPOFUN : TIPO
               | VACIO'''
    #print('Llego a tipo')

def p_FUNPARAM(p):
    '''FUNPARAM : PARAM
                | empty'''

def p_PARAM(p):
    '''PARAM : TIPO ID PARAMD PARAMS '''

def p_PARAMS(p):
    '''PARAMS : COMMA PARAM
              | empty'''

def p_PARAMD(p):
    '''PARAMD : OPENSQU CLOSESQU PDSEG
              | empty'''

def p_PDSEG(p):
    '''PDSEG : OPENSQU CLOSESQU PDTER
              | empty'''
def p_PDTER(p):
    '''PDTER : OPENSQU CLOSESQU 
             | empty'''


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
                | LEER'''

# Impresion -------------------------  
def p_IMPRESION(p):
    '''IMPRESION : IMPRIMIR OPENPAR PRINTABLE PRINTARGS CLOSEPAR SEMICOLON'''    

def p_PRINTARGS(p):
    '''PRINTARGS : COMMA PRINTABLE PRINTARGS
                 | empty'''

def p_PRINTABLE(p):
    '''PRINTABLE : EXPRESION
                 | CTE_STRING'''

# Asignacion -------------------

def p_ASIGNACION(p):
    'ASIGNACION : ID ADIMS EQ EXPRESION SEMICOLON'
    #print('Lee asignacion')

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

#####
# Expresion
#####

def p_EXPRESION(p):
    '''EXPRESION : EXPRESIONR EXPRLOG'''

def p_EXPRLOG(p):
    '''EXPRLOG : AND EXPRESIONR EXPRLOG
               | OR EXPRESIONR EXPRLOG
               | empty'''

def p_EXPRESIONR(p):
    '''EXPRESIONR : EXP
                 | EXP GT EXP
                 | EXP LT EXP
                 | EXP EXLAM EQ EXP
                 | EXP EQ EQ EXP
                 | EXP GT EQ EXP
                 | EXP LT EQ EXP'''
    
    
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

#####
# LLAMADAS
#####    
 
def p_VARCTE(p):
    '''VARCTE : ID
            | CTE_INT
            | CTE_FLOAT
            | CTE_STRING
            | CTE_BOOL
            | CTE_CHAR
            | LLAMADAFUNC
            | LLAMADAARR
            | ARR_TEX
            | NULO'''


#LLAMADA FUNCION
def p_LLAMADAFUNC(p):
    '''LLAMADAFUNC :  DLR FID OPENPAR CALLPARAMS CLOSEPAR '''

def p_FID(p):
    '''FID : ID
           | FUNID'''

#-------------------------
# Aquí se van agregando los nombres de las funciones especiales del lenguaje
def p_FUNID(p):
    '''FUNID : LEER'''

def p_CALLPARAMS(p):
    '''CALLPARAMS : CPARAM
                  | empty '''
def p_CPARAM(p):
    ''' CPARAM : EXPRESION CPARAMS '''
def p_CPARAMS(p):
    ''' CPARAMS : COMMA EXPRESION CPARAMS
                | empty'''

#LLAMADA ARREGLO
def p_LLAMADAARR(p):
    '''LLAMADAARR : ID OPENSQU EXPRESION CLOSESQU LLSEGD'''

def p_LLSEGD(p):
    '''LLSEGD : OPENSQU EXPRESION CLOSESQU LLTERD
              | empty'''
def p_LLTERD(p):
    '''LLTERD : OPENSQU EXPRESION CLOSESQU
              | empty'''

#ARREGLO TEXTUAL
def p_ARR_TEX(p):
    '''ARR_TEX : OPENSQU ATPRIC CLOSESQU'''

def p_ATPRIC(p):
    ''' ATPRIC : ATPRE ATPRISIG
               | empty'''

def p_ATPRE(p):
    '''ATPRE : EXPRESION
              | ATSEGD'''
def p_ATPRISIG(p):
    '''ATPRISIG : COMMA ATPRE ATPRISIG
                | empty'''

def p_ATSEGD(p):
    '''ATSEGD : OPENSQU ATSEGC CLOSESQU'''

def p_ATSEGC(p):
    ''' ATSEGC : ATSEGE ATSEGSIG
               | empty'''

def p_ATSEGE(p):
    '''ATSEGE : EXPRESION
              | ATTERD'''
def p_ATSEGSIG(p):
    '''ATSEGSIG : COMMA ATSEGE ATSEGSIG
                | empty'''

def p_ATTERD(p):
    '''ATTERD : OPENSQU ATTERC CLOSESQU'''

def p_ATTERC(p):
    ''' ATTERC : ATTERE ATTERSIG
               | empty'''

def p_ATTERE(p):
    '''ATTERE : EXPRESION'''
def p_ATTERSIG(p):
    '''ATTERSIG : COMMA ATTERE ATTERSIG
                | empty'''

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




