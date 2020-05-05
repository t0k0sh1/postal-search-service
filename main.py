# coding:utf-8

import os
from flask import Flask, request, jsonify
import mysql.connector

if os.getenv('ENV', 'DEVELOPMENT') == 'PRODUCTION':
    conn = mysql.connector.connect(
        user=os.getenv('MYSQL_USER', 'user'),
        password=os.getenv('MYSQL_PASS', 'password'),
        database=os.getenv('MYSQL_DB', 'sample'),
        unix_socket=os.getenv('MYSQL_HOST', '')
    )
else:
    conn = mysql.connector.connect(
        user=os.getenv('MYSQL_USER', 'user'),
        password=os.getenv('MYSQL_PASS', 'password'),
        host=os.getenv('MYSQL_HOST', 'localhost'),
        database=os.getenv('MYSQL_DB', 'sample')
    )

def select_by_query(request):
    # For more information about CORS and CORS preflight requests, see
    # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request
    # for more information.

    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
        }

        return ('', 204, headers)

    q = request.args.get('q')

    conn.ping(reconnect=True)
    cur = conn.cursor()
    cur.execute("SELECT * FROM address WHERE zipcode LIKE '{}%' OR pref_name LIKE '%{}%' OR pref_name_kana LIKE '%{}%' OR city_name LIKE '%{}%' OR city_name_kana LIKE '%{}%' OR town_name LIKE '%{}%' OR town_name_kana LIKE '%{}%'".format(q, q, q, q, q, q, q))
    ret = cur.fetchall()

    results = []
    for item in ret:
        results.append(dict(
            zipcode=item[1],
            pref_name=item[2],
            pref_name_kana=item[3],
            city_name=item[4],
            city_name_kana=item[5],
            town_name=item[6],
            town_name_kana=item[7]
        ))
    
    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*',
    }
    
    return (jsonify(results), 200, headers)

def find_by_zipcode(request, zipcode):
    # For more information about CORS and CORS preflight requests, see
    # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request
    # for more information.
    
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
        }

        return ('', 204, headers)

    conn.ping(reconnect=True)
    cur = conn.cursor()
    cur.execute("SELECT * FROM address WHERE zipcode = '{}'".format(zipcode))
    ret = cur.fetchall()

    results = []
    for item in ret:
        results.append(dict(
            zipcode=item[1],
            pref_name=item[2],
            pref_name_kana=item[3],
            city_name=item[4],
            city_name_kana=item[5],
            town_name=item[6],
            town_name_kana=item[7]
        ))
    
    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*',
    }

    return (jsonify(results), 200, headers)

if __name__ == '__main__':

    app = Flask(__name__)

    @app.route('/', methods=['GET','OPTIONS'])
    def index():
        return select_by_query(request)

    @app.route('/{zipcode}', methods=['GET','OPTIONS'])
    def find(zipcode):
        return find_by_zipcode(request, zipcode)

    app.run()
