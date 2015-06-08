from random import randint

class Apple:
	xPos_ = 0
	yPos_ = 0
	size_ = 20
	food_ = 400
	canvasObject_ = None
	
	def __init__(self, canvas):
		self.xPos_ = randint(0, 800)
		self.yPos_ = randint(0, 600)
		self.canvasObject_ = canvas.create_oval(self.xPos_, self.yPos_, self.xPos_ + self.size_, self.yPos_ + self.size_, outline="#AD0E13", fill="#AD0E13")
	
		#adjust x and y positions so that they refer to the object's center instead of the top left corner.
		self.xPos_ += self.size_ / 2
		self.yPos_ += self.size_ / 2
	
	def GetXPos(self): return self.xPos_
	def GetYPos(self): return self.yPos_
	def GetSize(self): return self.size_
	def GetFood(self): return self.food_
	def GetCanvasObject(self): return self.canvasObject_
	
	def DecreaseFood(self, food):
		self.food_ -= food
		
		
	
	
	
	
		