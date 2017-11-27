 """The main module which interface movies(data) and html display fresh_tomatoes.py"""

import movies
import fresh_tomatoes

# justice league movie

justiceleague=movies.Movie("Justice League",
			   "Batman and other heroes join together to defeat stepphenwolf",
			   "http://t0.gstatic.com/images?q=tbn:ANd9GcTbr9aajZtJiuhXc_biRws9jzCi4u1q4MWvyPVe0rGO9Z0RwDqT", #noqa
			   "https://www.youtube.com/watch?v=r9-DM9uBtVI")
# it(2017)movie

it=movies.Movie("It(2017)",
		""" Seven young outcasts in Derry, Maine, are about 
		    to face their worst nightmare
		    -- an ancient, shape-shifting evil that emerges 
		    from the sewer every 27 years
		    to prey on the town's children """",
		"http://t1.gstatic.com/images?q=tbn:ANd9GcTALjGaaCwNAfgH2Fa0jVpp2mEOhGRRw1v0lkRrHlUtXyKW0buX", # noqa
		"https://www.youtube.com/watch?v=FnCdOQsX5kc")

# wonderwoman movie

wonderwoman=movies.Movie("Wonder Woman",
			"""Before she was Wonder Woman (Gal Gadot), she was Diana, princess of 
			   the Amazons, trained to be an unconquerable warrior. Raised on a
			   sheltered island paradise, Diana meets an American pilot (Chris Pine)
			   who tells her about the massive conflict that's
			   raging in the outside world.""",
			"http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H", #noqa
			"https://www.youtube.com/watch?v=T5bj_fvwVTE")

# create a list of names of movie objects created
movielist=[justiceleague,it,wonderwoman]

# calling the function open_movies_page from module fresh_tomatoes
fresh_tomatoes.open_movies_page(movielist)
