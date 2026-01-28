# Recipe Finder

A **Python Flask web app** that lets users search for recipes based on ingredients and save their favorite recipes. Users can also filter recipes by cuisine.  

This project demonstrates **API integration**, **Flask web development** and **basic frontend design**.

---

## **Features**
- Search recipes by ingredients (e.g., chicken, tomato)  
- Filter recipes by cuisine (Italian, Indian, Chinese, Mexican)  
- Display recipe name, image, and link to the full recipe  
- Save favorite recipes for later viewing  
- Responsive and clean UI using HTML/CSS  

---

## **Tech Stack**
- Python 3  
- Flask  
- Requests library (for API calls)  
- HTML/CSS  
- Spoonacular API  

---

## **Installation**

1. **Clone the Repository**
```bash
git clone <YOUR_REPO_URL>
cd recipe_finder
```

2. **Create a virtual environment** (optional but recommended):
```bash
python -m venv venv
```

3. **Activate the virtual environment**:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

4. **Install dependencies**:
```bash
pip install -r requirements.txt
```

5. **Setup your API key**:

Create a `.env` file in the root folder:
```
SPOONACULAR_API_KEY=YOUR_API_KEY
```
Replace `YOUR_API_KEY` with your Spoonacular API key.

6. **Run the Flask app**:
```bash
python app.py
```

7. **Open your browser and go to**:
```
http://127.0.0.1:5000
```

---

## **Usage**

1. Enter ingredients separated by commas (e.g., chicken, tomato)
2. Optionally, select a cuisine filter
3. Click **Search**
4. Click **Save Favorite** to save any recipe
5. Scroll down to view your saved favorites

---

## **Folder Structure**
```
recipe_finder/
├── app.py                # Main Flask app
├── requirements.txt      # Dependencies
├── README.md             # This README file
├── .gitignore            # Ignore unnecessary files
├── .env                  # API key (not pushed to GitHub)
├── templates/
│   └── index.html        # Main HTML page
└── static/
    └── styles.css        # Styling
```

---

## **Future Improvements**
- Add live search suggestions
- Add recipe rating or comments
- Remove favorite recipes
- Deploy the app online using Heroku, Railway, or Render

---

## **Credits**
- [Spoonacular API](https://spoonacular.com/food-api) for recipe data





