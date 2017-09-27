# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from time import gmtime, strftime


# Create your views here.

print "in app views"


# Create your views here.

def index(request):
    return render(request, 'session_words/index.html')

def add(request):
    for k, v in request.POST.items():
        if len(v) < 1:
            messages.info(request, "But the word...we need it")
            return redirect('/')
    if 'big' in request.POST:
        font_size = "id='big'"
    else:
        font_size = ""
    print font_size
    if request.POST['color'] == "blue":
        request.session['word'] += "<p class='blue' {} >{} - {}</p>".format(font_size, request.POST['word'], strftime("%b %d, %Y %I:%M %p", gmtime()))
    elif request.POST['color'] == "green":
        request.session['word'] += "<p class='green' {} >{} - {}</p>".format(font_size, request.POST['word'], strftime("%b %d, %Y %I:%M %p", gmtime()))
    elif request.POST['color'] == "orange":
        request.session['word'] += "<p class='orange' {} >{} - {}</p>".format(font_size, request.POST['word'],strftime("%b %d, %Y %I:%M %p", gmtime()))
   

    return redirect('/')

def clear(request):
    request.session['word'] = ""
    return redirect('/')