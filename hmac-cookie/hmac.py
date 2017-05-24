#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import hmac

# Implement the hash_str function to use HMAC and our SECRET instead of md5
SECRET = 'imsosecret'
def hash_str(s):
    ###Your code here
    return hmac.new(SECRET,s).hexdigest()


def make_secure_val(s):
    return '%s,%s' %(s,hash_str(s))

print make_secure_val("apexa")

def check_secure_val(h):
    ###Your code here
    val = h.split(',')[0]
    if h == make_secure_val(val):
        return val

print check_secure_val("apexa,4283e6e0e2cd4456abdd5012e67346f5")


