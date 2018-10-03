# gkeep-evernote-sync

## Summary

This is a work in progress. 

I've written a simple script in Python to sync my shopping list note (or any note) stored on Google Keep with an Evernote note. This is because Apple doesn't like Google and I can't use Google Keep on my Apple Watch, which where is where I'd like to see my shopping list. Evernote on the other hand will work on WatchOS.

_"Why don't you just use Evernote then?"_

Because I have heaps of notes in Google Keep already including shared notes with people. 

## Usage
#### Option 1 - Lambda + Schedule

I'm aiming to have the script run via aws Lambda on a schedule, say once a minute. Nice and simple.

#### Option 2 - Docker + cron


As an alternative to Lambda (just for fun I guess) I'd like to be able to run the script on a cron schedule in a container. Then use something like aws ECS/Fargate to deploy.