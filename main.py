"""
This program was created under the premise that insects are nothing more than biological machines, living by executing a certain set of instructions because they lack the 
mental capability for anything else. I figured that if this were true, I should be able to program them, and I wanted to see how close I could get to their actual behaviour. 

HOW IT WORKS:
Ants can smell nearby food. If there is no food nearby, they wander around pseudo-arbitrarily until they find a source of food. Once the ant returns the food, that food source is remembered 
and used by the rest of the colony.

This program has a lot of bugs (hah) but only one of them is worth noting: sometimes, when the colony's known food sources list is updated with a new food source, ants that aren't at the 
colony somehow obtain that information and start moving toward it.

2015.06.08
"""

from Lawn import *

root = Tk()
lawn = Lawn(root)
lawn.Tick()
lawn.mainloop()