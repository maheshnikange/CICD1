from django.shortcuts import render
from .forms import AdditionForm

def add_numbers(request):
    result = None
    if request.method == 'POST':
        form = AdditionForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            result = num1 + num2
    else:
        form = AdditionForm()

    return render(request, 'index.html', {'form': form, 'result': result})
