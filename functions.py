import json


def get_json() -> list[dict]:
    with open("posts.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_find_post(post):
    result = []
    for i in get_json():
        if post.lower() in i["content"].lower():
            result.append(i)
    return result


def add_post(post: dict):
    posts: list[dict] = get_json()
    posts.append(post)
    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False)
    return post
