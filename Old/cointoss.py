import random

def cointoss():
    result = random.randint(0, 1);
    if result == 0:
        print "tails";
    else:
        print "heads";
    again = raw_input("\n Flip again? (\"yes\" or \"no\")\n")
    if again == "yes":
        print "\n"
        cointoss();
    elif again == "no":
        print "\nbye bye"
    else:
        print "\nEnglish, motherfucker, do you speak it?"
