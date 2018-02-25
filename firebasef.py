import firebase_admin # firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

from conf import firebase

cred = credentials.Certificate("./serviceKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': firebase['database_url'],
    'storageBucket': firebase['storage_bucket']
})

bucket = storage.bucket()

# db class
class rdb:
    def get (self, path):
        print ('[Firebase] getting ' + path + '...')
        return db.reference(path).get()
    def push (self, path, data):
        print ('[Firebase] pushing ' + str(data) + 'to ' + path + '...')
        db.reference(path).push().set(data)
    def update (self, path, data):
        print ('[Firebase] pushing ' + str(data) + 'to ' + path + '...')
        db.reference(path).update(data)

class fs:
    def add (self, path, fname, file):
        blob = bucket.blob(path)
        blob.upload_from_filename(file)
        return ('https://firebasestorage.googleapis.com/v0/b/' + firebase['storage_bucket'] + '/o/images%2F' + fname + '?alt=media')
