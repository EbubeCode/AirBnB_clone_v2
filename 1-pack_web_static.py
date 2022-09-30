#!/usr/bin/python3
'''module for package web static archive'''

from fabric.api import local
import os
import datetime


def do_pack():
    '''function to package web archive'''
    path = './versions'
    now = datetime.datetime.now()
    suf = '{}{}{}{}{}{}'.format(now.year, now.month,
                                now.day, now.hour, now.minute, now.second)
    if not os.path.exists(path):
        os.makedirs(path)
    code = local('tar -cvzf versions/web_static_{}.tgz web_static'.format(suf))
    if code == 0:
        return 'versions/web_static_{}.tgz'.format(suf)
    else:
        return None
