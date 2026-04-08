import streamlit as st
import pickle
import pandas as pd
import os
import requests

st.title("🍽️ Food Cuisine Recommender System")

# Load data
data = pickle.load(open('food_dict.pkl', 'rb'))
new_df = pd.DataFrame(data)

# Download similarity.pkl if not exists
if not os.path.exists("similarity.pkl"):
    url = "https://github.com/ANSHIKAJAIN665/Food_Cuisine_Recommender_System/releases/download/similarity.pkl/similarity.pkl"
    
    with requests.get(url, stream=True) as r:
        with open("similarity.pkl", "wb") as f:
            for chunk in r.iter_content(1024):
                if chunk:
                    f.write(chunk)

similarity = pickle.load(open("similarity.pkl", "rb"))

# Clean names
new_df['name_clean'] = new_df['name'].astype(str).str.strip().str.lower()

# Dropdown
food_list = sorted(new_df['name'].dropna().unique().tolist())
selected_food = st.selectbox("Select a food", food_list)

# Recommend function
def recommend(food):
    food = str(food).strip().lower()

    if food in new_df['name_clean'].values:
        food_index = new_df[new_df['name_clean'] == food].index[0]
    else:
        matches = new_df[new_df['name_clean'].str.contains(food, regex=False)]
        if matches.empty:
            return []
        food_index = matches.index[0]

    distances = similarity[food_index]

    food_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [new_df.iloc[i[0]]['name'] for i in food_list]


# Button
if st.button("Recommend"):
    results = recommend(selected_food)

    st.subheader("Recommended Foods:")
    for item in results:
        st.write(item)