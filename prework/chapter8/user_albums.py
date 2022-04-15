def make_album(a_name, a_title, a_age = ''):
    album = {'artist' : a_name, 'album' : a_title}

    if a_age:
        album['age'] = a_age
    return album

while True:
    print("\nEnter your information here here: ")
    print("(enter 'q' to quit any time!)")
    artist = input("Enter the artist's name: ")
    if artist == 'q':
        break
    album_title = input("Enter the title here: ")
    if album_title == 'q':
        break

full_album = album_title.title() + ", made by" + artist.title()
print(full_album)
