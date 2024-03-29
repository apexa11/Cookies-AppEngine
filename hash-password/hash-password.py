import random
import string
import hashlib

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

# implement the function make_pw_hash(name, pw) that returns a hashed password
# of the format:
# HASH(name + pw + salt),salt
# use sha256

def make_pw_hash(name, pw, salt = None):
    ###Your code here
    if not salt:
    salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' %(h,salt)

def valid_pw(name, pw, h):
    ###Your code here
    salt = h.split(',')[1]
    return h == make_pw_hash(name,pw,salt)

h = make_pw_hash('apexa', 'patel')
print valid_pw('apexa', 'patel', h)