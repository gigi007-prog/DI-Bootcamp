#Exercise 1
def display_message():
    print("I am learning programing and full stack development")

display_message()

#Exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Throne of glass")

#Exercise 3
def describe_city(city, country="Georgia"):
    print(f"{city} is in {country}")

describe_city("Tbilisi","Georgia")
describe_city("Krakow")

#Exercise 4
import random  
def random_num(number):
    correct_random_num = random.randint(0, 99)

    if number == correct_random_num:
        print(f'Our number was {correct_random_num}, you chose {number}.\nYou input the exact correct value!')
    else:
        num_difference = abs(correct_random_num - number)

        print(f'Our number was {correct_random_num}, you chose {number}.\nYou input the wrong value and were {num_difference} away.')

random_num(int(input("Input a random number between 1-100: ")))

#Exercise 5 
def make_shirt(size = "l", message = "I love coding in Python"):
    print(f'The size of the shirt is {size} and the message is {message}.')

make_shirt("m")
make_shirt("xxs", '"\'This is nice\' - Borat"')

my_size = "xxs"
shirt_slogan = "YAyyyyyy!"
make_shirt(my_size,shirt_slogan)

#Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    for on in magician_names:
        print(on)

show_magicians()

def make_great():
    for on in range(len(magician_names)):
        magician_names[on] = str(f'The great {magician_names[on]}')
    print(magician_names)

make_great()
show_magicians()

#exercise 7
def get_random_temp(season):
    season = season.lower()

    if season == 'winter':
        return(round(random.uniform(-11,10),2))
    if season == 'spring':
        return(round(random.uniform(5,15),2))
    if season == 'summer':
        return(round(random.uniform(20,36),2))
    if season == 'autumn':
        return(round(random.uniform(5,15),2))

def main():
    user_season = input("What season do you want temperatures on?")
    degrees = get_random_temp(user_season)

    if degrees < 0:
        print('It\'s sooo cold outised:(')
    elif degrees >= 0 and degrees < 16:
        print('Almost like winter in Israel')
    elif degrees >= 16 and degrees < 23:
        print('Were starting to warm upppp')
    elif degrees >= 23 and degrees < 33:
        print('Israel is soooo hot')
    elif degrees >= 33 and degrees < 40:
        print('Gimme a bucket of ice pls')

    print(f'The temprature now is {degrees} degrees Celcius.')

main()

#Exercise 8
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

correct = []
incorrect = []

def questionnaire():
    global correct, incorrect
    correct = []
    incorrect = []
    
    for on in data:
        user_answer = input(on["question"] + " ").lower()
        if user_answer == on["answer"].lower():
            correct.append(on)
        else:
            incorrect.append(on)

    print(f"\nQuiz finished!\nTotal Correct: {len(correct)}\nTotal Incorrect: {len(incorrect)}")
    
    check_score()

def check_score():
    if len(incorrect) > 3:
        print('You got more than three incorrect answers, try again.')
        questionnaire()
    else:
        print("Thanks for participating! You did amazing.")

questionnaire()




