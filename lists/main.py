# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

films = []
film = ""
golden_globe_films = ["jaws", "star sars: episode iv – a new hope","e.t. the extra-terrestrial","memoirs of a geisha"]
toto_albums = ["Fahrenheit","The Seventh One","Toto XX","Falling in Between","Toto XIV"]
albums = []


def alphabetical_order(films):
    films = sorted(films)
    return films

def won_golden_globe(film):
    #film = film.lower
    if film.lower() in(golden_globe_films):
        return True
    return False

def remove_toto_albums(albums):
    if "Fahrenheit" in albums:
        albums.remove("Fahrenheit")
    if "The Seventh One" in albums:
        albums.remove("The Seventh One")
    if "Toto XX" in albums:
        albums.remove("Toto XX")
    if "Falling in Between" in albums:
        albums.remove("Falling in Between")
    if "Toto XIV" in albums:
        albums.remove("Toto XIV")
    if "Old Is New" in albums:
        albums.remove("Old Is New")    
    return albums
