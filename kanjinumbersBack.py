from flask import Flask, jsonify, request, render_template
from number2kanji import number2kanji as n2k
from kanji2number import kanji2number as k2n

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# @app.route("/", methods=["GET", "POST"])
# def main_page():
#     # render_templateで ./templates/ 内のhtmlファイル読み込める
#     return render_template("mainpage.html")

@app.route("/v1/number2kanji/<number>", methods=["GET", "POST"])
def number2kanji(number):
    return jsonify({
        "number": str(number),
        "kanji": str(n2k(number))})

@app.route("/v1/kanji2number/<kanji>", methods=["GET", "POST"])
def kanji2number(kanji):
    return jsonify({
        "number": str(k2n(kanji)),
        "kanji": str(kanji)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80, threaded=True)