# -*- coding: utf-8 -*-
'''
Created on 01 29, 2016

@author: tolerious

'''

from fabric.api import *
import datetime
# env.hosts = ['wx.meiparking.com']
# env.user = 'tolerious'
env.roledefs = {
    'p': ['meibo@service.meiparking.com'],
    't': ['tolerious@wx.meiparking.com']
}


def l():
    o = local("git br", capture=True)
    print o


def t(b, c=""):
    timestamp = datetime.datetime.now().strftime("%F %R %S")
    with settings(warn_only=True):
        local("git commit -am ' update..., %s ; timestamp: %s'&&git push origin %s" % (c, timestamp, b))
    with cd("/home/tolerious/meibo_env/meibo"):
        run("git stash")
        commend = "git ck %s" % b
        run("git fetch")
        print commend
        run(commend)
        run("git pull origin %s" % b)
        run("source ../bin/activate")
        run("python manage.py collectstatic")
        run("cd .. && python restart_uwsgi.py uwsgi.ini")

def j(b,c=""):
    timestamp = datetime.datetime.now().strftime("%F %R %S")
    with settings(warn_only=True):
        local("git commit -am ' update..., %s ; timestamp: %s'&&git push origin %s" % (c, timestamp, b))

def f():
    with cd("/Users/fengxiaolong/APICloud/workspace/NearBuy"):
        # run("git stash")
        local("git commit -am 'update ...' && git push origin master")
