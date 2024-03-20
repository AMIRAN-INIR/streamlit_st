import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image

st.text("hello")

if st.button("X"):
    # تنظیمات مرورگر Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # برای اجرای بدون رابط کاربری
    chrome_options.add_argument("--proxy-server=21.195.225.59:8080")

    # ایجاد یک webdriver
    driver = webdriver.Chrome(options=chrome_options)

    # آدرس URL سایت
    url = "https://www.youtube.com"  # جایگزین با URL مورد نظر

    # باز کردن سایت
    driver.get(url)

    # صبر به مدت 20 ثانیه
    time.sleep(20)

    # گرفتن اسکرین شات
    screenshot = driver.save_screenshot("screenshot.png")

    # بستن مرورگر
    driver.quit()

    # خواندن تصویر اسکرین شات
    image = Image.open("screenshot.png")

    # نمایش تصویر در Streamlit
    st.title("اسکرین شات")
    st.image(image, caption="اسکرین شات از " + url)
