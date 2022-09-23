import pandas as pd

spacex_df = pd.read_csv("spacex_launch_dash.csv")
print(spacex_df['Launch Site'].unique())

