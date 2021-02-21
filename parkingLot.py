import VehicleClass
import sys

if sys.version_info[0] == 2:
	input = raw_input

class ParkingLot:
	def __init__(self):
		self.capacity = 0
		self.slotId = 0
		self.numOfOccupiedSlots = 0

	def createParkingLot(self,capacity):
		self.slots = [-1] * capacity
		self.capacity = capacity
		return self.capacity

	def getEmptySlot(self):
		for i in range(len(self.slots)):
			if self.slots[i] == -1:
				return i

	def park(self,regNo,color):
		if self.numOfOccupiedSlots < self.capacity: 
			slotId = self.getEmptySlot()
			self.slots[slotId] = VehicleClass.Car(regNo,color)
			self.slotId = self.slotId+1
			self.numOfOccupiedSlots = self.numOfOccupiedSlots + 1
			return slotId+1
		else:
			return -1

	def leave(self,slotId):

		if self.numOfOccupiedSlots > 0 and self.slots[slotId-1] != -1:
			self.slots[slotId-1] = -1
			self.numOfOccupiedSlots = self.numOfOccupiedSlots - 1
			return True
		else:
			return False

	def status(self):
		print("Slot No.\tRegistration No.\tColour")
		for i in range(len(self.slots)):
			if self.slots[i] != -1:
				print(str(i+1) + "\t\t" +str(self.slots[i].regNo) + "\t\t" + str(self.slots[i].color))
			else:
				continue

	def getRegNoFromColor(self,color):

		regNos = []
		for i in self.slots:

			if i == -1:
				continue
			if i.color == color:
				regNos.append(i.regNo)
		return regNos
			
	def getSlotNoFromRegNo(self,regNo):
		
		for i in range(len(self.slots)):
			if self.slots[i].regNo == regNo:
				return i+1
			else:
				continue
		return -1
			

	def getSlotNoFromColor(self,color):
		
		slotnos = []

		for i in range(len(self.slots)):

			if self.slots[i] == -1:
				continue
			if self.slots[i].color == color:
				slotnos.append(str(i+1))
		return slotnos

	def show(self,line):
		if line.startswith('create_parking_lot'):
			n = int(line.split(' ')[1])
			res = self.createParkingLot(n)
			print('Created a parking lot with '+str(res)+' slots')

		elif line.startswith('park'):
			regNo = line.split(' ')[1]
			color = line.split(' ')[2]
			res = self.park(regNo,color)
			if res == -1:
				print("Sorry, parking lot is full")
			else:
				print('Allocated slot number: '+str(res))

		elif line.startswith('leave'):
			leave_slotId = int(line.split(' ')[1])
			status = self.leave(leave_slotId)
			if status:
				print('Slot number '+str(leave_slotId)+' is free')

		elif line.startswith('status'):
			self.status()

		elif line.startswith('registration_numbers_for_cars_with_colour'):
			color = line.split(' ')[1]
			regNos = self.getRegNoFromColor(color)
			print(', '.join(regNos))

		elif line.startswith('slot_numbers_for_cars_with_colour'):
			color = line.split(' ')[1]
			slotnos = self.getSlotNoFromColor(color)
			print(', '.join(slotnos))

		elif line.startswith('slot_number_for_registration_number'):
			regNo = line.split(' ')[1]
			slotNo = self.getSlotNoFromRegNo(regNo)
			if slotNo == -1:
				print("Not found")
			else:
				print(slotNo)
		elif line.startswith('exit'):
			exit(0)

