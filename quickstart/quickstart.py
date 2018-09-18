

from feature.multiple import charting
from feature.multiple import search_songs, audio_features
from feature.beta import featured
from feature.multiple import playlist
import pandas as pd

def quickstart_charting(spotify, date):
    chartings = charting.get_top100(date)
    charting_df = search_songs.get_spotify_id(spotify, chartings['title'])
    charting_audio_features = audio_features.get_audio_features(spotify, charting_df['id'])
    return charting_audio_features


def quickstart_featured(spotify):
    categories = featured.get_categories(spotify)
    playlists = featured.get_playlists(spotify, categories)
    songs = featured.get_songs(spotify, playlists)
    songs_df = pd.DataFrame(list(set(songs)))
    df = featured.get_track_info(songs_df)
    return df




def quickstart_playlist(spotify, username, playlist_id):
    songs = playlist.get_playlist_tracks(spotify, "Spotify", "37i9dQZF1DWVYHdtUb7Wil")
    results = playlist.get_music_data(spotify, songs)
    return results

