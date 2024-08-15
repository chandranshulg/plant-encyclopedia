# Online Plant Encyclopedia

This is an Online Plant Encyclopedia web application built using Flask and SQLite. It allows users to search for plants by name, type, and sunlight requirements. The application also displays detailed information about each plant, including its type, watering needs, and a brief description.

## Features

- **Search Functionality**: Users can search for plants by name, type (e.g., Flower, Herb), and sunlight requirements.
- **Plant Information Display**: Detailed information about each plant is displayed, including its type, sunlight, watering needs, and description.
- **Bootstrap Integration**: The application uses Bootstrap for a responsive and clean design.

## Installation

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy

### Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/chandranshulg/online-plant-encyclopedia.git
    ```
   
2. **Navigate to the project directory:**
    ```bash
    cd online-plant-encyclopedia
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    python app.py
    ```

5. **Access the application in your browser:**
    ```
    http://127.0.0.1:5000/
    ```

## Database

The application uses SQLite to store plant data. On the first run, the database (`plants.db`) is automatically created and populated with sample data if it's empty.

## File Structure

```plaintext
online-plant-encyclopedia/
│
├── app.py                     # Main Flask application
├── plants.db                  # SQLite database file
├── static/
│   └── images/                # Directory for plant images
│
└── templates/
    └── index.html             # HTML template for the application

 

