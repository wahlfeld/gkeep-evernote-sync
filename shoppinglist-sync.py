#import modules
import gkeepapi
import os
import textile
from evernote.api.client import EvernoteClient
from evernote.edam.type import ttypes

#setting environment variables
user = os.environ['GKEEP_USERNAME']
pw = os.environ['GKEEP_APP_PASSWORD']
noteId = os.environ['GKEEP_NOTE_ID']
authToken = os.environ['EVERNOTE_DEV_TOKEN']
noteGuid = os.environ['EVERNOTE_NOTE_ID']

#keep login
keep = gkeepapi.Keep()
keep.login(user, pw)

#getting keep note contents and converting to html
syncnote = keep.get(noteId)
syncnotebody = syncnote.text
enotepayload = textile.textile(syncnotebody)

#evernote login
client = EvernoteClient(token=authToken)
userStore = client.get_user_store()
user = userStore.getUser()

#updating the evernote note with the keep note contents
noteStore = client.get_note_store()
note = ttypes.Note()
note.guid = noteGuid
note.title = 'Shopping List' #not sure if I should make this a variable
note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd"><en-note>' + enotepayload + '</en-note>'
noteStore.updateNote(authToken,note)
noteDone = noteStore.updateNote(authToken,note)

#uncomment line below if you want to do a get note
#print noteStore.getNote(authToken,noteGuid,True,True,True,True)
