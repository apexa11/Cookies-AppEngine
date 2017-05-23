import hashlib

def hash_str(s):
    return hashlib.md5(s).hexdigest()

def hash_val(s):
    return '%s,%s' %(s,hash_str(s))

print hash_val("apexa")
