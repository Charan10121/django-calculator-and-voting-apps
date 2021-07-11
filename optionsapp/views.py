from django import http
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

arr = ['HTML', 'CSS',
       'Python', 'Pearl', 'PHP',
       'Java',
       'JavaScript',
       'Swift',
       'C++',
       'C',
       'R',
       'Golang (Go)']

countdict={

}

def index(request):

    mydict = {
        'arr': arr
    }
    return render(request, 'index.html', context=mydict)


def submitquery(request):
    # from this line <input type="search" class="form-control" name="query" id = 'query'>
    q = request.GET['languages']
    if q in countdict:
        countdict[q]=countdict[q]+1
    else:
        countdict[q]=1
    mydict={
        'arr':arr,
        'countdict':countdict
    }
    return render(request, 'index.html', context=mydict)

def sortdata(request):
    global countdict
    countdict = dict(sorted(countdict.items(),key = lambda val:val[1],reverse=True))
    mydict = {
        'arr': arr,
        'countdict':countdict
    }
    return render(request, 'index.html', context=mydict)