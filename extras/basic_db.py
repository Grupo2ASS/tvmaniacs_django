from pymongo import MongoClient

databaseName = "tvmaniacsDB"
connection = MongoClient()

db = connection[databaseName]
actors = db['actor']
series = db['series']

a = [{"imdb_id": "nm0000102", "first_name": "Kevin", "last_name": "Bacon",
      "bio": "\nBorn on July 8, 1958 in Philadelphia, Pennsylvania, Kevin Bacon's early training as an actor came from The Manning Street. His debut as the strict Chip Diller in <a href=\"/title/tt0077975/?ref_=nm_ov_bio_lk1\">Animal House</a> almost seems like an inside joke, but he managed to escape almost unnoticed from that role. <a href=\"/title/tt0083833/?ref_=nm_ov_bio_lk2\">Diner</a> became the turning point after a couple of television series and a number of ...        <span class=\"see-more inline nobr-only\">\n                <a href=\"/name/nm0000102/bio?ref_=nm_ov_bio_sm\">See full bio</a> &raquo;\n        </span>\n",
      "pic": "http://ia.media-imdb.com/images/M/MV5BMTM0ODE5MjI1OV5BMl5BanBnXkFtZTcwNDc2MjAzMw@@._V1_SY317_CR8,0,214,317_.jpg",
      "birth_date": "1958-7-8", "birth_place": "Philadelphia, Pennsylvania, USA",
      "series": ["tt1837642"]},
          #[{"name": "The Following", "year": "2013-2014\n"},
          #       {"name": "Robot Chicken", "year": "2011\n"},
          #       {"name": "Bored to Death", "year": "2010\n"},
          #       {"name": "Frasier", "year": "1994\n"},
          #       {"name": "American Playhouse", "year": "1986-1988\n"},
          #       {"name": "The Guiding Light", "year": "1980-1981\n"},
          #       {"name": "Search for Tomorrow", "year": "1951\n"}]},
     {"imdb_id": "nm0700856", "first_name": "James", "last_name": "Purefoy",
      "bio": "\nJames Purefoy was born and brought up in Somerset. After leaving school at the age of sixteen, he took a succession of different jobs, including working on a pig farm and as a porter at Yeovil District Hospital, before travelling and working extensively throughout Europe. At eighteen, James returned to college to take his A-Levels, one of which ...        <span class=\"see-more inline nobr-only\">\n                <a href=\"/name/nm0700856/bio?ref_=nm_ov_bio_sm\">See full bio</a> &raquo;\n        </span>\n",
      "pic": "http://ia.media-imdb.com/images/M/MV5BMjAyMTE1NTk1OF5BMl5BanBnXkFtZTYwOTE3OTI1._V1_SY317_CR0,0,214,317_.jpg",
      "birth_date": "1964-6-3", "birth_place": "Taunton, Somerset, England, UK",
      "series": ["tt1837642"]},
          #
          #{"name": "The Following", "year": "2013-2014\n"},
          #       {"name": "Episodes", "year": "2012\n"},
          #       {"imdb_id": "tt1837642", "year": "2012\n"}, # "name": "Revenge"
          #       {"name": "Rev.", "year": "2011\n"},
          #       {"name": "The Philanthropist", "year": "2009\n"},
          #       {"name": "Rome", "year": "2005-2007\n"},
          #       {"name": "The Prince and the Pauper", "year": "1996\n"},
          #       {"name": "Tears Before Bedtime", "year": "1995\n"},
          #       {"name": "Crime Story", "year": "1993\n"},
          #       {"name": "Rides", "year": "1993\n"},
          #       {"name": "Boon", "year": "1991\n"},
          #       {"name": "The Case-Book of Sherlock Holmes", "year": "1991\n"},
          #       {"name": "Coasting", "year": "1990\n"}]},
     {"imdb_id": "nm0000656", "first_name": "Madeleine", "last_name": "Stowe",
      "bio": "\nMadeleine Stowe grew up in Eagle Rock, a working-class neighborhood of Los Angeles. At age ten she started practicing for a career as a concert pianist and trained every day for hours. However, when her instructor died in 1976 she more or less quit playing. She went to University of Southern California and studied cinema and journalism before ...        <span class=\"see-more inline nobr-only\">\n                <a href=\"/name/nm0000656/bio?ref_=nm_ov_bio_sm\">See full bio</a> &raquo;\n        </span>\n",
      "pic": "http://ia.media-imdb.com/images/M/MV5BMTA3OTI0NzkzODVeQTJeQWpwZ15BbWU3MDEyMzYyOTY@._V1_SY317_CR3,0,214,317_.jpg",
      "birth_date": "1958-8-18", "birth_place": "Los Angeles, California, USA",
      "series":["tt1837642", "tt0802148"]},

          #[{"imdb_id": "tt1837642", "year": "2011-2013\n"},#, "name": "Revenge"
          #       {"imdb_id": "tt0802148", "year": "2007\n"},#, "name": "Raines"
          #       {"name": "Trapper John, M.D.", "year": "1981\n"},
          #       {"name": "Little House on the Prairie", "year": "1980\n"},
          #       {"name": "Barnaby Jones", "year": "1979\n"},
          #       {"name": "The Amazing Spider-Man", "year": "1978\n"},
          #       {"name": "Baretta", "year": "1978\n"}]},
     {"imdb_id": "nm0000156", "first_name": "Jeff", "last_name": "Goldblum",
      "bio": "\nBorn Jeffrey Lynn Goldblum on October 22, 1952 in Pittsburgh, Pennsylvania, actor Jeff Goldblum began his career on the New York stage after moving to the city at age seventeen. Possessing his own unique style of delivery, Goldblum made an impression on moviegoers with little more than a single line in <a href=\"/name/nm0000095/?ref_=nm_ov_bio_lk1\">Woody Allen</a>'s <a href=\"/title/tt0075686/?ref_=nm_ov_bio_lk2\">Annie Hall</a>, when he fretted ...        <span class=\"see-more inline nobr-only\">\n                <a href=\"/name/nm0000156/bio?ref_=nm_ov_bio_sm\">See full bio</a> &raquo;\n        </span>\n",
      "pic": "http://ia.media-imdb.com/images/M/MV5BMTE5NzkyODg1Nl5BMl5BanBnXkFtZTYwMTY2OTE0._V1_SY317_CR22,0,214,317_.jpg",
      "birth_date": "1952-10-22", "birth_place": "Pittsburgh, Pennsylvania, USA",
      "series": ["tt0802148"]}
          #[{"name": "Portlandia", "year": "2012-2013\n"},
          #       {"name": "The League", "year": "2011-2012\n"},
          #       {"name": "Glee", "year": "2012\n"},
          #       {"name": "Allen Gregory", "year": "2011\n"},
          #       {"name": "NTSF:SD:SUV", "year": "2011\n"},
          #       {"name": "Law & Order: Criminal Intent", "year": "2009-2010\n"},
          #       {"imdb_id": "tt0802148", "year": "2007\n"},#, "name": "Raines"
          #       {"name": "Will & Grace", "year": "2005\n"},
          #       {"name": "Crank Yankers", "year": "2003-2005\n"},
          #       {"name": "Tom Goes to the Mayor", "year": "2004\n"},
          #       {"name": "Friends", "year": "2003\n"},
          #       {"name": "King of the Hill", "year": "2002\n"},
          #       {"name": "Mr. Show with Bob and David", "year": "1998\n"},
          #       {"name": "Saturday Night Live", "year": "1993-1997\n"},
          #       {"name": "The Simpsons", "year": "1996\n"},
          #       {"name": "The Larry Sanders Show", "year": "1995\n"},
          #       {"name": "Futurequest", "year": "1994\n"},
          #       {"name": "Captain Planet and the Planeteers", "year": "1990-1991\n"},
          #       {"name": "Sesame Street", "year": "1990\n"},
          #       {"name": "The Ray Bradbury Theater", "year": "1986\n"},
          #       {"name": "Faerie Tale Theatre", "year": "1985\n"},
          #       {"name": "American Playhouse", "year": "1984\n"},
          #       {"name": "The New Show", "year": "1984\n"},
          #       {"name": "The Devlin Connection", "year": "1982\n"},
          #       {"name": "Laverne & Shirley", "year": "1982\n"},
          #       {"name": "Tenspeed and Brown Shoe", "year": "1980\n"},
          #       {"name": "Starsky and Hutch", "year": "1977\n"},
          #       {"name": "The Blue Knight", "year": "1976\n"},
          #       {"name": "Columbo", "year": "1975\n"}]},
     #{"first_name": "Nat", "last_name": "Faxon",
     # "pic": "http://ia.media-imdb.com/images/M/MV5BMTYxMDM1MDEyM15BMl5BanBnXkFtZTcwMzg2NDY0Nw@@._V1_SX214_CR0,0,214,317_.jpg",
     # "series": [{"name": "Star Wars: Detours", "year": "2012\n"},
     #            {"name": "Ben and Kate", "year": "2012-2013\n"},
     #            {"name": "Up All Night", "year": "2012\n"},
     #            {"name": "The Cleveland Show", "year": "2009-2012\n"},
     #            {"name": "Are You There, Chelsea?", "year": "2012\n"},
     #            {"name": "Sketchy", "year": "2012\n"},
     #            {"name": "Allen Gregory", "year": "2011\n"},
     #            {"name": "Happy Endings", "year": "2011\n"},
     #            {"name": "Party Down", "year": "2010\n"},
     #            {"name": "American Dad!", "year": "2005-2009\n"},
     #            {"name": "Glenn Martin DDS", "year": "2009\n"},
     #            {"name": "DJ & The Fro", "year": "2009\n"},
     #            {"name": "Happy Hour", "year": "2006-2008\n"},
     #            {"name": "Mad Men", "year": "2008\n"},
     #            {"name": "My Name Is Earl", "year": "2006\n"},
     #            {"name": "Reba", "year": "2005\n"},
     #            {"name": "NCIS: Naval Criminal Investigative Service", "year": "2005\n"},
     #            {"name": "Joey", "year": "2004-2005\n"},
     #            {"name": "Reno 911!", "year": "2003-2004\n"},
     #            {"name": "Significant Others", "year": "2004\n"},
     #            {"name": "Grosse Pointe", "year": "2000-2001\n"},
     #            {"name": "Rude Awakening", "year": "1999\n"}]}
]

s = [{"imdb_id": "tt1837642", "name": "Revenge", "user_rating": 7.9,
      "description": "\nThe daughter of a framed executive makes it her mission to infiltrate upper Hamptons society and exact revenge on the people who set her father up.    ",
      "duration": 44, "genres": [" Drama", " Mystery", " Thriller"],
      "pic": "http://ia.media-imdb.com/images/M/MV5BMTg1NjE5NjQyM15BMl5BanBnXkFtZTcwOTM2MTQyOA@@._V1_SY317_CR12,0,214,317_.jpg",
      "year_start": "2011", "year_end": "",
      "cast": ["nm0000656"],
               #{"name": "Emily VanCamp"},
               #{"name": "Gabriel Mann"},
               #{"name": "Nick Wechsler"},
               #{"name": "Henry Czerny"},
               #{"name": "Joshua Bowman"},
               #{"name": "Christa B. Allen"},
               #{"name": "Ashley Madekwe"},
               #{"name": "Connor Paolo"},
               #{"name": "Barry Sloane"},
               #{"name": "Margarita Levieva"}],
      "seasons": [{"number": "3"}, {"number": "2"}, {"number": "1"}]},
     {"imdb_id": "tt0802148", "name": "Raines", "user_rating": 7.4,
      "description": "\nLos Angeles. Present day. Michael Raines, an eccentric but brilliant cop, solves murders in a very unusual way - he turns the victims into his partners. These visions are figments of Raines...                <a href=\"/title/tt0802148/plotsummary?ref_=tt_ov_pl\">See full summary</a>&nbsp;&raquo;\n    ",
      "duration": 45, "genres": [" Crime", " Drama"],
      "pic": "http://ia.media-imdb.com/images/M/MV5BNjQ3NjY5NjYyN15BMl5BanBnXkFtZTcwNTgzMjU0MQ@@._V1_SY317_CR20,0,214,317_.jpg",
      "year_start": "2007", "year_end": "",
      "cast": ["nm0000156", "nm0000656"],
      "seasons": [{"number": "1"}]},
     #{"imdb_id": "tt0903747", "name": "Breaking Bad", "user_rating": 9.5,
     # "description": "\nTo provide for his family's future after he is diagnosed with lung cancer, a chemistry genius turned high school teacher teams up with an ex-student to cook and sell the world's purest crystal meth.    ",
     # "duration": 45, "genres": [" Crime", " Drama", " Thriller"],
     # "pic": "http://ia.media-imdb.com/images/M/MV5BMTU2MTgzMzQxNV5BMl5BanBnXkFtZTcwODg4NTQ3OQ@@._V1_SX214_.jpg",
     # "year_start": "2008", "year_end": "",
     # "cast": [{"name": "Bryan Cranston"},
     #          {"name": "Anna Gunn"},
     #          {"name": "Aaron Paul"},
     #          {"name": "Dean Norris"},
     #          {"name": "Betsy Brandt"},
     #          {"name": "RJ Mitte"},
     #          {"name": "Bob Odenkirk"},
     #          {"name": "Steven Michael Quezada"},
     #          {"name": "Jonathan Banks"},
     #          {"name": "Giancarlo Esposito"}],
     # "seasons": [{"number": "5"}, {"number": "4"}, {"number": "3"}, {"number": "2"}, {"number": "1"}]}
     ]

a0 = a[0]
a1 = a[1]
a2 = a[2]
a3 = a[3]
#a4 = a[4]

print "clearing"
actors.remove()
series.remove()

print "saving"
actors.save(a0)
actors.save(a1)
actors.save(a2)
actors.save(a3)
#actors.save(a4)

series.save(s[0])
series.save(s[1])
#series.save(s[2])


print "searching"
