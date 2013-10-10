from pymongo import Connection

databaseName = "tvmaniacsDB"
connection = Connection()

db = connection[databaseName]
actors = db['actor']

a1 = { "firstname" : "John", "lastname" : "Doe" }

a2 = { "firstname" : "Kevin", "lastname" : "Bacon" }

a3 = { "firstname" : "Walter", "lastname" : "White" }

print "clearing"
actors.remove()

print "saving"
actors.save(a1)
actors.save(a2)
actors.save(a3)

print "searching"
for a in actors.find():
    print a["firstname"] + " " + a["lastname"]
