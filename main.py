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
import random

def GetRandomFortune():
    fortunes = [
    'Family, friends, food. These are what matter most.',
    'Slow down! Life is to be savored.',
    'Moderation in all things, including moderation.'
    'Abstain from wine, women, and song. Especially song.'
    ]
    fortune_num = random.randint(0,3)
    return fortunes[fortune_num]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        init = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8" />'
#        style = '<link rel="stylesheet" type="text/css" href="styles.css" />'
        title = '<title>Fortune Cookies!</title>'
        end_init = '</head><body>'
        header = '<h1>Fortune Cookie</h1>'
        fortune = '<p><strong>' + GetRandomFortune() + '</strong></p>'
        lucky_num = random.randint(1, 100)
        lucky_num_para = '<p>Your lucky number: <strong>' + str(lucky_num) + '</strong></p>'
        new_fortune = '<a href="."><button>Get me another fortune!</button></a>'
        end_page = '</body></html>'
        content = init + title + end_init + header + fortune + lucky_num_para + new_fortune + end_page
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
