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
INTARRAYMAX = 2000
FLOATARRAYMAX = 2000
CHARARRAYMAX = 1000
BOOLARRAYMAX = 1000
STRINGMAX = 1000

#Global
globalint = 1000
globalfloat = globalint + INTMAX
globalchar = globalfloat + FLOATMAX
globalbool = globalchar + CHARMAX
globalintarr = globalbool + BOOLMAX
globalfloatarr = globalintarr + INTARRAYMAX
globalchararr = globalfloatarr + FLOATARRAYMAX
globalboolarr = globalchararr + CHARARRAYMAX

#Local
localint = globalboolarr + BOOLARRAYMAX
localfloat = localint + INTMAX
localchar = localfloat + FLOATMAX
localbool = localchar + CHARMAX
localintarr = localbool + BOOLMAX
localfloatarr = localintarr + INTARRAYMAX
localchararr = localfloatarr + FLOATARRAYMAX
localboolarr = localchararr + CHARARRAYMAX

#Temporal
tempint = localboolarr + BOOLARRAYMAX
tempfloat = tempint + INTMAX
tempchar = tempfloat + FLOATMAX
tempbool = tempchar + CHARMAX
tempintarr = tempbool + BOOLMAX
tempfloatarr = tempintarr + INTARRAYMAX
tempchararr = tempfloatarr + FLOATARRAYMAX
tempboolarr = tempchararr + CHARARRAYMAX

#Constantes
constint = tempboolarr + BOOLARRAYMAX
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

#limpiar ctetab
for k in ctetab.keys():
    if type(ctetab[k]) is str:
        if re.match("\'*\'",ctetab[k]):
            ctetab[k] = ctetab[k][1]

print(ctetab)


##############FUNCIONES######################################

#generar una memoria
def genNewMem(funcname):
    if funcname == 'global':
        ints, floats, chars, bools = dirfunc['global']['varres'].values()
        return Memory(ints, floats, chars, bools)
    else:
        ints, floats, chars, bools = dirfunc[funcname]['varres'].values()
        auxmem = [Memory(ints, floats, chars, bools)]
        ints, floats, chars, bools = dirfunc[funcname]['tmpres'].values()
        auxmem.append(Memory(ints, floats, chars, bools))
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
        elif addr >= globalbool and addr < globalintarr:
            aoffset = addr - globalbool
            atype = 3
    
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
        elif addr >= localbool and addr < localintarr:
            aoffset = addr - localbool
            atype = 3

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
        elif addr >= tempbool and addr < tempintarr:
            aoffset = addr - tempbool
            atype = 3
    
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
                return memstack[-1][1].mpoint[aoff], atype

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
                eratemp[1].mpoint[aoff] = val
            else:
                memstack[-1][1].mpoint[aoff] = val

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



#################################################################
####### Ejecutar las acciones
#################################################################

#Cargar el espacio global
globmem = genNewMem('global')

#Crear el espacio de principal
memstack.append(genNewMem('principal'))

ipstack = []

ip = 0
runcode = True


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
    elif currcuad[0] == '*': # Multiplicacion
        lop,lt = getexpoper(currcuad[1])
        rop,rt = getexpoper(currcuad[2])

        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)     
        
        aux = lop * rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '/': # Division
        lop,lt = getexpoper(currcuad[1])
        rop,rt = getexpoper(currcuad[2])

        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)   

        aux = lop / rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '+': #Suma 
        lop,lt = getexpoper(currcuad[1])
        rop,rt = getexpoper(currcuad[2])
        
        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)    

        if rop == '':
            aux = 0 + lop
        else:
            aux = lop + rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '-': #Resta
        lop,lt = getexpoper(currcuad[1])
        rop,rt = getexpoper(currcuad[2])
        
        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)  

        if rop == '':
            aux = 0 - lop
        else:
            aux = lop - rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '>': #Mayorque
        lop,lt = getexpoper(currcuad[1])
        rop,rt = getexpoper(currcuad[2])
        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)  

        aux = lop > rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '<': #menor que
        lop,lt = getexpoper(currcuad[1])
        rop,rt = getexpoper(currcuad[2])
        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)   


        aux = lop < rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '>=': # mayor igual
        lop,lt = getexpoper(currcuad[1])
        rop,rt = getexpoper(currcuad[2])

        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)  


        aux = lop >= rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '<=': #menor igual
        lop,lt = getexpoper(currcuad[1])
        rop,rt = getexpoper(currcuad[2])

        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)  

        aux = lop <= rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '==': #igual (relacional)
        lop,lt = getexpoper(currcuad[1])
        rop,rt = getexpoper(currcuad[2])
        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)   

        aux = lop == rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '!=': #diferente
        lop,lt = getexpoper(currcuad[1])
        rop,rt = getexpoper(currcuad[2])
        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)   

        aux = lop != rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '&&': # and
        lop, lt = getexpoper(currcuad[1])
        rop, rt = getexpoper(currcuad[2])

        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)   

        aux = lop and rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '||': # or
        lop,lt = getexpoper(currcuad[1])
        rop,rt = getexpoper(currcuad[2])
        lop = valtonum(lop,lt)
        rop = valtonum(rop,rt)   

        aux = lop or rop
        storeinmem(currcuad[3],aux)
        ip+=1

    ##ESTATUTOS#########################
    elif currcuad[0] == '=':
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
        ip+=1

    elif currcuad[0] == 'imprimir': #imprimir
        lop, lt = getexpoper(currcuad[1])
        if type(lop) is bool:
            if lop:
                lop = 'verdadero'
            else:
                lop = 'falso'
        print(lop)
        ip+=1
    
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
    elif currcuad[0] == 'END': #fin del programa
        runcode = False
    
    

