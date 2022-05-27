import sys
import json
import re
from Memory import Memory

inobjfn = sys.argv[1]
obj = None

#Cubo semantico para verificar tipado en runtime
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
#Offsets de direcciones

#MAXIMOS POR VARIABLE
INTMAX = 2000
FLOATMAX = 2000
CHARMAX = 1000
BOOLMAX = 1000
POINTMAX = 2000


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
memstack = []
eratemp = None

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
ipstack = []
isNextPrintable = False
printall = ''
ip = 0

#limpiar ctetab
for k in ctetab.keys():
    if type(ctetab[k]) is str:
        if re.match("\'.\'",ctetab[k]):
            ctetab[k] = ctetab[k][1]
        elif re.match("\"[^\"]+\"",ctetab[k]):
            ctetab[k] = ctetab[k].replace('"','').encode('ascii').decode('unicode_escape')
#pdirfunc = json.dumps(ctetab,indent=4)
#print(pdirfunc)

# Parar ejecución e imprimir error
def printerr(msg,cn):
    runcode = False
    
    print("Error en la linea {} : ".format(scline[cn])+msg)
    raise SystemExit

##############FUNCIONES######################################

#generar una memoria
def genNewMem(funcname):
    if funcname == 'global':
        ints, floats, chars, bools = dirfunc['global']['varres'].values()
        return Memory(ints, floats, chars, bools)
    else:
        ints, floats, chars, bools = dirfunc[funcname]['varres'].values()
        auxmem = [Memory(ints, floats, chars, bools)]
        ints, floats, chars, bools, pointers = dirfunc[funcname]['tmpres'].values()
        auxmem.append(Memory(ints, floats, chars, bools, pointers))
        return auxmem


#obtener el tipo, offeset y scope de la dirección
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

#Funcion para obtener los operandos para expresiones
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

#Guardar en memoria el res
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
                    
                    

#Cambiar valor a numero si es necesario
def valtonum(val,t):
    if t == 2:
        val = ord(val)
    elif t == 3:
        if val:
            val = 1
        else:
            val = 0
    return val

def reusePointer(addrs,val):
    scop, atype, aoff = getTypeAndOffset(addrs)
    memstack[-1][1].mpoint[aoff] = val

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
    if type(resadd) is str:
        reusePointer(int(resadd[1:]),aux)
    else:
        storeinmem(resadd,aux)

#################################################################
####### Ejecutar las acciones
#################################################################

#Cargar el espacio global
globmem = genNewMem('global')

#Crear el espacio de principal
memstack.append(genNewMem('principal'))





while runcode:
    #Cargar cuadruplo
    currcuad = cuad[ip]
    #print(currcuad)

########################SALTOS###############################
    #Checar por las operaciones
    if currcuad[0] == 'GOTO': #SALTO
        ip = currcuad[3]

    elif currcuad[0] == 'GOTOF': # SALTO CONDICIONADO
        lop , _ = getexpoper(currcuad[1])
        if lop == False:
            ip = currcuad[3]
        else:
            ip += 1


#######################EXPRESIONES############################
    elif currcuad[0] in ['*','/','+','-','>','<','>=','<=','!=','==','||','&&']:
        exeExpresion(currcuad[0],currcuad[1],currcuad[2],currcuad[3])
        ip += 1

#########################ESTATUTOS###############################
    elif currcuad[0] == '=':
        lop,lt = getexpoper(currcuad[1])
        
        _ , et = getexpoper(currcuad[3])
        res = cubosem['='][et][lt]
        if lop == None:
            printerr('Esta intentando realizar operaciónes con variables que no cuentan con un valor. \nRevisa el códgo para asegurar que no haya alguna variable sin valor en alguna de tus operaciones',ip)
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
        ip+=1

    elif currcuad[0] == 'imprimir': #imprimir
        lop, lt = getexpoper(currcuad[1])
        
        if type(lop) is bool:
            if lop:
                lop = 'verdadero'
            else:
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
    elif currcuad[0] == 'VERIF':
        lop,lt = getexpoper(currcuad[1])
        rop,rt = getexpoper(currcuad[2])
        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)
        if lop < 0:
            printerr("Uno de los subindices se resulta en un valor negativo. Los subindices no pueden ser negativos, recuerda que van de 0 a el tamaño del arreglo.\nRevisa tu código para calcular los sub indices que no te den valores negativos")
        elif lop >= rop:
            printerr("Uno de tus subindices resulta ser más grande que el tamaño del arreglo. Recuerda que los subindices se limitan en valores entre 0 y el tamaño del arreglo.\nRevisa tu código para encontrar que expresión causa que el valor sobre pase el tamaño")
        ip += 1
        

#########################MODULOS (FUNCIONES)################################
    elif currcuad[0] == 'ERA':
        eratemp = genNewMem(currcuad[1])
        intc = 0
        floatc = 0
        charc = 0
        boolc = 0
        ip += 1
    elif currcuad[0] == 'PARAMETER':
        lop, lt = getexpoper(currcuad[1])
        addr = 0
        if lt == 0:
            addr = localint + intc
            intc += 1
        elif lt == 2:
            addr = localfloat + floatc
            floatc += 1
        elif lt == 3:
            addr = localchar + charc
            charc += 1
        elif lt == 4:
            addr = localbool + boolc
            boolc += 1
        storeinmem(addr,lop,True)
        ip += 1
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
    elif currcuad[0] == 'END': #fin del programa
        runcode = False
    
    

