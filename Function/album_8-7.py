def make_album(band_name, album_title, num_tracks=''):
    album = {'Band': band_name, 'Album': album_title}
    if num_tracks:
        album['#Tracks'] = num_tracks
    return album

album_maker = make_album('Arctic Monkeys', 505)
print(album_maker)

album_maker = make_album('Tame Impala', 'Currents', 12)
print(album_maker)

album_maker = make_album('Ghostly Kisses', 'Darkroom')
print(album_maker)