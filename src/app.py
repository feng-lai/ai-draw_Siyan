from flask import Flask, request, jsonify, send_from_directory
import image_generator
import os
import uuid
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# 获取 app.py 所在的绝对路径
# 这确保了无论从哪个目录运行 app.py，它都能正确找到相关文件夹
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'generated_images')
UPLOAD_TEMP_FOLDER = os.path.join(BASE_DIR, 'uploaded_temp_images')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(UPLOAD_TEMP_FOLDER, exist_ok=True)

@app.route('/api/generate-image', methods=['POST'])
def generate_image_api():
    data = request.json
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    filename = f"{uuid.uuid4()}.png"
    output_path = os.path.join(UPLOAD_FOLDER, filename) # 使用修正后的绝对路径
    
    try:
        image_generator.generate_image(prompt, output_path)
        return jsonify({
            "success": True,
            "imageUrl": f"/generated_images/{filename}"
        })
    except Exception as e:
        # 打印详细错误到控制台
        print(f"Error in /api/generate-image: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/api/edit-image', methods=['POST'])
def edit_image_api():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    if 'prompt' not in request.form:
        return jsonify({"error": "No prompt provided"}), 400

    image_file = request.files['image']
    prompt = request.form['prompt']

    if image_file.filename == '':
        return jsonify({"error": "No selected image file"}), 400

    temp_image_filename = secure_filename(f"{uuid.uuid4()}_{image_file.filename}")
    temp_image_path = os.path.join(UPLOAD_TEMP_FOLDER, temp_image_filename) # 使用修正后的绝对路径
    image_file.save(temp_image_path)

    output_filename = f"{uuid.uuid4()}.png"
    output_path = os.path.join(UPLOAD_FOLDER, output_filename) # 使用修正后的绝对路径

    try:
        # 调用 image_generator 中新定义的 edit_image 函数
        image_generator.edit_image(temp_image_path, prompt, output_path)
        os.remove(temp_image_path) # 清理临时上传的图片
        return jsonify({
            "success": True,
            "imageUrl": f"/generated_images/{output_filename}"
        })
    except Exception as e:
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path) # 确保即使出错也清理临时文件
        # 打印详细错误到控制台
        print(f"Error in /api/edit-image: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# 这个路由用于提供静态生成的图片文件
@app.route('/generated_images/<filename>')
def serve_image(filename):
    # send_from_directory 会在 UPLOAD_FOLDER 中查找文件
    # UPLOAD_FOLDER 现在是 app.py 所在目录下的 generated_images
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(port=3001, debug=True)
