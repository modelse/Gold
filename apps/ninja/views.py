from django.shortcuts import render, redirect

def index(request):
    return render(request, 'ninja/index.html')
def ninjas(request):
    return render(request, 'ninja/ninjas.html')
def color(request, color):
        context = {
        'color': color,
        }
        return render(request, 'ninja/show.html', context)
