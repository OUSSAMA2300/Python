def make_album(artist_name, album_title, num_tracks=''):
    album = {'artist': artist_name, 'album': album_title}
    if num_tracks:
        album['#tracks'] = num_tracks
    return album

# Created a list of dicionaries to show all the albums that's been created
albums = []

while True:
    print("\nPlease enter the album details:")
    print("(enter 'q' at any time to quit)")
    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break

    
    track_nums = input("#Tracks (Optional): ")
    album_maker = make_album(artist, title, num_tracks=track_nums)
        
    albums.append(album_maker)

print("\nAlbum created:")
for album in albums:
    print(album)