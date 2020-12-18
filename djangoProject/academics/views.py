from django.contrib.auth.decorators import login_required
from academics.models import Class, Note,Subject
from users.models import StudentProfile, Teach, TeacherProfile
from django.shortcuts import render
from academics.forms import AddNotesForm
from django.contrib import messages


@login_required
def view_list(request):
    if request.user.role == 'STD':
        student_profile = StudentProfile.objects.filter(user=request.user).first()
        class_obj = student_profile.section
        subjects = Teach.objects.filter(Class=class_obj)
        for subject in subjects:
            print(subject.subject.subject_name)
        return render(request, 'academics/notes-list.html', {'subjects': subjects})
    elif request.user.role == 'THR' or request.user.role == 'ADM':
        teacherProfile = TeacherProfile.objects.get(user=request.user)
        teaches = Teach.objects.filter(teacher=teacherProfile)
        return render(request, 'academics/notes-list.html', {'teaches': teaches})


@login_required
def view_notes(request, subjectId):
    notes = Note.objects.filter(subject=subjectId)
    if request.user.role == 'ADM' or request.user.role == 'THR':
        if request.method == 'GET':
            form = AddNotesForm()
            return render(request, 'academics/notes-detail.html', {'notes': notes, 'form': form})
        elif request.method == 'POST':
            form = AddNotesForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                subject = Subject.objects.get(id=subjectId)
                note.subject = subject
                teacherProfile = TeacherProfile(user=request.user)
                note.department = teacherProfile.department
                form.save()
                messages.success(request,
                                 message="Notes added successfully")
            return render(request, 'academics/notes-detail.html', {'notes': notes, 'form': form}, )
    elif request.user.role == 'STD':
        notes = Note.objects.filter(subject=subjectId)
        return render(request, 'academics/notes-detail.html', {'notes': notes})
