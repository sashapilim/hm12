from flask import Flask, request, render_template, send_from_directory
import logging
from loader.views import loader_blueprunt
from main.main import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprunt)
logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="utf-8")


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
