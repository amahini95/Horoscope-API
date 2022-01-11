import requests
from bs4 import BeautifulSoup


def get_daily_horoscope(zodiac_sign: int, day: str):
    #today's HS
    #"if the day is NOT a custom date, there's no '-' "
    if not "-" in day:
        res = requests.get(
            f"https://horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
        )
    #an older HS, i.e. a custom date
    else:
        day = day.replace("-", "")
        #make a GET request on url below
        res = requests.get(
            f"https://horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day}"
        )
    #pull HTML data from "res" using BS
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text


def get_weekly_horoscope(zodiac_sign: int):
    res = requests.get(
        f"https://horoscope.com/us/horoscopes/general/horoscope_general-weekly.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text


def get_monthly_horoscope(zodiac_sign: int):
    res = requests.get(
        f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text