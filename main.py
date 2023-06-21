from flask import Flask, render_template, jsonify
from database import load_data_from_db
app = Flask (__name__)

@app.route ("/")
def main_route():
  return render_template ("home.html")

@app.route ("/food/<food_type>")
def load_data_food_type(food_type):
  foods=load_data_from_db(food_type)
  return render_template ("food_type.html", foods=foods)


@app.route ("/food/save")
def load_data_food_type(food_type):
  foods=load_data_from_db(food_type)
  return render_template ("food_type.html", foods=foods)


if __name__ == "__main__":
  app.run(host="0.0.0.0",port=5001, debug=True)