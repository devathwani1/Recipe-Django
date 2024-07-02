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

def view_notes(request):

    notes = Notes.objects.all();

    if request.GET.get('search'):
        notes = notes.filter(student_sub__icontains = request.GET.get('search'))

    return render(request,"view_notes.html",context={'notes' : notes})

def delete_note(request,id):
    note = Notes.objects.get(id = id);
    note.delete()
    return redirect('/view_notes/')

def update_note(request,id):
    note = Notes.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        print(data)

        note.student_name = data.get('student_name')
        note.student_id = data.get('student_id')
        note.student_sem = data.get('student_sem')
        note.student_sub = data.get('student_sub')
        note.note_desc = data.get('note_description')
        file = request.FILES.get('note_file')

        if file : 
            note.note_file = file

        note.save()
        return redirect('/view_notes/')


    context = {"Note" : note}
 
    return render(request,'update_notes.html',context=context)