from django.shortcuts import render, redirect
from apps.login_register.models import User
from apps.rebase_app.models import Text

# Create your views here.
def home(request):
    
    # context = {
    #     'user': User.objects.get(id=request.session['id']),
    #     'wishes': User.objects.get(id=request.session['id']).wishes.all(),
    #     'granted_wishes': Granted_wish.objects.all()
    # }
    return render(request, 'rebase/home.html')

def users(request):
    context = {
        'user': User.objects.get(id=request.session['id'])
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
        newText = Text.objects.create(
            content = request.POST['add_text'],
            text_name = request.POST['text_name'],
            user = thisUser,
        )
        newText.save()
    print('hello')
    
    
    return redirect('/rebase/success2')

def success2(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
    }
    return render(request, "rebase/success2.html", context)


def read(request):
    return render(request, 'rebase/read.html')

def word(request):
    return render(request, 'rebase/word.html')

def phrase(request):
    return render(request, 'rebase/phrase.html')

def contact(request):
    return render(request, 'rebase/contact.html')