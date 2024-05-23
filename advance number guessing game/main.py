from random import randint

def greeter():
    print('Welcome to the ultimate guesser \n ')
    global user 
    user = input('Your name:  ')
    print('\nHello', user)
    print('So here is how it works, \n you have five trials to get a single guess right, each guess carries 10 marks')


def guesser():

    greeter()
    print("###############  Shall We ##############")
    
    
    
    try:
        answer1=randint(1, 20)
        guess_question_1 = input('Guess your first number within the range of 1 and 20: ')

        if guess_question_1 == int(answer1):
            pass 
    except:
        print('Thats terribl from you, try again')

def score_checker():
    pass


guesser()



