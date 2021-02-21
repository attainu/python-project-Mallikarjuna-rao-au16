class Vehicle:
    	def __init__(self,regNo,color):
		    self.color =  color
		    self.regNo = regNo

class Car(Vehicle):

	def __init__(self,regNo,color):
		Vehicle.__init__(self,regNo,color)

	def getType(self):
		return "Car"