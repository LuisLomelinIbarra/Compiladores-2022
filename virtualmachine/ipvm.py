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

def getTypeAndOffset(addr):
    #regresa el scope, tipo y offset
    atype = None
    aoffset = None
    ascope = None
    if addr >= globalint and addr < localint: #globales
        ascope = 'global'
        if addr >= globalint and addr < globalfloat:
            aoffset = addr - globalint
            atype = 'entero'
        elif addr >= globalfloat and addr < globalchar:
            aoffset = addr - globalfloat
            atype = 'flotante'
        elif addr >= globalchar and addr < globalbool:
            aoffset = addr - globalchar
            atype = 'char'
        elif addr >= globalbool and addr < globalintarr:
            aoffset = addr - globalbool
            atype = 'bool'
    
    elif addr >= localint and addr < tempint: #locales
        ascope = 'local'
        if addr >= localint and addr < localfloat:
            aoffset = addr - localint
            atype = 'entero'
        elif addr >= localfloat and addr < localchar:
            aoffset = addr - localfloat
            atype = 'flotante'
        elif addr >= localchar and addr < localbool:
            aoffset = addr - localchar
            atype = 'char'
        elif addr >= localbool and addr < localintarr:
            aoffset = addr - localbool
            atype = 'bool'

    elif addr >= tempint and addr < constint:#temporales
        ascope = 'temp'
        if addr >= tempint and addr < tempfloat:
            aoffset = addr - tempint
            atype = 'entero'
        elif addr >= tempfloat and addr < tempchar:
            aoffset = addr - tempfloat
            atype = 'flotante'
        elif addr >= tempchar and addr < tempbool:
            aoffset = addr - tempchar
            atype = 'char'
        elif addr >= tempbool and addr < tempintarr:
            aoffset = addr - tempbool
            atype = 'bool'
    
    return ascope,atype,aoffset

#Funcion para obtener los operandos para expresiones
def getexpoper(aopl, aopr):
    pass

#Cargar el archivo resultante de la compilación
with open(inobjfn) as objfile:
    obj = json.load(objfile)

#print(obj['ctetab'])

ctetab = obj['ctetab']
dirfunc = obj['dirfunc']
cuad = obj['cuadruplos']

#Ejecutar las acciones
ip = 0
runcode = True

print(ctetab)
#Cargar el espacio global
ints, floats, chars, bools = dirfunc['global']['varres'].values()

globmem = Memory(ints, floats, chars, bools)
#Crear el espacio de principal
ints, floats, chars, bools = dirfunc['principal']['varres'].values()
prinmem = [Memory(ints, floats, chars, bools)]
ints, floats, chars, bools = dirfunc['principal']['tmpres'].values()
prinmem.append(Memory(ints, floats, chars, bools))
print('\n\n\n',ints, floats, chars, bools)
print(prinmem[0].mint)
while runcode:
    #Cargar cuadruplo
    currcuad = cuad[ip]
    print(currcuad)
    #Checar por las operaciones
    if currcuad[0] == 'GOTO':
        ip = currcuad[3]
    elif currcuad[0] == '*':
        pass
    elif currcuad[0] == '/':
        pass
    elif currcuad[0] == '+':
        pass
    elif currcuad[0] == '-':
        pass
    elif currcuad[0] == '>':
        pass
    elif currcuad[0] == '<':
        pass
    elif currcuad[0] == '>=':
        pass
    elif currcuad[0] == '<=':
        pass
    elif currcuad[0] == '==':
        pass
    elif currcuad[0] == '!=':
        pass
    elif currcuad[0] == '&&':
        pass
    elif currcuad[0] == '||':
        pass
    elif currcuad[0] == 'imprimir':
        pass
    elif currcuad[0] == 'END':
        runcode = False
    
    ip+=1

