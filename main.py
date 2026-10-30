import random
attempts=[]

def show():
    if len (attempts)<=0:
       print("Currently no high score.")
    else:
        print("The current highest score is {} attempts".format(min(attempts)))

def start():
    random_number=int(random.randint(1,10))
    print("Welcome to the number guessing game!!!")
    name=input("Enter your name:")
    play=input("Hi, {} , would you like to play the number guessing game?(Enter yes/no)".format(name))
    a=0
    show()
    while play.lower()=="yes":
        try:
            guess=input("Pick a number between 1 and 10")
            if int(guess)<1 or int(guess)>10:
                raise ValueError("please guess number within valid range.")

            if int(guess)==random_number:
                print("Congrats you got it right!")
                a=a+1
                attempts.append(a)
                print("No of attempts={}".format(a))
                break
            elif int(guess)<random_number:
                print("Its lower.")
                a=a+1
            elif int(guess)>random_number:
                print("Its higher.")
                a=a+1
        except ValueError as err:
            print("Try again....")
            print("({})".format(err))

    else:
        print("GET OUT NOW!!!Run away while you can. I know where you live.....")
if __name__=="__main__":
    start()