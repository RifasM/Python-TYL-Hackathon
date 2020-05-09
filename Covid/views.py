from django.shortcuts import render, redirect
import ast, json
from django.http import JsonResponse, HttpResponse
from Covid.settings import BASE_DIR


def home(request):
    return render(request, "home.html")


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
