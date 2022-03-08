import time
import random


def start_point():
    print(
        "The last thing you remember is that a three-headed dog appeared from the earth and dragged your best friend to the ground. ")
    print("Later you found out that it was a Cerberus and he took it to the Underworld.")
    print("You have been looking for a way to get there to save the friend, but fainted.")
    print("When you opened your eyes you see just you are in the white room. What's happend? ")
    print("You see in the middle of the white room four boxes.On three boxes there are drawings.")
    print(".........On the first box: a HAMMER ")
    print(".........On the second box: a TRIDENT")
    print(".........On the third box: a LILY ")
    print(".........On the fourth - inscription: 'PANDORA's box' ")


def underworld():
    print("Finally you are in the underworld. Hades rules here, and he is very cruel, but he gave you a choice.")
    print("You can take your friend from the kingdom of the dead, but you need to go through the dog.")
    print("Hades told you choose only one from the three things in front of you:")
    print("1_____hummer_____(you decide to fight the three-headed dog).")
    print("2_____flute______(you decided to play a melody for the dog).")
    print("3_____meat_______(you decided to seduce the dog with meat).")
    print("Which option will you choose? (1,2,3)")
    a = input()
    if a == "1":
        print(
            "It was stupid to fight a big dog. You lose. But you are not far to go to the underworld. You are already here.")
    elif a == "2":
        print("PERFECT")
        print(
            "It was smart, the dog suddenly slept because of a pleasant melody and you took your friend with you and went upstairs.")
    else:
        print("The dog ate you with the meat. Oops ...")


def sea():
    print("You are in a magnificent castle in the underwater kingdom.")
    print("Around the castle, a water dome and outside, various fish and other marine reptiles swim.")
    print("You entered the castle, and the king sat on the throne, and in his hands was a trident.")
    print("You explained to the king that you want to get into the underworld.")
    print("He asked with a terrible face:")
    print("WHAT IS MY NAME?")
    print("Enter your answer: ")
    n = input()
    if n == "Poseidon" or n == "poseidon":
        print("CONGRATULATIONS-  you are very smart. For this I will send you to my brother's underworld.")
        print("Teleportation....")
        time.sleep(2)
        underworld()
    else:
        print(
            "HOW COULD YOU NOT KNOW WHO I AM! I am the god of the seas myself POSEIDON! Get out of my kingdom and never come back again.")


def heaven():
    print("You ended up in the kingdom of heaven where Zeus rules. ")
    print("When you walked in the kingdom of heaven you met Athena. Daughter of Zeus, goddess of wisdom and war.")
    print("And Tyche, the goddess of fortune.")
    print("You are lucky, today both goddesses are in a good mood. They gave you two options. ")
    print("First- answer the questions of Athena (the goddess of wisdom).")
    print("Second- go to Tyche and try your luck(the goddess of fortune).")
    print("Enter your choice: (1 or 2)")
    n = input()
    time.sleep(2)
    if n == "1":
        print("Athena is waiting for you...")
        time.sleep(2)
        print("Remember you have only one chance to give the correct answer for question.")
        time.sleep(2)
        print("In Greek mythology Medusa’s hair was made of what?")
        a = input("Your answer is: ")
        if a == "snakes" or a == "snake":
            print("Your answer is correct! Athena is satisfied.She shows you the gates to the underworld")
            time.sleep(2)
            underworld()
        else:
            print("Your answer is not correct.She turned you into an owl and you will serve her all your life. ")
    else:
        print("Tyche is waiting for you...")
        time.sleep(2)
        print(
            "Tyche took strawberries with her today for a picnic. Guess how many strawberries are left.The number is between 7 and 13. ")
        a = int(input())
        b = random.randint(7, 14)
        if a == b:
            print("Congratulations, you are very lucky person and she shows you the way out.")
            print("Teleportation....")
            time.sleep(2)
            underworld()
        else:
            print("Failure is just the will of fate. Remember this.")


def Pandora_box():
    print("Ohh,you discovered what could not be opened.You made the same mistake as Pandora. ")
    print("When you opened this box, chaos seized the earth. People are in trouble. ")
    print("But goddess Tyche (goddess of fortune) gave you a chance. ")
    print("Answer her question and you will take chance.")
    time.sleep(2)
    print("Answer: What was left in Pandora’s box after she released misery and evil?")
    ans1 = input()
    if ans1 == "Hope" or ans1 == "hope":
        print("Congratulation,your answer is correct! ")
        print("She decided to show you the gates to the Underworld. ")
        print("Teleportation....")
        time.sleep(2)
        underworld()
    else:
        print("Ohh, unfortunately you answered incorrectly!")
        print("Titanium swallowed you.")


# main program
chance = 'Y'
while chance == 'Y':
    start_point()
    print("Which box do you want to open? (1,2,3,4) ")
    number = input()
    if number == "1":
        heaven()
    elif number == "2":
        sea()
    if number == "3":
        underworld()
    if number == "4":
        Pandora_box()
    print('Want to play again? (Yes (Y) or No (N))')
    chance = input()
