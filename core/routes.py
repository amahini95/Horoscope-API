from core import api
from flask import jsonify
from flask_restx import Resource, reqparse
from datetime import datetime
from werkzeug.exceptions import BadRequest, NotFound

from core.utils import get_daily_horoscope, get_monthly_horoscope, get_weekly_horoscope

ns = api.namespace('/', description='Horoscope APIs')

ZODIAC_SIGNS = {
    "Aries": 1,
    "Taurus": 2,
    "Gemini": 3,
    "Cancer": 4,
    "Leo": 5,
    "Virgo": 6,
    "Libra": 7,
    "Scorpio": 8,
    "Sagittarius": 9,
    "Capricorn": 10,
    "Aquarius": 11,
    "Pisces": 12
}
'''
use this to parse query parms from URL
courtesy of reqparse - Flask-RESTX's library for req data validation
(akin to argparse)
'''
parser = reqparse.RequestParser()
'''
this adds args in the URL
Here, our parm must be a "str", and it IS required (True)
'''
parser.add_argument('sign', type=str, required=True)
'''
Need another query parameter day, only used in daily horoscope URL
To do this, write a parent parser with all shared args
Then extend parser with "copy()"
Where our parser_copy will require "day", and "sign"
'''
parser_copy = parser.copy()
parser_copy.add_argument('day', type=str, required=True)
'''
Main building blocks provided by Flask-RESTX are resources.
Resources are built on top of Flask pluggable views,
alloing for easy access to many HTTP methods -
simply by defining methods on my resource
'''


#The @ns.route() decorator sets the API route,
#and also help us add the query parms on the URL
@ns.route('/get-horoscope/daily')
#this class inherits the Resource class from flask_restx
class DailyHoroscopeAPI(Resource):
    #Shows daily horoscope of zodiac signs
    @ns.doc(parser=parser_copy)
    def get(self):
        args = parser_copy.parse_args()
        day = args.get('day')
        zodiac_sign = args.get('sign')
        try:
            zodiac_num = ZODIAC_SIGNS[zodiac_sign.capitalize()]
            if "-" in day:
                datetime.strptime(day, '%Y-%m-%d')
            horoscope_data = get_daily_horoscope(zodiac_num, day)
            return jsonify(success=True, data=horoscope_data, status=200)
        except KeyError:
            raise NotFound('No such zodiac sign exists')
        except AttributeError:
            raise BadRequest(
                'Something went wrong, please check the URL and the arguments.'
            )
        except ValueError:
            raise BadRequest('Please enter day in correct format: YYYY-MM-DD')


@ns.route('/get-horoscope/weekly')
class WeeklyHoroscropeAPI(Resource):
    #Show weekly horoscope zodiac signs
    @ns.doc(parser=parser)
    def get(self):
        args = parser.parse_args()
        zodiac_sign = args.get('sign')
        try:
            zodiac_num = ZODIAC_SIGNS[zodiac_sign.capitalize()]
            horoscope_data = get_weekly_horoscope(zodiac_num)
            return jsonify(success=True, data=horoscope_data, status=200)
        except KeyError:
            raise NotFound('No such zodiac sign exists')
        except AttributeError:
            raise BadRequest(
                'Something went wrong, please check the URL and the arguments.'
            )


@ns.route('/get-horoscope/monthly')
class MonthlyHoroscropeAPI(Resource):
    #Show weekly horoscope zodiac signs
    @ns.doc(parser=parser)
    def get(self):
        args = parser.parse_args()
        zodiac_sign = args.get('sign')
        try:
            zodiac_num = ZODIAC_SIGNS[zodiac_sign.capitalize()]
            horoscope_data = get_monthly_horoscope(zodiac_num)
            return jsonify(success=True, data=horoscope_data, status=200)
        except KeyError:
            raise NotFound('No such zodiac sign exists')
        except AttributeError:
            raise BadRequest(
                'Something went wrong, please check the URL and the arguments.'
            )