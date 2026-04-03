from flask import Flask, render_template, request
import pickle
import pandas as pd
import os
import requests

app = Flask(__name__)

# Load data
data = pickle.load(open('food_dict.pkl', 'rb'))
new_df = pd.DataFrame(data)

# 🔥 Download similarity.pkl if not exists
# 🔥 Download similarity.pkl if not exists
if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/uc?export=download&id=1qoH_sHrNREFCCGzz8E1l1sw6mv_LcqDD"

    print("Downloading similarity.pkl...")

    r = requests.get(url, stream=True)

    with open("similarity.pkl", "wb") as f:
        for chunk in r.iter_content(1024):
            if chunk:
                f.write(chunk)

    print("Download complete")

# 🔥 ADD THIS (MOST IMPORTANT)
similarity = pickle.load(open("similarity.pkl", "rb"))

# Clean names
new_df['name_clean'] = new_df['name'].astype(str).str.strip().str.lower()


# Recommendation function
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
        results.append(new_df.iloc[i[0]]['name'])

    return results


# Route
@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    selected_food = ""

    if request.method == 'POST':
        selected_food = request.form.get('food') or ""
        recommendations = recommend(selected_food)

    return render_template(
        'index.html',
        food_list=sorted(new_df['name'].dropna().unique().tolist()),
        recommendations=recommendations,
        selected_food=selected_food
    )


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)