from flask import Flask, render_template_string, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Set up the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Plant model
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    sunlight = db.Column(db.String(100), nullable=False)
    watering = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=False)

# Initialize the database
db.create_all()

# Sample plants data (if database is empty)
if Plant.query.count() == 0:
    sample_plants = [
        Plant(name="Tomato", type="Vegetable", sunlight="Full Sun", watering="Regular", 
              description="Tomatoes are a popular vegetable plant known for their juicy, red fruits.", 
              image="tomato.jpg"),
        Plant(name="Basil", type="Herb", sunlight="Partial Sun", watering="Moderate", 
              description="Basil is a fragrant herb often used in cooking, particularly in Italian dishes.", 
              image="basil.jpg"),
        Plant(name="Rose", type="Flower", sunlight="Full Sun", watering="Moderate", 
              description="Roses are beautiful, fragrant flowers that come in a variety of colors.", 
              image="rose.jpg"),
    ]
    db.session.bulk_save_objects(sample_plants)
    db.session.commit()

# HTML template as a string
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Plant Encyclopedia</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5 text-center">Online Plant Encyclopedia</h1>
        <form action="/" method="GET" class="mt-4">
            <div class="form-row">
                <div class="col-md-3 mb-3">
                    <input type="text" class="form-control" name="search" placeholder="Search by name">
                </div>
                <div class="col-md-3 mb-3">
                    <input type="text" class="form-control" name="type" placeholder="Type (e.g., Flower, Herb)">
                </div>
                <div class="col-md-3 mb-3">
                    <input type="text" class="form-control" name="sunlight" placeholder="Sunlight (e.g., Full Sun)">
                </div>
                <div class="col-md-3 mb-3">
                    <button type="submit" class="btn btn-primary btn-block">Search</button>
                </div>
            </div>
        </form>
        <div class="row mt-4">
            {% for plant in plants %}
            <div class="col-md-4">
                <div class="card mb-4">
                    <img src="{{ url_for('static', filename='images/' + plant.image) }}" class="card-img-top" alt="{{ plant.name }}">
                    <div class="card-body">
                        <h5 class="card-title">{{ plant.name }}</h5>
                        <p class="card-text"><strong>Type:</strong> {{ plant.type }}</p>
                        <p class="card-text"><strong>Sunlight:</strong> {{ plant.sunlight }}</p>
                        <p class="card-text"><strong>Watering:</strong> {{ plant.watering }}</p>
                        <p class="card-text">{{ plant.description }}</p>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
'''

# Home route with search functionality
@app.route('/', methods=['GET'])
def index():
    search_query = request.args.get('search', '')
    type_query = request.args.get('type', '')
    sunlight_query = request.args.get('sunlight', '')

    # Filter plants based on search criteria
    plants = Plant.query.filter(
        Plant.name.like(f"%{search_query}%"),
        Plant.type.like(f"%{type_query}%"),
        Plant.sunlight.like(f"%{sunlight_query}%")
    ).all()

    return render_template_string(html_template, plants=plants)

# Start the Flask app
if __name__ == '__main__':
    # Create directory for images if it doesn't exist
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    
    # Run the app
    app.run(debug=True)
