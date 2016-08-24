#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib2
import ConfigParser
import json

response = urllib2.urlopen('https://raw.githubusercontent.com/mplociennik/testConfig/master/config.json')
data = json.load(response)

for key in data['config']:
    print '{0}:{1}'.format(key, data['config'][key])