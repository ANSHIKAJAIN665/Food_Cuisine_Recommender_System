🍽️ Food Cuisine Recommender System

A Machine Learning-based web application that recommends similar food recipes based on user input. It uses text vectorization and cosine similarity to suggest relevant dishes through a simple and interactive interface.

🚀 Features
🔍 Search food by name
🤖 ML-based recommendation system
📊 Uses cosine similarity for accurate suggestions
🌐 Interactive web interface using Flask
⚡ Fast and user-friendly UI
🛠️ Tech Stack
Python
Flask
Pandas
Scikit-learn
HTML/CSS
🧠 How It Works
Food dataset is cleaned and preprocessed
Text data is converted into numerical vectors using CountVectorizer
Cosine similarity is calculated between food items
Based on user input, top similar food items are recommended
📂 Project Structure

Food_Cuisine_Recommender_System/

├── app.py
├── food_dict.pkl
├── similarity.pkl (downloaded at runtime)
├── requirements.txt
├── templates/
│ └── index.html

⚙️ Installation & Setup
1. Clone the repository

git clone https://github.com/ANSHIKAJAIN665/Food_Cuisine_Recommender_System.git

cd Food_Cuisine_Recommender_System

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python app.py

4. Open in browser

http://127.0.0.1:5000

🌍 Live Demo

https://food-cuisine-recommender-system.onrender.com

⚠️ Note
The file similarity.pkl is large and is not stored in the repository
It is automatically downloaded at runtime
Ensure you have an active internet connection during the first run
👩‍💻 Author

Anshika Jain

⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
