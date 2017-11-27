""" This is class which defines the template of each movies"""

import webbrowser

class Movie():
	""" 
	This class gives the template for movies and defines methoud which shows trailer
	"""	
	#Constructor 
	def __init__(self, title, plot, image_url, youtube_trailer_url):
		self.title=title
		self.storyline=plot
		self.poster_image_url=image_url
		self.trailer_youtube_url=youtube_trailer_url

	#function which show youtube trailer
	def showtrailer(self):
		webbrowser.open(self.trailer_youtube_url)
		
