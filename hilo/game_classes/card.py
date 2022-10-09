import random

'''Card Class

   responsibility: to hold and display the card value

   attributes: value (integer, a random number between 1 and 13)

   methods: get_value (returns the value of the card)

'''
class Card:

   def __init__(self):
      self.value = random.randint(1, 13)
   
   def get_value(self):
         return self.value

