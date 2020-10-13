from django.shortcuts import render
import qrcode
from .models import Website
from django import forms
# Create your views here.
class QRForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ('name',)


def home_view(request):
    if request.method == 'POST':
        form = QRForm(request.POST)
        if form.is_valid():
            x = form.save()
            img = x.qr_code
            print(img)
    else:
        form = QRForm()
    obj = Website.objects.get(id=2)

    context = {
        'img':img,
        'form':form,
        'obj': obj
    }
    return render(request, 'home.html', context)