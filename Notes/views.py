from django.shortcuts import render,redirect
from django.http import HttpResponse
from Notes.models import * 
# Create your views here.

def submit_notes(request):

    if request.method == "POST":
        data = request.POST
        
        name = data.get('student_name')
        id = data.get('student_id')
        sem = data.get('student_sem')
        subject = data.get('student_sub')
        desc = data.get('note_description')
        file = request.FILES.get('note_file')

        print(name)
        print(id)
        print(sem)
        print(subject)
        print(desc)
        print(file)

        Notes.objects.create(
            student_name = name,
            student_id = int(id),
            student_sem = int(sem),
            student_sub = subject,
            note_desc = desc,
            note_file = file, 
        )

        return redirect('/submit_notes/')




    return render(request,"Submit_notes.html")
