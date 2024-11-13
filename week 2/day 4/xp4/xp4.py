#Exercise 1
import random
def get_words_from_file(filename):
    try:
        with open(filename, 'r') as file:
            words = [line.strip().lower() for line in file.readlines()]
        return words
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        exit(1)

def get_random_sentence(length, word_list):
    return ' '.join(random.choice(word_list) for _ in range(length))

def main():
    print("Welcome to the Random Sentence Generator!")
    print("This program will generate a random sentence using a list of words.")
    
    while True:
        try:
            length = int(input("How long do you want the sentence to be? (between 2 and 20): "))
            if 2 <= length <= 20:
                break
            else:
                print("Error: Please enter a number between 2 and 20.")
        except ValueError:
            print("Error: Please enter a valid integer.")

    # Get words from the 'txtxp4.txt' 
    words = get_words_from_file('txtxp4.txt')  
    sentence = get_random_sentence(length, words)
    print("Generated Sentence:", sentence)
if __name__ == "__main__":
    main()



#Exercise 2
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"Gigi",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

salary = data["company"]["employee"]["payable"]["salary"]
print(f"Salary: {salary}")

data["company"]["employee"]["birth_date"] = "2006-04-19"
with open("modified_employee.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

changed_json = json.dumps(data, indent=4)
print(changed_json)
