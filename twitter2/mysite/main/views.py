from operator import mod

from django.shortcuts import redirect, render
from django.http import JsonResponse

# Create your views here.


from django.shortcuts import render
from django.urls import is_valid_path
import tweepy
from . import config
from . import recommendation
from .models import mode, username
# Create your views here.

spacee = []
def create(response):
    if response.POST.get('add'):
        print('added')
    
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN, 
    consumer_key=config.API_KEY,
    consumer_secret=config.API_SECRET,
    access_token=config.ACCESS_TOKEN,
    access_token_secret=config.ACCESS_TOKEN_SECRET)
    q = 'NFTs'
    space = spacee
  

    
    modes = mode.objects.all()
    users = username.objects.all()
    
    if response.POST.get('save'):
        
        t = response.POST.get('create')
        if t == '' or t == ' ' or t=='  ':
            return render(response, 'lists.html' , {'mods':modes, 'users':users, 'spaces':space})

        if mode.objects.filter(name=t).exists():
            
            mo = mode.objects.get(name=t)
            u = response.POST.get('usernames')
            if username.objects.filter(username=u).exists():
                return render(response, 'lists.html' , {'mods':modes, 'users':users, 'spaces':space})
            username.objects.create(username=u, mode=mo)
            mo.save()

            return render(response, 'lists.html' , {'mods':modes, 'users':users, 'spaces':space})
    

        else:
            
            mo = mode.objects.create(name=t)
            mo.save()
            u = response.POST.get('usernames')
            username.objects.create(username=u, mode=mo)

            return render(response, 'lists.html' , {'mods':modes, 'users':users, 'spaces':space, })
    if response.POST.get('search_space'):
        space.clear()
        txt = response.POST.get('new1')
        q = txt
        responses = client.search_spaces(query=q, max_results=10)
        for i in responses.data:
            id = i.id
            spaces = client.get_space(id=id, expansions='host_ids')
            for i in spaces.includes['users']:
                space.append(i['username'])
        

        return render(response, 'lists.html' , {'mods':modes, 'users':users, 'spaces':space, "q":q})


        
    
    else:
        
        
        return render(response, 'lists.html' , {'mods':modes, 'users':users, 'spaces':space, })



def delete(response, id):
    try:
        u = username.objects.get(id=id)
        u.delete()
    except:
        return redirect('create')


    return redirect('create')


def delete_mode(response, id):
    
    try:
        m = mode.objects.get(id=id)
        m.delete()
    except:
        return redirect('create')
    return redirect('create')

listname= ''
data = []
def add(request):
    print('rerun')
    try:
        if request.is_ajax():
            
            if request.GET.get('action') == 'id':
                print('rec1')
                id = int(request.GET.get('id'))
                print(id)
                data.append(id)
        if request.is_ajax():
            if request.GET.get('action') == 'name':
                print('rec')
                listname = str(request.GET.get('listname'))
                data.append(listname)
                
                mo = mode.objects.get(name=data[1])

                username.objects.create(username=spacee[data[0]], mode=mo)
                print('saved')
                mo.save()
                data.clear()
                return redirect('create')  
   
    
    except:
        print(spacee)
        print('crap')
        print(data)
        data.clear()

    return redirect('create')
        
            
    
  


    


