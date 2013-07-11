# old code
# from google.appengine.ext import webapp
# from google.appengine.ext.webapp.util import run_wsgi_app 

# from home import HomeHandler
# from bake import BakeHandler
# from image import ImageHandler
# from fbshare import FBShareHandler

import webapp2
import os
import sys
import logging
sys.path.insert(0, 'lib')			# not sure what this does 
sys.path.insert(0, 'requests')		# not sure what this does

# import pyimgur					# 3rd party modules
# import imgurpython
# import uploadimage

from home import HomeHandler
from fbshare import FBShareHandler
from image import ImageHandler


#class MainHandler(webapp2.RequestHandler):
#    def get(self):
#        self.response.write('Hello world!')



app = webapp2.WSGIApplication([
    ('/', HomeHandler),
	('/fbshare', FBShareHandler),
	('/image', ImageHandler),
], debug=True)

# old code
# appRoute = webapp.WSGIApplication( [
  # ('/', HomeHandler),
  # ('/bake', BakeHandler),
  # ('/image', ImageHandler),
  # ('/fbshare', FBShareHandler),
# ], debug=True)

# def main():
  # run_wsgi_app(appRoute)

# if __name__ == '__main__':
  # main()
