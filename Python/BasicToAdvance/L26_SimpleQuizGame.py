# Q1. Simple Create a Quiz Game. 

def new_game():
    guesses =[]
    correct_guesses = 0
    question_num = 1

    for key in questions: 
        print("---------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses+= check_answer(questions.get(key),guess)
        question_num +=1

    display_score(correct_guesses,guesses)


#..........................................
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else: 
        print("WRONG")
        return 0

#.....................................................


def display_score(correct_guesses, guesses):
    print("-------------------")
    print("RESULT")
    print("-------------------")

   
    print("Answer: ", end =" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    
    print("Guesses: ", end=" ")
    for i in guesses: 
        print(i, end =" ")
    print()


    score= int((correct_guesses/len(questions)) *100)
    print("You Score is : "+ str(score)+"%")  
#............................................

#............................................
def play_again():
    reponse = input("Do you want to play again ? (Yes or No ): ")
    reponse = reponse.upper()   

    if reponse == "YES":
        return True
    else:
        return False

questions = {
    "Who Created Python ?": "A",
    "What year was Python created?:" : "B",
    "Python is tributed to Which comedy group? :":"C",
    "Is the Earth Round ?" : "A" 
}

options = [["A. Guido Van Rossum", "B.Elon Musk", "C Bill Gates", "D Mark Zukarburg"], 
            ["A. 1989", "B. 1990", "C. 1991","D.1992"],
            ["A. Lonely Island", "B. Smosh","C. Monty Python","D.SNL"],
            ["A. True", "B. False", "C. Sometime","D . Nothing"] 
]

new_game()

while play_again():
    new_game()

print("Bye.............!!")
