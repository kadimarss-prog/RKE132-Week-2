# git init
# git add .
# git status
# git commit -m "Message"
# git remote add origin => Link githubi repositist nt git remote add origin https://github.com/kadimarss-prog/RKE151-Week-2.git
# git push -u origin master


"""mis päev on homme (töö või puhkus) ning väljastab sisu
Kui tööpäev = "Lähen magama, head ööd"
Kui puhkepäev= "Veel üks osa netflix
"""


""" day = input("Mis päev on homme? (tööpäev või puhkepäev):")

if day =="tööpäev": 
    print("Mine magama, head ööd")
elif day == "puhkepäev":
    print("Vaata veel üks osa netflixi")
else: 
    print("Vale väärtus") """



""" #finantsnõustaja
#osta uus iphone või mitte
print("Tere tulemast 'Finantsnõustaja'")
print("Sinu isiklin nõustaja")

money = int(input("Kui palju raha sul praegu on?"))

if money < 2500:
    print("Sul pole veel piisavalt raha. Kogu veel!")
elif money == 2500:
    print("Palju õnne saad osta iphone")
else:
    print("Saad osta ipone ja raha jääb ülegi") """



print("Eesmärk teha igapäev 10000 sammu päevas")

goal = 10000
steps = int(input("Mitu sammu oled juba teinud:"))

percent = (steps/goal) * 100

print(f"{percent}%")

if percent < 50:
    print("Alles alguses, liigu kindlasti veel")
elif percent < 75:
    print("Tubli oled, aga pinguta veel")
elif percent <100:
    print("Tubli, peaaegu kohal, veidi veel")
else:
    print("Palju õnne, saavutasid eesmärgi") 

