from django.shortcuts import render

# Create your views here.
def index(request):
    print(">>>>>>>> user index")
    return render(request,'user/index.html')

def login(request):
    print(">>>>>>>> user login")
    if request.method == 'POST':
        print('>>>> request post')
        id = request.POST['id']
        pwd = request.POST['pwd']
        # model - DB(Select)
        context = {'key':'value'}
        print('>>>> request param - ',id,pwd)
    else :
        print('>>>> request get')
        # request.GET['id']