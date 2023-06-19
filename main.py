from flask import Flask, render_template
app = Flask (__name__)

@app.route ("/")
def main_route():
  return render_template ("home.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=5001, debug=True)