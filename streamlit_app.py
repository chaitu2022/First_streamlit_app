## CREATING NEW STREMLIT_APP.PY FOR SNOWFLAKE DEMO
import streamlit
import pandas
streamlit.title ('My FIRST APP')
streamlit.title('my Husbands\'s healthy Breakfst')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
## Set the fruit as index 
my_fruit_list = my_fruit_list.set_index('Fruit')
## Let's put a list of the fruits to pick from user selection 
fruits_selected = streamlit.multiselect("PIck some fruits:" ,list(my_fruit_list.index),['Avocado','Apple'])
fruits_to_show = my_fruit_list.loc(fruits_selected)
## Display the table on the page 
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)
