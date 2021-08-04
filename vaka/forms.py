from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    title       = forms.CharField(label = 'Başlık', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Başlık'}))
    description = forms.CharField(label = 'Açıklama', max_length=100, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Açıklama'}))
    link    = forms.URLField(label = 'Link', initial='http://')
    email   = forms.EmailField(label = 'Email', help_text='Lütfen email adresi girin.', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lütfen email adresi girin.', 'type':'email'}))
    image   =  forms.ImageField(label="Resim")

    def __init__(self, *args, **kwargs):
	    super(BlogForm,self).__init__(*args, **kwargs)
	    self.fields['title'].widget.attrs={'rows':10}

    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'description', 'link', 'email', 'image']