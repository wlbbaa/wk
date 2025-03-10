import os
import time
import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm

# ==== 1. 配置信息 ====
COURSE_URL = "https://example.com/course/123"  # 替换为网课链接
USERNAME = "你的账号"
PASSWORD = "你的密码"
DOWNLOAD_PATH = "videos"  # 下载文件夹

# ==== 2. 启动浏览器 ====
options = uc.ChromeOptions()
options.add_argument("--headless")  # 无头模式（后台运行）
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = uc.Chrome(options=options)

# ==== 3. 登录网课网站 ====
driver.get(COURSE_URL)
time.sleep(3)

# 账号输入框
username_input = driver.find_element(By.NAME, "username")  # 替换为实际的 HTML Name
username_input.send_keys(USERNAME)

# 密码输入框
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)

time.sleep(5)  # 等待跳转

# ==== 4. 解析课程视频链接 ====
video_links = []
videos = driver.find_elements(By.TAG_NAME, "video")  # 查找所有 <video> 标签
for video in videos:
    src = video.get_attribute("src")
    if src:
        video_links.append(src)

driver.quit()  # 关闭浏览器

# ==== 5. 下载视频 ====
if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)

for index, url in enumerate(video_links, start=1):
    filename = f"{DOWNLOAD_PATH}/video_{index}.mp4"
    print(f"正在下载: {filename}")

    # 使用 requests 进行下载
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        with open(filename, 'wb') as f, tqdm(
            desc=filename, total=total_size, unit='B', unit_scale=True, unit_divisor=1024
        ) as bar:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                bar.update(len(chunk))

print("所有视频下载完成！")