# skku-sugang-monitor
- 성균관대학교 수강신청 자동화 프로그램 (for Windows)
- 티오통합 기간에 무작위로 나오는 티오를 꾸준히 모니터링하여 신청하기 위한 용도
![image](https://user-images.githubusercontent.com/70851516/155660987-4532dcce-b5f3-4b19-8849-45eb0c1e601e.png)

# Pre-requisite
- https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/ 참고하여 selenium 사용 가능한 상태여야 함.
- `pip install selenium`
- 첨부된 chromedriver.exe는 크롬 98.0.4758.102 버전용임. 반드시 자신의 버전 확인 후 알맞은 크롬드라이버 설치할 것.
- Windows 외 OS는 chromedriver 뿐만 아니라 관련 경로도 수정해야할 수 있음.

# Usage
- main.py에 필요에 맞게 파라미터 수정 (학번, 비밀번호, 대상 전공과목의 학수번호-분반, 신청기간, 시도주기)
- `python main.py`

# Future Work
- 상황 알림 기능 (신청 성공, 신청기간 종료 등) via Email or such
- 동일한 과목(학수번호 일치)간 선호도 반영한 신청 로직
