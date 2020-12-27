{% extends 'users/main.html' %}
{% load crispy_forms_filters %}
{% load static %}
{% load crispy_forms_tags %}

{% block css-imports %}
    <link rel="stylesheet" href="{% static 'users/profile.css' %}">
    <link rel="stylesheet" href="{% static 'attendance/main.css' %}">
{% endblock css-imports %}

{% block title %}
    <title>ATTENDANCE</title>
{% endblock title %}




{% block content %}
    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
    <div class="content">
    <h1>CLASS LIST</h1>
        {% if request.user.role == 'THR' %}
            {% if teaches.count != 0 %}
                <h4>Select the class</h4>
            <table id="data-table" class="table " style="border:1px">
                <thead class="thead-dark">
                <tr>
                    <th style="border-bottom: 2px solid black">Subject</th>
                    <th style="border-bottom: 2px solid black">Semester</th>
                    <th style="border-bottom: 2px solid black">Section</th>
                </tr>
                </thead>
                <tbody>
                {% for teach in teaches %}
                    <tr>
                        <td ><a
                               href=" {% url 'view-class' classId=teach.Class.id%}">{{ teach.subject.subject_name }}</a>
                        </td>
                        <td ><a
                               href=" {% url 'view-class' classId=teach.Class.id%}">{{ teach.Class.semester }}</a>
                        </td>
                        <td><a
                               href=" {% url 'view-class' classId=teach.Class.id%}">{{ teach.Class.section_name }}</a>
                        </td>
                    </tr>
                {% endfor %}
                </tbody>
            </table>
                {% else %}
                <h4>You do not teach any class! No record found</h4>
                {% endif %}
    {% endif %}
    </div>


{% endblock content %}