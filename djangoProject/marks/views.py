from django.contrib.auth.decorators import login_required
from django.shortcuts import render

'''
@login_required
def view_marks(request):
    return ""


@login_required
def view_marks_subject(request):
    return "" '''

# we can get the class of the user logged in from his profile. using the teaches model
# we can then find all the subjects taught to that class, which can form a drop down list.


# we can access Teach model using the teacher profile. which gives us the class and the subject that he teacher
# using which, we can get list of all students belonging to that class.
# for every student then can add marks field.
