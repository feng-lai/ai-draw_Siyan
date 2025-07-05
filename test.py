import os
import re
import requests
from urllib.parse import urlparse
import hashlib
import mimetypes
import json
import time

def extract_links(vue_filepath):
    """提取所有媒体属性中的远程URL"""
    with open(vue_filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 匹配所有可能的媒体属性（src, href, poster, data-src等）
    pattern = r'''(?:src|href|poster|data-src|data-poster|source)\s*=\s*["'](http[s]?://[^"']+)["']'''
    links = re.findall(pattern, content)
    return content, list(set(links))  # 去重

def get_extension_from_content_type(content_type, default='.bin'):
    """根据Content-Type获取文件扩展名"""
    if not content_type:
        return default
    
    # 常见类型映射
    type_map = {
        'image/jpeg': '.jpg',
        'image/png': '.png',
        'image/gif': '.gif',
        'image/webp': '.webp',
        'image/svg+xml': '.svg',
        'video/mp4': '.mp4',
        'video/webm': '.webm',
        'video/ogg': '.ogv',
        'audio/mpeg': '.mp3',
        'audio/ogg': '.ogg',
        'application/javascript': '.js',
        'text/css': '.css',
        'application/json': '.json',
        'text/html': '.html',
    }
    
    # 优先使用映射表
    if content_type in type_map:
        return type_map[content_type]
    
    # 使用mimetypes作为后备
    ext = mimetypes.guess_extension(content_type)
    return ext or default

def download_links(links, save_dir):
    """下载所有链接并返回本地路径映射"""
    os.makedirs(save_dir, exist_ok=True)
    local_paths = {}
    
    # 创建下载日志
    log_path = os.path.join(save_dir, 'download_log.json')
    if os.path.exists(log_path):
        with open(log_path, 'r', encoding='utf-8') as f:
            download_log = json.load(f)
    else:
        download_log = {}
    
    # 只下载媒体文件类型
    MEDIA_TYPES = [
        'image/jpeg', 'image/png', 'image/gif', 'image/webp', 'image/svg+xml',
        'video/mp4', 'video/webm', 'video/ogg', 'audio/mpeg', 'audio/ogg'
    ]
    
    for url in links:
        try:
            # 检查日志中是否已有记录
            if url in download_log:
                local_paths[url] = download_log[url]
                print(f"⏩ 使用缓存: {url}")
                continue
                
            # 获取文件名和扩展名
            parsed_url = urlparse(url)
            filename_base = os.path.basename(parsed_url.path) or hashlib.md5(url.encode()).hexdigest()
            
            # 发送HEAD请求获取内容类型
            head_resp = requests.head(url, timeout=10, allow_redirects=True)
            content_type = head_resp.headers.get('Content-Type', '').split(';')[0]
            ext = get_extension_from_content_type(content_type)
            
            # 检查是否是媒体文件类型
            if content_type not in MEDIA_TYPES:
                print(f"⏭️ 跳过非媒体文件: {url} ({content_type})")
                continue
                
            # 生成唯一文件名
            filename = f"{hashlib.md5(url.encode()).hexdigest()}{ext}"
            local_path = os.path.join(save_dir, filename)
            
            print(f"⬇️ 正在下载: {url} ({content_type})")
            
            # 下载文件
            response = requests.get(url, timeout=15, stream=True)
            response.raise_for_status()
            
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # 记录到映射和日志
            local_paths[url] = f"/downloaded_images/{filename}"
            download_log[url] = local_paths[url]
            
            print(f"✅ 下载成功: {filename}")
            time.sleep(0.5)  # 避免请求过快
            
        except Exception as e:
            print(f"❌ 下载失败 {url}: {str(e)[:100]}")
    
    # 保存下载日志
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(download_log, f, indent=2)
    
    return local_paths

def replace_links_in_content(content, link_map):
    """替换文件内容中的所有匹配链接"""
    # 按URL长度降序排序，避免部分替换
    sorted_urls = sorted(link_map.keys(), key=len, reverse=True)
    
    # 支持的所有属性
    attributes = ['src', 'href', 'poster', 'data-src', 'data-poster']
    
    for original_url in sorted_urls:
        local_path = link_map[original_url]
        
        # 处理不同引用方式
        for attr in attributes:
            # 构建正则表达式模式
            patterns = [
                rf'{attr}=["\']{re.escape(original_url)}["\']',
                rf'{attr}=\s*["\']{re.escape(original_url)}["\']',
            ]
            
            for pattern in patterns:
                # 查找并替换
                matches = re.findall(pattern, content)
                if matches:
                    replacement = f'{attr}="{local_path}"'
                    content = re.sub(pattern, replacement, content)
    
    return content

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    vue_filename = os.path.abspath(os.path.join(
        script_dir, '..', 'ai-draw_Siyan', 'src', 'pages', 'ImageEditor.vue'
    ))
    
    # 资源保存到public/downloaded_images
    save_dir = os.path.abspath(os.path.join(
        script_dir, '..', 'ai-draw_Siyan', 'public', 'downloaded_images'
    ))
    
    # 确保目录存在
    os.makedirs(save_dir, exist_ok=True)
    
    print(f"📄 处理文件: {vue_filename}")
    content, links = extract_links(vue_filename)
    
    if not links:
        print("⚠️ 未发现远程链接")
        return
    
    print(f"🔗 发现 {len(links)} 个远程媒体链接")
    local_paths = download_links(links, save_dir)
    
    if not local_paths:
        print("❌ 无有效下载，终止")
        return
    
    # 创建备份
    #backup_path = f"{vue_filename}.bak"
   # if not os.path.exists(backup_path):
      #  with open(backup_path, 'w', encoding='utf-8') as f:
      #      f.write(content)
       # print(f"📦 已创建备份: {backup_path}")
    
    # 替换内容
    updated_content = replace_links_in_content(content, local_paths)
    
    # 写入更新
    with open(vue_filename, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✅ 替换完成! {len(local_paths)} 个资源已本地化")
    print(f"📁 资源目录: {save_dir}")
    print(f"📝 下载日志: {os.path.join(save_dir, 'download_log.json')}")

if __name__ == "__main__":
    main()