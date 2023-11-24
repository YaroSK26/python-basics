# input umožňuje zadání čehokoliv od uživatele
print("Ahoj, já jsem " + input("Zadejte své jméno\n"))
print(len("David Šetek"))
print("ahoj"[3])

# F-string
x = 5
print(f"Proměnná x má hodnotu: {x}")

result = 25.6789
print(f"The result is {result:.2f}")







print("Vítejte v kalkulátoru na výpočet plateb")
cost = int(input("Kolik máte celkem zaplatit? "))
percentage = int(input("Kolik chcete dát spropitného (v %). "))
people = int(input("Mezi kolik lidí se má rozdělit částka? "))


one_payment = (cost + (cost * percentage / 100)) / people
final_payment = "{:+.2f}".format(one_payment)
print(f"Každý člověk by měl zaplatit {final_payment} Kč")





# BMI
height = float(input("Vložte svou výšku v metrech: "))
weight = float(input("Vložte svou váhu v kg: "))


bmi = weight / (height * height)


if bmi < 18.5:
    print(f"Váš BMI má hodnotu {round(bmi, 1)}, máte podváhu")
elif bmi < 24.9:
    print(f"Váš BMI má hodnotu {round(bmi, 1)}, jste v normálu")
elif bmi < 29.9:
    print(f"Váš BMI má hodnotu {round(bmi, 1)}, máte nadváhu")
elif bmi < 34.9:
    print(f"Váš BMI má hodnotu {round(bmi, 1)}, jste obézní")
else:
    print(f"Váš BMI má hodnotu {round(bmi, 1)}, máte extrémní obezitu")

# modulo
print(6 % 4) #2




print("Vítejte na horské dráze")
height = int(input("Jaká je vaše výška v cm?\n"))
bill = 0
 
if height >= 87:
    print("Můžete jet na horské dráze.")
    age = int(input("Jaká je váš věk?\n"))
    if age < 12:
        bill = 50
        print("Cena vašeho lístku je 50 Kč.")
    elif age >= 12 and age < 18:
        bill = 100
        print("Cena vašeho lístku je 100 Kč.")
    elif age >= 40 and age <= 50:
        bill = 0
    else:
        bill = 150
        print("Cena vašeho lístku je 150 Kč.")
   
    photo = input("Chcete běhemjízdy vyfotit? ano nebo ne\n")
    if photo == "ano":
        bill = bill + 40
        # bill += 40
   
    print(f"Vaše cena je: {bill} Kč")
else:
    print("Omlouváme se, ale na horské dráze jet nemůžete.")





print('''
_                                       _   _            
| |                                     | | | |          
| |__   __ _ _ __ _ __ _   _ _ __   ___ | |_| |_ ___ _ __
| '_ \ / _` | '__| '__| | | | '_ \ / _ \| __| __/ _ \ '__|
| | | | (_| | |  | |  | |_| | |_) | (_) | |_| ||  __/ |  
|_| |_|\__,_|_|  |_|   \__, | .__/ \___/ \__|\__\___|_|  
                        __/ | |                          
                       |___/|_|                          
''')
print("Vítejte v Bradavicích milí studenti")
print("Nyní se vypravíte do svých kolejí")


follow = input("Následovat spolužáky do své nebelvírské koleje? Napište ano nebo ne. ").lower()
if follow == "ano":
    stay = input("Jděte po samohýbajících se schodech společně s ostatními. Došli jste do nebelvírské společenské místnosti. Chcete zde zůstat nebo jít po schodech do své ložnice? Napište schody nebo ložnice. ").lower()
    if stay == "ložnice":
        print("Krásnou kouzelnou noc.")
    else:
        print("Zůstáváte a budete s ostatními ochutnávat kouzelné sladkosti.")
else:
    print("Odpojili jste se od svých spolužáků a stojíte sami na chodbě")
    left_or_right = input("Chcete se vydat doleva nebo doprava? Napište doleva nebo doprava. ").lower()
    if left_or_right == "doleva":
        print("Narazili jste na Filche a ten vás vezme do vaší koleje a pošle vás spát")
    else:
        door = input("Vidíte před sebou dveře na nádvoří. Chcete jít ven? Napište ven nebo zůstat").lower()
        if door == "ven":
            print("Venku je vám zima a raději se vrátíte na svou kolej.")
        else:
            print("Stojíš sám na chodbě a nudíš se. Raději se vrátíš do své koleje.")



import random
import math

# Generování náhodného celého čísla z rozsahu
print(random.randint(10, 18))


# Generování náhodného desetinného čísla mezi 0 a 1
print(random.random())


# Generování náhodného čísla z rozmezí + krok
print(random.randrange(15, 25, 2))


print(math.ceil(5.1))  # 6
print(math.floor(5.8)) # 5

print(math.ceil(random.random() * 6))


side_coin = random.randint(0,1)
if side_coin == 0:
    print("Hlava")
else:
    print("Orel")



# List
employees = ["David", "Harry", "Ron"]
print(employees[0])
print(employees[1])
print(employees[2])


# Mění položku
employees[1] = "Hermiona"
print(employees)


# Přidáváme obsah
employees.append("Harry")
print(employees)


# Přidáváme více položek
employees.extend(["Crabbe, Goyle"])
print(employees)


# Odstraňujeme položku
employees.remove("Ron")
print(employees)


# import random

names = input("Napiš mi jména všech, ale oddělené čárkou\n")


list_people = names.split(", ")
random_number = random.randint(0, len(list_people)-1)


print(f"{list_people[random_number]} bude dnes platit účet.")



# import random
 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
 
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
 
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
all_list = [rock, paper, scissors]


user_choose = int(input("Co si vyberete? Napište 0 pokud kámen, 1 pro papír a 2 pro nůžky\n"))
user_picture = all_list[user_choose]


computer_choose = random.randint(0, 2)
computer_picture = all_list[computer_choose]


print(f"Uživatel si vybral:\n {user_picture}")
print(f"Počítač si vybral:\n {computer_picture}")


if user_choose == computer_choose:
    print("Remíza")
elif user_choose == 0 and computer_choose == 1:
    print("Prohrál jsi, počítač vyhrává")
elif user_choose == 0 and computer_choose == 2:
    print("Vyhrál jsi, počítač prohrává")
elif user_choose == 1 and computer_choose == 0:
    print("Vyhrál jsi, počítač prohrává")
elif user_choose == 1 and computer_choose == 2:
    print("Prohrál jsi, počítač vyhrává")
elif user_choose == 2 and computer_choose == 0:
    print("Prohrál jsi, počítač vyhrává")
elif user_choose == 2 and computer_choose == 1:
    print("Vyhrál jsi, počítač prohrává")



ovoce = ["jablko", "hruška", "pomeranč", "jahoda"]


for jedno_ovoce in ovoce:
    print(jedno_ovoce)
    print(f"Nezapomeň koupit {jedno_ovoce}")






import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']


print("Generátor hesel")
num_letters = int(input("Kolik písmen chcete mít ve svém heslu?\n"))
num_numbers = int(input("Kolik čísel chcete mít ve svém heslu?\n"))
num_special_char = int(input("Kolik speciálních znaků chcete mít ve svém heslu?\n"))


# Písmena, čísla a speciální znaky se kterými budeme pracovat
result2 = []


for index in range(0, num_letters):
    random_number = random.randint(0, len(letters)-1)
    result2.append(letters[random_number])


for index in range(0, num_numbers):
    random_number = random.randint(0, len(numbers)-1)
    result2.append(numbers[random_number])


for index in range(0, num_special_char):
    random_number = random.randint(0, len(special_char)-1)
    result2.append(special_char[random_number])
print(result)
# Přeskupení

random.shuffle(result2)
print(result)


# Převod listu na string
result_password = ""


for one_character in result2:
    # result_password = result_password + one_character
    result_password += one_character


print(result_password)



# cyklus While
x = 0


while x <= 10:
    print(f"Já jsem {x} cyklus while")
    # x = x + 1
    x += 1


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



# Hangman
import random


# Uvítání a pravidla hry
print("Vítejte ve hře hádání postav z filmu Harry Potter. Vaším úkolem je...")


# Generování náhodného slova
words = ["harry", "ronald", "albus", "hermiona"]
random_word = words[random.randint(0, 3)]


# Generování podtržítek
hidden_word = []
for one_letter in random_word:
    hidden_word.append("_")


# Životy
lives = 6
print(stages[lives])


# vypsání slova s podtržítky v normální podobě
printedWord = ""
for one_letter in hidden_word:
    printedWord += one_letter
print(printedWord)


while "_" in hidden_word:
    guess = input("Zadejte hádané písmeno\n").lower()
    for index in range(0, len(random_word)):
        if guess == random_word[index]:
            hidden_word[index] = guess


    # kontrola životů
    if guess not in random_word:
        lives -= 1
        print(stages[lives])
    print(f"Počet vašich životů je {lives}")
    if lives == 0:
        print("Prohráli jste")
        break


    # vypsání slova s podtržítky v normální podobě
    printedWord = ""
    for one_letter in hidden_word:
        printedWord += one_letter
    print(printedWord)


    # kontrola vítězství
    if "_" not in hidden_word:
        print("Vyhráli jste!!!")



it_dictionary = {
    "Integer": "Celé číslo",
    "String": "Text",
    "Float": "Desetinné číslo",
    "Boolean": "Pravda nepravda"
}


print(it_dictionary["String"])



logo = """
 _____                     _                                          
|  __ \                   (_)                                        
| |  \/_   _  ___  ___ ___ _ _ __   __ _    __ _  __ _ _ __ ___   ___
| | __| | | |/ _ \/ __/ __| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ \\
| |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | (_| | (_| | | | | | |  __/
 \____/\__,_|\___||___/___/_|_| |_|\__, |  \__, |\__,_|_| |_| |_|\___|
                                    __/ |   __/ |                    
                                   |___/   |___/                      
"""


import random
import os


# Úvodní informace
print(logo)
print("Vítejte ve hře guess secret number. Porazte počítač.")
print("Myslím si číslo od 1 do 100")


# Příprava hry
secret_number = random.randint(1, 100)
print(f"Hádané číslo je {secret_number}")




def difficulty():
  difficulty = input("Vyberte obtížnost. Napište 'easy' nebo 'hard': ")
  if difficulty == "easy":
    return 10
  elif difficulty == "hard":
    return 5


# Počet pokusů
def guessing_game():
 
  attemps = difficulty()
 
  another_game = ""  


  while attemps > 0:
    print(f"Váš počet zbývajících pokusů je {attemps}")
    guess = int(input("Typněte si číslo: "))
   
    if guess < secret_number:
      print("Příliš nízké")
      attemps -= 1
    elif guess > secret_number:
      print("Příliš vysoké")
      attemps -= 1
    else:
      print("Vyhráli jste. Počítač poražen!")
      another_game = input("Napište 'yes', pokud chcete pokračovat. Napište 'no', pokud chcete hru ukončit")
   
    if attemps == 0:
      print("Prohráli jste. Počítač vyhrál!")
      another_game = input("Napište 'yes', pokud chcete pokračovat. Napište 'no', pokud chcete hru ukončit")
   
    if another_game == "yes":
      os.system("clear")
      guessing_game()
    elif another_game == "no":
      os.system("clear")
      break


guessing_game()
