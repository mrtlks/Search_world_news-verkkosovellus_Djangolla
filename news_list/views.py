#Views=Näkymät 
#--> Näkymä termin käyttö voi johtaa harhaan, jos asiaa ajattelee MVC:n kautta. Djangossa näkymä on käytännössä controller.
#Näkymässä päätetään, miten dataa näytetään templaateissa.
#https://stackoverflow.com/questions/5249792/why-does-django-call-it-views-py-instead-of-controller


from django.shortcuts import render
# django.shortcuts -paketti kerää auttajafunktioita ja luokkia jotka kattavat monta MVC:n tasoa (tai MVT)
#https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/



import requests #pip install request

API_KEY = '5b56a9b01f8141eaaa5a72dbc2244a1b'



def frontpage(request):
    
    category = request.GET.get('category')
    language = request.GET.get('language')
    

    if language:
        url = f'https://newsapi.org/v2/top-headlines?language={language}&apiKey={API_KEY}'
        response = requests.get(url) #get hakee tiedon urlista --> response -muuttuja sisältää tämän tiedon
        data = response.json() #tieto muutetaan json muotoon --> data -muuttuja sisältää nyt response-muuttujan tiedon muutettuna json-muotoon
        articles = data['articles']
    
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'articles' : articles
    }

    return render(request, 'news_list/frontpage.html', context)#hakee templaatin frontpage.html news_list -kansiosta

#uutta sivua varten, joka näyttää valitun artikkelin sekä keskustelualueen
def newspage(request):
    return render(request, 'news_list/newspage.html')#hakee templaatin newspage.html news_list -kansiosta