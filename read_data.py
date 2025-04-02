# read as pandas dataframe the data from Land_and_Ocean_summary.txt
# there is a short introduction at the beginning introduced by '%' in each line,
# then proceeded by a table in which columns are separated by tabulation

import pandas as pd

def read_land_ocean_data(file_path):
  """Reads data from Land_and_Ocean_summary.txt and returns it as a pandas DataFrame."""

  # Read the file, skipping lines starting with '%'
  df = pd.read_csv(file_path, sep='\s+', comment='%')

  # Assign column names
  df.columns = ['Year', 'Annual_Anomaly', 'Annual_Unc', 'Five-year_Anomaly', 'Five-year_Unc',
              'Annual_Anomaly_2', 'Annual_Unc_2', 'Five-year_Anomaly_2', 'Five-year_Unc_2']

  return df
