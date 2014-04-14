#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from datetime import datetime
import os
import jinja2
import logging
from google.appengine.ext import db

class Artist(db.Model):
    artist = db.StringProperty(required = True)
    members = db.StringListProperty()
    albums = db.StringListProperty(required = True)
    associated = db.StringListProperty()
    genres = db.StringListProperty()

class Record(db.Model):
    album = db.StringProperty(required = True)
    artist = db.StringProperty(required = True)
    personnel = db.StringListProperty()
    label = db.StringProperty()
    year = db.StringProperty()
    producers = db.StringListProperty()
    genres = db.StringProperty()
    tracks = db.StringListProperty(required=True)
    frontCover = db.StringProperty()
    backCover = db.StringProperty()
    inside = db.StringProperty()
    notes = db.TextProperty()
    dateAdded = db.DateProperty(auto_now_add = True)

class Person(db.Model):
    first = db.StringProperty(required = True)
    last = db.StringProperty()

class Genre(db.Model):
    name = db.StringProperty(required = True)
    subs = db.ListProperty(db.Key)

class SubGenre(db.Model):
    name = db.StringProperty(required = True)
    parent = db.Key

templateDir = os.path.join(os.path.dirname(__file__), 'templates')
jinjaEnv = jinja2.Environment(loader = jinja2.FileSystemLoader(templateDir), autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def renderStr(self, template, **params):
        t = jinjaEnv.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.renderStr(template, **kw))

yearList = list()
for year in range(1920, datetime.now().year+1):
    yearList.append(year)
yearList.append('')
yearList.reverse()

genreList = ['alternative', 'bluegrass', 'blues', 'folk', 'jazz', 'rock']

'''def recent16(update = False):
    key = 'recent'
    art = memcache.get(key)
    if art is None or update:
       art = db.GqlQuery('select * from Record order by dateAdded desc limit 16')
       art = list(art)
       memcache.set(key, art)
    return art'''

class MainPage(Handler):
    def get(self):
        '''art = recent16()
        art1 = art[:3]
        art2 = art[4:7]
        art3 = art[8:11]
        art4 = art[12:]'''
        self.render('main.html', genreList = genreList, art1 = "", art2 = "", art3 = "", art4 = "")

class AddPage(Handler):
    def renderPost(self):
        self.render('add.html', genreList = genreList, years = yearList, album = '', artist = '', personnel = '', label = '', year = '', producers = '',
                    genres = '', frontCover = '', backCover = '', inside = '', notes = '', error = '')

    def get(self):
        self.renderPost()

    def post(self):
        album = self.request.get('album')
        artist = self.request.get('artist')

        num = 1
        personnel = list()
        person = self.request.get('personnel1')
        while (person):
            personnel.append(person)
            num = num+1
            person = self.request.get('personnel%d' %num)

        label = self.request.get('label')
        year = self.request.get('year')

        num = 1
        producers = list()
        producer = self.request.get('producer1')
        while (producer):
            producers.append(producer)
            num = num+1
            producer = self.request.get('producer%d' %num)

        genres = self.request.get('genres')
        frontCover = self.request.get('frontCover')
        backCover = self.request.get('backCover')
        inside = self.request.get('inside')
        notes = self.request.get('notes')

        num = 1
        tracks = list()
        track = self.request.get('track1')
        while (track):
            tracks.append(track)
            num = num+1
            track = self.request.get('track%d' %num)

        if album and artist and tracks:
            record = Record(album = album, artist = artist, personnel = personnel, label = label, year = year, producers = producers,
                            genres = genres, tracks = tracks, frontCover = frontCover, backCover = backCover, inside = inside, notes = notes)

            recordId = record.put()

            self.redirect('/record%d' %recordId.id())
        else:
            error = 'Ooops...album, artist & tracks must be added!'
            self.renderPost(album = album, artist = artist, personnel = personnel, label = label, year = year, producers = producers,
                            genres = genres, tracks = tracks, frontCover = frontCover, backCover = backCover, inside = inside, notes = notes, error = error)

class RecordPage(Handler):
    def get(self, recordId):
        record = Record.get_by_id(int(recordId))

        if record:
            self.render('record.html', genreList = genreList, record = record)
        else:
            self.error(404)
            return

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/add', AddPage),
    (r'/record(\d+)', RecordPage)
], debug=True)
