import csv
import time
from selenium.common.exceptions import WebDriverException, TimeoutException, UnexpectedAlertPresentException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# 브라우저의 자동화 모듈


# 네이버 뉴스 크롤러에서 변형하여 제작 


# csv 파일로 저장
def write_csv(no, content, date): # 긁어온 댓글 순서, 내용, 작성시간을 csv파일로 저장
    with open('sample.csv', 'a', encoding = 'euckr', newline='', errors= 'replace') as file:
        # sample.csv 라는 파일을 생성 'a' : 추가모드로 파일을 오픈
        w = csv.writer(file) # sample.csv 에 입력
        w.writerow([no, content, date]) # 수집한 no, content, data 값을 입력

# 다음 뉴스 링크 입력 > 가능한 댓글 입력 한 링크로~
url = 'https://news.v.daum.net/v/20161129150004873'
# url에 접근
temp_contents_len = 1 # 댓글의 순서를 지정!

# 사이트 열기
try:
    options = webdriver.ChromeOptions()  # 크롬에 옵션을 줌
    options.add_argument("--start-maximized")  # 전체화면으로 크롬 창의 크기를 설정
    prefs = {"profile.managed_default_content_settings.images": 2}  # 이미지를 불러오는 속도 줄이기 위해서 image except
    options.add_experimental_option("prefs", prefs) # 실험적인 옵션 > 환경설정 파일을 찾는 옵션 : 왜 쓰는지에 대해서는 ?
    wd = webdriver.Chrome(executable_path='../chromedriver/chromedriver', chrome_options=options)
    #크롬 드라이버의 위치 지정, 위에 설정한 옵션들을 적용한 크롬창을 띄운다.
    wd.get(url)  # 실제로 크롬 드라이버가 작동!

 # 뜰 때까지 대기
    try:
        WebDriverWait(wd, 6).until(EC.presence_of_element_located((By.CLASS_NAME, "desc_txt"))) # 웹 페이지가 뜰 때까지 대기. 근데 왜 옵션이 이렇게 많이 붙었을까?
    except TimeoutException:  # 시간이 오래 걸리면 게시글이 존재하지 않다고 출력됨
        print("게시글이 존재하지 않음")
    wd.find_element_by_xpath("//div[@class='alex_more']").click()

    # 뜰 때까지 기다리기
    while True:
        time.sleep(3)  # 3초 대기

        # 댓글 개수가 늘어났으면 탈출
        for i in range(0, 8):
            # xpath 라는 변수 안에 다음 댓글 중 수집할 내용이 들어있는 클래스만 접근!
            # //: 현재 node로 부터 문서상의 모든 node 조회, @: 현재 node의 속성 선택
            xpath = '// ul[@class="list_comment"]/li['+str(temp_contents_len)+']/div[@class="cmt_info"]/p'
            # 태그의 class 도 써준다 < 한 태그 안에 다른 태그들이 많아서 태그만 입력할 경우 위치를 정확히 찾지 못해 오류...
            # xpath 안에 temp_contents_len 번째의 댓글의 경로 입력
            # list_comment : 댓글의 전체 클래스, desc_txt : 실제 댓글 내용

            xpath1 = '// ul[@class="list_comment"]/li['+str(temp_contents_len)+']/div[@class="cmt_info"]/strong/span[@class="info_author"]/span[@class="txt_date"]'
            # xpath 안에 temp_contents_len 번째의 댓글 작성 시간의 경로 입력
            # txt_date : 댓글 작성 시간의 정보를 담고 있는 클래스!
            print(temp_contents_len)  # 댓글 순서
            temp_contents_len += 1  # 댓글 순서 +1

            try:
                WebDriverWait(wd, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath)))
                # 정상 댓글이면 정상 출력
                content = wd.find_element_by_xpath(xpath).text
                # content 값에 위에서 설정했던 경로들을 대입!
                date = wd.find_element_by_xpath(xpath1).text
                write_csv(temp_contents_len, content, date)  # contents_len = 맨 앞의 숫자 < 댓글 순서
                # csv 파일에 댓글 입력!
            except TimeoutException:  # 정상 댓글이 아닐 경우
                print("삭제된 댓글이라 건너뜀")
                continue

        # 댓글 더보기 클릭
        wd.find_element_by_xpath("//div[@class='alex_more']").click()

except WebDriverException:
    print("크롬드라이버 에러 발생 잠시 후 다시 시도")
