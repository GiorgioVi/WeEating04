from pymongo import MongoClient

#Using the cursor object returned by search queries, a list of dictionaries is returned
def cursor_to_list(c):
    l = []
    for dictionary in c:
        l.append(dictionary)
    return l

#Establishes a connection to the restaurants collection
def connect():
    connection = MongoClient("homer.stuy.edu")
    db = connection.test
    return db.restaurants

#Returns a list of dictionaries of all restuarants in a borough
def get_by_borough(b):
    return cursor_to_list(connect().find({"borough": b}))

#Returns a list of dictionaries of all restaurants in this zipcode
def get_by_zipcode(zip):
    return cursor_to_list(connect().find({"address.zipcode": zip}))

#Returns a list of dictionaries of all restaurants in this zipcode and with this grade
def get_by_zipcode_and_grade(zip, grade):
    return cursor_to_list(connect().find({"address.zipcode": zip, "grades.grade": grade}))

#Returns a list of dictionaries of all restaurants in this zipcode with a score below this one
def get_by_zipcode_and_score(zip, score):
    return cursor_to_list(connect().find({"address.zipcode": zip, "grades.score": {"$lt": score}}))

#Returns a list of dictionaries of all restaurants in this borough with a certain cuisine
def interesting(borough, cuisine):
    return cursor_to_list(connect().find({"borough": borough, "cuisine": cuisine}))

###SCHEMA
"""
address: {building, coord[], street, zipcode},
borough,
cuisine,
grades: [{date, grade, score}]
"""
#note: grade is A-F while score is 0-5 (probably)

###TESTS
print "When in Brooklyn, go to"
print get_by_borough("Brooklyn")[:1]
print ""
print "When in 10282 (tribeca), go to"
print get_by_zipcode("10282")[:1]
print ""
print "The one with an A is"
print get_by_zipcode_and_grade("10282", "A")[:1]
print ""
print "The one with a score less than 10 is"
print get_by_zipcode_and_score("10282", "10")[:1]
print ""
print "Uhg, not this slop..."
print interesting("Brooklyn", "Russian")[:1]