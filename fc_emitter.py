#!/usr/bin/python
# -*- coding: utf-8 -*-

# Mats Melander, 2021-11-14
__author__ = 'mm'

from flask import Flask, request, abort, jsonify, render_template
import requests
import uritemplate
import logging
from logging.handlers import HTTPHandler

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)

http_handler = logging.handlers.HTTPHandler('www.viltstigen.se', '/logger/log', method='POST', secure=True)
_LOGGER.addHandler(http_handler)


class ReverseProxied(object):
    def __init__(self, app, script_name):
        self.app = app
        self.script_name = script_name

    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = self.script_name
        return self.app(environ, start_response)


app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app, script_name='/forecast')


def par_filter(lst, par):
    return next(item for item in lst['parameters'] if item['name'] == par)['values'][0]


@app.route('/_fc')
def fc():
    lat = request.args.get('lat', '')
    lon = request.args.get('lon', '')

    if lat == '' or lon == '':
        abort(404, description="Resource not found")
    else:
        site_url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json"

        data_url = uritemplate.expand(site_url, lon=lon, lat=lat)
        try:
            # "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json"
            data = requests.get(data_url).json()
            res = []
            for par in data['timeSeries']:
                res.append({'time': par['validTime'],
                            'temp': par_filter(par, 't'),
                            'hum': par_filter(par, 'r'),
                            'rain': par_filter(par, 'pmax'),
                            'wind_speed': par_filter(par, 'ws'),
                            'wind_dir': par_filter(par, 'wd'),
                            'wind_max': par_filter(par, 'gust')})
            return jsonify({'data': res})
        except requests.HTTPError:
            logging.warning("HTTPError")
            abort(404, description="Resource not found")


@app.route('/')
def index():
    return render_template('fc.html')
