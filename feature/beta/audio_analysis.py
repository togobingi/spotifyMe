
import pandas as pd
from util.helper_function import set_data_to_sql

def get_audio_analysis(spotify,id):
    """pass in individual Spotify Id's and query the audio analysis"""
    temp = spotify.audio_analysis(id)
    beats = pd.DataFrame(temp['bars'])
    beats['id'] = id
    beats = beats.set_index(['id'])
    sections = pd.DataFrame(temp['sections'])
    sections['id'] = id
    sections = sections.set_index(['id'])
    segments = pd.DataFrame(temp['tatums'])
    segments['id'] = id    
    segments = segments.set_index(['id'])
    return beats, sections, segments


# In[63]:



# Ok this takes way to fcking LONG ROFL
def superhuman_audio_query(ids):
    """Parameters:
            (Series) ids: Pass in a Series of Spotify Id's """
    for idx, result in enumerate(ids):
        beats, sections, segments = get_audio_analysis(result)
        set_data_to_sql(beats, 'spotify_beats')
        set_data_to_sql(sections, 'spotify_sections')
        set_data_to_sql(segments, 'spotify_segments')

