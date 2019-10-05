# https://unofficial-google-music-api.readthedocs.io/en/latest/index.html

"""
*TO DO*
- improve console output information
- fix spacing after final ''x/y processed''
- sort issue with uplaoding renamed file (google rejects)
    - probably just delete songs first
"""

import glob
import os
import sys
import time

from gmusicapi import Mobileclient
from gmusicapi import Musicmanager

def required_playlists(song):
    ''' 
    Args:
        song: str song name
    Returns:
        list of playlist name strings
        
    example:
    'song - artist [abc].mp3' --> ['a', 'b', 'c']
    '''
    pls = song[song.find('[')+1:song.find(']')]
    
    return list(pls)


def main():
    
    if len(sys.argv) != 3:
        print('Specify T/F arguments for uploading and updating playlists')
        print('e.g. python ' + sys.argv[0] + ' 1 0')
        print('which would:\n--> upload new songs\n--> NOT update playlists')
        sys.exit(0)
    
    
    #### Parameters
    music_dir = '/media/conor/5451-8AC1/Music/' # '/home/conor/Music/'
    print('Local music directory set to:', music_dir)
    accepted = input('Type "y" if this is correct directory: ')
    if accepted.lower() != 'y':
        print('Ending music management.')
        sys.exit(0)


    #### Manage upload/deletion of songs
#    uploading = sys.argv[1]
#    if uploading:
    mm = Musicmanager()
    mm.login() # Authenticates using on-disk token


    #### Create and edit playlists as required
#    playlisting = sys.argv[2]
#    if playlisting:
    mc = Mobileclient()
    mc.oauth_login(mc.FROM_MAC_ADDRESS) # Authenticates using on-disk token
    
    print('Authentication complete...')
    
    #### Get mp3 file names from music folder
    local_song_paths = glob.glob(music_dir + '*.mp3')
    
    # Get individual song names
    local_song_names = set()
    for p in local_song_paths:
        _, song_name = os.path.split(p)
        local_song_names.add(song_name)

    song_ids = {}
    gpm_songs = mc.get_all_songs()
    for song in gpm_songs:
        song_ids[song['title']] = song['id']
    
    #### Uploading 
    to_upload = []
    for s in local_song_names:
        if s not in song_ids:
            to_upload.append(music_dir + s)
    print('{} songs to upload.'.format(len(to_upload)))
    accepted = input('Type "y" to commence upload now: ')
    if accepted.lower() != 'y':
        print('Ending music management.')
        sys.exit(0)
    mm.upload(to_upload)
    
    
    #### Delete songs that no longer exist locally
    to_delete = set()
    for song in song_ids:
        if song not in local_song_names:
            to_delete.add(song)
    print('{} songs to delete:'.format(len(to_delete)))
    print([s for s in to_delete])
    
    # delete_songs() method requires a list as input
    to_delete_ids = []
    for s in to_delete:
        song_id = song_ids[s]
        to_delete_ids.append(song_id)
    print(to_delete_ids)
    mc.delete_songs(to_delete_ids)
    print('Deleted songs.')    
    
    #### Update playlists
    
    # Refresh song list
    song_ids = {}
    gpm_songs = mc.get_all_songs()
    for song in gpm_songs:
        song_ids[song['title']] = song['id']
        
    # Flush old playlists
    print('Deleting old playlists...')
    gpm_playlists = mc.get_all_playlists()
    for pl in gpm_playlists:
        mc.delete_playlist(pl['id'])
    
    playlist_ids = {}
    total = len(song_ids)
    completed = 0
    
    # Create and update playlists
    print('Organising songs:')
    for s in song_ids:
        sid = song_ids[s]
        req_pls = required_playlists(s)
        for pl in req_pls:
            if pl in playlist_ids:
                pid = playlist_ids[pl]
            else:
                pid = mc.create_playlist(name=pl)
                playlist_ids[pl] = pid
                
            mc.add_songs_to_playlist(pid, sid)
        completed += 1
        sys.stdout.write("\r{}/{} processed".format(completed,total))
        sys.stdout.flush()
    print()

if __name__ == '__main__':
    main()
