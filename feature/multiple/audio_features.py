

import pandas as pd



def get_audio_features(spotify,ids):
    """ Pass in a Series of Spotify song id's and returns a Dataframe"""

    print("Starting audio feature collection")
    music_features = pd.DataFrame(spotify.audio_features(ids))
    print("Finishe audio feature collection")
    return music_features
    




