package main

// need to convert to golang
import (
	"gkeepapi"
	"os"
	"textile"
	from evernote.api.client import EvernoteClient
	from evernote.edam.type import ttypes
)

// this is a comment

// setting environment variables
// need to convert to golang
user = os.environ['GKEEP_USERNAME']
pw = os.environ['GKEEP_APP_PASSWORD']
noteId = os.environ['GKEEP_NOTE_ID']
authToken = os.environ['EVERNOTE_DEV_TOKEN']
noteGuid = os.environ['EVERNOTE_NOTE_ID']

// keep login
keep = gkeepapi.Keep()
keep.login(user, pw)