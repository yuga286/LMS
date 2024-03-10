# from flask import Flask
# app= Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello"

# app.run(debug=True)

import os

# Get the full path of the current script
script_path = os.path.abspath(__file__)

# Print the full path
print("Full Path of the Script:", script_path)
