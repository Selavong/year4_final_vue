from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask_final'

# Updated path to include the database asdfasdfasdfasdfasdfasdfasdfasdfasdffile name
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///D:/SELAVONG/SCHOOL/SETEC/Y4/S1/Python/Midterm/database.db'
db = SQLAlchemy(app)

import routes

if __name__ == '__main__':
    with app.app_context():
        # Ensure database schema is created
        db.create_all()
    app.run()
