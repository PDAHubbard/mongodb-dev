import bottle
import pymongo

# Handler for the default route
@bottle.route('/')
def index():        # this function could have any name
    # Connect to MongoDB
    connection = pymongo.MongoClient('localhost', 27017)
    # Attach to test database
    db = connection.test
    # Get a handle for the names collection
    name = db.names
    # Find a single document
    item = name.find_one()

    return '<b>Hello %s!</b>' % item['name']


bottle.run(host='localhost', port=8080)
