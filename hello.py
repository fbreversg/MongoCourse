import bottle
import pymongo


# this is the handler for the default path of the web server

@bottle.route('/')
def index():

    # connect to mongoDB
    connection = pymongo.MongoClient('localhost', 27017)

    # attach to test database
    db = connection.video

    # get handle for movies collection
    movie = db.movies

    # find a single document
    item = movie.find_one()

    return '<b>Hello %s</b>' % item['title']

bottle.run(host='localhost', port=8080)

