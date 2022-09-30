#!/usr/bin/python3
'''module for package web static archive'''

from fabric.api import local, env, run, put
import datetime
import os


env.hosts = ['35.175.113.245', '18.232.105.65']


def do_pack():
    '''function to package web archive'''
    path = './versions'
    now = datetime.datetime.now()
    suf = '{}{}{}{}{}{}'.format(now.year, now.month,
                                now.day, now.hour, now.minute, now.second)
    if not os.path.exists(path):
        os.makedirs(path)
    code = local('tar -cvzf versions/web_static_{}.tgz web_static'.format(suf))
    if code.return_code == 0:
        return './versions/web_static_{}.tgz'.format(suf)
    else:
        return None


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
    return True


def deploy():
    '''deploy web archive'''

    arch_path = do_pack()
    if not arch_path:
        return False
    return do_deploy(arch_path)
