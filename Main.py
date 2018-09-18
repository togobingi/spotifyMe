

from auth import authentication
from feature.multiple import charting
from feature.multiple import search_songs
from quickstart import quickstart
from util import helper_function

if __name__== "__main__":
    #spotify = authentication.Spotify_auth("asd")
    df = quickstart.quickstart_charting(spotify, "2018-09-10")
    helper_function.set_pickle("./charting",df)
