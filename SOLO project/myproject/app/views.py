from .models import Student, Mark
from django.shortcuts import render, redirect
from app.models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, 'index.html')


def registration(request):
    error = Teacher.objects.login_validator(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        ps_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        Teacher.objects.create(
            teacher_name=request.POST['teacher_name'], email=request.POST['email'], password=ps_hash
        )
        messages.success(request, "teacher has been created Successfully!")
        return redirect('/')


def login(request):
    teacher = Teacher.objects.filter(email=request.POST['email'])
    if teacher:
        logged_teacher = teacher[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_teacher.password.encode()):
            request.session['teacher_id'] = logged_teacher.id
            messages.success(request, " logged in")
            return redirect('/home')
        else:
            messages.error(request, "email / password incorrect")
            return redirect('/')
    else:
        messages.error(request, "email / password incorrect")
        return redirect('/')


def successRedirect(request):
    list(messages.get_messages(request))
    return redirect('/home')


def success(request):
    teacher = Teacher.objects.get(id=request.session['teacher_id'])
    section = Section.objects.all()
    context = {
        'teacher_object': teacher,
        'section_object': section,
        'teacher_session': request.session['teacher_id'],
    }
    return render(request, 'home.html', context)


def logout(request):
    list(messages.get_messages(request))
    request.session.flush()
    return redirect('/')


def newSection(request):
    return render(request, 'new_section.html')


def newSectionRedirect(request):
    list(messages.get_messages(request))
    return redirect('/sections/new')


def sectionCreate(request):
    error = Section.objects.section_validator(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect('/sections/new')
    else:
        teacher = Teacher.objects.get(id=request.session['teacher_id'])
        Section.objects.create(
            section_name=request.POST['section_name'], skill_level=request.POST['skill_level'], game_day=request.POST['game_day'].capitalize(), student=student
        )
        return redirect('/successRedirect')


def sectionDetails(request, id):
    teacher = Teacher.objects.get(id=request.session['teacher_id'])
    section = Section.objects.get(id=id)
    student_obj = section.students.all()
    print(student_obj)
    context = {
        'current_teacher': teacher,
        'section_object': section,
        'student_object': student_obj,
        'teacher_session': request.session['teacher_id'],

    }
    return render(request, 'section_details.html', context)


def editSection(request, section_id):
    error = Section.objects.section_validator(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect('/sections/' + str(section_id) + '/edit')

    section = Section.objects.get(id=section_id)
    section.section_name = request.POST['section_name']
    section.skill_level = request.POST['skill_level']
    section.game_day = request.POST['game_day']
    section.save()

    return redirect('/successRedirect')


def deletesection(request, section_id):
    section = Section.objects.get(id=section_id)
    section.delete()
    return redirect('/successRedirect')


def sectionEdit(request, section_id):
    student = student.objects.get(id=request.session['student_id'])
    section = Section.objects.get(id=section_id)

    context = {
        'current_student': student,
        'section_object': section,
        'student_session': request.session['student_id']

    }
    return render(request, 'sectionEdit.html', context)


def addStudent(request, section_id):
    error = Student.objects.validate_student(request.POST, section_id)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect('/sections/' + str(section_id))
    section = Section.objects.get(id=section_id)
    Student.objects.create(
        student_name=request.POST['student_name'], section=section)
    return redirect('/sections/' + str(section_id))


def MarksView(request, student_id):
    student = Student.objects.POST(id=request.session['student'])
    section = Section.objects.POST(id=id)
    student_obj = section.students.all()
    print(student_obj)
    context = {
        'current_student': student,
        'section_object': section,
        'student_object': student_obj,
        'student_session': request.session['student'],
    }
    return render(request, 'marks.html', context)
