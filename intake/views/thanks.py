from django.shortcuts import render

def thanks(request):
    return render(request, 'thanks.html')