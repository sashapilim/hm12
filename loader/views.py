from flask import Blueprint, render_template, request

from lesson12_project_source_v3.functions import add_post
from lesson12_project_source_v3.loader.utils import save_picture

loader_blueprunt = Blueprint("loader_blueprunt", __name__, template_folder="templates")


@loader_blueprunt.route("/post")
def page_post():
    return render_template("post_form.html")


@loader_blueprunt.route("/post", methods=["POST"])
def loader_post():
    picture = request.files.get("picture")
    content = request.form.get("content")
    if picture.filename.split(".")[-1] not in ["jpeg", "png"]:
        return "Загруженный файл - не картинка"
    if not picture or not content:
        return "Нет картинки или теста"
    try:
        stroka = "/" + save_picture(picture)
    except FileNotFoundError:
        return f"файл не найден"
    post = add_post({"pic": stroka, "content": content})
    return render_template("post_uploaded.html", posts=post)
