from pathlib import Path

from flask import Flask, abort, render_template


BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)


@app.route("/")
def index():
    path = BASE_DIR / "content" / "index.md"
    md_text = path.read_text()
    return render_template("content.md", md_text=md_text)


@app.route("/<path:path_str>/")
def content(path_str):
    path = BASE_DIR / "content" / path_str
    if path.is_dir():
        path = path / "index.md"
    else:
        path = BASE_DIR / "content" / (path_str + ".md")
    if not path.is_file():
        abort(404)
    # Assert file is in content directory
    if BASE_DIR / "content" not in path.parents:
        abort(404)
    md_text = path.read_text()
    return render_template("content.md", md_text=md_text)


if __name__ == "__main__":
    app.run(debug=True)
