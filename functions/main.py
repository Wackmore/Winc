# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

Nr = -69

def greet (name) :
    return F"Hello, {name}!"


def add (x,y,z):
    x = int(x)
    y = int(y)
    z = int(z)

    return (x+y+z)

def positive (x):
    x = int(x)
    if x >= 0:
        return True
    else:
        return False

def negative (x):
    if positive(x) == True:
        return False
    else:
        return True

print (greet("Bob"))
print (add (5,3,2))
print (positive(Nr))
print (negative(Nr))


