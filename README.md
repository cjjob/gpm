#### Some extra gpm functionality

The upload/download bit will work with any music formats.

The playlist management is coded with implicit assumuption that file names have the following format:
* *song_name* - *artist_name* **[single_letter_playlist_tags]**.mp3
* e.g. new soul - yael naim [ac].mp3

i.e. do not use '\[' and '\]' anywhere else in the file name\!


##### Initial run

Current version of code assumes that authentication tokens are already saved to disk. See the [docs](https://unofficial-google-music-api.readthedocs.io/en/latest/index.html). 
