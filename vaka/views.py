from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
from django.contrib import messages

def add(request):
    url = request.META.get('HTTP_REFERER')

    if request.POST:
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ekleme İşlemi Başarılı')
            return redirect('category:add-list-category')
        else:
            messages.error(request, 'Ekleme İşlemi Başarısız')
    else:
        form = BlogForm()

    context = {'form': form}
    return render(request, 'web_uygulama/add.html', context)


def control(request, code):
    cnt = True
    try:
        obj = Blog.objects.get(code = code)
    except:
        cnt = False
        
    context = {'cnt': cnt}
    return render(request, 'web_uygulama/control.html', context)