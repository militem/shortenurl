from flask import request, jsonify
import hashlib


class URL:
    def get_shorten(self):
        data = request.json

        if "url" not in data:
            return jsonify({"error": "URL is required"}), 400

        shorten_url = hashlib.md5(data["url"].encode()).hexdigest()[:8]

        new_short_url = {
            "id": 1,
            "url": data["url"],
            "shortCode": shorten_url         
        }

        return new_short_url