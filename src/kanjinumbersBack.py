from flask import Flask, jsonify, request, render_template, make_response
from number2kanji import number2kanji as n2k
from kanji2number import kanji2number as k2n

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/", methods=["GET"])
def main_page():
    # render_templateで ./templates/ 内のhtmlファイル読み込める
    return render_template("index.html")


@app.route("/v1/number2kanji/<number>", methods=["GET"])
def number2kanji(number):
    try:
        return str(n2k(number))
    except:
        return make_response("", 204)

@app.route("/v1/kanji2number/<kanji>", methods=["GET"])
def kanji2number(kanji):
    try:
        return str(k2n(kanji))
    except:
        return make_response("", 204)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80, threaded=True)