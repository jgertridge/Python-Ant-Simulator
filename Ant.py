from tkinter import *
from Apple import *

class Ant():
	type_ = None
	colony_ = None
	color_ = "#000000"
	canvasObject_ = None
	
	xPos_ = None
	yPos_ = None
	xVelocity_ = 0
	yVelocity_ = 0
	
	size_ = 0
	speed_ = 0
	scentRange_ = 0
	age_ = 0
	
	food_ = 0
	knownFoodSources_ = []
	
	def __init__(self, colony):
		self.type_ = "Undefined"
		self.colony_ = colony
		
	def GetType(self): return self.type_
	def GetCanvasObject(self): return self.canvasObject_
	def GetXPos(self): return self.xPos_
	def GetYPos(self): return self.yPos_
	def GetXVelocity(self): return self.xVelocity_
	def GetYVelocity(self): return self.yVelocity_
	def GetSize(self): return self.size_
	def GetSpeed(self): return self.speed_
	def GetScentRange(self): return self.scentRange_
	def GetAge(self): return self.age_
	def GetFood(self): return self.food_
	
	def SetPosition(self, x, y):
		self.xPos_ = x
		self.yPos_ = y
		
	def Operate(self):
		return 0
	