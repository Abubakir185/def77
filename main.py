# 1

dostlar_soni = int(input("Nechta dost qoshmoqchisiz: "))

friends = {}

def create_friend(name, age):
    friends[name] = age

for i in range(dostlar_soni):
    name = input(f"{i + 1} - Dostingizni ismini kiriting: ")
    age = int(input(f"{i + 1} - Dostingizni yoshini kiriting:"))
    create_friend(name, age)

print(friends)


# 2

sonlar_soni = int(input("Sonlar soni: ")) 

sonlar = []

def add_to_list(son):
    sonlar.append(son)

for i in range(sonlar_soni): 
    son = int(input(f"{i + 1} - son: "))
    add_to_list(son)

print(sonlar)
print(sum(sonlar))


# 3


sonlar_soni = int(input("Sonlar soni: ")) 

sonlar = []


def add_to_list(son):
    if son not in sonlar:
        sonlar.append(son)
    


for i in range(sonlar_soni): 
    son = int(input(f"{i + 1} - son: "))
    add_to_list(son)



