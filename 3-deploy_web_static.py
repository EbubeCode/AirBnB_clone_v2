#!/usr/bin/python3
'''module for package web static archive'''

from fabric.api import local, env, run, put
import datetime
import os


env.hosts = ['35.175.113.245', '18.232.105.65']


def deploy():
    '''deploy web archive'''

    arch_path = do_pack()
    if not arch_path:
        return False
    return do_deploy(arch_path)
