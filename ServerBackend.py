import random
import string

import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open ('ServerFrontend.html')

    @cherrypy.expose
    def test(self, length = 8):                 #Wenn link "localhost/test?length=x" angegeben wird, wird ein random string der länge x erstellt
        return ''.join(random.sample(string.hexdigits, int(length)))

    @cherrypy.expose
    def display(self):
         return cherrypy.session['mystring']    #Scheiss auf fehler, funktin

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)