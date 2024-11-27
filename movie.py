import mrich
from pathlib import Path

class Movie():
	def __init__(self,*,name,title,year=None,description,imdb_url=None,trailer_url=None,more_data=None,awards=None):
		self.name = name
		self.title = title
		self.year = year
		self.description = description
		self.more_data = more_data
		self.trailer_url = trailer_url
		self.imdb_url = imdb_url
		self.awards = awards

	@property
	def target_url(self):
		return self.trailer_url or self.imdb_url

	@property
	def embed_url(self):
		if self.trailer_url:

			if "vimeo" in self.trailer_url:
				number = self.trailer_url.removesuffix("/").split("/")[-1]
				return f"https://player.vimeo.com/video/{number}"
			elif "?v=" in self.trailer_url:
				return f'https://www.youtube-nocookie.com/embed/{self.trailer_url.split("?v=")[-1]}'
			else:
				return f'https://www.youtube-nocookie.com/embed/{self.trailer_url.replace("https://youtu.be/","")}'

	@property
	def has_screencap(self):
		return Path(f'assets/{self.name}_screen.jpg').exists()

	@property
	def has_poster(self):
		exists = Path(f'assets/{self.name}_poster.jpg').exists()
		if not exists:
			mrich.error(self.name, "No Poster!")
		return exists
	
	@property
	def screencap_url(self):
		return f'assets/{self.name}_screen.jpg'

	@property
	def poster_url(self):
		return f'assets/{self.name}_poster.jpg'
