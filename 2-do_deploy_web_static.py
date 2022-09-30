#!/usr/bin/python3
'''module for package web static archive'''

from fabric.api import env, run, put
import os


env.hosts = ['35.175.113.245', '18.232.105.65']


def do_deploy(archive_path):
    '''deploy web archive'''
    if not os.path.exists(archive_path):
        return False
    file = archive_path.split('/')[-1]
    dirr = file.split('.')[0]
    stat = put(archive_path, '/tmp')
    if stat.failed:
        return False
    code = run('mkdir -p /data/web_static/releases/{}/'.format(dirr))
    if code.return_code != 0:
        return False
    code = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
               .format(file, dirr))
    if code.return_code != 0:
        return False
    code = run('rm /tmp/{}'.format(file))
    if code.return_code != 0:
        return False
    c = 'mv /data/web_static/releases/{}/web_static/* '.format(dirr)
    c += '/data/web_static/releases/{}/'.format(dirr)
    code = run(c)
    if code.return_code != 0:
        return False
    code = run('rm -rf /data/web_static/releases/{}/web_static'.format(dirr))
    if code.return_code != 0:
        return False
    code = run('rm -rf /data/web_static/current')
    if code.return_code != 0:
        return False
    c = 'ln -s /data/web_static/releases/{}/ '.format(dirr)
    c += '/data/web_static/current'
    code = run(c)
    if code.return_code != 0:
        return False
