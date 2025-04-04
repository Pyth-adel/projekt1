"""
main.py: projekt textového analyzátoru do Engeto Online Python Akademie

author: Adéla Bestová
email: adelka.bestova@seznam.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive topographic feature that rises sharply
some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet
above sea level. The butte is located just north of US 30 and the Union Pacific Railroad,
which traverse the valley.''',
    '''At the base of Fossil Butte are the bright red, purple, yellow and gray beds
of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually
upward from the valley floor and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper buff-to-white beds of the Green River
Formation, which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects a portion of the largest deposit
of freshwater fish fossils in the world. The richest fossil fish deposits are found
in multiple limestone layers, which lie some 100 feet below the top of the butte.
The fossils represent several varieties of perch, as well as other freshwater genera
and herring similar to those in modern oceans. Other fish such as paddlefish, garpike
and stingray are also present.'''
]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

print("=" * 40)
username = input("username: ")
password = input("password: ")

if users.get(username) != password:
    print("unregistered user, terminating the program..")
    exit()
else:
    print(f"\nWelcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("=" * 40)

selection = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")

if not selection.isdigit() or int(selection) not in range(1, len(TEXTS)+1):
    print("Invalid input, terminating the program.")
    exit()

selected_text = TEXTS[int(selection) - 1]

words = [word.strip(".,:;!?") for word in selected_text.split()]

word_count = len(words)
titlecase_count = sum(word.istitle() for word in words)
uppercase_count = sum(word.isupper() and word.isalpha() for word in words)
lowercase_count = sum(word.islower() for word in words)
numeric_count = sum(word.isdigit() for word in words)
numeric_sum = sum(int(word) for word in words if word.isdigit())

print("=" * 40)
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}")
print("=" * 40)

lengths = {}
for word in words:
    length = len(word)
    lengths[length] = lengths.get(length, 0) + 1

print(f"{'LEN':<3}|{'OCCURENCES':^20}|{'NR.':>3}")
print("-" * 30)
for length in sorted(lengths):
    count = lengths[length]
    print(f"{length:<3}|{'*' * count:<20}|{count:>3}")
