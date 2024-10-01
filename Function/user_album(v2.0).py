def make_album(artist_name, album_title, num_tracks=''):
    album = {'artist': artist_name, 'album': album_title}
    if num_tracks:
        album['#tracks'] = num_tracks
    return album

while True:
    print("\nPlease enter the album details:")
    print("(enter 'q' at any time to quit)")
    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break
    
    num_tracks = input("#Tracks (Optional) ")
    
    album_maker = make_album(artist, title, num_tracks)
    print(f"\nAlbum created: {album_maker}")