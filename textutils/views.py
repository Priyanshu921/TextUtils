        #I have Created this file-Attyus
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    
    return render(request,'index2.html')
    """" return HttpResponse("Home<h1><a href='/removepunc'> RemovePunc</a></h1> <h1><a href='/capitalizedfirst'>capitalizedfirst</a></h1> <h1><a href='/newlineremove'>newlineremove</a></h1><h1><a href='/spaceremove'> spaceremove</a></h1><h1><a href='/charcount'> charcount</a></h1>")
    f1=open("First.txt","r")
    return HttpResponse("<p>%s</p>"%(f1.read()))
    return HttpResponse("")"""
def analyze(request):
    ptext=request.POST.get('text','off')
    rm=request.POST.get('rmvpnc','off')
    rm1=request.POST.get('rmvspc','off')
    rm2=request.POST.get('cap','off')
    rm3=request.POST.get('nlr','off')
    if(rm=='on'):
        analyzed=" "
        punctuations='''.,?!'":;...-–—()[]'''
        for char in ptext:
            if char not in punctuations:
                analyzed=analyzed+char
        dict={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        ptext=analyzed
    if(rm1=='on'):
        analyzed=" "
        for index,char in enumerate(ptext):
            if not(ptext[index]==" " and ptext[index+1]==" "):
                analyzed=analyzed + char
        dict={'purpose':'Remove Extra space','analyzed_text':analyzed}
        ptext=analyzed
    if(rm2=='on'):
        analyzed=" "
        for char in ptext:
            analyzed=analyzed + char.upper()
        dict={'purpose':'UpperCase','analyzed_text':analyzed}
        ptext=analyzed
    if(rm3 =='on'):
        analyzed =" "
        for char in ptext:
            if char !="\n" and char !="\r":
                analyzed=analyzed + char
        print(analyzed)
        dict={'purpose':'Remove Extra space','analyzed_text':analyzed}
    count=0
    for char in ptext:
        if char != " ":
            count=count+1
    dict={'purpose':'Character Counter','analyzed_text':analyzed,'count':count}
    if (rm!='on' and rm1!='on' and rm2!='on' and rm3!='on'):
        return HttpResponse("Please select any ")

    return render(request,'analyze2.html',dict)
    
