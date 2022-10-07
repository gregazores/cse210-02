

''' Player Class

    responsibility: to collect and hold player guess, hold and display player points
    
    attributes: guess (an integer)
                points (an integer, starts at 300 and updates based on guess compared to card
                       relationship)
    
    methods: input (collect the player's guess, convert to integer, stores  
             internally as attribute guess)
             update_points (compare guess to card relationship takes the argument
                of a list of two card objects)
             display_points (display the new updated points)
             
'''
class Player:
   def __init__(self):
      self.guess = True
      self.points = 300
      self.isCorrect = 1
      self.isCorrect = 1

   def input(self):  
      self.guess = player_response()

   def update_points(self, card_data):
      #extracts the values of card_data
      #if user guess correctly gets 100 points
      #if guess incorrect minus 75 points
      card1 = card_data[0].value
      card2 = card_data[1].value
      if self.guess and card1 < card2:
         self.points += 100
         self.isCorrect = 1
      elif self.guess != True and card1 > card2:
         self.points += 100
         self.isCorrect = 1
      else:
         self.points -= 75
         self.isCorrect = 2

   def display_points(self):
      print(f'Your score is: {self.points}')


def player_response():
   #call the validate input function and will only accept h or l for an answer
   return validate_input("Higher or lower? [h/l] ", ['h', 'l']) == "h"

def validate_input(questions, correct_answers):
   while True:
      user_input = input(questions).lower()

      if user_input in correct_answers:
         return user_input
      else:
         print(f"Please, answer only with {correct_answers[0]} or {correct_answers[1]}, thank you!")







"""
def player_response():
   #input validation program will only accept h or l for an answer
   while True:
      user_input = input("Higher or lower? [h/l] ").lower()

      if user_input == "h" or user_input == "l":
         return user_input == "h"
      else:
         print("Please answer with only 'h' for high and 'l' for low. Thank you!")




      if self.guess and card_data[0] < card_data[1]:
         self.points += 100
      else:
         self.points -= 100


y = Player()
z = y.input()
print(y.guess)
y.update_points(card_data)
print(y.points)
self.points = check_score(self.points, card_data)
def check_score(points, card);
   if 

y = Player()
z = y.input()

print(y.guess)

 """