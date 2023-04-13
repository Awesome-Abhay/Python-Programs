# secret word game.
import os
os.system("cls")
secret_word= input("Enter the secret word:- ")
guess_limit= int(input("Enter the guess limit:- "))
guess_count= 0
out_of_guesses= False
i=" "
while i!=secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        if i!=" ":
            print("Sorry! better guess next time. Try Again.")
        i=input("enter the guess:- ")
        if i==secret_word:
            print("You win")
            break
        guess_count+= 1
    else:
        out_of_guesses= True
if out_of_guesses:
    print("Limit exceeded. YOU LOOSE!")
