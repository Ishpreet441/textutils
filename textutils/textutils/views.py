# I have created this file - ISHPREET SINGH
from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = string.punctuation
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalize (UPPER CASE)', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremove == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char

        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (spaceremover == "on"):

        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzed = analyzed + char
            else:
                pass
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == 'on':
        analyzed = analyzed + '\n' + (f'The characters in the text entered is:->  {len(djtext)}')
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        djtext = analyzed

    if (
            removepunc != 'on' and fullcaps != 'on' and newlineremove != 'on' and spaceremover != 'on' and charcount != 'on'):
        return HttpResponse("Error! Please select an option to proceed")
    return render(request, 'analyze.html', params)
