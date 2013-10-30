from pymongo import MongoClient

databaseName = "tvdb"
connection = MongoClient()

db = connection[databaseName]
actors = db['actor']
series = db['series']

a = [{"imdb_id": "nm0000102", "first_name": "Kevin", "last_name": "Bacon", "score":60, "high_score":70, "low_score":40,
      "bio": "\nBorn on July 8, 1958 in Philadelphia, Pennsylvania, Kevin Bacon's early training as an actor came from The Manning Street. His debut as the strict Chip Diller in <a href=\"/title/tt0077975/?ref_=nm_ov_bio_lk1\">Animal House</a> almost seems like an inside joke, but he managed to escape almost unnoticed from that role. <a href=\"/title/tt0083833/?ref_=nm_ov_bio_lk2\">Diner</a> became the turning point after a couple of television series and a number of ...        <span class=\"see-more inline nobr-only\">\n                <a href=\"/name/nm0000102/bio?ref_=nm_ov_bio_sm\">See full bio</a> &raquo;\n        </span>\n",
      "pic": "http://ia.media-imdb.com/images/M/MV5BMTM0ODE5MjI1OV5BMl5BanBnXkFtZTcwNDc2MjAzMw@@._V1_SY317_CR8,0,214,317_.jpg",
      "birth_date": "1958-7-8", "birth_place": "Philadelphia, Pennsylvania, USA",
      "series": ["tt1837642"]},
     {"imdb_id": "nm0700856", "first_name": "James", "last_name": "Purefoy",
      "bio": "\nJames Purefoy was born and brought up in Somerset. After leaving school at the age of sixteen, he took a succession of different jobs, including working on a pig farm and as a porter at Yeovil District Hospital, before travelling and working extensively throughout Europe. At eighteen, James returned to college to take his A-Levels, one of which ...        <span class=\"see-more inline nobr-only\">\n                <a href=\"/name/nm0700856/bio?ref_=nm_ov_bio_sm\">See full bio</a> &raquo;\n        </span>\n",
      "pic": "http://ia.media-imdb.com/images/M/MV5BMjAyMTE1NTk1OF5BMl5BanBnXkFtZTYwOTE3OTI1._V1_SY317_CR0,0,214,317_.jpg",
      "birth_date": "1964-6-3", "birth_place": "Taunton, Somerset, England, UK",
      "series": ["tt1837642"]},
     {"imdb_id": "nm0000656", "first_name": "Madeleine", "last_name": "Stowe",
      "bio": "\nMadeleine Stowe grew up in Eagle Rock, a working-class neighborhood of Los Angeles. At age ten she started practicing for a career as a concert pianist and trained every day for hours. However, when her instructor died in 1976 she more or less quit playing. She went to University of Southern California and studied cinema and journalism before ...        <span class=\"see-more inline nobr-only\">\n                <a href=\"/name/nm0000656/bio?ref_=nm_ov_bio_sm\">See full bio</a> &raquo;\n        </span>\n",
      "pic": "http://ia.media-imdb.com/images/M/MV5BMTA3OTI0NzkzODVeQTJeQWpwZ15BbWU3MDEyMzYyOTY@._V1_SY317_CR3,0,214,317_.jpg",
      "birth_date": "1958-8-18", "birth_place": "Los Angeles, California, USA",
      "series": ["tt1837642", "tt0802148"]},
     {"imdb_id": "nm0000156", "first_name": "Jeff", "last_name": "Goldblum",
      "bio": "\nBorn Jeffrey Lynn Goldblum on October 22, 1952 in Pittsburgh, Pennsylvania, actor Jeff Goldblum began his career on the New York stage after moving to the city at age seventeen. Possessing his own unique style of delivery, Goldblum made an impression on moviegoers with little more than a single line in <a href=\"/name/nm0000095/?ref_=nm_ov_bio_lk1\">Woody Allen</a>'s <a href=\"/title/tt0075686/?ref_=nm_ov_bio_lk2\">Annie Hall</a>, when he fretted ...        <span class=\"see-more inline nobr-only\">\n                <a href=\"/name/nm0000156/bio?ref_=nm_ov_bio_sm\">See full bio</a> &raquo;\n        </span>\n",
      "pic": "http://ia.media-imdb.com/images/M/MV5BMTE5NzkyODg1Nl5BMl5BanBnXkFtZTYwMTY2OTE0._V1_SY317_CR22,0,214,317_.jpg",
      "birth_date": "1952-10-22", "birth_place": "Pittsburgh, Pennsylvania, USA",
      "series": ["tt0802148"]}]

s = [{"imdb_id": "tt1837642", "name": "Revenge", "user_rating": 7.9,
      "description": "\nThe daughter of a framed executive makes it her mission to infiltrate upper Hamptons society and exact revenge on the people who set her father up.    ",
      "duration": 44, "genres": [" Drama", " Mystery", " Thriller"],
      "pic": "http://ia.media-imdb.com/images/M/MV5BMTg1NjE5NjQyM15BMl5BanBnXkFtZTcwOTM2MTQyOA@@._V1_SY317_CR12,0,214,317_.jpg",
      "year_start": "2011", "year_end": "",
      "cast": ["nm0000656"],
      "seasons": [{"number": 3, "chapters": [{"name": "ch1", "user_rating": 1, "desc": "chapssss"},
                                               {"name": "ch2", "user_rating": 2,
                                                "desc": "capitulo 2 de la serie Revenge"}]},
                  {"number": 2, "chapters": [ {"name": "ch1",
                                                   "user_rating": 3,
                                                   "desc": "casp"},
                                                  {"name": "ch2",
                                                   "user_rating": 4,
                                                   "desc": "capitulo 2 de temp 2 de la serie Revenge"}]},
                  {"number": 1, "chapters": [{"name": "ch1temp1", "user_rating": 5, "desc": "chapssss"},
                                               {"name": "ch2temp1", "user_rating": 6,
                                                "desc": "capitulo 2 temp 1 de la serie Revenge"}],
                   "reviews":[
			{
				"score": 100,
				"name": "Tom Shales",
				"institution": "Washington Post",
				"comment":"The most electrifying new main character to hit television in years.",
				"date":"2013-03-11",
                "link":"http://google.com",
				"critic":"true"
			},
			{
				"score": 91,
				"name": "Manuel Mendoza",
				"institution": "Dallas morning news",
				"comment": "In place of the by-now cliches, House substitutes wit, taut writing ...",
				"date": "2013-03-11",
				"critic": "true"
			}]}],

     },
     {"imdb_id": "tt0802148", "length":50, "name": "Raines", "user_rating": 7.4, "metascore":58,
      "description": "\nLos Angeles. Present day. Michael Raines, an eccentric but brilliant cop, solves murders in a very unusual way - he turns the victims into his partners. These visions are figments of Raines...                <a href=\"/title/tt0802148/plotsummary?ref_=tt_ov_pl\">See full summary</a>&nbsp;&raquo;\n    ",
      "duration": 45, "genres": [" Crime", " Drama"],
      "pic": "http://ia.media-imdb.com/images/M/MV5BNjQ3NjY5NjYyN15BMl5BanBnXkFtZTcwNTgzMjU0MQ@@._V1_SY317_CR20,0,214,317_.jpg",
      "year_start": "2007", "year_end": "",
      "cast": ["nm0000156", "nm0000656"],
      "seasons": [{"number": 1,
                   "chapters": [{"name": "capitulo1", "user_rating": 5, "desc": "cprimer campitulo ssss"},
                                {"name": "ch2", "user_rating": 8, "desc": "capitulo 2 de la serie Raines"}]}]}, ]

print "clearing"
actors.remove()
series.remove()

print "saving"
actors.save(a[0])
actors.save(a[1])
actors.save(a[2])
actors.save(a[3])

series.save(s[0])
series.save(s[1])

print "searching"
