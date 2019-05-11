import json
import mechanize
import boto3

def lambda_handler(event, context):
    LOGIN_URL = 'https://industry.socs.binus.ac.id/learning-plan/auth/login'
    LOGBOOK_URL = 'https://industry.socs.binus.ac.id/learning-plan/student/log-book/insert'

    # or like you know, you can instead pull data from dynamodb instead...
    # take shit from event

    USERNAME = ''
    PASSWORD = ''

    br = mechanize.Browser()
    br.set_handle_robots(False)   # ignore robots
    br.addheaders = [('User-agent', 'Firefox')]

    # login to get session n shit
    br.open(LOGIN_URL)

    br.form = br.forms()[0]
    br.form['username'] = USERNAME
    br.form['password'] = PASSWORD
    req = br.submit()

    # post stuff on logbook
    br.open(LOGBOOK_URL)

    br.form = br.forms()[2]
    br.form['clock-in'] = '0'
    br.form['clock-out'] = '0'
    br.form['activity'] = 'off'
    br.form['description'] = 'off'
    br.submit()

    # send ses here!

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "ayy lmao",
        }),
    }
