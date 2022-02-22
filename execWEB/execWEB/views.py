from django.shortcuts import HttpResponse,render

def greeting(request):
    return HttpResponse('섭이와 함께하는 즐거운 WEB');

def index(request):
    print('web index~')
    return render(request,'index.html')
