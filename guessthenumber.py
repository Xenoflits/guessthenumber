import random
#global variables
answer = 0
attempts = 0
difficulty = ""
game_end = 0
attempts = 0
#functions
def choose_difficulty():
    global difficulty
    global attempts
    difficulty = input("Do you want easy or hard mode easy/hard?")
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    
def choose_number():
    return random.randint(1,100)        

#initial setup    
while difficulty !="easy" and difficulty != "hard":
    print (difficulty)
    choose_difficulty()

number = choose_number()


while game_end == 0:
    print(f"{difficulty} - attempts left = {attempts} \n")
    x = int(input("choose your number"))
    if x == number:
        print("you win")
        game_end == 1
    elif x>number:
        print("to high \n") 
        attempts -= 1
        if attempts == 0:
            game_end = 1
    elif x<number:
        print("to low \n")
        attempts -= 1
        if attempts == 0:
            game_end = 1
        
print("you lose")