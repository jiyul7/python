# 연합뉴스 속보
from selenium import webdriver
# click 후 결과 나올때까지 처리용
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
#browser.maximize_window()   # windows 최대화
#######################################################################################################
# naver는 스크롤해야 마지막까지 나와서 중간에 끊김 --> 스크롤 기능 구현 필요
# interpark는 전체 다 나오나, EC로 항공스케줄만 뽑으면 중간에 끊김
# so, EC를 화면 아래 영역 수신을 체크하고, 값은 중간(항공스케줄)을 추출하는 방식으로 구현함
url = "https://domair.interpark.com/dom/main.do?trip=OW&dep=TAE&arr=CJU&depdate=20220110&adt=1&chd=0&inf=0&mbn=tourair&mln=airdome_search1#anchor-list"
# url = "https://m-flight.naver.com/flights/domestic/TAE-CJU-20220104?adult=1&fareType=YC"
# browser.implicitly_wait(15)
browser.get(url)
# 날짜 등 입력해야 할 때 
# browser.find_element_by_link_text("가는날 선택").click()
# 버튼 클릭시
# browser.find_element_by_class_name("searchBox_txt__3RoCw").click()
#elem = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]").click()
try:
    endwait = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, "anchor-choice")))
    print(endwait.text)
    elem = elem = browser.find_element(By.XPATH, "//*[@id='availDepResult']/table/tbody")
    print(elem.text)
finally:
    browser.quit()
