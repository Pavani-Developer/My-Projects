import random
def guessing_game():
    answer=random.randint(0,100)
    print(answer)
    
    while True:
      try:
       user_input=int(input("Enter your guess Between 0 to 100:"))
      except:
       print("Enter a valid input")
       continue
       
      if user_input==answer:
          print(f"Just right The correct answer is {answer}")
          break
        
      if user_input>answer:
          print(f"Your guess of {user_input} is too high")
        
      else:
          print(f"Your guess of {user_input} is too low")
      
guessing_game()