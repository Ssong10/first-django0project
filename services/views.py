from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'services/index.html')


def artii(request):
    return render(request, 'services/artii.html')

def artii_result(request):
    text = request.GET.get('text')
    font = request.GET.get('font')
    if font == 'base':
        response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    else:
        response = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
    result = response.text
    context = {
        "result" : result
    }
    return render(request, 'services/artii_result.html',context)

def push(request):
    return render(request, 'services/push.html')

def pull(request):
    number = request.GET.get('number')
    context = {
        'number' : number
    }
    return render(request,'services/pull.html',context)
