# 🍽️ Food Cuisine Recommender System

A Machine Learning-based web application that recommends similar food recipes based on user input. 
The system uses text vectorization and cosine similarity to suggest relevant dishes through an interactive web interface.
---

## 🚀 Live Demo
⚡ **Streamlit App:**  
👉 https://foodcuisinerecommendersystem-z4xqwoj9rivjt7asjtncpk.streamlit.app/  

---

## 🚀 Features

- 🔍 Search food by name  
- 🤖 ML-based recommendation system  
- 📊 Uses cosine similarity for accurate results  
- 🌐 Interactive UI (Flask + Streamlit)  
- ⚡ Fast and user-friendly interface  

---

## 🛠️ Tech Stack

- Python  
- Flask  
- Streamlit  
- Pandas  
- Scikit-learn  
- HTML/CSS  

---

## 🧠 How It Works

1. Food dataset is cleaned and preprocessed  
2. Text data is converted into vectors using CountVectorizer  
3. Cosine similarity is calculated between recipes  
4. Based on user input, top similar food items are recommended  

---

## 📂 Project Structure

Food_Cuisine_Recommender_System/

├── app.py (Flask app)  
├── streamlit_app.py (Streamlit app)  
├── food_dict.pkl  
├── similarity.pkl (downloaded at runtime)  
├── requirements.txt  
├── templates/  
│   └── index.html  

---

## ⚙️ Installation & Setup

### 1. Clone the repository

git clone https://github.com/ANSHIKAJAIN665/Food_Cuisine_Recommender_System.git  
cd Food_Cuisine_Recommender_System  

---

### 2. Install dependencies

pip install -r requirements.txt  

---

### 3. Run Flask App

python app.py  

---

### 4. Run Streamlit App

streamlit run streamlit_app.py  

---

## ⚠️ Note

- `similarity.pkl` is a large file and is not stored in the repository  
- It is automatically downloaded at runtime  
- Ensure internet connection during first run  

---

## 👩‍💻 Author

**Anshika Jain**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
