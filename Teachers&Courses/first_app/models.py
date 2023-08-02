from django.db import models
import re


class TeacherManager(models.Manager):
    def login_validator(self, postData):
        error = {}
        get_emails = Teacher.objects.all()
        if len(postData['teacher_name']) < 2:
            error['teacher_name'] = "teacher name 2 characters or more"

        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            error['email'] = "nnvalid email address!"

        for teacher in get_emails:
            if postData['email'] == teacher.email:
                error['email_exists'] = "email exists"

        if postData['password'] != postData['conf_password']:
            error['password_conf'] = " confirmation password not matched"

        if len(postData['password']) < 8:
            error['password'] = "password Must be at least 8 characters"
        return error

    def course_validator(self, postData):
        error = {}
        days_list = ['saturday', 'monday',
                     'tuesday', 'wednesday', 'thursday']
        day_exist = False
        if len(postData['course_name']) < 2:
            error['course_name'] = "course name 2 characters or more"
        if len(postData['teaching_level']) < 1:
            error['teaching_level_empty'] = "teaching level required"
        elif int(postData['teaching_level']) > 3 or int(postData['teaching_level']) <= 0:
            error['teaching_level_range'] = "teaching level between 1 to 3"

        lecture_day = postData['lecture_day']
        for day in days_list:
            if lecture_day == day:
                day_exist = True
                break
        if not day_exist:
            error['lecture_day'] = "please enter a day name "
        return error

    def validate_student(self, postData, course_id):
        error = {}
        if len(postData['student_name']) < 2:
            error['student_name'] = "students Name 2 characters or more"
        course = Course.objects.get(id=course_id)
        if course.students.all().count() >= 25:
            error['student_number'] = " Maximum number of students in 25"
        return error


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # courses
    objects = TeacherManager()


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    teaching_level = models.SmallIntegerField()
    lecture_day = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, related_name='courses',
                             on_delete=models.CASCADE)
    objects = TeacherManager()
    # students


class Student(models.Model):
    student_name = models.CharField(max_length=255)
    course = models.ForeignKey(
        Course, related_name='students', on_delete=models.CASCADE)
    objects = TeacherManager()
