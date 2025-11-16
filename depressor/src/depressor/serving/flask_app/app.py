"""Minimal Flask application exposing prediction endpoints."""

from flask import Flask, jsonify, request


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/predict", methods=["POST"])
    def predict():  # type: ignore[override]
        payload = request.get_json(force=True)
        text = payload.get("text", "")
        return jsonify({"text": text, "labels": [], "scores": []})

    @app.route("/explain", methods=["POST"])
    def explain():  # type: ignore[override]
        payload = request.get_json(force=True)
        text = payload.get("text", "")
        return jsonify({"text": text, "attributions": []})

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000, debug=True)
