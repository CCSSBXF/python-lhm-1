def make_album(singer_name,album_name):
    album={'a':singer_name,'b':album_name}
    return album

while True:
    s_name = input('singer name')
    a_name = input('album_name')
    album = make_album(s_name,s_name)
    print(album)
    ifquit = input("'q' to quit ,else to continue")
    if ifquit == 'q':
        break



