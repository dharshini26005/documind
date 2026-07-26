from flask import Flask, render_template
from config import *

import sqlite3
from routes.upload_routes import upload_bp
from routes.summary_routes import summary_bp
from routes.notes_routes import notes_bp
from routes.flowchart_routes import flowchart_bp
from routes.mindmap_routes import mindmap_bp
from routes.semantic_routes import search_bp
from routes.chat_routes import chat_bp
from routes.how_routes import how_bp


# -------------------------------
# Create Flask App
# -------------------------------
app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = SECRET_KEY


# -------------------------------
# Register Blueprints
# -------------------------------
app.register_blueprint(upload_bp)
app.register_blueprint(summary_bp)
app.register_blueprint(notes_bp)
app.register_blueprint(flowchart_bp)
app.register_blueprint(mindmap_bp)
app.register_blueprint(search_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(how_bp)


# -------------------------------
# Initialize Database
# -------------------------------
def init_db():
    conn = sqlite3.connect(DATABASE)

    with open("database/schema.sql") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()


init_db()


# -------------------------------
# Routes
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# Run Server
# -------------------------------
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )