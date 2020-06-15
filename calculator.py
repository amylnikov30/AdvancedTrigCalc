import math

class Calculator:
    
    a = float
    b = float
    c = float
    A = float
    B = float
    C = float

    sides = []
    angles = []

    enoughInfo = bool
    
    def __init__(self, a=0.0, b=0.0, c=0.0, A=0.0, B=0.0, C=0.0):
        self.a = a
        self.b = b
        self.c = c
        self.A = A
        self.B = B
        self.C = C

        self.sides = [self.a, self.b, self.c]
        self.angles = [self.A, self.B, self.C]

        self.enoughInfo = False
    

    def __call__(self, a=0.0, b=0.0, c=0.0, A=0.0, B=0.0, C=0.0):
        self.a = a
        self.b = b
        self.c = c
        self.A = A
        self.B = B
        self.C = C

        self.sides = [self.a, self.b, self.c]
        self.angles = [self.A, self.B, self.C]        


    def completeAngles(self, angle1: float, angle2: float) -> float:
        angle3 = 180 - (angle1 + angle2)

        return angle3

    def updateLists(self):
        self.sides = [self.a, self.b, self.c]
        self.angles = [self.A, self.B, self.C]

    def updateVars(self):

        self.a = self.sides[0]
        self.b = self.sides[1]
        self.c = self.sides[2]
        self.A = self.angles[0]
        self.B = self.angles[1]
        self.C = self.angles[2]


    def finalCheck(self):
        
        if sum(self.angles) < 180:
            self.angles[self.angles.index(max(self.angles))] = 180 - max(self.angles)
        



    def revCosLaw(self):

        numerator = self.a**2 + self.b**2 - self.c**2
        denominator = 2*self.a*self.b

        self.C = math.degrees(math.acos(numerator/denominator))

        

        self.updateLists()


    def cosLaw(self):
        existingSides = []
        #nonExSide = float
        existingAngle = float

        for i in range(len(self.sides)):
            if self.sides[i] != 0:
                existingSides.append(self.sides[i])
        for i in range(len(self.angles)):
            if self.angles[i] or self.angles[i] != 0:
                existingAngle = self.angles[i]

        finalSide = math.sqrt(existingSides[0]**2 + existingSides[1]**2 - 2*existingSides[0]*existingSides[1]*math.cos(math.radians(float(existingAngle))))

        for i in range(len(self.sides)):
            if not self.sides[i] or self.sides[i] == 0:
                self.sides[i] = finalSide        
            




    def isBetween(self) -> bool:
        result = False

        if self.a and self.b and self.C:
            result = True
        elif self.a and self.c and self.B:
            result = True
        elif self.b and self.c and self.A:
            result = True

        return result



    def existingElems(self, ls):
        result = []
        for i in ls:
            if i:
                result.append(i)

        return result




    def sinLaw(self):

        exSides = self.existingElems(self.sides)
        exAngles = self.existingElems(self.angles)

        if len(exSides) >= 2 and len(exAngles) >= 1:
            #initialAngle = 0.0
            #secondAngle = 0.0
            ratio = 0
        
            #finding ratio
            for i in range(len(self.sides)):
                if self.sides[i] and self.angles[i]:
                    ratio = self.sides[i] / math.sin(math.radians(self.angles[i]))
                    break
        
            
        #finding second angle and appending to exAngles
            for i in range(len(self.sides)):
                if self.sides[i] and not self.angles[i]:
                    self.angles[i] = math.degrees(math.asin(self.sides[i] / ratio))
                    exAngles.append(self.angles[i])
                    break

            finalAngle = self.completeAngles(exAngles[0], exAngles[1])

            for i in range(len(self.angles)):
                if not self.angles[i]:
                    self.angles[i] = finalAngle
                    break

            for i in range(len(self.sides)):
                if not self.sides[i]:
                    self.sides[i] = math.sin(math.radians(self.angles[i])) * ratio
                    break

            self.updateVars()

        elif len(exSides) >= 1 and len(exAngles) >= 2:

            ratio = 0

            exAngles.append(self.completeAngles(exAngles[0], exAngles[1]))
            for i in range(len(self.angles)):
                if not self.angles[i]:
                    self.angles[i] = self.completeAngles(exAngles[0], exAngles[1])
                    exAngles.append(self.completeAngles(exAngles[0], exAngles[1]))

        
            #finding ratio
            for i in range(len(self.sides)):
                if self.sides[i]:
                    ratio = self.sides[i] / math.sin(math.radians(self.angles[i]))
                    break


            for i in range(len(self.sides)):
                if not self.sides[i]:
                    self.sides[i] = math.sin(math.radians(self.angles[i])) * ratio

            self.updateVars()



    def main(self):

        existingSides = self.existingElems(self.sides)
        existingAngles = self.existingElems(self.angles)
        if len(existingSides) >= 3:
            self.revCosLaw()
            self.sinLaw()
            self.finalCheck()
            self.enoughInfo = True
        elif len(existingSides) >= 2 and len(existingAngles) >= 1:
            if self.isBetween():
                self.cosLaw()
                self.sinLaw()
                self.finalCheck()
            else:
                self.sinLaw()
                self.finalCheck()
            self.enoughInfo = True
        elif len(existingSides) >= 1 and len(existingAngles) >= 2:
                self.sinLaw()
                self.finalCheck()
                self.enoughInfo = True

        else:
            self.enoughInfo = False

        
        
            
        
                
        
        
        
        
            



















        
        
    
