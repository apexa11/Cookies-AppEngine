import hashlib

def hash_str(s):
    return hashlib.md5(s).hexdigest()

def make_secure_val(s):
    return '%s,%s' %(s,hash_str(s))

print make_secure_val("apexa")

def check_secure_val(h):
    ###Your code here
    val = h.split(',')[0]
    if h == make_secure_val(val):
        return val

print check_secure_val("apexa,4283e6e0e2cd4456abdd5012e67346f5")

