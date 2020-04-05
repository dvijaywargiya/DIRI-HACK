# Pandas for data management
import pandas as pd

# os methods for manipulating paths
from os.path import dirname, join

# Bokeh basics 
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs


# Each tab is drawn by one script
from scripts.histogram import histogram_tab
from scripts.density import density_tab
from scripts.table import table_tab
from scripts.draw_map import map_tab
from scripts.routes import route_tab
from scripts.histogram_me import histogram_tab_me

# Using included state data from Bokeh for map
from bokeh.sampledata.us_states import data as states

# Read data into dataframes
flights = pd.read_csv(join(dirname(__file__), 'data', 'flights.csv'), 
	                                          index_col=0).dropna()

bangalore_discord = pd.read_csv("./ISB_B/discord_bangalore.csv", sep=";")
bangalore_discord = bangalore_discord[bangalore_discord['Series'] == "Discord Social Volume"] 
# print(bangalore_discord)

bangalore_telegram = pd.read_csv("./ISB_B/telegram_bangalore.csv", sep=";")
bangalore_telegram = bangalore_telegram[bangalore_telegram['Series'] == "Telegram Social Volume"] 
# print(bangalore_telegram)

bangalore_reddit = pd.read_csv("./ISB_B/reddit_bangalore.csv", sep=";")
bangalore_reddit = bangalore_reddit[bangalore_reddit['Series'] == "Reddit Social Volume"] 
# print(bangalore_reddit)

frames = [bangalore_discord, bangalore_reddit, bangalore_telegram]
result = pd.concat(frames)
# # Formatted Flight Delay Data for map
# map_data = pd.read_csv(join(dirname(__file__), 'data', 'flights_map.csv'),
#                             header=[0,1], index_col=0)

# # Create each of the tabs
tab1 = histogram_tab(flights)
tab2 = histogram_tab_me(result)
# tab2 = density_tab(flights)
# tab3 = table_tab(flights)
# tab4 = map_tab(map_data, states)
# tab5 = route_tab(flights)

# Put all the tabs into one application
tabs = Tabs(tabs = [tab1])

# Put the tabs in the current document for display
curdoc().add_root(tabs)


