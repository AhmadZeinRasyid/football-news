from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406408395',
        'name': 'Ahmad Zein Rasyid Siregar',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)