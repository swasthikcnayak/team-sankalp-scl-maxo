{% extends 'users/main.html' %}
{% load crispy_forms_filters %}

{% load static %}
{% load crispy_forms_tags %}

{% block css-imports %}
      <link rel="stylesheet" href="{% static 'users/profile.css' %}">
{% endblock css-imports %}

{% block title %}
    <title>PROFILE</title>
{% endblock title %}


{% block content %}
<div class="student-profile py-4">
{% if messages %}
                    {%  for message in messages %}
                        <div class="alert alert-{{ message.tags }}">
                            {{ message }}
                        </div>
                    {% endfor %}
            {% endif %}
          <div class="container">
              <div class="row">
              <div class="col-lg-3 col-lg-offset-4">
                  <div class="card shadow-sm">
                    <div class="card-header bg-transparent text-center">
                        <img class="profile_img" src="{{ user.image.url }}" alt="Profile photo">
                        <h3>{{ user.username }}</h3>
                        <h4>{{ user.email }}</h4>
                    </div>
                  </div>
              </div>
              </div>
              <br/>
              <form method="POST" enctype="multipart/form-data">
                {% csrf_token %}
                    <div class="row">
                        <div class="col-lg-6">
                            <fieldset class="form-group ">
                                <legend class="border-bottom mb-4">Personal Information</legend>
                                    {{ u_form|crispy }}
                            </fieldset>
                        </div>
                        <div class="col-lg-6">
                            <fieldset class="form-group">
                                {% if user.role != 'ADM' %}
                                <legend class="border-bottom mb-4">Academic Information</legend>
                                    {{ p_form|crispy }}
                                {% endif %}
                            </fieldset>
                        </div>
                    </div>
                   <div class="row text-center">
                      <div class="form-group">
                          <button class="button btn-info" style="vertical-align:middle"><span>Update changes</span></button>
                          <a href="{% url 'password_reset' %}"><button class="button btn  btn-info" type="button" ><span>Change password </span></button></a>
                      </div>
                   </div>
              </form>
            </div>
            </div>
{% endblock content%}

