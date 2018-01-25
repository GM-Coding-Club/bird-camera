import firebase_admin # firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("./firebaseKey.json")
firebase_admin.initialize_app(cred)

# db class
class rdb:
    def get (self, path):
        return db.reference(path).get()