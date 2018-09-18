
import billboard
import pandas as pd 






def get_top100(date):
    """Get to top 100 songs
    parameters:
            date: year-Month-day eg. 2018-09-10"""
    charts = billboard.ChartData("hot-100", date=date, fetch=True)
    top100 = [{'title': chart.title, 'artist': chart.artist} for chart in charts]
    df_top100 = pd.DataFrame(top100)
    return df_top100


