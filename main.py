import os
import jinja2
import webapp2

from google.appengine.ext import db

#set templet directory
template_dir = os.path.join(os.path.dirname(__file__),'templates')
#add jinja environment
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
    autoescape = True)

import hashlib

def hash_str(s):
    return hashlib.md5(s).hexdigest()

def make_secure_val(s):
    return '%s|%s' %(s,hash_str(s))

print hash_val("apexa")

def check_secure_val(h):
    ###Your code here
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val


class Handler(webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template , **kw))

class MainHandler(Handler):
  def get(self):
      visits = 0
      visits_cookie_str = self.request.cookies.get('visits')
      if visits_cookie_val:
        cookie_val = check_secure_val(visits_cookie_str)
        if cookie_val:
          visits = int(cookie_val)
      visits +=1
      new_cookie_val = make_secure_val(str(visit))
      self.response.headers.add_header('Set-Cookie' , 'visits = %s' %visits)

      if visits >10:
        self.write("you are the Best!!")
      else:
        self.write("you've been here %s times!" %visits)


app = webapp2.WSGIApplication([
                              ('/',MainHandler),
                              ], debug= True)