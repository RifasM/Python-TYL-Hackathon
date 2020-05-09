from django.core.mail import EmailMessage, send_mail
from django.db.models import Sum
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import pandas as pd
from random import randint
from django.contrib.auth import logout
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import re
from collections import Counter


def home(request):
    return render(request, "home.html")
