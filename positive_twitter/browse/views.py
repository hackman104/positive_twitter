import os
from pprint import pprint

import twitter
from django.http import HttpResponse
from django.shortcuts import render

from .services import get_recent


def index(request):
    results = get_recent()
    result_text = [result.text for result in results]
    pprint(result_text)
    return HttpResponse("This is a placeholder for the main page.")
