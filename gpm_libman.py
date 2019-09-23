# https://unofficial-google-music-api.readthedocs.io/en/latest/index.html

import glob
import sys

from gmusicapi import Mobileclient
from gmusicapi import Musicmanager


def 

#### Parameters
music_dir = '/home/conor/Music/'

#### Authenticate gpm connection


mc = Mobileclient()
# Line below only done once and token saved to disk
# mc.perform_oauth()
mc.oauth_login(mc.FROM_MAC_ADDRESS) # Uses token from above

mm = Musicmanager()
# mm.perform_oauth()


#### Get mp3 file names from music folder
local_song_names = glob.glob(music_dir + '*.mp3')

#### Create dictionary of existing song ids
# { 'song_name': id }
song_ids = {}

gpm_songs = mc.get_all_songs()
for song in gpm_songs:
    song_ids[song['title']] = song['id']

#### Create dictionary of existing playlists ids
# { 'playlist_name': id }
playlist_ids = {}

gpm_playlists = mc.get_all_playlists()
for pl in gpm_playlists:
    playlist_ids[pl['name']] = pl['id']


if uploading:
    pass

if playlisting:
    pass

#### Add every song to playlists

def main():
    if len(sys.argv) != 3:
        print('Specify T/F arguments for uploading and updating playlists')
        print('e.g. python ' + sys.argv[0] + ' 0 1')
        print('which would:\n--> not upload new songs\n--> update playlists')
        sys.exit(0)
        
    print('Local music directory set to:', music_dir)
    accepted = input('Type "y" if this is correct directory: ')
    
    if accepted.lower() != 'y':
        sys.exit(0)
    
        
    # If True will upload all new music
    uploading = sys.argv[1]
    if uploading:
        mc = 
        
    # If True will update all playlists
    playlisting = sys.argv[2]
    if playlisting:
        mm.login()
        
   


if __name__ == '__main__':
    main()
