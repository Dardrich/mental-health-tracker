from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306206856',
        'name': 'Darren Aldrich',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)