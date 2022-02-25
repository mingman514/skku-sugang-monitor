from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import random, time
from sys import exit
from datetime import datetime

sugang_id = ''
sugang_pw = ''
target_list = []
degree = ''

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver', chrome_options=options)

def set_ID(ID):
    global sugang_id
    sugang_id = ID
def set_PW(PW):
    global sugang_pw
    sugang_pw = PW
def set_target_list(list):
    global target_list
    target_list = list

def sleep_to_pretend_human():
    sleeping_t = random.random() * 3
    print('sleeping for {} sec'.format(sleeping_t))
    time.sleep(sleeping_t)

def access_to_webpage():
    driver.maximize_window()
    driver.get('https://sugang.skku.edu')

    driver.implicitly_wait(15)
    frame = driver.find_element_by_xpath('/html/body/iframe')
    driver.switch_to.frame(frame)

def sugang_page_login():

    try:
        id_input = driver.find_element_by_xpath('//*[@id="id"]')
        pw_input = driver.find_element_by_xpath('//*[@id="pwd"]')
        login_btn = driver.find_element_by_xpath('//*[@id="btn_login"]')
        id_input.send_keys(sugang_id)
        pw_input.send_keys(sugang_pw)
        
        sleep_to_pretend_human()
        login_btn.click()
        print('수강신청 페이지 로그인 성공')
    except Exception:
        print('수강신청 페이지 로그인 실패')
        exit(1)

def get_degree_course():
    driver.switch_to.default_content()
    frame = driver.find_element_by_xpath('/html/body/iframe')
    driver.switch_to.frame(frame)
    
    global degree
    name = driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[4]/td').text
    degree = driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[6]/td').text
    print('{} 학생 - {} 과정'.format(name, degree))

def move_to_sugang_tab():
    try:
        driver.switch_to.default_content()
        frame = driver.find_element_by_xpath('/html/body/iframe')
        driver.switch_to.frame(frame)
        frame = driver.find_element_by_xpath('//*[@id="contentFrame"]')
        driver.switch_to.frame(frame)
        frame = driver.find_element_by_xpath('//*[@id="topFrame"]')
        driver.switch_to.frame(frame)
    except Exception:
        print('수강신청 탭 찾기 실패')
        
    sugang_tab = driver.find_element_by_xpath('//*[@id="cssmenu"]/ul/li[2]/a')
    sleep_to_pretend_human()
    sugang_tab.click()
    time.sleep(5)

def check_available():
    try:
        driver.switch_to.default_content()
        frame = driver.find_element_by_xpath('/html/body/iframe')
        driver.switch_to.frame(frame)
        frame = driver.find_element_by_xpath('//*[@id="contentFrame"]')
        driver.switch_to.frame(frame)
        frame = driver.find_element_by_xpath('//*[@id="mainFrame"]')
        driver.switch_to.frame(frame)
    except Exception:
        print('수강신청 목록 찾기 실패')

    subject_rows = driver.find_elements_by_xpath('//*[@id="listLecture"]/tbody/tr')
    subject_num = len(subject_rows) - 1
    print('책가방에 담은 {}개 과목 확인'.format(subject_num))
    subject_data = []

    for i in range(subject_num):
        tr = driver.find_element_by_xpath('//*[@id="{}"]'.format(i+1))
        tr_data = []
        for td in tr.find_elements_by_tag_name('td'):
            tr_data.append(td.text)
        subject_data.append(tr_data)
    
    cnt = 0
    for data in subject_data:
        if data[2] not in target_list:
            continue
        elif data[1] == '신청완료':
            cnt += 1
        if cnt == len(target_list):
            print('모든 목표 과목에 대한 수강신청 완료!')
            exit(1)
    
    # find target
    # 총 합계 인원수 기준으로 판별
    print('\n--------- 수강신청 가능여부 ---------')
    print('{} 현재'.format(datetime.now()))
    target_idx = []
    for idx, data in enumerate(subject_data):
        if data[1] == '신청완료' or data[2] not in target_list:
            continue
        regist_num = int(data[15].split('/')[0])
        wait_num = int(data[15].split('/')[1])
        if regist_num < wait_num:
            target_idx.append(idx)
            print('{}번째 과목 - {}'.format(str(idx+1), data[3]))
        else:
            print('[{}({}/{})] 수강신청 불가'.format(data[3], regist_num, wait_num))
    print('------------------------------------\n')

    return target_idx

def register(subjects_idx):

    for idx in subjects_idx:
        try:
            driver.switch_to.default_content()
            frame = driver.find_element_by_xpath('/html/body/iframe')
            driver.switch_to.frame(frame)
            frame = driver.find_element_by_xpath('//*[@id="contentFrame"]')
            driver.switch_to.frame(frame)
            frame = driver.find_element_by_xpath('//*[@id="mainFrame"]')
            driver.switch_to.frame(frame)
        except Exception:
            print('수강신청 목록 찾기 실패')

        if degree == '학사':
            driver.find_element_by_xpath('//*[@id="{}"]/td[2]/span'.format(idx+1)).click()
        else:   # 석사/박사
            driver.find_element_by_xpath('//*[@id="{}"]/td[2]/input[1]'.format(idx+1)).click()
        time.sleep(3)
        # repeat process
        move_to_sugang_tab()