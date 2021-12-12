from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import time

# ブラウザーを起動
options = Options()
#options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

# Google検索画面にアクセス
driver.get('https://www.google.co.jp/')

# htmlを取得・表示
html = driver.page_source
print(html)

#gLFyf gsfi
#/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input

element = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input")

#検索テキストボックスに文字列を入力
element.send_keys("キーボード入力をする(通常キー)")

time.sleep(5)



# ブラウザーを終了
driver.quit()
