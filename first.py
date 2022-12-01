from task.control import CalendarControl
from task.setup import get_calendar_service
from datetime import datetime, timedelta
from datetime import datetime as dateq
from datetime import date
import datetime  

control_api = CalendarControl()

print("───────────────────────────────────────")
print("1. 나의 캘린더")
print("2. 회의실 예약 캘린더")
print("3. 연차/반차 사용 캘린더")
print("4. 다른 캘린더 추가")
print("───────────────────────────────────────")
print("EX. 1 or 1번 or 일번 or 나")
print("EX. 2 or 2번 or 이번 or 회의실")
print("EX. 3 or 3번 or 삼번 or 연차")
print("EX. 4 or 4번 or 사번 or 추가", '\n')

sentence = input("원하시는 캘린더를 입력해주세요 : ")

if sentence == "1" or sentence == "1번" or sentence == "일번" or sentence == "나": 
    print("───────────────────────────────────────")
    print("1. 캘린더 조회")
    print("2. 캘린더 등록")
    print("3. 캘린더 삭제")
    print("4. 캘린더 수정")
    print("───────────────────────────────────────")
    print("EX. 1 or 1번 or 일번 or 조회")
    print("EX. 2 or 2번 or 이번 or 등록")
    print("EX. 3 or 3번 or 삼번 or 삭제")
    print("EX. 4 or 4번 or 사번 or 수정", "\n")
    
    first_seq = input("원하시는 캘린더 용도를 입력해주세요 : ")
    if first_seq == "1" or first_seq == "1번" or first_seq == "일번" or first_seq == "조회":
        sentence_one = input("이름, 날짜 중 어떤 걸로 찾으시겠습니까? : ")
        if sentence_one == "이름":
            print("구글 캘린더에 등록된 이름과 동일하게 작성 부탁드립니다.", "\n")
            sentence = input("캘린더의 이름을 작성해주세요 : ")
            
            now = datetime.datetime.utcnow().isoformat() + 'Z'

            events = control_api.get_event_list(calendarId = "primary", timeMin=now, orderBy='startTime')
            for event in events['items']: 
                value = event.get("start")
                if "date" in value:
                    if sentence == event['summary']:
                        time_j_one = event['start']['date']
                        print("조회 하신 캘린더 이름의 날짜는 {} 입니다.".format(time_j_one))                
                elif "dateTime" in value:
                    if sentence == event['summary']:
                        time_j_two = event['start']['dateTime']
                        trans_time_j_two = dateq.fromisoformat(time_j_two)
                        upend_time_j_two = trans_time_j_two.time().strftime('%H:%M')
                        print("조회 하신 캘린더 이름의 날짜는 {}, 시간은 {} 입니다.".format(trans_time_j_two.date(), upend_time_j_two))
                else:
                    pass

        elif sentence_one == "날짜":
            print("구글 캘린더에 등록된 날짜와 동일하게 작성 부탁드립니다.", "\n")
            year_data = input("이벤트 생성 년도를 말씀해주세요 : ")
            month_data = input("이벤트 생성 월을 말씀해주세요 : ")
            day_data = input("이벤트 생성 일을 말씀해주세요 : ")

            date_seq = date(int(year_data), int(month_data), int(day_data))

            now = datetime.datetime.utcnow().isoformat() + 'Z'

            events = control_api.get_event_list(calendarId = "primary", timeMin=now, orderBy='startTime')
            for event in events['items']:
                value = event.get("start")
                if "date" in value:
                    time_dm_one = event['start']['date']
                    if str(date_seq) == str(time_dm_one):
                        cal_name = event['summary']
                        print("조회된 이벤트 이름은 {}, 날짜는 {} 입니다.".format(cal_name, time_dm_one))
                elif "dateTime" in value:
                    time_dm_two = event['start']['dateTime']
                    trans_time_dm_two = dateq.fromisoformat(time_dm_two)
                    upend_time_dm_two = trans_time_dm_two.date().strftime('%Y-%m-%d')
                    upend_date_dm_two = trans_time_dm_two.time().strftime('%H:%M')
                    if str(date_seq) == str(upend_time_dm_two):
                        cal_name = event['summary']
                        print("조회된 이벤트 이름은 {}, 날짜는 {}, 시간은 {} 입니다.".format(cal_name, upend_time_dm_two, upend_date_dm_two))
                else:
                    pass
                        
    elif first_seq == "2" or first_seq == "2번" or first_seq == "이번" or first_seq == "등록":
        sentence_two = input("종일/시간 종류 중 어느 방식으로 등록하시겠습니까? : ")
        if sentence_two == "종일":
            sentence = input("이벤트 이름을 입력해주세요 : ")
            year_data = input("이벤트 생성 년도를 말씀해주세요 : ")
            month_data = input("이벤트 생성 월을 말씀해주세요 : ")
            day_data = input("이벤트 생성 일을 말씀해주세요 : ")
            print("상세 내용이 없는 경우 '없음' 으로 입력 부탁드립니다. ")
            comment_data = input("이벤트 상세 내용을 말씀해주세요 : ")

            date_time = dateq(int(year_data), int(month_data), int(day_data))
            timedata_start = date_time.isoformat()
            timedata_end = (date_time + timedelta(days=1)).isoformat()

            body = {
                "summary": sentence,
                "description": comment_data,
                "start": {"dateTime": timedata_start, "timeZone": "Asia/Seoul"},
                "end": {"dateTime": timedata_end, "timeZone": "Asia/Seoul"},
            }

            add = control_api.create_event(calendarId="primary", body = body)
            print(add)
            
        elif sentence_two == "시간":
            sentence = input("이벤트 이름을 입력해주세요 : ")
            year_data = input("이벤트 생성 년도를 말씀해주세요 : ")
            month_data = input("이벤트 생성 월을 말씀해주세요 : ")
            day_data = input("이벤트 생성 일을 말씀해주세요 : ")
            time_data = input("이벤트 생성 시간을 말씀해주세요 : ")
            minute_data = input("이벤트 생성 분을 말씀해주세요 : ")
            print("상세 내용이 없는 경우 '없음' 으로 입력 부탁드립니다. ")
            comment_data = input("이벤트 상세 내용을 말씀해주세요 : ")

            date_time = dateq(int(year_data), int(month_data), int(day_data), int(time_data), int(minute_data))
            timedata_start = date_time.isoformat()
            timedata_end = (date_time + timedelta(hours=1)).isoformat()

            body = {
                "summary": sentence,
                "description": comment_data,
                "start": {"dateTime": timedata_start, "timeZone": "Asia/Seoul"},
                "end": {"dateTime": timedata_end, "timeZone": "Asia/Seoul"},
            }

            add = control_api.create_event(calendarId="primary", body = body)
            print(add)
        
    elif first_seq == "3" or first_seq == "3번" or first_seq == "삼번" or first_seq == "삭제":
        print("구글 캘린더에 등록된 이름과 동일하게 작성 부탁드립니다.", "\n")
        sentence = input("캘린더의 이름을 작성해주세요 : ")
        year_data = input("이벤트 생성 년도를 말씀해주세요 : ")
        month_data = input("이벤트 생성 월을 말씀해주세요 : ")
        day_data = input("이벤트 생성 일을 말씀해주세요 : ")

        date_seq = date(int(year_data), int(month_data), int(day_data))

        now = datetime.datetime.utcnow().isoformat() + 'Z'

        events = control_api.get_event_list(calendarId = "primary", timeMin=now, orderBy='startTime')
        for event in events['items']:
            value = event.get("start")
            if "date" in value:
                time_j_one = event['start']['date']
                trans_time_j_one = dateq.fromisoformat(time_j_one).date()
                if sentence == event['summary'] and str(date_seq) == str(trans_time_j_one):
                    delete = control_api.delete_event(calendarId = "primary", eventId = event['id'])
                    print(delete)
            elif "dateTime" in value:
                time_dm_one = event['start']['dateTime']
                trans_time_dm_one = dateq.fromisoformat(time_dm_one).date()
                if sentence == event['summary'] and str(date_seq) == str(trans_time_dm_one):
                    delete = control_api.delete_event(calendarId = "primary", eventId = event['id'])
                    print(delete)
            else:
                pass
    
    elif first_seq == "4" or first_seq == "4번" or first_seq == "사번" or first_seq == "수정":
        print("1. 이벤트 이름")
        print("2. 시작 시간")
        print("3. 종료 시간")
        print("4. 이벤트 내용")
        print("ex: 1번 or 이름 / 2번 or 시작 / 3번 or 종료 / 4번 or 내용")
        sentence_three = input("원하는 수정을 입력해주세요. : ")

        if sentence_three == "1번" or sentence_three == "이름":
            print("구글 캘린더에 등록된 이름과 동일하게 작성 부탁드립니다.")
            sentence = input("캘린더의 이름을 작성해주세요. : ")
            year_data = input("이벤트 생성 년도를 말씀해주세요 : ")
            month_data = input("이벤트 생성 월을 말씀해주세요 : ")
            day_data = input("이벤트 생성 일을 말씀해주세요 : ")
            update_sentence = input("변경하고 싶은 이벤트 이름을 입력해주세요 : ")
            
            date_time = dateq(int(year_data), int(month_data), int(day_data))

            now = datetime.datetime.utcnow().isoformat() + 'Z'
            
            events = control_api.get_event_list(calendarId = "primary", timeMin=now, orderBy='startTime')
            for event in events['items']:   
                value = event.get("start")
                if "date" in value:
                    if sentence == event['summary'] and date_time.date() == value['date']:
                        event['summary'] = update_sentence
                        event = control_api.update_event_name(calendarId = 'primary', eventId = event['id'], body = event)
                        print(event)
                        
                elif "dateTime" in value:
                    time = value['dateTime']
                    transform_time = dateq.fromisoformat(time)
                    if sentence == event['summary'] and date_time.date() == transform_time.date():
                        event['summary'] = update_sentence
                        event = control_api.update_event_name(calendarId = 'primary', eventId = event['id'], body = event)
                        print(event)
                else:
                    pass
     
        elif sentence_three == "2번" or sentence_three == "시작":
            print("구글 캘린더에 등록된 이름과 동일하게 작성 부탁드립니다.")
            sentence = input("캘린더의 이름을 작성해주세요. : ")
            year_data = input("이벤트 생성 년도를 말씀해주세요 : ")
            month_data = input("이벤트 생성 월을 말씀해주세요 : ")
            day_data = input("이벤트 생성 일을 말씀해주세요 : ")
            
            date_time = dateq(int(year_data), int(month_data), int(day_data))
            
            now = datetime.datetime.utcnow().isoformat() + 'Z'
            
            events = control_api.get_event_list(calendarId = "primary", timeMin=now, orderBy='startTime')
            for event in events['items']:   
                value = event.get("start")
                if "date" in value:       
                    time = value['date']
                    transform_time = dateq.fromisoformat(time)                 
                    if sentence == event['summary'] and date_time.date() == transform_time.date():
                        update_year_data = input("변경하고 싶은 시작 생성 년도를 입력해주세요 : ")
                        update_month_data = input("변경하고 싶은 시작 생성 월을 입력해주세요 : ")
                        update_day_data = input("변경하고 싶은 시작 생성 일을 입력해주세요 : ")
                        
                        update_time_j = dateq(int(update_year_data), int(update_month_data), int(update_day_data))
                        update_time_j_start = update_time_j.date()
                        update_time_j_end_j = (update_time_j + timedelta(days=1)).isoformat()
                        update_time_j_end_dm = dateq.fromisoformat(update_time_j_end_j).date()
                        upstart_data = update_time_j_start.strftime('%Y-%m-%d')
                        upend_data = update_time_j_end_dm.strftime('%Y-%m-%d')
                                                            
                        body ={
                            "summary" : event['summary'],
                            "description": event['description'],
                            "start" : {"date" : upstart_data},
                            "end": {"date": upend_data},
                            }
                        
                        event = control_api.update_event_starttime_j(calendarId = 'primary', eventId = event['id'], body = body)
                        print(event)
                        
                elif "dateTime" in value:
                    time = value['dateTime']
                    transform_time = dateq.fromisoformat(time)
                    if sentence == event['summary'] and date_time.date() == transform_time.date():
                        update_year_data = input("변경하고 싶은 시작 생성 년도를 입력해주세요 : ")
                        update_month_data = input("변경하고 싶은 시작 생성 월을 입력해주세요 : ")
                        update_day_data = input("변경하고 싶은 시작 생성 일을 입력해주세요 : ")
                        update_time_data = input("변경하고 싶은 시작 생성 시간을 입력해주세요 : ")
                        update_minute_data = input("변경하고 싶은 시작 생성 분을 입력해주세요 : ")
                        
                        update_time_j = dateq(int(update_year_data), int(update_month_data), int(update_day_data), int(update_time_data), int(update_minute_data))
                        update_time_dm_start = update_time_j.isoformat()
                        update_time_dm_end = (update_time_j + timedelta(hours=1)).isoformat()
                        
                        body ={
                            "summary" : event['summary'],
                            "description": event['description'],
                            "start" : {"dateTime" : update_time_dm_start, "timeZone": "Asia/Seoul"},
                            "end": {"dateTime": update_time_dm_end, "timeZone": "Asia/Seoul"},
                            }
                        
                        event = control_api.update_event_starttime_dm(calendarId = 'primary', eventId = event['id'], body = body)
                        print(event)
                else:
                    pass

        elif sentence_three == "3번" or sentence_three == "종료":
            print("구글 캘린더에 등록된 이름과 동일하게 작성 부탁드립니다.")
            sentence = input("캘린더의 이름을 작성해주세요. : ")
            year_data = input("이벤트 생성 년도를 말씀해주세요 : ")
            month_data = input("이벤트 생성 월을 말씀해주세요 : ")
            day_data = input("이벤트 생성 일을 말씀해주세요 : ")
            
            date_time = dateq(int(year_data), int(month_data), int(day_data))
            
            now = datetime.datetime.utcnow().isoformat() + 'Z'
            
            events = control_api.get_event_list(calendarId = "primary", timeMin=now, orderBy='startTime')
            for event in events['items']:   
                value = event.get("start")
                if "date" in value:       
                    time = value['date']
                    transform_time = dateq.fromisoformat(time)                 
                    if sentence == event['summary'] and date_time.date() == transform_time.date():
                        update_year_data = input("변경하고 싶은 종료 생성 년도를 입력해주세요 : ")
                        update_month_data = input("변경하고 싶은 종료 생성 월을 입력해주세요 : ")
                        update_day_data = input("변경하고 싶은 종료 생성 일을 입력해주세요 : ")
                        
                        update_time_j = dateq(int(update_year_data), int(update_month_data), int(update_day_data))
                        update_time_j_end_j = update_time_j.isoformat()
                        update_time_j_end_dm = dateq.fromisoformat(update_time_j_end_j).date()
                        upend_data = update_time_j_end_dm.strftime('%Y-%m-%d')
                                                            
                        body ={
                            "summary" : event['summary'],
                            "description": event['description'],
                            "start" : {"date" : event['start']['date']},
                            "end": {"date": upend_data},
                            }
                        
                        event = control_api.update_event_starttime_j(calendarId = 'primary', eventId = event['id'], body = body)
                        print(event)
                        
                elif "dateTime" in value:
                    time = value['dateTime']
                    transform_time = dateq.fromisoformat(time)
                    if sentence == event['summary'] and date_time.date() == transform_time.date():
                        update_year_data = input("변경하고 싶은 종료 생성 년도를 입력해주세요 : ")
                        update_month_data = input("변경하고 싶은 종료 생성 월을 입력해주세요 : ")
                        update_day_data = input("변경하고 싶은 종료 생성 일을 입력해주세요 : ")
                        update_time_data = input("변경하고 싶은 종료 생성 시간을 입력해주세요 : ")
                        update_minute_data = input("변경하고 싶은 종료 생성 분을 입력해주세요 : ")
                        
                        update_time_j = dateq(int(update_year_data), int(update_month_data), int(update_day_data), int(update_time_data), int(update_minute_data))
                        update_time_dm_end = update_time_j.isoformat()
                        
                        body ={
                            "summary" : event['summary'],
                            "description": event['description'],
                            "start" : {"dateTime" : event['start']['dateTime'], "timeZone": "Asia/Seoul"},
                            "end": {"dateTime": update_time_dm_end, "timeZone": "Asia/Seoul"},
                            }
                        
                        event = control_api.update_event_starttime_dm(calendarId = 'primary', eventId = event['id'], body = body)
                        print(event)
                else:
                    pass    
        
        elif sentence_three == "4번" or sentence_three == "내용":
            print("구글 캘린더에 등록된 이름과 동일하게 작성 부탁드립니다.")
            sentence = input("캘린더의 이름을 작성해주세요. : ")
            year_data = input("이벤트 생성 년도를 말씀해주세요 : ")
            month_data = input("이벤트 생성 월을 말씀해주세요 : ")
            day_data = input("이벤트 생성 일을 말씀해주세요 : ")
            update_sentence = input("변경하고 싶은 이벤트 내용을 입력해주세요 : ")
            
            date_time = dateq(int(year_data), int(month_data), int(day_data))

            now = datetime.datetime.utcnow().isoformat() + 'Z'
            
            events = control_api.get_event_list(calendarId = "primary", timeMin=now, orderBy='startTime')
            for event in events['items']:   
                value = event.get("start")
                if "date" in value:
                    if sentence == event['summary'] and date_time.date() == value['date']:
                        event['description'] = update_sentence
                        event = control_api.update_event_comment(calendarId = 'primary', eventId = event['id'], body = event)
                        print(event)
                        
                elif "dateTime" in value:
                    time = value['dateTime']
                    transform_time = dateq.fromisoformat(time)
                    if sentence == event['summary'] and date_time.date() == transform_time.date():
                        event['description'] = update_sentence
                        event = control_api.update_event_comment(calendarId = 'primary', eventId = event['id'], body = event)
                        print(event)
                else:
                    pass
                
    else:
        print("예시와 같은 방법으로 입력해주세요.")
