# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line

def create_passport(name , date_of_birth , place_of_birth , height , nationality):
    # date of birth stored as year-month-day (ISO 8601).
    passport = {
        'name' : name,
        'date_of_birth' : date_of_birth,
        'place_of_birth' : place_of_birth,
        'height' : height,
        'nationality' : nationality
    }

    return passport

def add_stamp(passport,country):

    if country != passport["nationality"]:
        if country not in passport["nationality"]:
            passport.update({"stamps":country})
   
    return passport


def add_biometric_data(passport,data_name,biometric_data,date):
    biometric = {
        "biometric" :{
            data_name : {
                "date" : date,
                "value": biometric_data
    }}}
    passport.update(biometric)
    return passport





#print (create_passport("kaas","1998-04-14","Haarlem","1.78","Netherlands"))
#print (add_stamp(create_passport("kaas","1998-04-14","Haarlem","1.78","Netherlands"),"Netherlands2"))