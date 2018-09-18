
import os
import spotipy
from json.decoder import JSONDecodeError
import spotipy.util as util

def Spotify_auth(client_id, client_secret):
    """Required to use Spotify's API start with this always must pass a client ID & client secret"""
    try:
        token = util.prompt_for_user_token("Alvin Chung",
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri="https://example.com/callback/")
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-Alvin Chung")
        token = util.prompt_for_user_token("Alvin Chung",
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri="https://example.com/callback/")


    spotify = spotipy.Spotify(auth=token)
    return spotify

