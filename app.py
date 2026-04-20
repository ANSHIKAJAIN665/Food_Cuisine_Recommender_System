import streamlit as st
import pickle
import pandas as pd
import os
import requests
import re

st.set_page_config(page_title="Food Recommender", layout="wide")

st.title("🍽️ Food Cuisine Recommender System")

# ---------------- LOAD DATA ----------------
data = pickle.load(open('food_dict.pkl', 'rb'))
new_df = pd.DataFrame(data)

# ---------------- DOWNLOAD SIMILARITY ----------------
if not os.path.exists("similarity.pkl"):
    url = "https://github.com/ANSHIKAJAIN665/Food_Cuisine_Recommender_System/releases/download/similarity.pkl/similarity.pkl"

    with requests.get(url, stream=True) as r:
        with open("similarity.pkl", "wb") as f:
            for chunk in r.iter_content(1024):
                if chunk:
                    f.write(chunk)

similarity = pickle.load(open("similarity.pkl", "rb"))

# ---------------- CLEAN TEXT ----------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    return text.strip()

new_df['name_clean'] = new_df['name'].astype(str).str.strip().str.lower()

# ---------------- IMAGE MAP ----------------
image_map = {}

for file in os.listdir("images"):
    name_part = file.split('.', 1)[1]
    name_part = name_part.rsplit('-', 1)[0]

    cleaned = clean_text(name_part.replace('_', ' '))
    image_map[cleaned] = os.path.join("images", file)

# ---------------- IMAGE MATCH ----------------
def get_image(food_name):
    food_clean = clean_text(food_name)
    food_words = set(food_clean.split())

    best_match = None
    max_score = 0

    for key in image_map:
        key_words = set(key.split())

        score = len(food_words & key_words)

        if food_clean.split()[0] in key_words:
            score += 2

        if score > max_score:
            max_score = score
            best_match = image_map[key]

    return best_match

# ---------------- RECOMMEND ----------------
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

    results = []
    for i in food_list:
        name = new_df.iloc[i[0]]['name']
        image = get_image(name)

        results.append((name, image))

    return results

# ---------------- UI ----------------
food_list = sorted(new_df['name'].dropna().unique().tolist())
selected_food = st.selectbox("Select a food", food_list)

if st.button("Recommend"):
    results = recommend(selected_food)

    if not results:
        st.warning("No recommendations found")
    else:
        cols = st.columns(len(results))

        for i in range(len(results)):
            with cols[i]:
                if results[i][1]:
                    st.image(results[i][1])
                st.write(results[i][0])