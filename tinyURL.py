from __future__ import with_statement
import PySimpleGUI as sg
# coding: utf-8
import contextlib

try:
    from urllib.parse import urlencode

except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen

except ImportError:
    from urllib2 import urlopen

import sys


def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8 ')

layout = [[sg.Text('Enter your URL')],
                 [sg.InputText()],
                 [sg.Submit()]]

window = sg.Window('Tinyurl Service', layout)

event, values = window.read()
window.close()

text_input = values[0]
sg.popup('Your shorten url: ', make_tiny(text_input))