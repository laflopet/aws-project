from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, 'index.html')

def segunda_pagina(request):
    return render(request, 'segunda.html')