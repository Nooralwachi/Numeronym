class Numeronym():
	def __init__(self, dictionary_file) :
		self.file = dictionary_file
		self.num= {}

	def create_dictionary(self):
		with open(self.file, 'r') as file:
			for line in file:
				item = line.strip()
				self.num[self.calc_numeronym(item)]= True

	def calc_numeronym(self,word):
		if len(word) <3 : 
			return word
		first, last, mid = word[0], word[-1], str(len(word)-2)
		return "{}{}{}".format(first,mid,last)

	def fancy_numeronym(self, word):
		result=self.calc_numeronym(word)
		if result in self.num:
			print("{} = {} which is already exist".format(word,result))
			new= self.shortest(word)
			self.num[new]= True
			print("Fancy Numeronym = {}".format(new))
		else:
			print('False')

	def shortest(self,word):
		if len(word) %2 ==0 :
			new=self.calc_numeronym(word[:int(len(word)/2)]) + self.calc_numeronym(word[int((len(word)/2)):])
			return new
		else:
			new=self.calc_numeronym(word[:int(len(word)/2)]) +word[int((len(word)/2))]+self.calc_numeronym(word[int((len(word)/2)+1):])
			return new


N = Numeronym('dictionary.txt')
N.create_dictionary()
N.fancy_numeronym('kubernetas')
N.fancy_numeronym('aravaza')
N.fancy_numeronym('carbonade')

