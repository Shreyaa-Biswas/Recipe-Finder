# Recipe Finder

A **standalone HTML/JavaScript web app** that lets users search for recipes based on ingredients and save their favorite recipes. Users can also filter recipes by cuisine type.

This project demonstrates **API integration**, **vanilla JavaScript**, and **modern frontend development** - all in a single HTML file with no backend required.

---

## **Features**

- 🔍 Search recipes by ingredients (e.g., chicken, rice, tomato)
- 🌍 Filter recipes by cuisine (Italian, Indian, Chinese, Mexican, etc.)
- 📸 Display recipe name, image, and link to full recipe
- ⭐ Save favorite recipes with local storage
- 📱 Fully responsive design
- 🎨 Clean red and white UI
- ⚡ No installation or server required - just open and use!

---

## **Tech Stack**

- HTML5
- CSS3
- Vanilla JavaScript (ES6+)
- Spoonacular API
- LocalStorage for data persistence

---

## **Quick Start**

### **1. Get Your Free API Key**

1. Visit [spoonacular.com/food-api](https://spoonacular.com/food-api)
2. Sign up for a free account (150 requests/day)
3. Copy your API key

### **2. Add API Key to the File**

1. Open `recipe-finder.html` in any text editor
2. Find the line:
   ```javascript
   const API_KEY = 'Enter your API_KEY here';
   ```
3. Replace with your actual key:
   ```javascript
   const API_KEY = 'abc123xyz789';
   ```
4. Save the file

### **3. Run the App**

Simply **double-click** `recipe-finder.html` to open it in your browser!

Or:
- Right-click → Open with → Chrome/Firefox/Safari
- Drag and drop the file into your browser window

**That's it!** No installation, no dependencies, no npm, no server.

---

## **Usage**

1. Enter ingredients separated by commas (e.g., `chicken, rice, garlic`)
2. Optionally, select a cuisine filter
3. Click **Search**
4. Browse recipe results with images
5. Click **View** to see the full recipe on Spoonacular
6. Click **⭐ Save** to add recipes to your favorites
7. Your favorites are stored locally and persist between sessions

---

## **Project Structure**

```
recipe-finder/
├── recipe-finder.html    # Complete standalone app (HTML + CSS + JS)
└── README.md            # Documentation
```

**Everything is in one file!** This makes it:
- Easy to share
- Simple to deploy
- Zero configuration needed

---

## **Key Features Explained**

### **No Backend Required**
- All API calls are made directly from the browser
- No Flask, Node.js, or any server needed
- Pure client-side JavaScript

### **Local Storage**
- Favorites are saved in your browser's localStorage
- Data persists even after closing the browser
- No database required

### **Responsive Design**
- Works on desktop, tablet, and mobile
- Grid layout adapts to screen size
- Touch-friendly interface

### **Efficient Code**
- Clean, readable JavaScript
- Minimal CSS with modern features
- Fast page load and smooth interactions

---

## **Browser Compatibility**

Works on all modern browsers:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

---

## **API Limits**

The free Spoonacular API tier includes:
- 150 requests per day
- Up to 12 recipes per search
- Full recipe information and images

If you need more, upgrade to a paid plan at [spoonacular.com/food-api/pricing](https://spoonacular.com/food-api/pricing)

---

## **Troubleshooting**

### **No recipes found?**
- Make sure you added your API key correctly
- Try searching with 2-3 ingredients instead of just one
- Example: `chicken, rice` instead of just `chicken`
- Select a cuisine filter for better results

### **API errors?**
- Check the browser console (F12 → Console tab)
- Verify your API key is active at spoonacular.com
- Make sure you haven't exceeded the daily limit (150 requests)

### **Favorites not saving?**
- Make sure your browser allows localStorage
- Don't use incognito/private mode
- Check browser settings for cookie/storage permissions

---

## **Deployment**

### **GitHub Pages** (Free hosting)
1. Create a GitHub repository
2. Upload `recipe-finder.html`
3. Go to Settings → Pages
4. Select main branch
5. Your app will be live at `https://yourusername.github.io/recipe-finder/recipe-finder.html`

### **Other Options**
- Upload to any web hosting service
- Share the HTML file directly via email/USB
- Host on Netlify, Vercel, or Render

---

## **Future Improvements**

- [ ] Add recipe ratings and reviews
- [ ] Implement recipe categories/tags
- [ ] Add nutrition information display
- [ ] Create a "Random Recipe" feature
- [ ] Add cooking time and difficulty filters
- [ ] Allow users to add notes to saved recipes
- [ ] Export favorites as PDF or shareable link

---

## **Contributing**

Feel free to fork this project and add your own features! Some ideas:
- Different color themes
- Dark mode toggle
- Advanced search filters
- Recipe sharing functionality

---

## **License**

This project is open source and available for personal and educational use.

---

## **Credits**

- Recipe data provided by [Spoonacular API](https://spoonacular.com/food-api)
- Font: [Inter](https://fonts.google.com/specimen/Inter) by Google Fonts
- Created as a demonstration of modern vanilla JavaScript web development

---

## **Contact**

For questions or suggestions, open an issue on GitHub or contact the developer.

---

**Enjoy cooking! 🍳**

