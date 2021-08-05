from django import forms
from .models import Blog
from django.utils.translation import gettext_lazy as _

class BlogForm(forms.ModelForm):
    title       = forms.CharField(label= _('title'), max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('title')}))
    description = forms.CharField(label = _('description'), max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('description')}))
    link    = forms.URLField(label = _('link'), initial='http://', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('title')}))
    email   = forms.EmailField(label =_('email'), help_text=_('Please enter email address'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Please enter email address'), 'type':'email'}))
    image   =  forms.ImageField(label=_('image'), widget=forms.ClearableFileInput(attrs={'multiple':'multiple', 'class':'file-input', 'data-fouc':True}))

    def __init__(self, *args, **kwargs):
	    super(BlogForm,self).__init__(*args, **kwargs)
	    self.fields['title'].widget.attrs={'rows':10}

    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'description', 'link', 'email', 'image']