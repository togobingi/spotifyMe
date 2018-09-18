
import pandas as pd




def get_playlist_tracks(spotify, username,playlist_id):
    """Parameters:
        (String) username: username of playlist owner
        (String) playlist_id: the playlist id """
    results = spotify.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    return tracks



def get_music_data(spotify,songs):
    """
    parameters:
        Used in tandem with the get_playlist_tracks,
        pass in the variable from the query of get_playlist_track to preprocess the data into a Dataframe
    """
    mydict = []
    for song in songs:
        mydict.append({
            'id': song['track']['id'],
            'name': song['track']['album']['name'],
            'release_date': song['track']['album']['release_date'],
            'added_at':song['added_at'],
            'album_type': song['track']['album']['album_type'],
            'artist': song['track']['album']['artists'][0]['name'],
            'popularity': song['track']['popularity'],
            'personal_type': 'favourite'
        })
    df = pd.DataFrame(mydict)
    music_features = pd.DataFrame(spotify.audio_features(df['id']))
    df = df.merge(music_features)
    df.set_index(keys=['id'], inplace=True)
    
    return df