hero_name = input("Vem ska historien handla om? ")
hero_age = int(input("Hur gammal är hen? "))

print("Det här är historien om", hero_name)

print("Hen var", hero_age + 3, "år gammal 3 år senare.")

choice = input("Ska hjälten öppna dörren? (ja/nej): ")

if choice == "ja" or choice == "Ja" or choice == "JA":
    print(hero_name, "öppnar försiktigt dörren... Där finns Sundus kompis, som säljer svärd!")
    gold =int(input("Hur många guldmynt har hjälten?"))

    if gold >= 10:
        print(hero_name, "har råd att köpa svärdet.")
    else:
        print (hero_name, "har inte pengar.")
else:
    print(hero_name, "bestämmer sig för att gå därifrån.")

