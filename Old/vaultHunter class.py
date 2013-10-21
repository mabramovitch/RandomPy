class vaultHunter:
    def __init__(self):
        self.name = raw_input('Name: ')
        self.role = raw_input('Role: ')
        self.actionSkill = raw_input('Action skill: ')
    def doActionSkill(self):
        print self.actionSkill
    def intro(self):
        print self.name + ' as the ' + self.role
