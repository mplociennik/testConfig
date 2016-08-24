#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib2
import ConfigParser

response = urllib2.urlopen('https://raw.githubusercontent.com/mplociennik/testConfig/master/config.cfg')
print response