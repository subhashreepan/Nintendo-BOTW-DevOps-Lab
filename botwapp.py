from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    print ("Shrine-history-ui")
    return "Nintendo-botw-ui korak seed ui"

if __name__ == "__main__":
    app.run(debug=True)
