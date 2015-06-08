import math
from Worker import *
from Apple import *

class Colony:
	ants_ = []
	food_ = 100
	
	size_ = 10
	xPos_ = 0
	yPos_ = 0
	area_ = math.pi * ((size_ / 2)**2)
	
	color_ = "#996600"
	canvasObject_ = None
	
	age_ = 0
	knownFoodSources_ = []
	
	def __init__(self, x, y, canvas):
		self.xPos_ = x
		self.yPos_ = y
		
		self.canvasObject_ = canvas.create_oval(self.xPos_, self.yPos_, self.xPos_ + self.size_, self.yPos_ + self.size_, outline=self.color_, fill=self.color_)
		
		#adjust x and y positions so that they refer to the object's center instead of the top left corner.
		self.xPos_ += self.size_ / 2
		self.yPos_ += self.size_ / 2
		
	def GetXPos(self): return self.xPos_
	def GetYPos(self): return self.yPos_
	def GetSize(self): return self.size_
	def GetFood(self): return self.food_
	def GetPopulation(self): return len(self.ants_)
	def GetKnownFoodSources(self): 
		return self.knownFoodSources_
	
	def Operate(self, canvas, apples):
		for (a, ant) in enumerate(self.ants_):
			if self.ants_[a].GetAge() > 1000:
				canvas.delete(self.ants_[a].GetCanvasObject())
				del self.ants_[a]
			else:
				self.ants_[a].Operate(canvas, apples)
		
		if self.age_ % 20 == 0 and self.food_ >= 20:
			self.ants_.append(Worker(self.xPos_, self.yPos_, canvas, self))
			self.food_ -= 20
		
		self.size_ = math.sqrt(self.area_ / math.pi)
		canvas.itemconfig(self.canvasObject_, width=self.size_)
		
		self.age_ += 1
		
	def IncreaseFood(self, food):
		self.food_ += food
		
		self.area_ += 4
	
	def UpdateKnownFoodSources(self, foodSource):
		if foodSource.GetFood() != 0:
			if self.IsKnownFoodSource(foodSource) == False:
				self.knownFoodSources_.append(foodSource)
	
	def IsKnownFoodSource(self, foodSource):
		for (f, food) in enumerate(self.knownFoodSources_):
			if foodSource == self.knownFoodSources_[f]:
				return True
		
		return False
	
	def RemoveFromKnownFoodSources(self, foodSource):
		for (a, ant) in enumerate(self.ants_):
			self.ants_[a].RemoveFromKnownFoodSources(foodSource)
	
		for (f, food) in enumerate(self.knownFoodSources_):
			if self.knownFoodSources_[f] == foodSource:
				del self.knownFoodSources_[f]
				
				
				
				
				
				
				