# skku-sugang-monitor
성균관대학교 수강신청 자동화 프로그램 (for Windows)

# Pre-requisite
- https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/ 참고하여 selenium 사용 가능한 상태여야 함.
- `pip install selenium`
- 첨부된 chromedriver.exe는 크롬 98.0.4758.102 버전용임. 반드시 자신의 버전 확인 후 알맞은 크롬드라이버 설치할 것.

# Usage
- main.py에 필요에 맞게 파라미터 수정 (학번, 비밀번호, 대상 전공과목의 학수번호-분반, 신청기간, 시도주기)
- `python main.py`