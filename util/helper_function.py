
import time
import json
import pandas as pd
from sqlalchemy import create_engine



def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__, 'took', end - start, 'seconds')
        return result
    return f_timer




def json_dump(json_file, data):
    """JSON dump, 
    Parameters:
        (String) json_file: filename of json you want to save as
        (json) data: data passed in which you want to save as Json"""
    with open('{}'.format(json_file), 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)


def set_pickle(filepath, df):
    """Pickle information"""
    df.to_pickle("{}.pkl".format(filepath))
    
def get_pickle(filepath):
    """Load pickled information"""
    df = pd.read_pickle("{}.pkl".format(filepath))
    return df


def set_data_to_sql(df, table_name, username, password):
    """Send data to databse
    Parameters:
        (DataFrame) df: pass Dataframe to put into Database
        table_name: name of table you want
        """
    engine = create_engine('postgresql://{}:{}@localhost:5432/postgres'.format(username, password))
    df.to_sql(table_name, con = engine, if_exists="append")

