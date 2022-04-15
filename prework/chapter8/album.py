def make_album(a_name, a_title, a_age = ''):
    album = {'artist' : a_name, 'album' : a_title}

    if a_age:
        album['age'] = a_age
    return album

made_album = make_album('connor', 'beat')
print(made_album)