class Memory():
    def _arrinit(self,num):
        arr = []
        if num <= 0:
            return arr
        for i in range(num):
            arr.append(None)
        return arr

    def __init__(self,intcount = 0,floatcount = 0,charcount = 0,boolcount = 0,pointercount = 0):
        self.mint = self._arrinit(intcount)
        self.mfloat = self._arrinit(floatcount)
        self.mchar = self._arrinit(charcount)
        self.mbool = self._arrinit(boolcount)
        self.mpoint = self._arrinit(pointercount)

    