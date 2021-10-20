# ALU Hangman


# ask the user to enter the Nickname to use in game
def username():
    name = input(" what is your name:")
    print("hello", name, " welcome to the quiz")

def quest_answer():
    score = 0                       # this is for calculating scores and number of win questions as you get one point for correct answer
    incorrect = 0                    # this is for calculating number of loses

    for i in Questions:              # this is for defining any input answer in Questions and answers set
        print(i)
        answer = input("enter your answer")       # this is for imput the answer
        if answer.upper() == Questions[i]:        # this is for turning the answer into upper as writen in the program
            score = score + 1
            print("correct,you score is", score)


        else:
            incorrect = incorrect + 1   #this for counting number of looses
            print("you are hanging the man, your score is: ", score)

            if incorrect == 6:                          # if the wrong or incorrect answers equal 6
                print(" man dies!!!\n thank you for playing, \n your final score is : ", score, " you win ", score,
                      "question(s) and you loose ", incorrect, "question(s)")


                break            # this for braking if the user loose six questions

    if score == 10:           # this for when player maximize the game
        print("Congratirations, your man lives! the game is over")

    elif incorrect < 6:                # if the player loose less than six questions
        print("your man is alive, game is over")
        print("thank you for playing, \n your final score is : ", score," you wins ",score, "questions and you loose ",incorrect,"questions")

def try_again():         # this is for defining to have an other trial

    response = input("Would you like to play again?\n"
                     "If yes enter 'yes', if not enter 'no' to quit:\n")

    if response.lower() == "yes":         # this for when the user want to pray again
        print("Here is the ALU hanging man again")
        return True                                       # this for returning the game


    elif response.lower() == "no":     #this for quitting the game
        print("thank you playing")
        return False                # this for not returning the game


    else:          # this for when user entered invalid or undefined value
         print("**Invalid input please enter 'yes' if you want to play again\n or 'no' if you would like to quit game**\n")

# questions

q1= """ 1.When was ALU founded?"""
q2= """2.Who is the CEO of ALU? """
q3= """3.Where are ALU campuses? (use comma to separate """
q4= """4.How many campuses does ALU have?"""
q5= """5.What is the name of ALU Rwanda’s Dean?"""
q6= """6.Who is in charge of Student Life?"""
q7= """7.What is the name of our Lab?"""
q8= """8.How many students do we have in Year 2 CS?"""
q9= """9.How many degrees does ALU offer?"""
q10= """10.Where are the headquarters of ALU ?"""

# set of matching questions with its answer
Questions ={q1:"2015", q2:"FRED SWANIKER" or "SWANIKER FRED", q3:"RWANDA,MAURITIUS" or "MAURITIUS,RWANDA ", q4:"2", q5:"SUNASSEE VEDA" or "VEDA SUNASSEE" , q6:"SILA OGIDI" or "OGIDI SILA", q7:"FAB LAB",q8:"90", q9:"8",q10:"MAURITIUS" }


# calling functions
username()
quest_answer()
while try_again():
      quest_answer()

