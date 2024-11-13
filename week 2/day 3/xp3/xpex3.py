#Exercise 1
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __add__(self, other):
#         if isinstance(other, (int, float)):
#             return Currency(self.currency, self.amount + other)
#         elif isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             return Currency(self.currency, self.amount + other.amount)
#         raise TypeError("Unsupported type for addition with Currency")

#     def __iadd__(self, other):
#         if isinstance(other, (int, float)):
#             self.amount += other
#         elif isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             self.amount += other.amount
#         else:
#             raise TypeError("Unsupported type for in-place addition with Currency")
#         return self

#     def __str__(self):
#         return f"{self.amount} {self.currency}"

#     def __int__(self):
#         return self.amount

# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# print(str(c1))  
# print(int(c1)) 
# print(c1 + 5)  
# c1 += 5
# print(c1)


#Exercise 3
import random
import string

def generate_random_string(length=5):
    letters = string.ascii_letters  
    random_string = ''.join(random.choice(letters) for _ in range(length))
    
    return random_string

random_string = generate_random_string(10)
print(random_string)

#Exercise 4
import datetime
def current_date():
    current_date = datetime.date.today()
    print("Today is :", current_date)


current_date()

#Exercise 5
import datetime

def time_until_new_year():
    current_time = datetime.datetime.now()
    current_year = current_time.year
    new_year = datetime.datetime(current_year + 1, 1, 1)
    time_difference = new_year - current_time
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(f"The 1st of January is in {days} days, {hours:02d}:{minutes:02d}:{seconds:02d} hours.")

time_until_new_year()


#Exercise 6
import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
    current_time = datetime.datetime.now()
    time_difference = current_time - birthdate
    total_minutes = time_difference.total_seconds() / 60
    print(f"You have lived for {int(total_minutes)} minutes.")

birthdate_input = "2006-04-19"  
minutes_lived(birthdate_input)

#Exercise 7

