from django.shortcuts import render
from django.http import HttpResponse
from static import globals

def index(request):
    context = {'names': [], 'Count': 0}

    #Store sorted packages from globals.data
    for pkg in sorted(globals.data):
        context['names'].append(pkg)

    #Store the count of the packages
    context['Count'] = len(globals.data)
    return render(request, 'file_browser/index.html', context)

def browse(request, key):
    context = {}
    for pkg in globals.data:
        #Serve package data if found
        if key == pkg:
            #Store all of the interesting fields from globals.data
            context =  {       'Name': globals.data[pkg]['Name'],
                        'Description': globals.data[pkg]['Description'],
                            'Depends': sorted(globals.data[pkg]['Depends']),
                            'Reverse': sorted(globals.data[pkg]['Reverse'])
                        }
            return render(request, 'file_browser/search.html', context)
    #If package is not found return 404
    return HttpResponse("404 Not found")
