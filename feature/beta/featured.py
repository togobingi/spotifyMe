
import time
import pandas as pd




# get categories
def get_categories(spotify):
    category_ids = []
    for i in spotify.categories(limit = 50)['categories']['items']:
        category_ids.append(i.get('id'))
    return category_ids


def get_playlists(spotify,categories):
    playlist_ids = []
    for i in categories:
        for j in spotify.category_playlists(i, limit = 50)['playlists']['items']:
            playlist_ids.append(j.get('id'))
    return playlist_ids


# In[46]:


# get song ids from list of playlist ids
def get_songs(spotify, playlists):
    song_ids = []
    for i in playlists:
        try:
            for j in spotify.user_playlist('spotify', i)['tracks']['items']:
                song_ids.append(j['track']['id'])
        except:
            pass
        time.sleep(.1)
    return song_ids



def get_track_info(df_ids):
    """Featured songs preprocessing used in tandem with get songs:
    Parameters:
        VERY TRICKY
        df_ids: pass in the Dataframe what was given by get_songs
    """
    df = pd.DataFrame()
    n = 50
    list_df = [df_ids[i:i+n] for i in range(0,df_ids.shape[0],n)]
    print("Starting")
    for idx, ids in enumerate(list_df):
        try:
            details = spotify.tracks(list_df[idx][0])
            queried_data = json_normalize(details['tracks'], record_path=['artists'], meta =['popularity', 'id' , 'name', 
                                                                   'is_local', 'type', 'uri', 'href', 'explicit',
                                                                   'duration_ms', 'disc_number','track_number'], record_prefix='artist_' )

            music_features = pd.DataFrame(spotify.audio_features(queried_data['id']))
            temp = music_features.merge(queried_data, left_on = 'id', right_on='id')
            df = df.append(temp)
            print("Thank you!")
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue
        df.set_index(keys=['id'], inplace=True)
        
    return df

