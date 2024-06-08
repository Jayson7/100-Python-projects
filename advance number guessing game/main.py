import sqlite3
from random import randint

# Database setup
def create_table():
    conn = sqlite3.connect('guesser.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scores
                 (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)''')
    conn.commit()
    conn.close()

def insert_score(name, score):
    conn = sqlite3.connect('guesser.db')
    c = conn.cursor()
    c.execute('INSERT INTO scores (name, score) VALUES (?, ?)', (name, score))
    conn.commit()
    conn.close()

def get_high_scores():
    conn = sqlite3.connect('guesser.db')
    c = conn.cursor()
    c.execute('SELECT name, score FROM scores ORDER BY score DESC LIMIT 5')
    scores = c.fetchall()
    conn.close()
    return scores

# Game setup
def greeter():
    print('Welcome to the ultimate guesser \n')
    global user 
    user = input('Your name: ')
    print('\nHello', user)
    print('So here is how it works, \n you have five trials to get a single guess right, each guess carries 10 marks')

def guesser():
    greeter()
    print("###############  Shall We ##############")
    
    score = 0
    for trial in range(1, 6):
        try:
            answer = randint(1, 20)
            guess = int(input(f'Guess your number {trial} within the range of 1 and 20: '))
            
            if guess == answer:
                print(f'Congratulations! You guessed it right. The answer was {answer}.')
                score += 10
            else:
                print(f'Sorry, the correct answer was {answer}.')
        except ValueError:
            print('Invalid input! Please enter a number.')
    
    print(f'Game over! Your total score is {score} points.')
    insert_score(user, score)

def show_high_scores():
    high_scores = get_high_scores()
    if high_scores:
        print('Top 5 High Scores:')
        for i, (name, score) in enumerate(high_scores, 1):
            print(f'{i}. {name} - {score} points')
    else:
        print('No high scores yet. Be the first to set one!')

def main():
    create_table()
    show_high_scores()
    guesser()

if __name__ == '__main__':
    main()
