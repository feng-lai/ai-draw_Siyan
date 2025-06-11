from flask import Flask, request, jsonify
import image_generator
import os
import uuid
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'generated_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/generate-image', methods=['POST'])
def generate_image_api():
    data = request.json
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    filename = f"{uuid.uuid4()}.png"
    output_path = os.path.join(UPLOAD_FOLDER, filename)
    
    try:
        image_generator.generate_image(prompt, output_path)
        return jsonify({
            "success": True,
            "imageUrl": f"/generated_images/{filename}"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/generated_images/<filename>')
def serve_image(filename):
    from flask import send_from_directory
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(port=3001, debug=True)