# Health Prediction Application

## Project Overview

This is a Flask-based Health Prediction Application that performs CRUD operations and predicts possible health conditions based on patient blood test values.

## Features

- Create Patient
- View Patient
- Update Patient
- Delete Patient
- AI-based Health Prediction
- SQLite Database
- Bootstrap User Interface

## Technology Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- Bootstrap

## Installation

```bash
pip install flask flask_sqlalchemy
python app.py
```

Open:

http://127.0.0.1:5000

## AI Prediction Logic

- Glucose >= 140 → High Diabetes Risk
- Cholesterol >= 200 → High Cholesterol Risk
- Haemoglobin < 12 → Possible Anemia
- Otherwise → Normal Health

## Author

Varshitha H J