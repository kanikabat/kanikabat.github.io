domain = 'http://walshbr.com/'
pages = ['about','blog','pedagogy','projects','cv']

urls = ["http://walshbr.com/about", "'http://walshbr.com/blog",
"http://walshbr.com/pedagogy", "http://walshbr.com/projects",
 "http://walshbr.com/cv"]

for page in pages:
	url = domain + page
	urls.append(url)

urls
