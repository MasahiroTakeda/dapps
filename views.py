from requests_oauthlib import OAuth1Session
import json
import re
import os
import requests
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    Message = {
        'words': request.GET.get('words'),
    }

    msg = request.GET.get('words')

    C_KEY = "***********************"
    C_SECRET = "***********************"
    A_KEY = "***********************"
    A_SECRET = "***********************"

    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = {"status": msg,"lang": "ja"}
    tw = OAuth1Session(C_KEY,C_SECRET,A_KEY,A_SECRET)
    req = tw.post(url, params = params)

    return render(request, 'index.html', Message)