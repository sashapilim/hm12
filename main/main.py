import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from lesson12_project_source_v3.functions import get_find_post

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    return render_template("index.html")


@main_blueprint.route("/search/")
def get_posts_page():
    find_request = request.args.get("s")
    logging.info("выполняю поиск")
    try:
        posts = get_find_post(find_request)
    except FileNotFoundError:
        return f"файл не найден"
    except JSONDecodeError:
        return f"невалидный файл"
    return render_template("post_list.html", find_request=find_request, posts=posts)
