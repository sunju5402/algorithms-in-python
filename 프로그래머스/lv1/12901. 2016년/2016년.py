from datetime import date
def solution(a, b):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return days[date(2016, a, b).weekday()]