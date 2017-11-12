# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#
# def Home(request):
#     return

def SignUp(request):

    return render(request, 'signup.html', {
        'data' : 'demo'
    })


def Login(request):

    return render(request, 'login.html', {
        'data' : 'demo'
    })

def LogOut(request):

    return render(request, 'logout.html', {
        'data' : 'demo'
    })

def Search(request):

    return render(request, 'search.html', {
        'data' : 'search'
    })

def Result(request):

    return render(request, 'result.html', {
        'data' : 'demo'
    })

def Otp(request):

    return render(request, 'otp.html', {
        'data' : 'demo'
    })
