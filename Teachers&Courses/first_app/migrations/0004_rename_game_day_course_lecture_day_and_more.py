# Generated by Django 4.2.2 on 2023-08-02 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_course_student_teacher_remove_team_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='game_day',
            new_name='lecture_day',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='skill_level',
            new_name='teaching_level',
        ),
    ]
