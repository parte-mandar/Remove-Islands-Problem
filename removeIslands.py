class Surface:
    def __init__(self, isDryLand, isCoast, attached):
        self.isDryLand = isDryLand
        self.isCoast = isCoast
        self.isAttached = attached


class RemoveIslandClass:
    def __init__(self, matrixOfIslands):
        self.rowLen = len(matrixOfIslands)
        self.colLen = len(matrixOfIslands[0])
        self.rowCount = 0
        self.colCount = 0
        self.workingMatrix = []
        self.isCoast = False
        self.attached = False
        self.eachRow = []
        
        for row in matrixOfIslands:
            for col in row:
                self.isCoast = False
                self.attached = False

                if (col == 1):
                    if (self.rowCount == 0 or self.colCount == 0 or self.rowCount == self.rowLen-1 or self.colCount == self.colLen-1):
                        self.isCoast = True
                        self.attached = True
                    
                    self.eachRow.append(Surface(True, self.isCoast, self.attached)) 
                
                else:
                    if (self.rowCount == 0 or self.colCount == 0 or self.rowCount == self.rowLen-1 or self.colCount == self.colLen-1):
                        self.isCoast = True
                        self.attached = True

                    self.eachRow.append(Surface(False, self.isCoast, self.attached)) 

                self.colCount = self.colCount + 1

            self.workingMatrix.append(self.__appendListCompletely(self.eachRow)) 
            self.eachRow.clear()
            self.rowCount = self.rowCount + 1
            self.colCount = 0

        self.__removeIslands()
        #self.returnResult()

    def __removeIslands(self):
        self.colCount = 0
        self.rowCount = 0
        for row in self.workingMatrix:
            for col in row:
                if (self.rowCount == 0 or self.colCount == 0 or self.rowCount == self.rowLen-1 or self.colCount == self.colLen-1):
                    pass
                else:
                    if (col.isDryLand == True and col.isAttached == False):
                        self.__checkSurface(self.rowCount, self.colCount)

                self.colCount = self.colCount + 1

            self.rowCount = self.rowCount + 1
            self.colCount = 0

    def __checkSurface(self, row, col):
        self.workingMatrix[row][col]
        if (self.workingMatrix[row][col-1].isDryLand == True):
            self.workingMatrix[row][col].isAttached = True
            if (self.workingMatrix[row][col-1].isCoast == True):
                self.workingMatrix[row][col].isCoast = True
                return True
            elif (self.workingMatrix[row][col-1].isAttached == True):
                self.workingMatrix[row][col].isAttached = True
            else:
                self.workingMatrix[row][col].isAttached = True
                checker = self.__checkSurface(row, col-1)
                if (checker == True):
                    self.workingMatrix[row][col].isCoast = True
                    return True

        if (self.workingMatrix[row][col+1].isDryLand == True):
            self.workingMatrix[row][col].isAttached = True
            if (self.workingMatrix[row][col+1].isCoast == True):
                self.workingMatrix[row][col].isCoast = True
                return True
            elif (self.workingMatrix[row][col+1].isAttached == True):
                self.workingMatrix[row][col].isAttached = True
            else:
                self.workingMatrix[row][col].isAttached = True
                checker = self.__checkSurface(row, col+1)
                if (checker == True):
                    self.workingMatrix[row][col].isCoast = True
                    return True

        if (self.workingMatrix[row-1][col].isDryLand == True):
            self.workingMatrix[row][col].isAttached = True
            if (self.workingMatrix[row-1][col].isCoast == True):
                self.workingMatrix[row][col].isCoast = True
                return True
            elif (self.workingMatrix[row-1][col].isAttached == True):
                self.workingMatrix[row][col].isAttached = True
            else:
                self.workingMatrix[row][col].isAttached = True
                checker = self.__checkSurface(row-1, col)
                if (checker == True):
                    self.workingMatrix[row][col].isCoast = True
                    return True

        if (self.workingMatrix[row+1][col].isDryLand == True):
            self.workingMatrix[row][col].isAttached = True
            if (self.workingMatrix[row+1][col].isCoast == True):
                self.workingMatrix[row][col].isCoast = True
                return True
            elif (self.workingMatrix[row+1][col].isAttached == True):
                self.workingMatrix[row][col].isAttached = True
            else:
                self.workingMatrix[row][col].isAttached = True
                checker = self.__checkSurface(row+1, col)
                if (checker == True):
                    self.workingMatrix[row][col].isCoast = True
                    return True

    def returnResult(self):
        resultMatrix = []
        for row in self.workingMatrix:
            for col in row:
                if (col.isDryLand == True and col.isCoast == True):
                    self.eachRow.append(1)
                else:
                    self.eachRow.append(0)


            resultMatrix.append(self.__appendListCompletely(self.eachRow)) 
            self.eachRow.clear()

        return resultMatrix

    # Helper Functions    
    def __appendListCompletely(self, tempList):
        tempList2 = []
        for temp in tempList:
            tempList2.append(temp)

        return tempList2
