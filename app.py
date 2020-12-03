#use Flask to render a template
from flask import Flask, render_template
#use PyMongo to interact with our Mongo database
from flask_pymongo import PyMongo
#to use the scraping code, we will convert from Jupyter notebook to Python
import scraping

app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#define the route for the HTML page. when we visit our web app's HTML page, we will see the home page
@app.route("/")
def index():
    # uses PyMongo to find the "mars" collection in our database, 
    # which we will create when we convert our Jupyter scraping code to Python Script. 
    # We will also assign that path to themars variable for use later
   mars = mongo.db.mars.find_one()
   #tells Flask to return an HTML template using an index.html file.
   return render_template("index.html", mars=mars)

#Set up scraping route
@app.route("/scrape")
def scrape():
    #assign a new variable that points to our Mongo database
   mars = mongo.db.mars
   #created a new variable to hold the newly scraped data
   mars_data = scraping.scrape_all()
   #Update database
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"

   #Tell flask to run
   if __name__ == "__main__":
    app.run()