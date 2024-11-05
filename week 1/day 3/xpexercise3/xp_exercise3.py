#Exercse 1
keys=['Ten', 'Twenty', 'Thirty']
values=[10, 20, 30]
my_dicitionary=dict(zip(keys,values))
print(my_dicitionary)

#Exercise 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
in_cost=0

for age in family.values():
    if age <3:
        cost=0
    elif 3<= age <=12:
        cost=10
    else:
        cost=15
    in_cost+=cost

print(f"The total cost is {in_cost}")

family_name=input("Input the names of all family memebres seperated by space").split()
family_age=input("Input the ages of all the family memebers seperated by space").split()

for age in family_age:
    if int(age)>3:
        cost=0
    elif 3 <= int(age) <=12:
        cost=10
    else:
        cost=15
    in_cost+=cost

print(dict(zip(family_name,family_age)))
print(f"The total cost is {in_cost}")

#Exercise 3
brand={'name':'Zara',
       'creation_date':'1975',
       'creator_name':'Amancio Ortega Gaona ',
       'type_of_clothes':['men','women','children','home'],
       'international_competitors':['Gap','H&M','Benetton'],
       'number_stores': 7000,
       'major_color':{'France':'blue',
                      'Spain':'red',
                      'US':['pink','green']}
       }

brand['number_stores']=2
print('Zara clients are', ', '.join(brand['type_of_clothes']))

brand['country_creation']='Spain'

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')



brand.pop('creation_date')
print(brand)
print(brand['international_competitors'][-1])
#major clothe colors in the us
print(brand['major_color']['US'])
keypairs=len(brand) + len(brand['major_color'])
#print(keypairs)

#print(brand.keys())

more_on_brand={'creation_date':1975, 'number_stores':10000}

zara={**brand,**more_on_brand}
print(zara)

print(zara['number_stores'])

#Exercise 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
on={}
number=0
on2={}
number2=0
number3=0
on3={}
for i in users:
    on[i]=number
    number+=1

print(on)

for i in users:
    on2[number2]=i
    number2+=1

print(on2)

for i in sorted(users):
    on3[i]=number3
    number3+=1

print(on3)

characters_i=[]
characters_m_p=[]

for name in users:
    if 'i' in name.lower():
        characters_i.append(name)
    if name[0].lower() in ['m', 'p']:
        characters_m_p.append(name)

print(characters_i)
print(characters_m_p)



