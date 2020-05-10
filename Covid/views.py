from django.shortcuts import render, redirect
import ast
from django.http import JsonResponse, HttpResponse
from Covid.settings import BASE_DIR
from geopy.geocoders import Nominatim
from random import randrange, shuffle, choices
import datetime
import json

noncont = ["Shimoga", "Ramanagara", "Kolar", "Koppal", "Gulbarga", "Raichuru",
        "Yadagiri", "Chamarajanagara", "Chikmagalur", "Hassan", "Kodagu", "Udupi"]

move = []
current = []
key = []
value = []
creation = True


def create():
    global creation
    creation = False
    with open(BASE_DIR+'/data/mapping.json') as file:
        f = json.loads(file.read())
        for k, v in f.items():
            key.append(k)
            value.append(v)
    shuffle(key)
    [current.append(key[i]) for i in range(3)]
    shuffle(noncont)
    [move.append(noncont[i]) for i in range(3)]


def random_date(start, l):
    cur = start
    while l >= 0:
        curr = cur + datetime.timedelta(hours=randrange(24))
        yield curr
        l-=1


def home(request):
    if creation:
        create()
    geolocator = Nominatim(user_agent="tyl")

    locations = [geolocator.geocode(a) for a in current]
    next_location = [geolocator.geocode(a) for a in move]

    clatitudes = [i.latitude for i in locations]
    clongitudes = [i.longitude for i in locations]

    nlatitudes = [i.latitude for i in next_location]
    nlongitudes = [i.longitude for i in next_location]

    areas = zip(clatitudes, clongitudes)
    narea = zip(nlatitudes, nlongitudes)

    nloc = zip(clatitudes, clongitudes, nlatitudes, nlongitudes)

    startDate = datetime.datetime.now()

    movt = []
    for x in random_date(startDate, len(next_location)-1):
        movt.append(x.strftime("%d/%m/%y %H:%M"))

    if not len(locations) == len(next_location):
        for i in range(len(next_location)-1, 3):
            next_location.append("None")
            movt.append("None")

    locs = zip(locations, next_location, movt)

    data = zip(key, value)
    van_data = zip(choices(noncont, k=randrange(len(noncont))),
                   choices(noncont, k=randrange(len(noncont))),
                   choices(noncont, k=randrange(len(noncont))))

    return render(request, "base.html", {'areas': areas,
                                         'locs': locs,
                                         'narea': narea,
                                         'nloc': nloc,
                                         'data': data,
                                         'van_data': van_data})


def india(request):
    return render(request, "india.html")


def karnataka(request):
    return render(request, "karnataka.html")


def positive(request):
    try:
        with open(BASE_DIR+"/data/positive.json") as f:
            return JsonResponse(ast.literal_eval(f.read()), safe=False)
    except FileNotFoundError:
        return HttpResponse(status=204)


def negative(request):
    try:
        with open(BASE_DIR+"/data/negative.json") as f:
            return JsonResponse(ast.literal_eval(f.read()), safe=False)
    except FileNotFoundError:
        return HttpResponse(status=204)


def isolation(request):
    try:
        with open(BASE_DIR+"/data/isolation.json") as f:
            return JsonResponse(ast.literal_eval(f.read()), safe=False)
    except FileNotFoundError:
        return HttpResponse(status=204)


def wards(request):
    try:
        with open(BASE_DIR+"/data/table.json") as f:
            return JsonResponse(ast.literal_eval(f.read()), safe=False)
    except FileNotFoundError:
        return HttpResponse(status=204)


def deaths(request):
    try:
        with open(BASE_DIR+"/data/death.json") as f:
            return JsonResponse(ast.literal_eval(f.read()), safe=False)
    except FileNotFoundError:
        return HttpResponse(status=204)


def discharged(request):
    try:
        with open(BASE_DIR+"/data/discharge.json") as f:
            return JsonResponse(ast.literal_eval(f.read()), safe=False)
    except FileNotFoundError:
        return HttpResponse(status=204)


def district(request):
    try:
        with open(BASE_DIR+"/data/mapping.json") as f:
            return JsonResponse(ast.literal_eval(f.read()), safe=False)
    except FileNotFoundError:
        return HttpResponse(status=204)
