df = {
    "type": "CARD_CLICKED",
    "eventTime": "2023-01-13T05:19:13.925126Z",
    "message": {
        "name": "spaces/AAAAzn3Bzac/messages/RI2JF8DQs_s.RI2JF8DQs_s",
        "sender": {
            "name": "users/112570383047032352572",
            "displayName": "코코봇",
            "avatarUrl": "https://lh6.googleusercontent.com/proxy/yNIjT7WKl3HxSm-u468-yf4LJHPpTC9IoXHhtCxnDSmiaJsosj3rrIXUZgLhU3mhVmsfbKaCujIhNI9nywD4btdYsqKPuMeIqHqLw1cUSok0dDV4V_ap",
            "type": "BOT"
        },
        "createTime": "2023-01-13T05:07:55.198415Z",
        "thread": {
            "name": "spaces/AAAAzn3Bzac/threads/RI2JF8DQs_s",
            "retentionSettings": {
                "state": "PERMANENT"
            }
        },
        "space": {
            "name": "spaces/AAAAzn3Bzac",
            "type": "ROOM",
            "displayName": "챗봇 테스트",
            "externalUserAllowed": True,
            "spaceThreadingState": "THREADED_MESSAGES",
            "spaceType": "SPACE",
            "spaceHistoryState": "HISTORY_ON"
        },
        "cardsV2": [
            {
                "cardId": "exampleCard",
                "card": {
                    "sections": [
                        {
                            "widgets": [
                                {
                                    "buttonList": {
                                        "buttons": [
                                            {
                                                "text": "대한민국의 휴일",
                                                "onClick": {
                                                    "action": {
                                                        "function": "open_dialog",
                                                        "parameters": [
                                                            {
                                                                "key": "ko.south_korea#holiday@group.v.calendar.google.com",
                                                                "value": "삭제"
                                                            }
                                                        ],
                                                        "interaction": "OPEN_DIALOG"
                                                    }
                                                }
                                            },
                                            {
                                                "text": "생일",
                                                "onClick": {
                                                    "action": {
                                                        "function": "open_dialog",
                                                        "parameters": [
                                                            {
                                                                "key": "addressbook#contacts@group.v.calendar.google.com",
                                                                "value": "삭제"
                                                            }
                                                        ],
                                                        "interaction": "OPEN_DIALOG"
                                                    }
                                                }
                                            },
                                            {
                                                "text": "dmjeong@jei.com",
                                                "onClick": {
                                                    "action": {
                                                        "function": "open_dialog",
                                                        "parameters": [
                                                            {
                                                                "key": "dmjeong@jei.com",
                                                                "value": "삭제"
                                                            }
                                                        ],
                                                        "interaction": "OPEN_DIALOG"
                                                    }
                                                }
                                            },
                                            {
                                                "text": "4층 비타민C 회의실 예약",
                                                "onClick": {
                                                    "action": {
                                                        "function": "open_dialog",
                                                        "parameters": [
                                                            {
                                                                "key": "c_vaoqt576u3d3erbq7fit4cgcmk@group.calendar.google.com",
                                                                "value": "삭제"
                                                            }
                                                        ],
                                                        "interaction": "OPEN_DIALOG"
                                                    }
                                                }
                                            },
                                            {
                                                "text": "2022년 법정의무교육(정사원)",
                                                "onClick": {
                                                    "action": {
                                                        "function": "open_dialog",
                                                        "parameters": [
                                                            {
                                                                "key": "c_classroom2e447944@group.calendar.google.com",
                                                                "value": "삭제"
                                                            }
                                                        ],
                                                        "interaction": "OPEN_DIALOG"
                                                    }
                                                }
                                            },
                                            {
                                                "text": "연차(휴가)/반차 사용",
                                                "onClick": {
                                                    "action": {
                                                        "function": "open_dialog",
                                                        "parameters": [
                                                            {
                                                                "key": "c_d3r9nsibhcdbc3br7hv5tce99g@group.calendar.google.com",
                                                                "value": "삭제"
                                                            }
                                                        ],
                                                        "interaction": "OPEN_DIALOG"
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ],
        "retentionSettings": {
            "state": "PERMANENT"
        },
        "messageHistoryState": "HISTORY_ON"
    },
    "user": {
        "name": "users/114164005879224092462",
        "displayName": "정동명",
        "avatarUrl": "https://lh3.googleusercontent.com/a/AEdFTp4J4TdQUN6XAWLTPpVLaGeE4cxvpixbs6jY9Tzb4w=k",
        "email": "dmjeong@jei.com",
        "type": "HUMAN",
        "domainId": "0t6u1sf"
    },
    "space": {
        "name": "spaces/AAAAzn3Bzac",
        "type": "ROOM",
        "displayName": "챗봇 테스트",
        "externalUserAllowed": True,
        "spaceThreadingState": "THREADED_MESSAGES",
        "spaceType": "SPACE",
        "spaceHistoryState": "HISTORY_ON"
    },
    "action": {
        "actionMethodName": "calendar_delete"
    },
    "configCompleteRedirectUrl": "https://chat.google.com/api/bot_config_complete?token=AEs0LCAwAMDjT5vDJtC8KeGtsERu5BYSqk17DGqej0gnOVa8GwPU5jg0aw47-eDcizK7ckqLM7b7Jbp_paaM5r6FeYNd81VSGaBEQR5gUOexP6Hhxm5HUKxL9Qz8_WoXj2_zX4Tvz34DnsnRQY54azg%3D",
    "isDialogEvent": True,
    "dialogEventType": "SUBMIT_DIALOG",
    "common": {
        "userLocale": "ko-KR",
        "hostApp": "CHAT",
        "formInputs": {
            "calendar_date": {
                "stringInputs": {
                    "value": [
                        ""
                    ]
                }
            },
            "calendar_name": {
                "stringInputs": {
                    "value": [
                        ""
                    ]
                }
            }
        },
        "invokedFunction": "calendar_delete"
    }
}

calendar_name = df['message']['cardsV2'][0]['card']['sections'][0]['widgets'][0]['buttonList']['buttons']

bin_list= []
for i in calendar_name:
    a = i["onClick"]["action"]["parameters"][0]["key"]
    bin_list.append(a)
    
if "c_vaoqt576u3d3erbq7fit4cgcmk@group.calendar.google.com" in bin_list:
    print("ㄴㄴㄴㄴ")
else:
    print("eeeeeee")