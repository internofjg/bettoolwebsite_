from flask import render_template
from modules import modules

def configure_routes(app):
    @app.route("/")
    def index():
        hello = modules.hello()
        content = modules.content()
        home = modules.home()
        return render_template("index.html", hello=hello, content=content, home=home)
