# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name , tamplete = 1):
        if tamplete == 1:
                greet = f"Hello, {name}"
                return greet
        else:
                greet = F"{tamplete}{name}"
                return greet
        
print(greet("Jesse"))
