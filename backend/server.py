# Import flask and datetime module for showing date and time
from flask import Flask, jsonify
import datetime
from app import create_app
from flask_cors import CORS
  
x = datetime.datetime.now()
  
# Initializing flask app
app = create_app()
# Route for seeing a data
@app.route('/')
def get_data():  
    # Returning an api for showing in  reactjs
    message = 'Hello World!'
    return jsonify(message)

# Running app
if __name__ == '__main__':
    app.run(debug=True)