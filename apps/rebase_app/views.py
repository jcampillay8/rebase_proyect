from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    
    # context = {
    #     'user': User.objects.get(id=request.session['id']),
    #     'wishes': User.objects.get(id=request.session['id']).wishes.all(),
    #     'granted_wishes': Granted_wish.objects.all()
    # }
    return render(request, 'rebase/home.html')

def logout(request):
    if request.method == 'POST':
        request.session.clear()
        return redirect('/')
    else:
        return redirect('/')