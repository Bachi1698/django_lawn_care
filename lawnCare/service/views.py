from django.shortcuts import render

# Create your views here.
def service(request):
    datas = {

    }
    return render(request,'pages/service.html',datas)

def conseil(request):
    datas = {

    }
    return render(request,'pages/conseil.html',datas)