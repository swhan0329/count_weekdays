from business_duration import businessDuration
import pandas as pd
import datetime

print("======================================")
print("            2020, 2021 year           ")
print("  주말 및 공휴일 제외 날짜 카운팅 프로그램   ")
print("          made by Seo Woo Han         ")
print("======================================")

while(True):
    sd = input("start date를 입력하세요. 입력 후, Enter 키 입력. (format) yyyy-mm-dd:")
    if not len(sd) == 10:
        print('입력 data format이 다릅니다. 프로그램을 다시 시도해주세요.')
        exit(200)
    startdate = pd.to_datetime(sd)
    ed = input("end date를 입력하세요. 입력 후, Enter 키 입력. (format) yyyy-mm-dd:")
    if not len(ed) == 10:
        print('입력 data format이 다릅니다. 프로그램을 다시 시도해주세요.')
        exit(200)
    enddate = pd.to_datetime(ed)
    korean_holidaylist_2020_2021 = {
        datetime.date(2020, 1, 1): '새해',
        datetime.date(2020, 1, 24): '설날',
        datetime.date(2020, 1, 25): '설날',
        datetime.date(2020, 1, 26): '설날',
        datetime.date(2020, 3, 1): '삼일절',
        datetime.date(2020, 4, 30): '부처님오신날',
        datetime.date(2020, 5, 5): '어린이날',
        datetime.date(2020, 6, 6): '현충일',
        datetime.date(2020, 8, 15): '광복절',
        datetime.date(2020, 9, 30): '추석',
        datetime.date(2020, 10, 1): '추석',
        datetime.date(2020, 10, 2): '추석',
        datetime.date(2020, 10, 3): '개천절',
        datetime.date(2020, 10, 9): '한글날',
        datetime.date(2020, 12, 25): '크리스마스',
        datetime.date(2021, 1, 1): '새해',
        datetime.date(2021, 2, 11): '설날',
        datetime.date(2021, 2, 12): '설날',
        datetime.date(2021, 2, 13): '설날',
        datetime.date(2021, 3, 1): '삼일절',
        datetime.date(2021, 5, 5): '어린이날',
        datetime.date(2021, 5, 19): '부처님오신날',
        datetime.date(2021, 6, 6): '현충일',
        datetime.date(2021, 8, 15): '광복절',
        datetime.date(2021, 9, 20): '추석',
        datetime.date(2021, 9, 21): '추석',
        datetime.date(2021, 9, 22): '추석',
        datetime.date(2021, 10, 3): '개천절',
        datetime.date(2021, 10, 9): '한글날',
        datetime.date(2021, 12, 25): '크리스마스'}

    unit='day'
    #By default Saturday and Sunday are excluded
    print(sd,"부터 ", ed,"까지 주말 및 공휴일 제외 평일 날짜수:",
                   int(businessDuration(startdate,enddate,holidaylist=korean_holidaylist_2020_2021,unit=unit))+1,"일")
    print((int(businessDuration(startdate,enddate,holidaylist=korean_holidaylist_2020_2021,unit=unit))+1)/5,"주")
