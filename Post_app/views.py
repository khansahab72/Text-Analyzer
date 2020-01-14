from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtxt = (request.POST.get('text','default'))
    # check checkbox values
    removepunc=(request.POST.get('removepunc','Off' ))
    fullcaps=(request.POST.get('fullcaps','Off' ))
    newlineremover=(request.POST.get('newlineremover','Off' ))
    extraspaceremover=(request.POST.get('extraspaceremover','Off' ))

    if removepunc=='on':
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = " "
        punc_marks = " "
        for char in djtxt:
            if char not in punctuation:
                analyzed = analyzed + char
            elif char in punctuation:
                punc_marks = punc_marks + char

        params = {'purpose':"removed punc is\n"+ punc_marks, 'analyze_text': analyzed}
        djtxt=analyzed
        # return render(request, 'analyze.html', params)
    if(fullcaps=='on'):
        analyzed=""
        for char in djtxt:
            analyzed=analyzed + char.upper()
        params = {'purpose':"changed to Uppercase", 'analyze_text': analyzed}
        djtxt=analyzed
        #return render(request, 'analyze.html', params)
    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtxt:
            if (char !="\n" and char !="\r"):
                analyzed = analyzed + char
        params = {'purpose': "new line removed", 'analyze_text': analyzed}
        djtxt=analyzed
        # return render(request, 'analyze.html', params)

    if(extraspaceremover == 'on'):
         analyzed = ""
         for index,char in enumerate(djtxt):
                if not(djtxt[index] ==" " and djtxt[index+1]==" "):
                    analyzed = analyzed + char

         params = {'purpose': "Extra Space removed", 'analyze_text':analyzed}
         djtxt=analyzed
        #  return render(request, 'analyze.html', params)

    if (removepunc !="on" and extraspaceremover !="on" and newlineremover!="on" and fullcaps!='on'):
        return HttpResponse("Please select any option and try again ")

    return render(request,"analyze.html",params)




