from django.shortcuts import render

# Create your views here.
def home(request):
    home = Home.objects.first()
    alternate_home = AlternateHome.objects.filter(home=home)
    return render(request, 'index.html')