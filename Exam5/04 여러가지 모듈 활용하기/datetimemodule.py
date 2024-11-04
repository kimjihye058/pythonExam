from datetime import datetime

print("현재 날짜 시각 객체 얻기")
today = datetime.now()
print("today = datetime.now() : ", today)
print("연, 월, 일: ", today.year, today.month, today.day)
print("시, 분, 초: ", today.hour, today.minute, today.second)
print("요일: ", today.weekday())
print("특정 날짜 시각 객체 만들기")
day = datetime(2007, 5, 8, 0, 0, 0)
print("day = datetime(2007, 5, 8, 0, 0, 0) : ", day)
print("2007년부터 지나온 시간 구하기")
print("today - day : ", today-day)