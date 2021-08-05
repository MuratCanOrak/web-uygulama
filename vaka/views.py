from django.contrib.messages.api import error
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

def add(request):
    if request.POST:
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form_obj = form.save()
            messages.success(request, 'Ekleme İşlemi Başarılı')

            context = {'form': form,'form_obj': form_obj}
            return render(request, 'web_uygulama/index.html', context)
        else:
            messages.error(request, 'Ekleme İşlemi Başarısız')
    else:
        form = BlogForm()
    context = {'form': form}
    return render(request, 'web_uygulama/index.html', context)


def control(request):
    if request.POST:
        code = request.POST.get("code")
        cnt = False
        context = {}
        error_msg =""
        try:
            obj = Blog.objects.get(code = code)
            serialized_obj = {
                "title" : obj.title,
                "description": obj.description,
                "link": obj.link,
                "email": obj.email,
                "image": obj.image.url,
            }
            language_obj = {
                "title" : _('title'),
                "description": _('description'),
                "link": _('link'),
                "email": _('email'),
                "image": _('image'),
            }
            context["obj"] = serialized_obj 
            context["labels"] = language_obj
            cnt = True
        except:
            cnt = False
            error_msg = _('error_msg')
        context["cnt"] = cnt
        context["error_msg"] = error_msg
        return JsonResponse(context)
    else:
        return redirect('vaka:add')

