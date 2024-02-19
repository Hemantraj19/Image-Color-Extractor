from flask import Flask, render_template, request, redirect, url_for
import colorgram

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/extract", methods=["POST"])
def extract():

    if "img" not in request.files:
        return redirect(url_for("home"))

    image = request.files["img"]

    if image.filename == "":
        return redirect(url_for("home"))

    no_of_colors = int(request.form.get("no_of_colors"))

    colors = colorgram.extract(image, no_of_colors)
    return render_template("result.html", colors=colors)


if __name__ == "__main__":
    app.run(debug=True)
