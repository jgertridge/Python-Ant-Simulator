from tkinter import *
from Colony import *
from Apple import *

class Lawn(Frame):
	canvas_ = None
	
	colony_ = None
	apples_ = []
	
	foodText_ = None
	populationText_ = None
	
	def __init__(self, master): 
		Frame.__init__(self, master)
		self.pack()
		self.InitUI()
		
		self.colony_ = Colony(400, 300, self.canvas_)
		
		for a in range(0, 10):
			self.apples_.append(Apple(self.canvas_))
		
	def InitUI(self):
		self.master.title("Ant Simulator by Jeremy Gertridge")
		self.master.geometry("800x600")
		self.master.maxsize(800, 600)
		self.pack(fill=BOTH, expand=1)
		
		self.canvas_ = Canvas(self)
		self.canvas_.pack(fill=BOTH, expand=1)
		background = self.canvas_.create_rectangle(800, 600, 0, 0, outline="#487A09", fill="#487A09")
		self.foodText_ = self.canvas_.create_text(30, 10, text="")
		self.populationText_ = self.canvas_.create_text(100, 10, text="")
		
	def Tick(self):
		self.colony_.Operate(self.canvas_, self.apples_)
		
		foodTextValue = "Food: " + str(self.colony_.GetFood())
		self.canvas_.itemconfig(self.foodText_, text=foodTextValue)
		
		populationTextValue = "Population: " + str(self.colony_.GetPopulation())
		self.canvas_.itemconfig(self.populationText_, text=populationTextValue)
		
		#delete depleted apples
		for (a, apple) in enumerate(self.apples_):
			if self.apples_[a].GetFood() <= 0:
				self.colony_.RemoveFromKnownFoodSources(self.apples_[a])
				self.canvas_.delete(self.apples_[a].GetCanvasObject())
				del self.apples_[a]
		
		self.canvas_.update()
		self.master.after(100, self.Tick)
	
