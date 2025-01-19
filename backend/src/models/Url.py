from flask import request, jsonify
import hashlib
import uuid
from datetime import datetime, timezone
from src.utils.validator import valid_url

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("src/utils/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

class URL:

    def get_shorten(self):
        data = request.json

        if "url" not in data:
            return jsonify({"error": "URL is required"}), 400
        
        url = data["url"]

        if not valid_url(url):
            return jsonify({"error": "URL is not valid"}), 400

        id_url = str(uuid.uuid4())
        enconde_data = url + id_url

        now = datetime.now(timezone.utc)

        created_at = now.isoformat(timespec='seconds').replace("+00:00", "Z")

        shorten_url = hashlib.md5(enconde_data.encode()).hexdigest()[:8]

        new_short_url = {
            "id": id_url,
            "url": url,
            "shortCode": shorten_url,
            "createdAt": created_at,
            "updatedAt": created_at,
            "accessCount": 0         
        }

        doc_ref = db.collection("links").document(id_url)
        doc_ref.set(new_short_url)

        return jsonify(new_short_url), 200

    def get_long_url(self, shortCode):
        documentos = db.collection("links").where("shortCode", "==", shortCode).stream()
        links = []
        for doc in documentos:
            data = {}
            data["shortCode"] = doc.to_dict()['shortCode'] 
            data["createdAt"] = doc.to_dict()['createdAt'] 
            data["updatedAt"] = doc.to_dict()['updatedAt'] 
            data["url"] = doc.to_dict()['url'] 
            data["id"] = doc.id 
            links.append(data)

            doc_ref = db.collection("links").document(doc.id)
            current_count = int(doc.to_dict()['accessCount'])
            doc_ref.update({"accessCount": current_count + 1})

        if not links:
            return jsonify({"error": "Link not found"}), 404
        
        return jsonify(links[0]), 200
    
    def get_shorten_update(self, shortCode):
        #ESTO SE DEBE ACTUALIZAR EN LA BASE DE DATOS DE FIREBASE
        return {'update_shorCode': shortCode}
    
    def get_shorten_delete(self, shortCode):
        #ESTO SE DEBE ELIMINAR EN LA BASE DE DATOS DE FIREBASE
        return {'delete_shorCode': shortCode}
    
    def get_stats(self, shortCode):
        documentos = db.collection("links").where("shortCode", "==", shortCode).stream()
        links = []
        for doc in documentos:
            data = doc.to_dict()
            data["id"] = doc.id 
            links.append(data)

        if not links:
            return jsonify({"error": "Link not found"}), 404
        
        return jsonify(links), 200