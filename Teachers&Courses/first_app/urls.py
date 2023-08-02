from django.urls import path
from . import views

app_name = 'first_app'
urlpatterns = [
    path('', views.index),
    path('registration', views.registration,
         name='registration'),
    path('login', views.login,
         name='login'),
    path('logout', views.logout,
         name='logout'),
    path('home', views.success, name='home'),
    path('courses/new', views.newCourse, name='newCourse'),
    path('courseCreate', views.courseCreate,
         name='courseCreate'),
    path('newCourseRedirect', views.newCourseRedirect,
         name='newCourseRedirect'),
    path('successRedirect', views.successRedirect,
         name='successRedirect'),
    path('courses/<int:id>', views.courseDetails, name='courseDetails'),
    path('courses/<int:course_id>/edit', views.courseEdit, name='courseEdit'),
    path('editCourse/<int:course_id>', views.editCourse,
         name='editCourse'),
    path('deleteCourse/<int:course_id>/', views.deleteCourse, name='deleteCourse'),
    path('add_student/<int:course_id>/',
         views.addStudent, name='addStudent'),

]
