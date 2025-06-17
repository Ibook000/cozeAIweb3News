# merge_audio.py - 音频合并模块
from pydub import AudioSegment
import os

def merge_audio_files(audio_paths, output_path):
    """
    合并多个音频文件
    :param audio_paths: 音频文件路径列表
    :param output_path: 输出文件路径
    """
    combined = AudioSegment.empty()

    for path in audio_paths:
        if not os.path.exists(path):
            raise FileNotFoundError(f"音频文件不存在: {path}")
        # 加载音频文件
        audio = AudioSegment.from_mp3(path)
        # 添加到合并音频
        combined += audio

    # 导出合并后的音频
    combined.export(output_path, format='mp3')
    return output_path