'''Card Class

   responsibility: to hold and display the card value

   attributes: value (integer, a random number between 1 and 13)

   methods: get_value (returns the value of the card)

'''
class Card: 
          value: [“1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “10”, “11”, “12”, “13”,]
      def __init__(self, value):
         sef.value= value 
      def __str__(self):
         return f”{Card.value[self.value]}”

class Card:

   def __init__(self):
      self.value = random.randint(1, 13)
   
   def get_value(self):
         return self.value
