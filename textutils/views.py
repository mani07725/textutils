# we have created this file
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1> personal navigator using django</h1>
#     <h1><a href="http://google.com" target="_blank"> google</a></h1>
#     <h1><a href="http://facebook.com" target="_blank"> facebook</a></h1>
#     <h1><a href="http://twitter.com" target="_blank"> twitter</a></h1>
#     ''')


# def about(request):
#     return HttpResponse("this is about page")

# def text(request):
#     file = open("textutils/new.txt", "r+")
#     return HttpResponse(file.read())
# this code is for laying papeline
# def index(request):
#     return HttpResponse('''<h1> personal navigator using django
# <button><a href="/removepunc" target="_blank"> remove punc</a></button>
# <button><a href="/capfirst" target="_blank"> cap first</a></button>
# <button><a href="/newlineremove" target="_blank"> new line remove</a></button>
# <button><a href="/spaceremove" target="_blank"> space remove</a></button>
# <button><a href="/charcounter" target="_blank">charcounter</a></button>
#     ''')
# here we have used the template and used the index.html as our template file
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def analyze(request):
    # here we are extracting the resquested text using the textbox id and saving using the get method and saving it in a variable djtext
    djtext = request.POST.get('textarea','default')
    remove = request.POST.get('removepunc','off')
    cap = request.POST.get('fullcap','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    character_counter = request.POST.get('character_counter','off')
    # analyzed= djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed=""
    # this for loops simply takes the all the characters from djtext and checks it those characters are not equal to the characters in punctuations and if soo makes that character equal to analyzed and in the end analyzed is printed
    while True:
        if (remove=="on"):
            for char in djtext:
                if char not in punctuations:
                    analyzed += char
            djtext=analyzed
            params = {'purpose': 'remove punc', 'analyzed_text': analyzed}
            # return render(request,'analyze.html',params)
        if(cap=="on"):
            analyzed =""
            for char in djtext:
                analyzed += char.upper()
            djtext=analyzed
            params = {'purpose': 'capitizied', 'analyzed_text': analyzed}
            # return render(request,'analyze.html',params)
        if(newlineremover=="on"):
            analyzed =""
            for char in djtext:
                if(char!="\n") and (char!="\r"):
                    analyzed += char
            djtext=analyzed
            params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
            # return render(request,'analyze.html',params)
        if(extraspaceremover=="on"):
            analyzed =""
            # this enumerate function is used to count the characters in a string each is assigned with a specific index
            for index,char in enumerate(djtext):
                if  not(djtext[index]==" " and djtext[index+1]==" "):
                    analyzed += char
            djtext=analyzed
            params = {'purpose': 'removed extra spaces', 'analyzed_text': analyzed}
            # return render(request,'analyze.html',params)
        return render(request,'analyze.html',params)

# def capfirst(request):
#     return HttpResponse("capitilize first")

# def newlineremove(request):
#     return HttpResponse("new line remove")

# def spaceremove(request):
#     return HttpResponse("removing all spaces")

# def charcounter(request):
#     return HttpResponse("count all characters")