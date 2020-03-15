from django.shortcuts import render

# Create your views here.
def blog(request):
    datas = {

    }
    return render(request,"pages/blog.html",datas)

def gallery(request):
    datas = {

    }
    return render(request,"pages/gallery.html",datas)
    
