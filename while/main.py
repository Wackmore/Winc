from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())
    
def unique_koala_facts(amount):
    factlist = []
    facts = 0
    i = 0
    while facts != amount and i < 1000:
        string = random_koala_fact()
        if string not in factlist:
            factlist.append(string)
            facts = facts + 1
        i = i +1
    #print(factlist)
    facts = int(facts)     
    return factlist

def num_joey_facts():
    factlist = []
    amount = 0
    joey_facts = 0
    while amount != 1000:
        string = random_koala_fact()
        if string not in factlist and "joey" in string:
            factlist.append(string)
            joey_facts = joey_facts + 1
        amount = amount + 1
    print(factlist)     
    return joey_facts

def koala_weight():
    weight = 0
    while weight == 0:
        string = random_koala_fact()
        if "kg" in string:            
            weight = string[-5:-3]
            weight = int(weight)
            print (weight)
            return weight

    return weight

#koala_weight()
#print (num_joey_facts())
#print (unique_koala_facts(10))