#1 create skeletons for different functions
def new_game():

#5 guesses or options on questions
    guesses = []
    correct_guesses = 0
    question_num = 1

#6 need to display questions in dictionary of questions
    for key in questions:
        print(key)

#7 list options for the first questions
        for i in options[question_num-1]:
            print(i)

#9 prompt user choose
        guess = input("Enter (A, B, C, or D):  ")

#10 put answers uppercase
        guess = guess.upper()

#11 append/ compare guess answers to our answer and so append is needed
        guesses.append(guess)

#12 check the answer/ call the function  / pass the key function or right answer
        correct_guesses += check_answer(questions.get(key), guess)

#8 will display everything for one question by one / increment the questions by one
        question_num += 1

#15 display a final score/ that will pass guesses which are correct guesses and list of guesses
    display_score(correct_guesses, guesses)

#13 to get the answer/ create parameters
def check_answer(answer,guess):

#14 the function to check whether you answer is correct or not
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

#16 guesses and correct guesses/ print the results
def  display_score(correct_guesses, guesses):
    print("-----------")
    print("results")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="  ")
    print()

#17 Guesses are the same
    print("Guesses:  ", end="  ")
    for i in guesses:
        print(i, end="  ")
    print()

#18 display the scores to be shown/ this will give the percentage
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False




#2  dictionaries of questions and Answers or you can see an associated value
questions  =  {
    "What's the capital city of The Bahamas?: ": "A",
    "Which country do Bahamians tend to go to study?: ": "B",
    "Which computer programming language are we are learning now?: ": "D",
    "The day of the independence of The Bahamas: ": "B"
    }
#3 options this is a list of a list
options = [["A. New Providence", "B. Toronto", "C.Washington DC", "D.Seoul"],
           ["A.Haiti", "B.Canada", "C.Brazil", "D.England"],
           ["A.Java programming", "B.Ruby on Rails", "C.Javascript", "D.Python"],
           ["A.july 10 1963", "B.july 10 1973", "C.August 4 1995", "D. january 1 1804"]]

#4  calling a new game function to begin a new game
new_game()

while play_again():
    new_game()
print("Bye")