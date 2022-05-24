import sys
import json
from Memory import Memory

inobjfn = sys.argv[1]
obj = None

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


#Cargar el archivo resultante de la compilación
with open(inobjfn) as objfile:
    obj = json.load(objfile)


ctetab = obj['ctetab']
dirfunc = obj['dirfunc']
cuad = obj['cuadruplos']


print(ctetab)
#Cargar el espacio global
ints, floats, chars, bools = dirfunc['global']['varres'].values()

globmem = Memory(ints, floats, chars, bools)
memstack = []
#Crear el espacio de principal
ints, floats, chars, bools = dirfunc['principal']['varres'].values()
prinmem = [Memory(ints, floats, chars, bools)]
ints, floats, chars, bools = dirfunc['principal']['tmpres'].values()
prinmem.append(Memory(ints, floats, chars, bools))

memstack.append(prinmem)


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
        return ''
    
    if str(addrs) in ctetab.keys():
        return ctetab[str(addrs)]
    else:
        scop, atype, aoff = getTypeAndOffset(addrs)
        if scop == 'global':
            if atype == 0: #entero
                return globmem.mint[aoff]
            elif atype == 1: #float
                return globmem.mfloat[aoff]
            elif atype == 2: #char
                return globmem.mchar[aoff]
            elif atype == 3: #bool
                return globmem.mbool[aoff]
            elif atype == 4: #pointer
                return globmem.mpoint[aoff]
        elif scop == 'local':
            if atype == 0: #entero
                return memstack[-1][0].mint[aoff]
            elif atype == 1: #float
                return memstack[-1][0].mfloat[aoff]
            elif atype == 2: #char
                return memstack[-1][0].mchar[aoff]
            elif atype == 3: #bool
                return memstack[-1][0].mbool[aoff]
            elif atype == 4: #pointer
                return memstack[-1][0].mpoint[aoff]
        elif scop == 'temp':
            if atype == 0: #entero
                return memstack[-1][1].mint[aoff]
            elif atype == 1: #float
                return memstack[-1][1].mfloat[aoff]
            elif atype == 2: #char
                return memstack[-1][1].mchar[aoff]
            elif atype == 3: #bool
                return memstack[-1][1].mbool[aoff]
            elif atype == 4: #pointer
                return memstack[-1][1].mpoint[aoff]


def storeinmem(addrs,val):
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
            memstack[-1][0].mint[aoff] = val
        elif atype == 1: #float
            memstack[-1][0].mfloat[aoff] = val
        elif atype == 2: #char
            memstack[-1][0].mchar[aoff] = val
        elif atype == 3: #bool
            memstack[-1][0].mbool[aoff] = val
        elif atype == 4: #pointer
            memstack[-1][0].mpoint[aoff] = val
    elif scop == 'temp':
        if atype == 0: #entero
            memstack[-1][1].mint[aoff] = val
        elif atype == 1: #float
            memstack[-1][1].mfloat[aoff] = val
        elif atype == 2: #char
            memstack[-1][1].mchar[aoff] = val
        elif atype == 3: #bool
            memstack[-1][1].mbool[aoff] = val
        elif atype == 4: #pointer
            memstack[-1][1].mpoint[aoff] = val



#Ejecutar las acciones
ip = 0
runcode = True


while runcode:
    #Cargar cuadruplo
    currcuad = cuad[ip]
    #print(currcuad)
    #Checar por las operaciones
    if currcuad[0] == 'GOTO': #SALTO
        ip = currcuad[3]

    elif currcuad[0] == '*': # Multiplicacion
        lop = getexpoper(currcuad[1])
        rop = getexpoper(currcuad[2])
        
        aux = lop * rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '/': # Divicion
        lop = getexpoper(currcuad[1])
        rop = getexpoper(currcuad[2])
        aux = lop / rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '+': #Suma 
        lop = getexpoper(currcuad[1])
        rop = getexpoper(currcuad[2])
        if rop == '':
            aux = + lop
        else:
            aux = lop + rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '-': #Resta
        lop = getexpoper(currcuad[1])
        rop = getexpoper(currcuad[2])
        if rop == '':
            aux = - lop
        else:
            aux = lop - rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '>': #Mayorque
        lop = getexpoper(currcuad[1])
        rop = getexpoper(currcuad[2])
        aux = lop > rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '<': #menor que
        lop = getexpoper(currcuad[1])
        rop = getexpoper(currcuad[2])
        aux = lop < rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '>=': # mayor igual
        lop = getexpoper(currcuad[1])
        rop = getexpoper(currcuad[2])
        aux = lop >= rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '<=': #menor igual
        lop = getexpoper(currcuad[1])
        rop = getexpoper(currcuad[2])
        aux = lop <= rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '==': #igual (relacional)
        lop = getexpoper(currcuad[1])
        rop = getexpoper(currcuad[2])
        aux = lop == rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '!=': #diferente
        lop = getexpoper(currcuad[1])
        rop = getexpoper(currcuad[2])
        aux = lop != rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '&&': # and
        lop = getexpoper(currcuad[1])
        rop = getexpoper(currcuad[2])
        aux = lop and rop
        storeinmem(currcuad[3],aux)
        ip+=1

    elif currcuad[0] == '||': # or
        lop = getexpoper(currcuad[1])
        rop = getexpoper(currcuad[2])
        aux = lop or rop
        storeinmem(currcuad[3],aux)
        ip+=1

    ##ESTATUTOS#########################
    elif currcuad[0] == '=':
        lop = getexpoper(currcuad[1])
        storeinmem(currcuad[3],lop)
        ip+=1

    elif currcuad[0] == 'imprimir': #imprimir
        lop = getexpoper(currcuad[1])
        if type(lop) is bool:
            if lop:
                lop = 'verdadero'
            else:
                lop = 'falso'
        print(lop)
        ip+=1
    elif currcuad[0] == 'END': #fin del programa
        runcode = False
    
    

