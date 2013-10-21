##PRACTICE

##    Slicing
def reverse(stuff):
        return stuff[-1::-1]
    
##    .extend()
vault_hunters = ['Salvador', 'Axton', 'Maya', 'Zero', 'Gaige', 'Kreig']
original_vault_hunters = ['Roland', 'Lilith', 'Mordechai', 'Brick']

##    ??? Doesn't work; original_vault_hunters is assigned this instead
all_vault_hunters = original_vault_hunters.extend(vault_hunters)

##    .join() -- method of joining string, takes 
joiner = ' and '
sentence = "Have a nice day."

##    .replace() -- only works on strings
##
##    dictionaries -- {key0:value0, key1, value1, ...}
classes = {'Salvador':'Gunzerker', 'Axton':'Commando', 'Maya':'Siren',
            'Zero':'Assassin', 'Gaige':'Mechromancer', 'Kreig':'Psycho'}
##        methods
##
##    operators, comparisons, and logic
##        is (variables must be the same in memory, not just same value)
##        in
##        ==, <, >, <=, >= can also be used for strings (alphabetize)
##        and, or
##
##    loops
i = 0
while i < len(vault_hunters):
    print "lvl 61 " + vault_hunters[i]
    i+=1

print "\n\n"

for vh in classes:
    print vh + " as the ", classes[vh]

##    Notes on defining functions:
##
##    >> Make default parameter values by setting parameter variables in the
##    function definition equal to their default value
##
##    >> Allow multiple parameters (tuple) by putting one asterisk in front of
##    the parameter -- ex: f(*numbers) --> f(1, 2, 3)
##    
##    >> Allow multiple parameters (dictionary) by putting two asterisks in
##    front of the parameter -- ex: f(**ages) --> f(Jim = 55, Jebadiah = 31)
##    
##    >> Can also call pre-existing tuples or dictionaries (still must use
##    asterisks)


##    Notes on classes and objects:
##
##    >> Create an object exampleObject in a class called exampleClass:
##    class exampleClass:
##        variables = values      #properties of the object
##        def methods(self):      #NOTE: self must be the first argument for all
##            methods -- actions the object can take (using properties)
##    
##    exampleObject = exampleClass()
##    exampleObject.variable
##    exampleObject.method()
##
##    >> Create a subclass:
##    class subClass(superClass):
##        whatever else is in subClass (can overwrite variables from superClass)
##        if nothing is changed, write "pass"
##    #can inherit from multiple superclasses (but make sure their variables  
##    don't overwrite each other)
##
##    >> A Constructor is a method that is executed immediately upon the
##    creation of an object in the class.  Must be written as:
##    def __init__(self):
##            whatever the constructor does


##    Modules
##
##    >> Save modules from a new window as .py files in the python27 folder
##
##    >> Can import saved modules once per program (but can reload(module)
##    whenever)
##
##    >> Use dir(module) to see everything in the module
##
##    >> Use .__doc__ method for built-in modules to get a description


##    Working with files
##
##    fileObject = open(file pathway, 'w' to write or 'r' to read)
##    fileObject.write('whatever you want to write') #\n creates a new line
##    fileObject.read(x) to read first x bytes
##    fileObject.read() to read the rest of the file
##    fileObject.readline() to read single line
##    fileObject.readlines() to return all lines as a list --> can then edit
##        individual lines in the list and overwrite the new list into the file
##        using fileObject.writelines()
##    fileObject.colse() when you're done
