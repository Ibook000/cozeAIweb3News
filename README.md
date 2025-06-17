# Coze音频下载与合并工具

这个工具用于从Coze工作流获取数据，下载相关音频文件并合并成一个完整的音频文件。

## 功能特点

- 调用Coze工作流API获取数据
- 下载音频文件到本地
- 合并多个音频文件为一个完整文件
- 自动创建输出目录
- 错误处理和日志输出

## 安装要求

1. Python 3.6+
2. 安装依赖包：
```bash
pip install -r requirements.txt
```

3. 安装ffmpeg（用于音频处理）：
   - Windows: 下载并安装ffmpeg，将bin目录添加到系统环境变量
   - Linux: `sudo apt-get install ffmpeg`
   - Mac: `brew install ffmpeg`

## 使用方法

1. 确保已安装所有依赖
2. 运行主程序：
```bash
python main.py
```

## 输出

- 程序会在当前目录下创建`voice`文件夹
- 下载的音频文件将保存为`audio_1.mp3`、`audio_2.mp3`等
- 合并后的文件将保存为`combined_audio.mp3`

## 注意事项

- 确保有足够的磁盘空间
- 确保有网络连接
- 确保有写入目标目录的权限
- 如果遇到权限问题，请检查ffmpeg是否正确安装 