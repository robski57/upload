from django.shortcuts import render
from django.http import HttpResponse


def Form(request):
    return render(request, "index/form.html", {})

def Upload(request):
    print("file uploading")
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            with open('/Users/RobskiRig/Documents/mydjango/upload/media/file_' + str(count), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
    return HttpResponse("File(s) uploaded!")



# Create your views here.
