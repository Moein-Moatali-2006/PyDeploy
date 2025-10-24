import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Simple Data science app")

with st.sidebar:
    st.write("""🦠 What is COVID-19?
            COVID-19 is a disease caused by a virus called coronavirus.
            It started in China in December 2019 and spread to almost every country in the world.
            People can get it when someone coughs, sneezes, or talks, and small drops with the virus go into the air.
            In this project I show you a Covid information in Iran.""")

upload_file = st.file_uploader("Please upload your .csv file:")

if upload_file is not None:
    st.success("Your file uploaded!")
    df = pd.read_csv(upload_file)
    st.write("Here is your head data: ")
    st.table(data=df.head())

    # Process in Iran
    st.write("New Deaths vs New Cases in Iran (April 2020)")
    df["Date"] = pd.to_datetime(df["Date"])  
    april_2020 = df[(df['Date'].dt.year == 2020) & (df['Date'].dt.month == 4)]
    
    iran_april_2020 = april_2020[(april_2020['CountryRegion'] == 'Iran')]

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(iran_april_2020['Date'], iran_april_2020['New deaths'], label='New Deaths', color='red')
    ax.plot(iran_april_2020['Date'], iran_april_2020['New cases'], label='New Cases', color='blue')

    ax.set_title('New Deaths vs New Cases in Iran (April 2020)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Count')
    ax.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(fig)
else:
    st.info("Upload your .csv file.")