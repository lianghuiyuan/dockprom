#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#

# 参考：https://www.cnblogs.com/wilber2013/p/4763067.html
from wsgiref.simple_server import make_server
import json

def routers():
    urlpatterns = (
        ('/book', f1),
        ('/web', f2),
        ('/grafana/alerts/gt', grafana_alerts),
        #('/alertmanager/alerts/gt', alertmanager_alerts),
    )
    return  urlpatterns


def f1(x):
    print('Hello, book')
    return [b'<h1>Hello, book</h1>']


def f2(x):

    print('Hello, web')
    return [b'<h1>Hello, web</h1>']

def grafana_alerts(x):
    print('grafana alert Message')
    return [b'<h1>Hello, grafana alert Message</h1>']

def alertmanager_alerts(x):
    print("入口参数: %s", x)
    print('Alertmanager alert Message')
    return [b'<h1>Hello, Alertmanager alert Message</h1>']



def application(environ, start_response):

    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
        
    # When the method is POST the query string will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = environ['wsgi.input'].read(request_body_size)
    data = json.loads(request_body)
    print("data keys: %s", data.keys())
    alerts = data.get('alerts') # Returns a list of alerts.
    
    print("wsgi.input %s", environ['wsgi.input'])
    print("request_body_size %s", environ.get('CONTENT_LENGTH', 0))
    print("request_body %s", request_body)
    print("alerts %s", alerts)
    
    urlpatterns = routers()
    path = environ["PATH_INFO"]
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func(alerts)
    else:
        return ["<h1>404</h1>".encode("utf8")]
    start_response('200 OK', [('Content-Type', 'text/html')])
    print('HTTP Request on port 8080, Response 200 OK...')




httpd = make_server('', 8080, application)
print('Serving HTTP on port 8080...')
httpd.serve_forever()
