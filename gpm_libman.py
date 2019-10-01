# https://unofficial-google-music-api.readthedocs.io/en/latest/index.html

import glob
import sys

from gmusicapi import Mobileclient
from gmusicapi import Musicmanager


def 

def required_playlists(songs):
    ''' 
    Args:
        songs: list of mp3 song file name
    Returns:
        list of playlist name strings
    '''

#### Create dictionary of existing playlists ids
# { 'playlist_name': id }
playlist_ids = {}

gpm_playlists = mc.get_all_playlists()
for pl in gpm_playlists:
    playlist_ids[pl['name']] = pl['id']


def main():
    #### Ensure user parameters/behaviour is clear

    # Parameters
    music_dir = '/home/conor/Music/'


    if len(sys.argv) != 3:
        print('Specify T/F arguments for uploading and updating playlists')
        print('e.g. python ' + sys.argv[0] + ' 0 1')
        print('which would:\n--> not upload new songs\n--> update playlists')
        sys.exit(0)
        
    print('Local music directory set to:', music_dir)
    accepted = input('Type "y" if this is correct directory: ')
    
    if accepted.lower() != 'y':
        sys.exit(0)

    #### Values useful for both 'sections'

    #### Get mp3 file names from music folder
local_song_names = glob.glob(music_dir + '*.mp3')

    # Create dictionary of existing song ids
    # { 'song_name': id }
    song_ids = {}

gpm_songs = mc.get_all_songs()
for song in gpm_songs:
    song_ids[song['title']] = song['id']

    #### Manage upload/deletion of songs
    uploading = sys.argv[1]
    if uploading:
        mm = Musicmanager()
        mm.login() # Authenticates using on-disk token


    #### Create and edit playlists as required
    playlisting = sys.argv[2]
    if playlisting:
        mc = Mobileclient()
        mc.oauth_login(mc.FROM_MAC_ADDRESS) # Authenticates using on-disk token

        


if __name__ == '__main__':
    main()
