from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def submit_query(request):
    # from this line <input type="search" class="form-control" name="query" id = 'query'>
    q = request.GET['query']
    try:
        ans = eval(q) #eval is inbuilt func that takes string input #initially q will be blank, so the except block will be executed
        mydict ={
            'q':q,
            'ans':ans,
            'error':False,
            'result':True
        }
        return render(request,'index.html',context=mydict)
    except:
        mydict ={   #result = false, then the success alert won't be shown
            'error':True,
            'result':False
        }
        return render(request,'index.html',context=mydict)