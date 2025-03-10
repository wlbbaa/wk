---

AutoCourseDownloader 📚🎥

自动爬取网课视频并下载到本地

📌 项目介绍

AutoCourseDownloader 是一个 Python 工具，支持自动登录网课平台、解析课程视频链接，并下载到本地。

✅ 支持功能：

自动登录：使用 Selenium 进行网页模拟登录。

视频解析：自动获取课程页面的 video 标签地址。

视频下载：支持 MP4 格式的直接下载，并显示进度条。

无头模式：可在后台运行，无需人工干预。



---

📦 安装

1. 克隆项目

git clone https://github.com/你的用户名/AutoCourseDownloader.git
cd AutoCourseDownloader

2. 安装依赖

pip install -r requirements.txt

此外，你需要安装 ffmpeg（用于处理 M3U8 视频格式）：

Windows: 下载 ffmpeg 并配置环境变量。

Linux/macOS:

sudo apt install ffmpeg  # Debian/Ubuntu
brew install ffmpeg      # macOS



---

🚀 使用方法

1. 修改配置信息

在 config.py 或 main.py 内修改以下信息：

COURSE_URL = "https://example.com/course/123"  # 课程链接
USERNAME = "你的账号"
PASSWORD = "你的密码"
DOWNLOAD_PATH = "videos"  # 下载目录

2. 运行爬取脚本

python main.py

程序会自动：

1. 打开网课平台并进行登录。


2. 解析课程页面的视频地址。


3. 下载视频到本地 videos/ 目录。




---

📜 代码结构

AutoCourseDownloader/
│── main.py             # 主程序
│── config.py           # 账号配置
│── requirements.txt    # 依赖库
│── README.md           # 说明文档
└── videos/             # 下载的视频存放目录


---

💡 注意事项

该工具仅用于 个人学习，请勿用于非法用途。

部分网课平台可能使用 DRM 加密，此工具无法破解加密视频。

如果网课需要验证码登录，可以 手动登录后获取 Cookies，并在 requests 里设置 headers 进行访问。



---

📜 许可证

本项目基于 MIT License 开源，你可以自由使用、修改和分享。
