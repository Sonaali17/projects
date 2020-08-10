#FUN FRIENDSHIP CALCULATOR GAME

print("TEST YOUR FRIENDSHIP HERE!!!")
print("***Only Fun Game***\n")
alphabet="bcdfghjklmnpqrstvwxyz"
score=0
names=input("Enter First name and Second name ").lower()


for charac in names:
    if charac in 'aeiou':
        score+=5

    if charac in 'friends':
        score+=10

    if charac in alphabet:
        score+=alphabet.find(charac)

    else:
        score+=0


if score>100:
    print ("Your friendship score is: ", score)
    print ("Congratulations you both are best friends!")

else:

    print ("Your friendship score is: ", score)
