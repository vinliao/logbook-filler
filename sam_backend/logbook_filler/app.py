import json
import mechanize
import boto3
import datetime
import random

def lambda_handler(event, context):
    LOGIN_URL = 'https://industry.socs.binus.ac.id/learning-plan/auth/login'
    LOGBOOK_URL = 'https://industry.socs.binus.ac.id/learning-plan/student/log-book/insert'

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('logbook-table')

    response = table.get_item(
    Key={
            'id': '2001577604',
        }
    )

    # print(response)
    logbook_data = response['Item']
    username = logbook_data['id']
    password = logbook_data['password']

    # check datetime, if not saturday ors sunday, abort the function
    day_of_week = datetime.datetime.today().weekday()
    # if it's weekend
    if(day_of_week == 6 or day_of_week == 7):
        clock_in = '0'
        clock_out = '0'
        activity = 'off'
        description = 'off'
    #if it's weekday
    else:
        activity_detail_dict = logbook_data['activity']
        activity_detail = random.choice(list(activity_detail_dict))
        
        print(activity_detail)
        clock_in = '7'
        clock_out = '18'
        activity = activity_detail
        description = activity_detail_dict[activity_detail]


    br = mechanize.Browser()
    br.set_handle_robots(False)   # ignore robots
    br.addheaders = [('User-agent', 'Firefox')]

    # login to get session n shit
    br.open(LOGIN_URL)

    br.form = br.forms()[0]
    br.form['username'] = username
    br.form['password'] = password
    req = br.submit()

    # post stuff on logbook
    br.open(LOGBOOK_URL)

    br.form = br.forms()[2]
    br.form['clock-in'] = clock_in
    br.form['clock-out'] = clock_out
    br.form['activity'] = activity
    br.form['description'] = description
    br.submit()

    # send ses here!

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "ayy lmao",
        }),
    }
