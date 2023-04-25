from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
def shortest_names(list):
    list = sorted(list, key=len)
    shortest_name = len(list[0])
    short_name_list=[]   
    for name in list:
        if len(name) == shortest_name:
            short_name_list.append(name)
            print (short_name_list)
            continue
    return (list)


def most_vowels(countries):
    vowel_list = []
    for name in countries:
        num_vowels = 0       
        for char in name:
            if char in "aeiouAEIOU":
                num_vowels = num_vowels +1
        vowel_per_country = F"{num_vowels}{name}" 
        vowel_list.append(vowel_per_country)   
        print(vowel_list)   
        #hiernaa haal ik de nummers uit de data, om de juiste volgorde te krijgen met de orignele namen.
        #print (vowel_per_country)
    vowel_list = vowel_list.sort()
    print (vowel_list)
    return vowel_list




def alphabet_set(countries):
    countries = sorted(countries)
    return (countries)

most_vowels(countries)
