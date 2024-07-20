# I have created this file
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'default')
    fullcaps = request.POST.get('fullcaps', 'default')
    newlineremover = request.POST.get('newlineremover', 'default')
    extraspaceremover = request.POST.get('extraspaceremover', 'default')
    charactercounter = request.POST.get('charactercounter', 'default')

    if removepunc == "on":
        punctuations = '''.,?!:;"'*&$(){}[]<>/\@&_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'remove punc', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        djtext = analyzed
    return render(request, 'analyze.html', params)


def navigation(request):
    s = '''<h1>NAVIGATION</h1>
    <a href='https://www.instagram.com'>Instagram</a><br>
    <a href='https://internshala.com'>Intershala</a><br>
    <a href='https://in.linkedin.com'>Linkdin</a><br>
    <a href='https://www.youtube.com'>You Tube</a>
'''
    return HttpResponse(s)
