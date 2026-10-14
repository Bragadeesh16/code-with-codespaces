from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Completed during MLH Global Hack Week: Hacktoberfest."

if __name__ == "__main__":
    app.run()
