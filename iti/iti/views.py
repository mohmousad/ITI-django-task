from django.shortcuts import render, redirect


def project_index(request):
    return render(request, 'main/index.html')
