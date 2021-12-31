from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Goodbye 2021! Happy new year 2022"

if __name__ == "__main__":
    app.run()