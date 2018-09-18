

import pandas as pd




def get_spotify_id(spotify, series):
    """Pass in a Series which the function loops through the songs, queries the data and puts it into a Dataframe
    parameters: 
            df: DataFrame
            column_name: column name of the column in the the Dataframe with the song titles
    """
    print("getting ready Rrrrrrrrr")
    print("starting")
    mydict = []
    for idx, song_title in enumerate(series):
        song = spotify.search(song_title)['tracks']['items'][0]
        mydict.append({
            'id': song['id'],
            'title': song_title
        })
    df = pd.DataFrame(mydict)

    print("Finished")
    return df