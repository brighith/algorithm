from django.shortcuts import render, redirect
from first_app.models import *
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
        messages.success(request, "Teacher has been created Successfully!")
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
    course = Course.objects.all()
    context = {
        'teacher_object': teacher,
        'course_object': course,
        'teacher_session': request.session['teacher_id'],
    }
    return render(request, 'home.html', context)


def logout(request):
    list(messages.get_messages(request))
    request.session.flush()
    return redirect('/')


def newCourse(request):
    return render(request, 'new_course.html')


def newCourseRedirect(request):
    list(messages.get_messages(request))
    return redirect('/courses/new')


def courseCreate(request):
    error = Course.objects.course_validator(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect('/courses/new')
    else:
        teacher = Teacher.objects.get(id=request.session['teacher_id'])
        Course.objects.create(
            course_name=request.POST['course_name'], teaching_level=request.POST['teaching_level'], lecture_day=request.POST['lecture_day'].capitalize(), teacher=teacher
        )
        return redirect('/successRedirect')


def courseDetails(request, id):
    teacher = Teacher.objects.get(id=request.session['teacher_id'])
    course = Course.objects.get(id=id)
    student_obj = course.students.all()
    print(student_obj)
    context = {
        'current_teacher': teacher,
        'course_object': course,
        'student_object': student_obj,
        'teacher_session': request.session['teacher_id'],

    }
    return render(request, 'course_details.html', context)


def editCourse(request, course_id):
    error = Course.objects.course_validator(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect('/courses/' + str(course_id) + '/edit')

    course = Course.objects.get(id=course_id)
    course.course_name = request.POST['course_name']
    course.teaching_level = request.POST['teaching_level']
    course.lecture_day = request.POST['lecture_day']
    course.save()

    return redirect('/successRedirect')


def deleteCourse(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('/successRedirect')


def courseEdit(request, course_id):
    teacher = Teacher.objects.get(id=request.session['teacher_id'])
    course = Course.objects.get(id=course_id)

    context = {
        'current_teacher': teacher,
        'course_object': course,
        'teacher_session': request.session['teacher_id']

    }
    return render(request, 'courseEdit.html', context)


def addStudent(request, course_id):
    error = Student.objects.validate_student(request.POST, course_id)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect('/courses/' + str(course_id))
    course = Course.objects.get(id=course_id)
    Student.objects.create(student_name=request.POST['student_name'], course=course)
    return redirect('/courses/' + str(course_id))
