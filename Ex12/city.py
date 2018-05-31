class City:
	def __init__(self, name , places = []):
		self.name = name
		self.places = places

	def addPlace(self,placeName):
		self.places.append(placeName)

	def removePlace(self, placeName):
		self.places.remove(placeName)

	def dispPlaceNames(self):
		print("Places visited in", self.name, "are", ",".join(self.places))

