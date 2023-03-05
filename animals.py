

class Animals:
	
	def __init__(self):
		self.description = 'All animals are heterotrophs'
		self.something = 'The human population uses a variety of animals for food'
	
	
class Herbivores(Animals):
	
	def __init__(self,name):
		super().__init__()
		self.name = name
		self.chordates = 'Tип вторичноротых животных, для которых характерно наличие энтодермального осевого скелета в виде хорды'

class Tiger(Herbivores):
	
	def __init__(self):
		super(Tiger, self).__init__('Tiger')
		self.evolution = 'The tigers closest living relatives were previously thought'
		self.Hybrids = 'Captive tigers were bred with lions to create hybrids called liger and tigon.'
		self.lerfbb = 'A tigers coat pattern is still visible when it is shaved'

class Crocodile(Herbivores):
	
	def __init__(self):
		super(Crocodile, self).__init__('Crocodile')
		self.asd = 'Crocodiles (family Crocodylidae) or true crocodiles are large'
		self.cmnv = 'The form crocodrillus is attested in Medieval Latin.'
		self.tutuzheinpadlu = 'A crocodiles physical traits allow it to be a successful predator. '
		

class Kangaroo(Herbivores):
	
	def __init__(self):
		super(Kangaroo, self).__init__('Kangaroo')
		self.qiwef = 'Kangaroos are four marsupials from the family Macropodidae'
		self.cbg = 'The word kangaroo derives from the Guugu Yimithirr word gangurru, referring to'
		self.Locomotion = 'Kangaroos are the only large mammals to use hopping on two legs as their primary means of locomotion.'


s = Tiger()
a = Crocodile()
d = Kangaroo()
print(s.__dict__)
print(a.__dict__)
print(d.__dict__)





