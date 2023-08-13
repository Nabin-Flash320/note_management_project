from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Note
import json

# Each views in the app's view.py file are mapped to a specific url route and are recognized using name parameter
# Create your views here.
# this function is called when the app is called, it lists all the available notes in the database.
def notes_listing(request):
    notes_data = list(Note.objects.all().values())
    return render(request=request, template_name='list.html', context={'notes_data':notes_data})

# add note makes a post request with exempted CSRF token.
# after data is added to database, it redirects to notes_listing URL
@csrf_exempt
def notes_adding(request):
    if request.method == "POST":
        data = request.POST
        print(data['title'])
        print(data['content'])
        id = max(list(Note.objects.values_list('id', flat=True)), default=0) + 1
        print(id)
        note = Note(id=id, title=data['title'], content=data['content'])
        note.save()
        return redirect('notes_listing')
    return render(request=request, template_name='add.html')

# Deleting notes also makes POST request with exempted CSRF
# Once deleted from databse, val:deleted JSON response is sent back to the UI.
@csrf_exempt
def notes_deleting(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        print(data['id'])
        note = Note.objects.get(id=data['id'])
        note.delete()
        return JsonResponse({'val':'deleted'})


