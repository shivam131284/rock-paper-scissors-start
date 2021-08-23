import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock , paper , scissors]

print("welcome to rock paper scissors")

user_choice = int(input("what no. do you chose 0 for rock , 1 for scisssors and 2 for paper \n"))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("the computer chose:")
print(game_images[computer_choice])

if user_choice == 0 and  computer_choice== 2:
  print("you lose !!")
elif user_choice < computer_choice:
  print("you win !")
elif user_choice == computer_choice:
  print("tied")
elif user_choice == 2 and computer_choice == 0:
  print("you win!!")
else:
  print("you typed an invalid no. you lose!!!")