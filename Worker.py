from random import randint, uniform
import math
from Ant import *

class Worker(Ant):
	target_ = None

	def __init__(self, x, y, canvas, colony):
		self.type_ = "Worker"
		self.xPos_ = x
		self.yPos_ = y
		self.colony_ = colony
		
		self.size_ = 3
		self.speed_ = 3
		self.scentRange_ = 100
		self.knownFoodSources_ = self.colony_.GetKnownFoodSources()
		
		self.canvasObject_ = canvas.create_oval(self.xPos_, self.yPos_, self.xPos_ + self.size_, self.yPos_ + self.size_, outline=self.color_, fill=self.color_)	
		
		#adjust x and y positions so that they refer to the object's center instead of the top left corner.
		self.xPos_ += self.size_ / 2
		self.yPos_ += self.size_ / 2
	
	def Operate(self, canvas, apples):
		if self.food_ < 5: #if the ant is looking for food
			self.target_ = self.GetClosestApple(apples)
		
			if self.target_ != None: #if the ant knows of a food source
				if self.IsColliding(self.target_) == True and self.food_ < 5: #if the ant is at that food source, but still needs to gather food
					self.xVelocity_ = 0
					self.yVelocity_ = 0
					self.food_ += 5
					self.target_.DecreaseFood(5)
				else: #move towards target food
					xDifference = self.target_.GetXPos() - self.xPos_
					yDifference = self.target_.GetYPos() - self.yPos_
					
					total = 0
					if xDifference < 0: total += xDifference * -1 
					else: total += xDifference
					if yDifference < 0: total += yDifference * -1 
					else: total += yDifference
					
					if xDifference != 0: self.xVelocity_ = (xDifference / total) * self.speed_ 
					if yDifference != 0: self.yVelocity_ = (yDifference / total) * self.speed_
			else: #search for a food source
				if self.xVelocity_ == 0:
					self.xVelocity_ = uniform(-(self.speed_), self.speed_)
					
				if self.yVelocity_ == 0:
					isNegative = randint(0, 1)
					multiplier = 1
					if isNegative == 0: multiplier = -1
					
					if self.xVelocity_  < 0: self.yVelocity_ = (self.speed_ - (self.xVelocity_ * -1)) * multiplier
					else: self.yVelocity_ = (self.speed_ - self.xVelocity_) * multiplier
					
				if self.age_ % 10 == 0:
					vChange = uniform(-0.3, 0.3)
					self.xVelocity_ += vChange
					self.yVelocity_ -= vChange
				
		else: #return the gathered food
			if self.IsColliding(self.colony_) == True: #if the ant has returned to the colony and still has food left to deliver
				self.xVelocity_ = 0
				self.yVelocity_ = 0
				self.food_ -= 5
				self.colony_.IncreaseFood(5)
				self.colony_.UpdateKnownFoodSources(self.target_)
				self.knownFoodSources_ = self.colony_.GetKnownFoodSources()
			else: #move towards the colony
				xDifference = self.colony_.GetXPos() - self.xPos_
				yDifference = self.colony_.GetYPos() - self.yPos_
						
				total = 0
				if xDifference < 0: total += xDifference * -1 
				else: total += xDifference
				if yDifference < 0: total += yDifference * -1 
				else: total += yDifference
						
				if xDifference != 0: self.xVelocity_ = (xDifference / total) * self.speed_ 
				if yDifference != 0: self.yVelocity_ = (yDifference / total) * self.speed_ 
		
		
		#make sure the ant stays within the boundary of the window.
		if self.xPos_ + self.xVelocity_ < 0 or self.xPos_ + (self.size_ / 2) + self.xVelocity_ > 800:
			self.xVelocity_ = 0
			
		if self.yPos_ + self.yVelocity_ < 0 or self.yPos_ + (self.size_ / 2) + self.yVelocity_ > 600:
			self.yVelocity_ = 0
		
		canvas.move(self.canvasObject_, self.xVelocity_, self.yVelocity_)
		self.xPos_ += self.xVelocity_
		self.yPos_ += self.yVelocity_
		self.age_ += 1
	
	#apple has to be within the ant's scent range.
	def GetClosestApple(self, apples):
		closestApple = None
		
		if len(self.knownFoodSources_) != 0: #select from known food sources first
			for (f, food) in enumerate(self.knownFoodSources_):
				if self.knownFoodSources_[f].GetFood() != 0: 
					if closestApple == None:
							closestApple = self.knownFoodSources_[f]
					else:
						if self.GetDistanceFrom(self.knownFoodSources_[f]) < self.GetDistanceFrom(closestApple):
							closestApple = self.knownFoodSources_[f]
		else: #if no food sources are known, try to smell one that's nearby
			for a in range(0, len(apples)):
				if self.GetDistanceFrom(apples[a]) <= self.scentRange_:
					if closestApple == None or self.GetDistanceFrom(apples[a]) < self.GetDistanceFrom(closestApple):
						closestApple = apples[a]
		
		return closestApple
		
	def GetDistanceFrom(self, apple):
		xDist = self.GetDifference(self.xPos_, apple.GetXPos())
		yDist = self.GetDifference(self.yPos_, apple.GetYPos()) 
		distance = math.sqrt((xDist**2) + (yDist**2))
		return distance
		
	def GetDifference(self, value1, value2):
		difference = value1 - value2
		
		if difference < 0:
			difference *= -1
		
		return difference
		
	def IsColliding(self, circularObject):
		selfRadius = self.size_ / 2
		circularObjectRadius = circularObject.GetSize() / 2
		distanceBetween = self.GetDistanceFrom(circularObject)
		
		if distanceBetween <= selfRadius + circularObjectRadius:
			return True
		
		return False
	
	def RemoveFromKnownFoodSources(self, foodSource):
		for (f, food) in enumerate(self.knownFoodSources_):
			if self.knownFoodSources_[f] == foodSource:
				del self.knownFoodSources_[f]
				
				
	
	
	
	