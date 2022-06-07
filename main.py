#Step 2

import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
  display.append("_")

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
end_of_game = False
life = 6
while(not end_of_game):
  guess = input("Guess a letter: ").lower()
  if guess in display:
   print(f"{guess} is already in word")
   life -=1
   print(stages[life])
  for i in range(0, len(chosen_word)):
    if chosen_word[i] == guess:
      display[i]  = guess
  print(display)

  if guess not in chosen_word:
        print(stages[life])
        life -= 1
        if life == 0:
          print(stages[life])
          print("You loose a game")
          end_of_game = True
  if "_" not in display:
    end_of_game = True
    print("You won a game")
    print(f"solution is:  {' '.join(display)}")
      

