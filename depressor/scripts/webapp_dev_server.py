#!/usr/bin/env python
"""Runs the Flask development server for local testing."""

from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/health", methods=["GET"])
    def health() -> str:
        return "ok"

    return app


def main() -> None:
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
