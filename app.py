import os
from pathlib import Path

from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/")
def index():
    path = 'content' / Path('index.md')
    md_text = path.read_text()
    return render_template('content.md', md_text=md_text)



@app.route("/<path:path_str>/")
def content(path_str):
    path = 'content' / Path(path_str)
    if path.is_dir():
        path = path / 'index.md'
    else:
        path = 'content' / Path(path_str + '.md')
    if not path.is_file():
        abort(404)
    # Assert file is in content directory
    if Path('content').resolve() not in path.resolve().parents:
        abort(404)
    md_text = path.read_text()
    return render_template('content.md', md_text=md_text)


if __name__ == '__main__':
    app.run(debug=True)
