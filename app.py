from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def bangladesh():
        return render_template("bd.html")

    @app.route("/<place>/")
    def bandarbans(place):
        template = "place.html"
        return render_template(template, place= place)  
    
    return app