# Programa: ipvm
# Descripción : Una máquina virtual para leer el objeto obj generado por el compilador IntroProg.py
# Por : Luis Fernando Lomelín Ibarra

# Importar las librerías necesarias para la ejecución
import sys
import json
import re
import numpy as np
import math
import random
from statistics import mode
from scipy.stats import wilcoxon
from Memory import Memory
import matplotlib.pyplot as plt

inobjfn = sys.argv[1]
infilename = inobjfn.split('.')[0]
obj = None

#Cubo semantico para verificar tipado en runtime
# 0 -> entero
# 1 -> flotante
# 2 -> char
# 3 -> bool
# 6 -> cadena
cubosem = {
        '=':{0:{
                        0:0,
                        1: 0,
                        2:0,
                        3: 0,
                        6:'error'
                        },
                1:{
                        0:1,
                        1: 1,
                        2:1,
                        3: 1,
                        6:'error'
                        },
                2:{
                        0:2,
                        1: 2,
                        2:2,
                        3: 2,
                        6:'error'
                        },
                3:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                6:{
                        0:'error',
                        1: 'error',
                        2:'error',
                        3: 'error',
                        6:6
                        },

                },
        '||':{
            0:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                1:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                2:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                3:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                6:{
                        0:'error',
                        1: 'error',
                        2:'error',
                        3: 'error',
                        6:3
                        },
        },
        '&&':{
                0:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                1:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                2:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                3:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                6:{
                        0:'error',
                        1: 'error',
                        2:'error',
                        3: 'error',
                        6:3
                        },
        },
        '<':{
                0:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                    },
                1:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                2:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                3:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                6:{
                        0:'error',
                        1: 'error',
                        2:'error',
                        3: 'error',
                        6:3
                        },
        },
        '>':{
                0:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                1:{
                        0:3,
                        1: 3,
                        2:3,
                        3: 3,
                        6:'error'
                        },
                2:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                3:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                6:{
                            0:'error',
                            1: 'error',
                            2:'error',
                            3: 'error',
                            6:3
                        },
            },
            '<=':{
                0:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                1:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                2:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                3:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                6:{
                            0:'error',
                            1: 'error',
                            2:'error',
                            3: 'error',
                            6:3
                        },
            },
            '>=':{
                0:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                1:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                2:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                3:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                6:{
                            0:'error',
                            1: 'error',
                            2:'error',
                            3: 'error',
                            6:3
                        },
            },
            '!=':{
                0:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                1:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                2:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                3:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                6:{
                            0:'error',
                            1: 'error',
                            2:'error',
                            3: 'error',
                            6:3
                        },
            },
            '==':{
                0:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                1:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                2:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                3:{
                            0:3,
                            1: 3,
                            2:3,
                            3: 3,
                            6:'error'
                        },
                6:{
                            0:'error',
                            1: 'error',
                            2:'error',
                            3: 'error',
                            6:3
                        },
            },
            '+':{
                0:{
                            0:0,
                            1: 1,
                            2:0,
                            3: 0,
                            6:'error'
                        },
                1:{
                            0:1,
                            1: 1,
                            2:1,
                            3: 1,
                            6:'error'
                        },
                2:{
                            0:0,
                            1: 1,
                            2:0,
                            3: 0,
                            6:'error'
                        },
                3:{
                            0:0,
                            1: 1,
                            2:0,
                            3: 0,
                            6:'error'
                        },
                6:{
                            0:'error',
                            1: 'error',
                            2:'error',
                            3: 'error',
                            6:6
                        },
                'none' : {
                    0 : 0,
                    1 : 1,
                    2 : 'error',
                    3 : 'error',
                    6 : 'error'
                }
            },
            '-':{
                0:{
                            0:0,
                            1: 1,
                            2:0,
                            3: 0,
                            6:'error',
                        },
                1:{
                            0:1,
                            1: 1,
                            2:1,
                            3: 1,
                            6:'error'
                        },
                2:{
                            0:0,
                            1: 1,
                            2:0,
                            3: 0,
                            6:'error'
                        },
                3:{
                            0:0,
                            1: 1,
                            2:0,
                            3: 0,
                            6:'error'
                        },
                6:{
                            0:'error',
                            1: 'error',
                            2:'error',
                            3: 'error',
                            6:'error'
                        },
                'none' : {
                    0 : 0,
                    1 : 1,
                    2 : 'error',
                    3 : 'error',
                    6 : 'error'
                }

            },
            '*':{
                0:{
                            0:0,
                            1: 1,
                            2:0,
                            3: 0,
                            6:'error'
                        },
                1:{
                            0:1,
                            1: 1,
                            2:1,
                            3: 1,
                            6:'error'
                        },
                2:{
                            0:0,
                            1: 1,
                            2:0,
                            3: 0,
                            6:'error'
                        },
                3:{
                            0:0,
                            1: 1,
                            2:0,
                            3: 0,
                            6:'error'
                        },
                6:{
                            0:'error',
                            1: 'error',
                            2:'error',
                            3: 'error',
                            6:'error'
                        },
            },
            '/':{
                0: {
                    0: 0,
                    1: 1,
                    2: 0,
                    3: 0,
                    6: 'error'
                },
                1: {
                    0: 1,
                    1: 1,
                    2: 1,
                    3: 1,
                    6: 'error'
                },
                2: {
                    0: 0,
                    1: 1,
                    2: 0,
                    3: 0,
                    6: 'error'
                },
                3: {
                    0: 0,
                    1: 1,
                    2: 0,
                    3: 0,
                    6: 'error'
                },
                6: {
                    0: 'error',
                    1: 'error',
                    2: 'error',
                    3: 'error',
                    6: 'error'
                },

            },
            'arr':{0:{
                            0:0,
                            1: 1,
                            2:0,
                            3: 0,
                            6:'error'
                        },
                1:{
                            0:1,
                            1: 1,
                            2:1,
                            3: 1,
                            6:'error'
                        },
                2:{
                            0:0,
                            1: 1,
                            2:2,
                            3: 0,
                            6:'error'
                        },
                3:{
                            0:0,
                            1: 1,
                            2:0,
                            3: 3,
                            6:'error'
                        },
                6:{
                            0:'error',
                            1: 'error',
                            2:'error',
                            3: 'error',
                            6:6
                        },
            }


            }

#Las direcciones virtuales usadas por el compilador
#Se usa para calcular los offsets de direcciones

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

#Variables para el manejo de memoria
memstack = [] # Para manejar las memorías a como van llegando
eratemp = None # Variable temporal para la creación de espacios de memoria

#Contadores de parametros
intc = 0
floatc = 0
charc = 0
boolc = 0


#Cargar el archivo resultante de la compilación
with open(inobjfn) as objfile:
    obj = json.load(objfile)


ctetab = obj['ctetab']
dirfunc = obj['dirfunc']
cuad = obj['cuadruplos']
scline = obj['sclines']

##Variables importantes para la ejecución
#Flag de correr el código
runcode = True

ipstack = [] # Stack para manejar el ip cuando se utilizan funciones

sparrstack = [] # Un stack para mantener los tamaños de cada parametro definido en funcion especial
isNextPrintable = False # Flag para detectar si imprimir todo junto
printall = '' # Variable auxiliar para imprimir junto la información
ip = 0 # Instruction pointer
plotcounter = [0,0,0] # Un contador de gráficos generados

#Limpiar ctetab
# Cuando se pasa a un archivo los caracteres los transforma a strings
# Tambien se aprovecha la pasada para codificar bien los strings recividos
for k in ctetab.keys():
    if type(ctetab[k]) is str:
        if re.match("\'.\'",ctetab[k]):
            ctetab[k] = ctetab[k][1]
        elif re.match("\"[^\"]+\"",ctetab[k]):
            ctetab[k] = ctetab[k].replace('"','').encode('ascii').decode('unicode_escape')




##############FUNCIONES######################################

# Func: printerr
# Params: Mensaje de error msg, número del cuaruplo cn
# Desc: Imprime un mensaje de error con el formato correcto y acaba la ejecución
def printerr(msg,cn):
    runcode = False
    if cn < 0:
        print("\u001b[31m\n*******************\n\nError : \u001b[0m \u001b[33;1m"+msg+'\u001b[0m')
    else:
        print("\u001b[31m\n*******************\n\n\u001b[0m\u001b[31;1mError en la linea {} : \u001b[0m \u001b[33;1m".format(scline[cn])+msg+'\u001b[0m')
    raise SystemExit

# Func: genNewMem
# params: Nombre de funcion funcname, opcionalmente recursos locales de las funciones especiales
# returns: Regresa un nuevo espacio de memoria con los recursos apropiados
# Desc: Genera un nuevo espacio de memoria
def genNewMem(funcname,splc = []):
    if funcname == 'global':
        ints, floats, chars, bools = dirfunc['global']['varres'].values()
        return Memory(ints, floats, chars, bools)
    elif funcname == 'special':
        ints, floats, chars, bools = splc
        return [Memory(ints, floats, chars, bools),Memory()]
    else:
        ints, floats, chars, bools = dirfunc[funcname]['varres'].values()
        auxmem = [Memory(ints, floats, chars, bools)]
        ints, floats, chars, bools, pointers = dirfunc[funcname]['tmpres'].values()
        auxmem.append(Memory(ints, floats, chars, bools, pointers))
        return auxmem

# Func: getTypeAndOffset
# Params: la dirección virtual a convertir a espacio en memoria
# Returns: El scope de la variable, el tipo de la variable y el offset en la memoria
# Desc: La función busca obtener el tipo, offset y scope de la dirección virtual recivida y regresa
# el scope, el tipo y el offset en la memoria de la máquina virtual.

def getTypeAndOffset(addr):
    #regresa el scope, tipo y offset
    atype = None
    aoffset = None
    ascope = None
    if addr >= globalint and addr < localint: #globales
        ascope = 'global'
        if addr >= globalint and addr < globalfloat:
            aoffset = addr - globalint
            atype = 0
        elif addr >= globalfloat and addr < globalchar:
            aoffset = addr - globalfloat
            atype = 1
        elif addr >= globalchar and addr < globalbool:
            aoffset = addr - globalchar
            atype = 2
        elif addr >= globalbool and addr < globalpoint:
            aoffset = addr - globalbool
            atype = 3
        elif addr >= globalpoint and addr < localint:
            aoffset = addr - globalpoint
            atype = 4
    
    elif addr >= localint and addr < tempint: #locales
        ascope = 'local'
        if addr >= localint and addr < localfloat:
            aoffset = addr - localint
            atype = 0
        elif addr >= localfloat and addr < localchar:
            aoffset = addr - localfloat
            atype = 1
        elif addr >= localchar and addr < localbool:
            aoffset = addr - localchar
            atype = 2
        elif addr >= localbool and addr < localpoint:
            aoffset = addr - localbool
            atype = 3
        elif addr >= localpoint and addr < tempint:
            aoffset = addr - localpoint
            atype = 4

    elif addr >= tempint and addr < constint:#temporales
        ascope = 'temp'
        if addr >= tempint and addr < tempfloat:
            aoffset = addr - tempint
            atype = 0
        elif addr >= tempfloat and addr < tempchar:
            aoffset = addr - tempfloat
            atype = 1
        elif addr >= tempchar and addr < tempbool:
            aoffset = addr - tempchar
            atype = 2
        elif addr >= tempbool and addr < temppoint:
            aoffset = addr - tempbool
            atype = 3
        elif addr >= temppoint and addr < constint:
            aoffset = addr - temppoint
            atype = 4
            
    
    return ascope,atype,aoffset


# Func: getexpoper
# Params: La dirección de memoria virtual
# Ret: El valor de la dirección y el tipo de la variable
# Desc: Funcion para obtener los valores de los operandos para expresiones 
# y operaciones de la máquina virtual
def getexpoper(addrs):
    if addrs == '':
        return '',None
    
    if str(addrs) in ctetab.keys():
        
        if addrs >= constint and addrs < constfloat:
            
            atype = 0
        elif addrs >= constfloat and addrs < constchar:
            
            atype = 1
        elif addrs >= constchar and addrs < constbool:
            
            atype = 2
        elif addrs >= constbool and addrs < conststring:
            atype = 3
        else: #STRING
            atype = 6
        
        return ctetab[str(addrs)],atype
    else:
        scop, atype, aoff = getTypeAndOffset(addrs)
        if scop == 'global':
            if atype == 0: #entero
                return globmem.mint[aoff], atype
            elif atype == 1: #float
                return globmem.mfloat[aoff], atype
            elif atype == 2: #char
                return globmem.mchar[aoff], atype
            elif atype == 3: #bool
                return globmem.mbool[aoff], atype
            elif atype == 4: #pointer
                return globmem.mpoint[aoff], atype
        elif scop == 'local':
            
            if atype == 0: #entero
                
                return memstack[-1][0].mint[aoff], atype
            elif atype == 1: #float
                return memstack[-1][0].mfloat[aoff], atype
            elif atype == 2: #char
                return memstack[-1][0].mchar[aoff], atype
            elif atype == 3: #bool
                return memstack[-1][0].mbool[aoff], atype
            elif atype == 4: #pointer
                return memstack[-1][0].mpoint[aoff], atype
        elif scop == 'temp':
            if atype == 0: #entero
                return memstack[-1][1].mint[aoff], atype
            elif atype == 1: #float
                return memstack[-1][1].mfloat[aoff], atype
            elif atype == 2: #char
                return memstack[-1][1].mchar[aoff], atype
            elif atype == 3: #bool
                return memstack[-1][1].mbool[aoff], atype
            elif atype == 4: #pointer
                if memstack[-1][1].mpoint[aoff] == None:
                    printerr('El valor del arreglo que usted esta accesando no tiene ningún valor.\n Revise su código para asgurar que el espacio del arreglo que anda buscando si tenga valor',ip)
                else:
                #ascop, atype, val = getTypeAndOffset(memstack[-1][1].mpoint[aoff])
                    #print('Pila Pointers:\n',list(map(lambda x: None if x == None else getexpoper(x)[0],memstack[-1][1].mpoint)),'\nADDRESS : ', addrs, ' offset : ',aoff)
                    val, atype = getexpoper(memstack[-1][1].mpoint[aoff])
                    return val, atype

# Func: storeinmem
# Param: Una direccion virtual addrs, un valor val, y opcionalmente un flag indicando 
# si guardar en la variable temporal era
# Desc: Guardar en memoria el valor dado.
def storeinmem(addrs,val, isera = False):
    scop, atype, aoff = getTypeAndOffset(addrs)
    if scop == 'global':
        if atype == 0: #entero
            globmem.mint[aoff] = val
        elif atype == 1: #float
            globmem.mfloat[aoff] = val
        elif atype == 2: #char
            globmem.mchar[aoff] = val
        elif atype == 3: #bool
            globmem.mbool[aoff] = val
        elif atype == 4: #pointer
            globmem.mpoint[aoff] = val
    elif scop == 'local':
        if atype == 0: #entero
            if isera:
                eratemp[0].mint[aoff] = val
            else:
                memstack[-1][0].mint[aoff] = val
        elif atype == 1: #float
            if isera:
                eratemp[0].mfloat[aoff] = val
            else:
                memstack[-1][0].mfloat[aoff] = val
        elif atype == 2: #char
            if isera:
                eratemp[0].mchar[aoff] = val
            else:
                memstack[-1][0].mchar[aoff] = val
        elif atype == 3: #bool
            if isera:
                eratemp[0].mbool[aoff] = val
            else:
                memstack[-1][0].mbool[aoff] = val
        elif atype == 4: #pointer
            if isera:
                eratemp[0].mpoint[aoff] = val
            else:
                memstack[-1][0].mpoint[aoff] = val
    elif scop == 'temp':
        if atype == 0: #entero
            if isera:
                eratemp[1].mint[aoff] = val
            else:
                memstack[-1][1].mint[aoff] = val
        elif atype == 1: #float
            if isera:
                eratemp[1].mfloat[aoff] = val
            else:
                memstack[-1][1].mfloat[aoff] = val
        elif atype == 2: #char
            if isera:
                eratemp[1].mchar[aoff] = val
            else:
                memstack[-1][1].mchar[aoff] = val
        elif atype == 3: #bool
            if isera:
                eratemp[1].mbool[aoff] = val
            else:
                memstack[-1][1].mbool[aoff] = val
        elif atype == 4: #pointer
            if isera:
                if eratemp[1].mpoint[aoff] == None:
                    eratemp[1].mpoint[aoff] = val
                else:
                    
                    storeinmem(eratemp[1].mpoint[aoff],val,isera)
            else:
                
                if memstack[-1][1].mpoint[aoff] == None:
                    memstack[-1][1].mpoint[aoff] = val
                    
                else:
                    #val, _ = getexpoper(memstack[-1][1].mpoint[aoff])
                    
                    storeinmem(memstack[-1][1].mpoint[aoff],val)
                    
                    
# Func: valtonum
# params: Un valor val, y un tipo t
# ret: Regresa el valor de v como el tipo t
# Desc: Cambiar valor a numero si es necesario
def valtonum(val,t):
    if t == 2:
        val = ord(val)
    elif t == 3:
        if val:
            val = 1
        else:
            val = 0
    return val


# Func: reusePointer
# Params: Una dirección virtual addrs y un valor 
# Reescribir el valor del apuntador cuando es necesario
def reusePointer(addrs,val):
    scop, atype, aoff = getTypeAndOffset(addrs)
    memstack[-1][1].mpoint[aoff] = val


# Func : exeExpresion
# Params : Un operador op, tres direcciones virtuals ladd, radd resadd
# Desc : Ejecuta la acción del cuadruplo y la guarda en memoria
def exeExpresion(op,ladd,radd,resadd):
    lop,lt = getexpoper(ladd)
    rop,rt = getexpoper(radd)
    if lop == None or rop == None:
        printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
    lop = valtonum(lop,lt)
    rop = valtonum(rop,rt)
    aux = 0
    # Operadores ['*','/','+','-','>','<','>=','<=','!=','==','||','&&']
    if op == '*': 
        # Multiplicacion
        aux = lop * rop

    elif op == '/': 
        # Division
        aux = lop / rop

    elif op == '+': 
        #Suma 
        if rop == '':
            aux = abs(lop)
        else:
            aux = lop + rop

    elif op == '-': 
        #Resta
        if rop == '':
            aux = -1 * abs(lop)
        else:
            aux = lop - rop

    elif op == '>': 
        #Mayorque
        aux = lop > rop

    elif op == '<':
        #menor que
        aux = lop < rop

    elif op == '>=': 
        # mayor igual
        aux = lop >= rop

    elif op == '<=': 
        #menor igual
        aux = lop <= rop

    elif op == '==': 
        #igual (relacional)
        aux = lop == rop

    elif op == '!=': 
        #diferente
        aux = lop != rop

    elif op == '&&': 
        # and
        aux = lop and rop

    elif op == '||': 
        # or
        aux = lop or rop
    if type(resadd) is str: # Reescribir el pointer en caso de ser necesaria
        reusePointer(int(resadd[1:]),aux)
    else:
        storeinmem(resadd,aux)

######### Funciones Especiales del lenguaje

# Func : spfuncs
# Params : Nombre de función especial fname, y una función resultante raddress
# Desc : Ejecuta la lógica de las funciones especiales. Al acabar libera la memoria que estaba utilizaba

def spfuncs(fname, raddres):
    # Cada funcion va a sacar la info de la memoria
    # En el caso de recibir un arreglo se va a hacer una fila con los tamaños de cada arreglo recibido por el cuadruplo param
    global sparrstack
    global plotcounter

    # Leer el primier caracter o núm de consola
    if fname == 'leer':
        cin = input()
        #Primero checar si es un float
        if re.fullmatch("([+-])?[0-9]+\.[0-9]+([eE][+-]?[0-9]+)?",cin):
            cin = float(cin)
        #Despues checo si es un int
        elif re.fullmatch("([+-])?[0-9]+",cin):
            cin = int(cin)
        #Checo si es un char
        elif len(cin) == 1:
            cin = ord(cin)
        elif re.fullmatch("\'.\'",cin):
            cin = ord(cin[1])
        #Finalmente checo si escribieron verdadero o falso
        elif re.fullmatch("[vV][eE][rR][dD][aA][dD][eE][rR][oO]",cin):
            cin = 1
        elif re.fullmatch("[fF][Aa][Ll][Ss][Oo]",cin):
            cin = 0
        else:
            printerr(" Recuerda que leer solo puede leer los datos primitivos del lenguaje. Es decir tienes que dar un número entero o flotante, o un caracter o escribir verdadero o falso.",-1)
        #Si llego a este punto sin hacer match a alguno de los anteriores levanto error

        #Paso el resultado a un float si los encontro

        # Guardar
        storeinmem(raddres,cin)
    # Funciones de matemáticas

    elif fname == 'modulo': # Función Modulo
        # Recive dos argumentos a,b ambos float
        ladd = localfloat
        radd = localfloat + 1
        lop,lt = getexpoper(ladd)
        rop,rt = getexpoper(radd)
        if lop == None or rop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)
        storeinmem(raddres,lop%rop)
    
    elif fname == 'suma': # Función de suma de todos los elementos de un arreglo
        # Recive un arrglo de floats a
        addr = localfloat
        arr = []
        for i in range(sparrstack[0]):
            arr.append(getexpoper(addr+i)[0])
        storeinmem(raddres, np.sum(arr))
    elif fname == 'raiz': # función de raíz cuadrada
        # Solo recive un arg float a
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,math.sqrt(lop))
    elif fname == 'exp': # Función exponencial
        # Solo recive un arg float a
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,math.exp(lop))
    elif fname == 'elevar': # Función de elevar a ^ b
        # Recive dos argumentos a,b ambos float
        ladd = localfloat
        radd = localfloat + 1
        lop,lt = getexpoper(ladd)
        rop,rt = getexpoper(radd)
        if lop == None or rop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)
        storeinmem(raddres,lop**rop)
    elif fname == 'techo': # Función ceil
        # Solo recive un arg float a
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,math.ceil(lop))
    elif fname == 'piso': # Función floor
        # Solo recive un arg float a
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,math.floor(lop))
    elif fname == 'cos': # Función trigonométrica cos
        # Solo recive un arg float a
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,math.cos(lop))
    elif fname == 'sen': # Función trigonométrica sen
            # Solo recive un arg float a
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,math.sin(lop))
    elif fname == 'tan': # Función trigonométrica tan
            # Solo recive un arg float a
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,math.tan(lop))
    elif fname == 'cotan': # Función trigonométrica cotangente
            # Solo recive un arg float a
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,1.0/math.tan(lop))
    elif fname == 'sec': # Función trigonométrica secante
            # Solo recive un arg float a
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,1.0/math.cos(lop))
    elif fname == 'cosec': # Función trigonométrica cosecante
            # Solo recive un arg float a
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,1.0/math.sin(lop))
    elif fname == 'log': # Función logaritmo
            # Solo recive un arg float a
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,math.log(lop))
    elif fname == 'minimo': # Función minimo, Regresa el minimo de un arreglo
            # Recive un arrglo de floats a
        addr = localfloat
        arr = []
        for i in range(sparrstack[0]):
            arr.append(getexpoper(addr+i)[0])
        storeinmem(raddres, np.min(arr))
    elif fname == 'maximo': # Función máximo, Regresa el máximo de un arreglo
            # Recive un arrglo de floats a
        addr = localfloat
        arr = []
        for i in range(sparrstack[0]):
            arr.append(getexpoper(addr+i)[0])
        storeinmem(raddres, np.max(arr))
    elif fname == 'redondear': # Función de redondear
                # Solo recive un arg float a
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,round(lop))
    elif fname == 'productoPunto': # Función de producto punto
            # Recive un arrglo de floats a y un arreglo de floats b
        addr = localfloat
        arr = []
        arr2 = []
        # Obtener los valores del primer arreglo
        for i in range(sparrstack[0]):
            arr.append(getexpoper(addr+i)[0])

        # Sacar el address del segundo arreglo y sacarlo a una variable
        addr = localfloat + sparrstack[0]
        sparrstack = sparrstack[1:]
        for i in range(sparrstack[0]):
            arr2.append(getexpoper(addr+i)[0])
        
        storeinmem(raddres, np.dot(arr,arr2))
    
    #--------------------------------- Funciones de estadítica
    elif fname == 'media': #Función media, Calcula de media de un arreglo
            # Recive un arrglo de floats a
        addr = localfloat
        arr = []
        for i in range(sparrstack[0]):
            arr.append(getexpoper(addr+i)[0])
        storeinmem(raddres, np.mean(arr))
    elif fname == 'mediana': #Función mediana, Calcula de mediana de un arreglo
            # Recive un arrglo de floats a
        addr = localfloat
        arr = []
        for i in range(sparrstack[0]):
            arr.append(getexpoper(addr+i)[0])
        storeinmem(raddres, np.median(arr))
    elif fname == 'moda': #Función moda, Calcula de moda de un arreglo
            # Recive un arrglo de floats a
        addr = localfloat
        arr = []
        for i in range(sparrstack[0]):
            arr.append(getexpoper(addr+i)[0])
        storeinmem(raddres, mode(arr))
    elif fname == 'varianza': #Función media, Calcula de varianza de un arreglo
            # Recive un arrglo de floats a
        addr = localfloat
        arr = []
        for i in range(sparrstack[0]):
            arr.append(getexpoper(addr+i)[0])
        storeinmem(raddres, np.var(arr))
    elif fname == 'percentil': # función percentil, Regresa el valor del percentil q con los datos a
            # Recive un arrglo de floats a y un porciento q
        addr = localfloat
        arr = []
        for i in range(sparrstack[0]):
            arr.append(getexpoper(addr+i)[0])
        addr = localfloat + sparrstack[0]
        q = getexpoper(addr)[0]
        print('Q : ',q)
        storeinmem(raddres, np.percentile(arr,q))
    elif fname == 'aleatorio': # Función aleatorio Genera un número aleatoria en los rangos min,max
            # Recive dos argumentos min,max ambos float
        ladd = localfloat
        radd = localfloat + 1
        lop,lt = getexpoper(ladd)
        rop,rt = getexpoper(radd)
        if lop == None or rop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)
        storeinmem(raddres,random.uniform(lop,rop))
    elif fname == 'wilcoxon': # Función wilcoxon, Esta función recive un set de datos a y realiza la prueba de wilcoxon, regresando el valor de p
            # Recive un arrglo de floats a
        addr = localfloat
        arr = []
        for i in range(sparrstack[0]):
            arr.append(getexpoper(addr+i)[0])
        w, p = wilcoxon(arr)
        storeinmem(raddres, p)
    elif fname == 'wilcoxonComp': # Función wilcoxon Comparativa, Esta función recive dos sets de datos a y b, y realiza la prueba de wilcoxon, regresando el valor de p
            # Recive un arrglo de floats a y un arreglo de floats b
        addr = localfloat
        arr = []
        arr2 = []
        # Obtener los valores del primer arreglo
        for i in range(sparrstack[0]):
            arr.append(getexpoper(addr+i)[0])

        # Sacar el address del segundo arreglo y sacarlo a una variable
        addr = localfloat + sparrstack[0]
        sparrstack = sparrstack[1:]
        for i in range(sparrstack[0]):
            arr2.append(getexpoper(addr+i)[0])
        w, p = wilcoxon(arr,arr2)
        storeinmem(raddres, p)
        
    elif fname == 'regresionSimple': # Función regresión simple. Realiza regresión simple con los datos proporcionados y aproxima una xi
            # Recive x y y que son arreglos de floats y una xi que se va aproximar
            addr = localfloat
            x = []
            y = []
            n = sparrstack[0]
            # Obtener los valores del primer arreglo
            for i in range(sparrstack[0]):
                x.append(getexpoper(addr+i)[0])
            x = np.array(x)
            # Sacar el address del segundo arreglo y sacarlo a una variable
            addr = localfloat + sparrstack[0]
            sparrstack = sparrstack[1:]
            for i in range(sparrstack[0]):
                y.append(getexpoper(addr+i)[0])
            y = np.array(y)
            addr = localfloat + sparrstack[0]
            #Obtener la x a estimar
            xi = getexpoper(addr)[0]
            #Calcular la función de regresion lineal simple h(x) = b_0 + b_1 * x
            mean_x = np.mean(x)
            mean_y = np.mean(y)

            SS_xy = np.sum(y*x) - n * mean_y * mean_x
            SS_xx = np.sum(x*x) - n * mean_x * mean_x

            b_1 = SS_xy / SS_xx
            b_0 = mean_y - b_1 * mean_x

            storeinmem(raddres, b_0 + b_1*xi)

    elif fname == 'normal': # Función normal:  Regresa un número aleatorio perteneciente a la distribución normal
            # Recive dos argumentos media,desv ambos float
        ladd = localfloat
        radd = localfloat + 1
        lop,lt = getexpoper(ladd)
        rop,rt = getexpoper(radd)
        if lop == None or rop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)
        storeinmem(raddres,np.random.normal(lop,rop))
    elif fname == 'poisson': # Función Poisson:  Regresa un número aleatorio perteneciente a la distribución Poisson
            # Recive lambda que es float
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,np.random.poisson(lop))
    elif fname == 'dexponencial':# Función Exponencial:  Regresa un número aleatorio perteneciente a la distribución Exponencial
            # Recive beta que es float
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None :
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        
        storeinmem(raddres,np.random.exponential(lop))
    elif fname == 'dgeometrica':# Función Geométrica:  Regresa un número aleatorio perteneciente a la distribución Geométrica
            # Recive pexito que es float
        ladd = localfloat
        lop,lt = getexpoper(ladd)
        if lop == None :
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        lop = valtonum(lop,lt)
        storeinmem(raddres,np.random.geometric(lop))
    elif fname == 'histograma': # Función histograma. Genera un histograma con la cantidad de barras x y lo guarda en un png
        # Recive un arreglo a de floats y una x con la cantidad de barras para las gráficas
        addr = localfloat
        a = []
        # Obtener los valores del arreglo
        for i in range(sparrstack[0]):
            a.append(getexpoper(addr+i)[0])
        a = np.array(a)
        addr = localint
        x = getexpoper(addr)[0]
        plt.hist(a,x)
        plt.savefig('{}_grafico_{}{}.png'.format(infilename,'hist_',plotcounter[0]))
        plotcounter[0] += 1
        plt.clf()


    elif fname == 'diagramaDeCaja': # Función diagrama de Caja y Bigotes. Genera un diagrama de Caja y Bigotes y lo guarda en un png
        
        # Recive un arreglo a de floats
        addr = localfloat
        a = []
        # Obtener los valores del arreglo
        for i in range(sparrstack[0]):
            a.append(getexpoper(addr+i)[0])
        a = np.array(a)

        plt.boxplot(a)
        plt.savefig('{}_grafico_{}{}.png'.format(infilename,'caja_',plotcounter[1]))
        plotcounter[1] += 1
        plt.clf()
    elif fname == 'grafDispersion': # Función gráfico de dispersión. Genera un gráfico de dispersión y lo guarda en un png
        # Recive x y y que son arreglos de floats
        addr = localfloat
        x = []
        y = []
        n = sparrstack[0]
        # Obtener los valores del primer arreglo
        for i in range(sparrstack[0]):
            x.append(getexpoper(addr+i)[0])
        x = np.array(x)
        # Sacar el address del segundo arreglo y sacarlo a una variable
        addr = localfloat + sparrstack[0]
        sparrstack = sparrstack[1:]
        for i in range(sparrstack[0]):
            y.append(getexpoper(addr+i)[0])
        y = np.array(y)
        plt.scatter(x,y)
        plt.savefig('{}_grafico_{}{}.png'.format(infilename,'disp_',plotcounter[2]))
        plotcounter[2] += 1
        plt.clf()
    sparrstack = [] # Limpiar el stack para la siguiente llamada
    memstack.pop()




    
    

#################################################################
####### Ejecutar las acciones
#################################################################

#Cargar el espacio global a la variable global de memoria global
globmem = genNewMem('global')

#Crear el espacio de memoria principal del código leído
memstack.append(genNewMem('principal'))




# While para iterar por todos los cuadruplos
while runcode:
    #Cargar cuadruplo
    currcuad = cuad[ip]
    
    # Se checa el primer elemento del cuadruplo para saber que acción tomar
########################SALTOS###############################
    # Cuadruplos de saltos
    if currcuad[0] == 'GOTO': #SALTO
        ip = currcuad[3]

    elif currcuad[0] == 'GOTOF': # SALTO CONDICIONADO
        lop , _ = getexpoper(currcuad[1])
        if lop == False:
            ip = currcuad[3]
        else:
            ip += 1


#######################EXPRESIONES############################
    # Manejo de expresiones el cuadruplo esta estructurado como:
    # [ oper , operador izq, operador der, dirreción resultante]
    elif currcuad[0] in ['*','/','+','-','>','<','>=','<=','!=','==','||','&&']:
        exeExpresion(currcuad[0],currcuad[1],currcuad[2],currcuad[3])
        ip += 1

#########################ESTATUTOS###############################
    # Manejo de la lógica de los estatutos

    # Estatuto de asignación. Se checa primero el tipo al que se va a guardar y se asegura que no
    # se este haciendo operaciones con operadores nulos. Si se puede realizar la operación se hacen
    # las conversiones necesarias segun el cubo semántico 
    elif currcuad[0] == '=':
        lop,lt = getexpoper(currcuad[1])
        lop = valtonum(lop,lt)
        _ , et = getexpoper(currcuad[3])
        res = cubosem['='][et][lt]
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        # Asegurar que se este guardando con el tipo correcto
        if res != lt:
            if res == 0 and type(lop) is not int:
                lop = int(lop)
            elif res == 1 and type(lop) is not float:
                lop = float(lop)
            elif res == 2 and type(lop) is not chr:
                lop = chr(lop)
            elif res == 3 and type(lop) is not bool:
                lop = lop != 0
        
        #Checar si los temporales fueron transformados apropiadamente
        if lt == et and lt == 2 and type(lop) is not chr:
            lop = chr(lop)
        elif lt == et and lt == 3 and type(lop) is not bool:
            lop = lop != 0

        storeinmem(currcuad[3],lop)
        ip+=1

    # Estatuto de imprimir. Este estatuto imprime a pantalla lo que recive. En el caso de que se haya escrito
    # Multiples imprimir seguidos o imprimir separado por comas (ej. imprimir(x);imprimir(y); ó imprimir(x,y);)
    # Los imprime todos en la misma linea, sino hace salto de linea. 
    elif currcuad[0] == 'imprimir': #imprimir
        
        if currcuad[1] != '':
            lop, lt = getexpoper(currcuad[1])
        else:
            lop = ''
            
        if lop == None:
            lop = 'indefinido'
        elif type(lop) is bool:
            
            if lop:
                lop = 'verdadero'
                
            elif lop == False:
                
                lop = 'falso'

        elif type(lop) is not str:
            lop = str(lop)
        
        ip+=1
        isNextPrintable = cuad[ip][0] == 'imprimir'
        
        
        if isNextPrintable:
            printall += lop
        else:
            
            if printall == '':
                print(lop)
            else:
                print(printall+lop)
                printall = ''
                isNextPrintable = False


#########################ARREGLOS###########################################
    # Cuadruplo para verificar si el arreglo esta dentro del indice. Como la indexación en el lenguaje 
    # empieza en 0 Solo se recive el tamaño de la dimensión y se checa que el resultdo del expresión. 
    # Con eso revisa que la expresion no sea un valor menor a 0 ó un valor mayor al tamaño N de 
    # la dimensión. El cuadruplo se lee como : [VERIF , EXPRESION, SIZE, '']
    elif currcuad[0] == 'VERIF':
        lop,lt = getexpoper(currcuad[1])
        rop,rt = getexpoper(currcuad[2])

        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)
        
        if lop < 0:
            printerr("Uno de los subindices se resulta en un valor negativo. Los subindices no pueden ser negativos, recuerda que van de 0 a el tamaño del arreglo.\nRevisa tu código para calcular los sub indices que no te den valores negativos",ip)
        elif lop >= rop:
            printerr("Uno de tus subindices resulta ser más grande que el tamaño del arreglo. Recuerda que los subindices se limitan en valores entre 0 y el tamaño del arreglo.\nRevisa tu código para encontrar que expresión causa que el valor sobre pase el tamaño",ip)
        ip += 1
        

#########################MODULOS (FUNCIONES)################################
    # Cuadruplo de generación de memoria. Este cuadruplo indica a la máquina virtual a que
    # genere un nuevo espacio de memoria al cual se le van a copiar los parametros y el cual
    # al llegar al GOTOSUB se va a agregar al stack de memorias. 
    # El cuadruplo se lee como [ERA, nombre_funcion, '' ,'']. En caso de ser función especial
    # Se lee como : [ERA, nombre_funcion, '', recursos_locales]
    elif currcuad[0] == 'ERA':
        if currcuad[3] != '':
            res = list(map(int,currcuad[3].split(',')))
            eratemp = genNewMem('special',res)
        else:
            eratemp = genNewMem(currcuad[1])
        
        intc = 0
        floatc = 0
        charc = 0
        boolc = 0
        ip += 1
    # Cuadruplo de PARAMETER. Este cuadruplo indica que hay que pasar esta información como una
    # variable local al nuevo espacio de memoria. El cuadruplo se lee: [PARAMETER, expresion, '', tipoparam#NumParam]
    # En caso de que el parametro es arreglo se lee : [PARAMETER, expresion, size, tipoparam#NumParam]
    elif currcuad[0] == 'PARAMETER':
        lop, lt = getexpoper(currcuad[1])
        lop = valtonum(lop,lt)
        et = int(currcuad[3].split('#')[0]) # Obtener el tipo del parametro
        res = cubosem['='][et][lt]
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
        # Asegurar que se este guardando con el tipo correcto
        if res != lt:
            if res == 0 and type(lop) is not int:
                lop = int(lop)
            elif res == 1 and type(lop) is not float:
                lop = float(lop)
            elif res == 2 and type(lop) is not chr:
                lop = chr(lop)
            elif res == 3 and type(lop) is not bool:
                lop = lop != 0
        
        #Checar si los temporales fueron transformados apropiadamente
        if lt == et and lt == 2 and type(lop) is not chr:
            lop = chr(lop)
        elif lt == et and lt == 3 and type(lop) is not bool:
            lop = lop != 0

        addr = 0
        if currcuad[2] != '':#Es array
            sparrstack.append(currcuad[2])
            base = 0
            basep = currcuad[1]
            moff = 0
            count = 0
            if et == 0:
                base = localint
                count = intc
            elif et == 1:
                base = localfloat 
                count = floatc
            elif et == 2:
                base = localchar
                count = charc 
            elif et == 3:
                base = localbool
                count = boolc 
            
            
            for i in range(currcuad[2]):
                addr = base + count
                
                lop, lt = getexpoper(basep + moff)
                storeinmem(addr,lop,True)
                moff += 1
                count+=1
            
            if et == 0:
                intc = count 
            elif et == 1:
                floatc = count 
            elif et == 2:
                charc  = count 
            elif et == 3:
                boolc  = count 
            
        else:
        # Es Solo un elemento
            if et == 0:
                addr = localint + intc
                intc += 1
            elif et == 1:
                addr = localfloat + floatc
                floatc += 1
            elif et == 2:
                addr = localchar + charc
                charc += 1
            elif et == 3:
                addr = localbool + boolc
                boolc += 1
            storeinmem(addr,lop,True)
        
        ip += 1
    
    # Cuadruplo de GOTOSUB. Este cuadruplo indica a la máquina saltar al código de una función.
    # A su vez mete la memoria temporal a donde se copio los parametros al stack de memorias.
    # El cuadruplo se lee: [GOTOSUB, nombre_funcion, '', NewIp] 
    elif currcuad[0] == 'GOTOSUB':
        memstack.append(eratemp)
        eratemp = None
        ipstack.append(ip+1)
        ip = currcuad[3]
    elif currcuad[0] == 'ENDFUNC':
        memstack.pop()
        ip = ipstack.pop()
    elif currcuad[0] == 'RET':
        lop,lt = getexpoper(currcuad[1])
        _ , et = getexpoper(currcuad[3])
        res = cubosem['='][et][lt]
        # Asegurar que se este guardando con el tipo correcto
        if res != lt:
            if res == 0:
                lop = int(lop)
            elif res == 1:
                lop = float(lop)
            elif res == 2:
                lop = chr(lop)
            elif res == 3:
                if lop != 0:
                    lop = True
                else:
                    lop = False
        storeinmem(currcuad[3],lop)
        memstack.pop()
        ip = ipstack.pop()
    # Cuadruplo de función especial. Llama a la función spfuncs para ejecutar las funciones especial.
    # El cuadruplo se lee [SPFUNC, nombre_funcion, tipoReturn, Direccion_del_resultado] 
    elif currcuad[0] == 'SPFUNC':
        memstack.append(eratemp)
        
        eratemp = None
        fname = currcuad[1]
        rt = currcuad[2]
        resadd = currcuad[3]
        spfuncs(fname,resadd)
        ip += 1
    # Cuadruplo de Fin. Indica el fin del programa.
    elif currcuad[0] == 'END': #fin del programa
        runcode = False
    
    

