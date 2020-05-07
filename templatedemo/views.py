from django.shortcuts import render

def index(request):
    variable1 = 'aaaaa'
    variable2 = 'bbbbb'
    variable3 = 'ccccc'
    return render(
        request, 'index.html', {'var1': variable1, 'var2': variable2, 'var3': variable3}
    )