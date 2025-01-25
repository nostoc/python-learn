# def city_country(city,country):
#     location = print(f"{city.title()}, {country.title()}")
#     return location

# city_country("gampaha","sri lanka")
# city_country("Melbourn","Australia")
# city_country("Nagasaki","japan")

def make_album(artist_name,album_title,number_of_songs = None):
    if number_of_songs:
        music_album_info = {'artist name':artist_name.title(),'album title':album_title,'# of songs':number_of_songs}
    else:
        music_album_info = {'artist name':artist_name.title(),'album title':album_title}
    return music_album_info

ed_sheeran = make_album("Ed sheeran","Never let you go",12)
wayo = make_album("Wayo","6 th lane amma")
msunil = make_album("Sunil shantha","olu pipiila")

print(ed_sheeran)
print(wayo)
print(msunil)


while True:
    print("\nPlease enter 'q' at any time to exit.")
    print("\n Enter artists name : ")
    artist_name = input("Artist's name : ")
    if artist_name == 'q':
        break
   
    album_name =  input("\nEnter album name : ")
    if album_name == 'q':
        break

    album_info = make_album(artist_name,album_name)
    print(album_info)
    
