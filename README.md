# Google Calendar API

## 1. Intorduce
- 캘린더의 기능을 조작해보기 위해 Google Open API를 사용하기로 했다. 
- 기능으로 다음과 같이 구현하였다. 

## 2. Function
- 2-1. 조회
    - 이름/날짜 중 선택할 수 있다.

- 2-2. 등록
    - 풀타임/파트타임 중 선택할 수 있다.

- 2-3. 삭제

- 2-4. 수정
    - 이름/시작시간/종료시간/이벤트내용 중 선택할 수 있다.

## 3. Used
> conda env create -f 'google_cal.yaml'

> pip install -r requirements.txt

- 수정 필요 
    - google_oauth.py 
        - [your_key] : 유저의 비밀 키 
        - [your_client] : 유저의 클라이언트 
        - [your_key.json] : 유저의 키 파일(json 형식)

## 4. Reference
- [Google Calendar](https://developers.google.com/apps-script/reference/calendar/calendar?hl=ko)
- [Google Auth Setting](https://accounts.google.com/v3/signin/identifier?dsh=S1494126451%3A1676515166615165&continue=https%3A%2F%2Fconsole.cloud.google.com%2F&followup=https%3A%2F%2Fconsole.cloud.google.com%2F&osid=1&passive=1209600&service=cloudconsole&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHdSaedEpVs88S0R65OA0-8Ftht_OuKTsts0VS580YhSJmq5QO69dOr9OvIEBM-NU79xKHVuQQ)
- [ADD](https://developers.google.com/workspace/guides/get-started?hl=ko)