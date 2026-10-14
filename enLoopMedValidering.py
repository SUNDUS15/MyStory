x = 1
while x < 50 :
    print (x)
    x = x + 15

run= True
while run:
    try: 
        age = int(input("Skriv in din ålder: "))
        if age > 0 and age < 120:
            print ("Du har en mänsklig ålder.")
            run = False  
        else:
            print ("Du måste använda en mänsklig ålder.")
    except:
        print("Du måste använda heltal.")

print ("Hej då.")

