import random

def fortune():
    #prompt question
    question = raw_input("Ask away.\n\n")
    #you screwed up
    if question == "":
        print "Really?  Was \"ask away\" not self-explanatory? \n\
You type in a yes or no question and press enter. \n\
Don't be discouraged.  Try again.  I believe in you.\n"
        fortune()
    elif question[-1] != "?":
        print "Use a question mark when asking a question.  \
This isn't the Internet.  Try again.\n"
        fortune()
    #random response
    else:
        response = random.randint(0, 4)
        if response == 0:
            print "no"
        elif response == 1:
            print "*laughs*"
        elif response == 2:
            print "doubtful"
        elif response == 3:
            print "probably"
        else:
            print "yes"
        print "\n"
        #restart automatically
        fortune()
        #or ask to restart
##        again = raw_input("\nAgain? (\"yes\" or \"no\")\n")
##        if again == "yes":
##            print "\n"
##            fortune();
##        elif again == "no":
##            print "\nbye bye"
##        #you screwed up
##        else:
##            print "\nEnglish, motherfucker, do you speak it?"
