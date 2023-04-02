from django.http import HttpResponse
from django.shortcuts import render

import datetime

def home(request):

    IsActive= True
    if request.method=='POST':
        check=request.POST.get('check')
        print(check)
        if check is None: IsActive=False
        else: IsActive=True
    #request.GET['check']

    date=datetime.datetime.now()
    
    name="Anime"
    list_of_anime=[
        'One piece','MHA','Death note'
    ]
    member={
        'member1':"Lalit",
        'college':"Cu",
        'city':"MAthura"
    }

    data={
        'Date':date,
        'isactive':IsActive,
        'Name':name,
        'Anime':list_of_anime,
        'Members':member
    }
    #print("This is test page.")
    # return HttpResponse( "<h1>Hello this is index page.</h1>"+str(date))
    return render(request, "home.html",data)
# orreturn render(request, "home.html",{isactive:IsActive,Name:name,Anime:list_of_anime,Members:member})

def about(request):
    #return HttpResponse("<h1>this is about page.</h1>")
    return render(request, "about.html",{})
    
def services(request):
    #return HttpResponse("<h1>this is services page.</h1>")
    return render(request, "services.html",{})