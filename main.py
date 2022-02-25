from sugang_utils import *

# 경로 설정에 따라 chromedriver.exe 파일이 같은 폴더 내에 있어야 함.
"""
To Fill Out
"""
Student_ID = '2021XXXXXX'
Password = 'p@ssw0rd'
# 대상 전공과목 (학수번호-분반) 입력 - ex. 'SUP5003-41'
Target_List = ['SWE3002-42', 'SWE3047-42', 'SWE3047-43']

# 신청기간
Start_Date = datetime.strptime('2022-02-22 08:00','%Y-%m-%d %H:%M')
End_Date = datetime.strptime('2022-02-25 22:59','%Y-%m-%d %H:%M')

# 신청시도 주기 (minute)
# ex. At_Least = 1, At_Most = 5  :  1~5분 사이 랜덤시간마다 반복
At_Least = 1
At_Most = 5

def is_register_period():
    if Start_Date > End_Date:
        print('신청기간 확인 필요')
        exit()
    Now = datetime.now()
    if Start_Date <= Now and Now <= End_Date:
        return True
    return False

if __name__ == '__main__':
    set_ID(Student_ID)
    set_PW(Password)
    set_target_list(Target_List)   
    # open page
    access_to_webpage()
    # login
    sugang_page_login()
    # get degree course
    get_degree_course()
    # move to 수강신청 tab == refresh
    move_to_sugang_tab()
    
    # check availability & register
    while True:
        # 수강신청 가능시간대 벗어나면 종료
        if is_register_period():
            available_subjects = check_available()

            if len(available_subjects) > 0:
                register(available_subjects)

            wait_time = 60 * random.uniform(At_Least, At_Most)
            print('{}초 대기 후에 모니터링 재개'.format(round(wait_time, 2)))
            time.sleep(wait_time)
            move_to_sugang_tab()

        else:
            print('신청 기간이 아니므로 종료')
            exit()
    