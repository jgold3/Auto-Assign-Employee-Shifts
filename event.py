from brother import Brother

class Event(object):
	def __init__(self, name, date="NA"):
		self.name = name
		self.date = date
		self.brothers = []
