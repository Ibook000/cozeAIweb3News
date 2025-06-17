# main.py - Coze音频下载与合并工具主程序
import os
import requests
from merge_audio import merge_audio_files
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# Coze API配置
COZE_API_KEY = os.getenv('COZE_API_KEY')
COZE_WORKFLOW_ID = os.getenv('COZE_WORKFLOW_ID')

# 音频保存目录
AUDIO_DIR = 'voice'
os.makedirs(AUDIO_DIR, exist_ok=True)

def get_coze_data():
    """从Coze工作流API获取数据"""
    url = f"https://api.coze.com/v1/workflows/{COZE_WORKFLOW_ID}/run"
    headers = {
        'Authorization': f'Bearer {COZE_API_KEY}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json={})
    response.raise_for_status()
    return response.json()

def download_audio(url, save_path):
    """下载音频文件"""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

def main():
    try:
        print("开始从Coze工作流获取数据...")
        data = get_coze_data()

        # 下载音频文件
        audio_urls = data.get('audio_urls', [])
        if not audio_urls:
            print("未找到音频URL")
            return

        print(f"找到{len(audio_urls)}个音频文件，开始下载...")
        audio_files = []
        for i, url in enumerate(audio_urls, 1):
            save_path = os.path.join(AUDIO_DIR, f'audio_{i}.mp3')
            download_audio(url, save_path)
            audio_files.append(save_path)
            print(f"下载完成: {save_path}")

        # 合并音频文件
        output_path = os.path.join(AUDIO_DIR, 'combined_audio.mp3')
        print("开始合并音频文件...")
        merge_audio_files(audio_files, output_path)
        print(f"音频合并完成: {output_path}")

    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main()