<<<<<<< HEAD
import firebase_admin # firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from conf import firebase

cred = credentials.Certificate("./firebaseKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': firebase['database_url']
})

# db class
class rdb:
    def get (self, path):
        print ('[Firebase] getting ' + path + '...')
        return db.reference(path).get()
    def push (self, path, data):
        print ('[Firebase] pushing ' + str(data) + 'to ' + path + '...')
        db.reference(path).set(data)
    def update (self, path, data):
        print ('[Firebase] pushing ' + str(data) + 'to ' + path + '...')
=======
import firebase_admin # firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from conf import firebase

cred = credentials.Certificate("./firebaseKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': firebase['database_url']
})

# db class
class rdb:
    def get (self, path):
        print ('[Firebase] getting ' + path + '...')
        return db.reference(path).get()
    def push (self, path, data):
        print ('[Firebase] pushing ' + str(data) + 'to ' + path + '...')
        db.reference(path).set(data)
    def update (self, path, data):
        print ('[Firebase] pushing ' + str(data) + 'to ' + path + '...')
>>>>>>> e50165ac40ebc3d885aa3c27cdf9e22c3b99ba62
        db.reference(path).set(data)