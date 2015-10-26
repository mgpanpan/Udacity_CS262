# 06 Selecting Substrings
print("hello"[1:3])
print("hello"[1:])

def myfirst_yoursecond(p, q):
    i = p.find(" ")
    j = q.find(" ")
    return p[:i] == q[j+1:]

print(myfirst_yoursecond("hello world", "python hello"))
