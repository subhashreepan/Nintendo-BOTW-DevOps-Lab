from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    print ("korak-seed-ui")
    return "Nintendo BOTW ui"

if __name__ == "__main__":
    app.run(debug=True)
