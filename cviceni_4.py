veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'

# Samohlásky & souhlásky
samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'

# Slovník s evidencí výskytu jednotlivých typů písmen
vysledek = {'souhlasky': 0, 'samohlasky': 0}

# Iterace přes zadanou proměnnou 'veta'
for pismeno in veta:
    # .. pokud znak není písmeno
    if not pismeno.isalpha():
        continue

    # .. pokud je převedený znak mezi hodnotami samohlásek
    elif pismeno.lower() in samohlasky:
        vysledek['samohlasky'] += 1
    # .. pokud je převedený znak mezi hodnotami souhlásek
    elif pismeno.lower() in souhlasky:
        vysledek['souhlasky'] += 1

# Vypiš závěrečný výstup v podobě celkového počtu samohlásek a souhlásek
print('Počet souhlásek:', vysledek['souhlasky'], '| Počet samohlásek:', vysledek['samohlasky'])

cisla = [1, 2, 3, 4, 5, 6, 7, 8]
licha = 0
suda= 0

for cislo in cisla:
    if cislo % 2 == 0:
        suda = suda + cislo
    else:
        licha = licha + cislo

vysledek = abs(suda - licha)
print('Rozdíl je:', vysledek)
cisla = [1, 2, 3, 4, 5, 6, 7, 8]

vysledek = []

# Zadané hodnoty: počáteční hodn., konečná hodn., dělitel
start = 3
stop = 9
delitel = 3

if isinstance(start, int) \
        and isinstance(stop, int) \
        and isinstance(delitel, int):
    print("Zadaný rozsah: <", start, ", ", stop, ">", sep="")

    # Iteruj skrze rozsah zadaných čísel
    for number in range(start, stop + 1):
        # .. pokud je vybrané číslo dělitelné hodnotou v prom. "delitel"
        if number % int(delitel) == 0:
            # .. přidej jej do seznamu "vysledek"
            vysledek.append(number)
    # doplň výpis hodnot v proměnné 'vysledek'
    print('Čísla dělitelná', delitel, ':', vysledek)

else:
    print("Zadané vstupy musí být čísla.")


seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]

# Dict comprehension
delky_slov = {slovo: len(slovo) for slovo in seznam_slov}

# Vypsaný výstup
print(delky_slov)

index = 1

while index <= 6:
   print("index:", index)
   # Pokud je index 4 vypiš a ukonči smyčku 
   if index == 4:
       print("Mám hodnotu 4")
       break
   index = index + 1

index = 0

while index <= 19:
   index = index + 1
   # pokud je aktuální hodnota proměnné sudá, 
   # pokračuj dále(přeskoč ji)
   if index % 2 == 0:
     continue
   print("index:", index)

index = 0

while index < 6:
   print("index:", index)
   index = index + 1

# vypíše se po ukončení smyčky
else:
   print("index:", index, "--> hodnoty jsou si rovny, ukončuji smyčku..")

print("Pokračuji..")

dotazovani = True

while dotazovani:
   odpoved = input("Zadej celé číslo od 1 do 5")

   if odpoved.isnumeric() and int(odpoved) in range(1, 6):
       print("Výborně")
       dotazovani = False
   else:
       print("Špatná hodnota, zkus to znovu")