# import Streamlit.
import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import neattext.functions as nfx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import altair as alt

st.write("Alejandra Mollo  21800242")

# import the Bible module.
from Bible import Bible

# create an instance of the Bible class.
my_bible = Bible()

# initialize the Bible module.
my_bible.init()

# implement a Bible search app using Streamlit.

# Title
st.title('Handong Bible App')

# Header
st.header("This is the Heading")

# Subh
st.subheading("This is the subheading")

#text
st.text("Hello this is Ale's Bible")

# success, info
st.sucess("Executed successfully")
st.info("This is an information")
st.warning("This is a warning")
st.error("An error occured")
channel = "iakdskjfdkj"
st.write("Subscribe to my channel", channel)

#Text input box
name = st.text_input("Enter the Bible name", "Bible Name")

book, chapter, verse = name.split(name)
text = my_bible.search(book, int(chapter), int(verse))
#button
st.button("Click here")

if(st.button("click here")):
    st.text(f"{st.write(text)}")
