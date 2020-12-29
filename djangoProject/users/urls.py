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
    <h1>CLASS DETAILS</h1>
        <p>semester : {{ class.semester }}</p>
        <p>section : {{ class.section_name }}</p>
        <p>department : {{ class.department.department_name }}</p>
        <p>class joining link : {{ class.link }}</p>
        <p>timetable : {{ class.timetable }}</p>
    </div>
{% endblock content %}

