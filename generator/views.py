from xml.dom.pulldom import parseString
from django.shortcuts import render
from django.http import HttpResponse
from random import choice

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')



def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    upperCharacter = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    specialCharacter = list('!#$%&/()=?¡¿[]´´*|')
    numberCharacters = list('1234567890')

    generatedPassword = ''

    length = int(request.GET.get('length'))

    if(request.GET.get('uppercase') == 'on'):
        characters.extend(upperCharacter)
    
    if(request.GET.get('special') == 'on'):
        characters.extend(specialCharacter)
    
    if(request.GET.get('numbers') == 'on'):
        characters.extend(numberCharacters)

    for i in range(length):
        generatedPassword += choice(characters)
    
    return render(request, 'password.html', {"password": generatedPassword})
