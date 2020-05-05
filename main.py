# coding:utf-8

import os
from flask import Flask, request, jsonify
import mysql.connector

conn = mysql.connector.connect(
    user=os.getenv('MYSQL_USER', 'user'),
    password=os.getenv('MYSQL_PASS', 'password'),
    host=os.getenv('MYSQL_HOST', 'localhost'),
    database=os.getenv('MYSQL_DB', 'sample')
)

app = Flask(__name__)

@app.route('/')
def index():
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
    return jsonify(results)

@app.route('/{zipcode}')
def find(zipcode):
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
    return jsonify(results)

if __name__ == '__main__':
    app.run()
