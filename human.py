

class Human:
	
	def __init__(self):
		self.area = 'Man inhabits almost the entire Earth.'
		self.brain = 'Man has a highly developed brain.'
		self.Appearance = 'The head is big. There are five long flexible fingers on the upper limbs. Most often, people move on two legs.'
		self.diet = 'People are omnivorous.'

class Builder(Human):
	
	def __init__(self):
		Human.__init__(self)
		self.physical_form = ''
		self.necessary_skills = ''
		self.experience = ''
		
	def form(self,phys_form):
		self.physical_form = phys_form
		
	def skill(self,skill):
		self.necessary_skills = skill
		
	def exp(self,exp):
		self.experience = exp

class Pilot(Builder):
	
	def __init__(self):
		Builder.__init__(self)
	
ob = Human()
o = Builder()
obj = Pilot()
obj.skill('123')
o.skill('asd')

print(ob.__dict__)
print(o.__dict__)
print(obj.__dict__)