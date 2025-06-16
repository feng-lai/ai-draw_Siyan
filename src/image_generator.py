import sys
import os
import traceback
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

def generate_image(prompt, output_path):
    try:
        # Set up proxy if needed (uncomment if you need proxy)
        os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
        os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
        
        # Initialize the client with your API key
        # Replace with your actual API key or use environment variable
        api_key = os.environ.get("GEMINI_API_KEY", "AIzaSyAy5-_q94y8DeBkoBFG9oTXPF4dbDD2cBQ")
        client = genai.Client(api_key=api_key)
        
        print(f"Generating image for prompt: {prompt}")
        
        # Generate content with image
        response = client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"]),
        )
        
        # Process the response
        image_saved = False
        for part in response.candidates[0].content.parts:
            if part.text is not None:
                print(f"Generated text: {part.text}")
            elif part.inline_data is not None:
                # Save the generated image
                image = Image.open(BytesIO(part.inline_data.data))
                image.save(output_path)
                print(f"Image saved to: {output_path}")
                image_saved = True
                break
        
        if not image_saved:
            print("No image data found in response")
            sys.exit(1)
            
        print("Image generation completed successfully")
        
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        sys.exit(1)



def edit_image(input_image_path, prompt, output_path):
    """
    编辑现有图片，并生成新图片。
    :param input_image_path: 输入图片的路径。
    :param prompt: 编辑图片的文本提示。
    :param output_path: 编辑后新图片的保存路径。
    """
    try:
        api_key = os.environ.get("GEMINI_API_KEY", "AIzaSyAy5-_q94y8DeBkoBFG9oTXPF4dbDD2cBQ")
        client = genai.Client(api_key=api_key)
        genai.api_key = api_key
        os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
        os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
        
        # 加载输入图片
        try:
            with open(input_image_path, 'rb') as f:
                img_data = BytesIO(f.read())
            img = Image.open(img_data)

            # 确保图片是RGB模式，有些模型可能对模式有要求
            if img.mode != 'RGB':
                img = img.convert('RGB')
        except FileNotFoundError:
            raise Exception(f"输入图片文件未找到: {input_image_path}")
        except Exception as e:
            raise Exception(f"加载输入图片 {input_image_path} 时发生错误: {str(e)}")

        print(f"正在编辑图片 {input_image_path}，提示词: {prompt}")

        # 准备多模态请求的内容：图片对象和文本提示
        # Gemini API 期望图片以 PIL.Image 对象形式传入
        contents = [img, prompt]

        # 使用支持多模态输入和图像生成功能的模型


        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents=contents,
            config=types.GenerateContentConfig(response_mime_type="image/jpeg",),
            
        )

        image_saved = False
        if response.candidates:
            for part in response.candidates[0].content.parts:
                # 优先处理最新的 _media_info 结构
                if hasattr(part, '_media_info') and part._media_info is not None and part._media_info.mime_type.startswith("image"):
                    image_data = BytesIO(part._media_info.raw_data)
                    image = Image.open(image_data)
                    image.save(output_path)
                    print(f"编辑后的图片已保存到: {output_path}")
                    image_saved = True
                    break
                # 兼容旧版或不同API返回的 inline_data 结构
                elif hasattr(part, 'inline_data') and part.inline_data is not None and part.inline_data.mime_type.startswith("image"):
                    image = Image.open(BytesIO(part.inline_data.data))
                    image.save(output_path)
                    print(f"编辑后的图片已保存到: {output_path}")
                    image_saved = True
                    break

        if not image_saved:
            print("API响应中未找到编辑后的图片数据或保存失败。")
            print(f"Gemini API 完整响应: {response}") # 打印完整响应以便调试
            raise Exception("Gemini API 未能生成或保存编辑后的图片。")

        print("图片编辑完成。")

    except Exception as e:
        print(f"编辑图片时发生错误: {str(e)}")
        traceback.print_exc() # 打印完整的错误追踪信息
        raise # 重新抛出异常，让 app.py 能够捕获并返回 500 错误
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage for generate: python image_generator.py generate <prompt> <output_path>")
        print("Usage for edit: python image_generator.py edit <input_image_path> <prompt> <output_path>")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "generate":
        if len(sys.argv) != 3:
            print("Usage: python image_generator.py <prompt> <output_path>")
            sys.exit(1)
    
        prompt = sys.argv[1]
        output_path = sys.argv[2]
        
        generate_image(prompt, output_path)
    elif command == "edit":
        if len(sys.argv) != 5:
            print("Usage: python image_generator.py edit <input_image_path> <prompt> <output_path>")
            sys.exit(1)
        input_image_path = sys.argv[2]
        prompt = sys.argv[3]
        output_path = sys.argv[4]
        edit_image(input_image_path, prompt, output_path)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
