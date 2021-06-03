from secrets import token_urlsafe

DATABASE = {}

def shorten(url: str, nbytes: int=5) -> str:
	ext = token_urlsafe(nbytes=nbytes)
	if ext in DATABASE:
		return shorten(url, nbytes=nbytes)
	else:
		DATABASE.update({ext: url})
		return f'short.ly/{ext}'

if __name__=='__main__':
	urls = (
		'https://realpython.com/',
		'https://realpython.com/courses/generating-random-data-python/'
	)
	for url in urls:
		print(shorten(url))

	print(DATABASE)

