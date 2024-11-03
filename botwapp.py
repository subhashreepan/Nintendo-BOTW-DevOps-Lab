from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Shrine history ui"

if __name__ == "__main__":
    app.run(debug=True)
