from django.shortcuts import render, redirect
from apps.login_register.models import User
from apps.rebase_app.models import Text
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Home
def home(request):
    
    # context = {
    #     'user': User.objects.get(id=request.session['id']),
    #     'wishes': User.objects.get(id=request.session['id']).wishes.all(),
    #     'granted_wishes': Granted_wish.objects.all()
    # }
    return render(request, 'rebase/home.html')

def users(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
        'textos': Text.objects.all(),
    }
    return render(request, "rebase/users.html", context)

def logout(request):
    if request.method == 'POST':
        request.session.clear()
        return redirect('/')
    else:
        return redirect('/')


def add_text(request):
    return render(request, 'rebase/add_text.html')

def add_text2(request):
    print('add message initiated')
    if request.method == 'POST':
        thisUser = User.objects.get(id=request.session['id'])
        print(request.session['id'])
        recoger_texto = request.POST['add_text']
        
        recoger_texto1=recoger_texto.replace(' “ ',' " ')
        recoger_texto2=recoger_texto1.replace('”','"')
        recoger_texto3=recoger_texto2.replace("’","'")
        recoger_texto4=recoger_texto3.replace("•","*")
        recoger_texto5=recoger_texto4.replace("—","--")
        recoger_texto6=recoger_texto5.replace(":",".")
        
        lst=list(recoger_texto6)
        
        str=''
        for i in lst:
                str+=i
                
        lst1=str.split("\n")
        str2 = '\t'.join([line.strip() for line in lst1])
        print(str2)  
        newText = Text.objects.create(
            content = str2,
            text_name = request.POST['text_name'],
            user = thisUser,
        )
        newText.save()
    
    
    return redirect('/rebase/success2')

def delete(request, textId):
    Text.objects.get(id=textId).delete()

    return redirect('/rebase/users')

def success2(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
    }
    return render(request, "rebase/success2.html", context)



def read(request):
    text_list = Text.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(text_list,3)
    try:
        textos = paginator.page(page)
    except PageNotAnInteger:
        textos = paginator.page(1)
    except EmptyPage:
        textos = paginator.page(paginator.num_pages)

    context = {
        'user': User.objects.get(id=request.session['id']),
        'textos': textos
    }
    return render(request, 'rebase/read.html', context)

def word(request):
    return render(request, 'rebase/word.html')

def phrase(request):
    return render(request, 'rebase/phrase.html')

def contact(request):
    return render(request, 'rebase/contact.html')