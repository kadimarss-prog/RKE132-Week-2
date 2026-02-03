perekonnanimi = input("Sisesta oma perekonnanimi: ") 
sugu = input("Sisesta oma sugu (m või n): ").lower() 
if sugu == "m": 
    print(f"Tere, härra {perekonnanimi}!") 
elif sugu == "n": 
    print(f"Tere, proua {perekonnanimi}!") 
else: print(f"Tere tulemast, {perekonnanimi}! (sugu ei olegi tähtis).")