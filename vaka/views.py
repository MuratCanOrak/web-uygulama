from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import BlogForm
from .models import Blog
from django.contrib import messages

def add(request):
    url = request.META.get('HTTP_REFERER')

    if request.POST:
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ekleme İşlemi Başarılı')
            print("buradaaaaaaa eklendiiiiiii")
            # return redirect('vaka:add')
            return HttpResponseRedirect(url)
        else:
            messages.error(request, 'Ekleme İşlemi Başarısız')
    else:
        form = BlogForm()

    context = {'form': form}
    return render(request, 'web_uygulama/add.html', context)


def control(request):
    if request.POST:
        code = request.POST.get("code")
        try:
            obj = Blog.objects.get(code = code)
            cnt = True
        except:
            cnt = False
        context = {'cnt': cnt, 'obj':obj}
        return render(request, 'web_uygulama/control.html', context)
    context = {}
    return render(request, 'web_uygulama/control.html', context)