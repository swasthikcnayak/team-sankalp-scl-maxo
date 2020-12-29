{% extends 'users/main.html' %}
{% load static %}
{% load crispy_forms_tags %}

{% block css-imports %}
      <link rel="stylesheet" href="{% static 'users/profile.css' %}">
{% endblock css-imports %}

{% block title %}
    <title>PASSWORD-RESET</title>
{% endblock title %}


{% block content %}
<div class="templatemo-content-widget templatemo-login-widget white-bg" style="margin-top: 150px;">
			<header class="text-center" style="margin-bottom: 20px;">
                    {% if messages %}
                    {%  for message in messages %}
                        <div class="alert alert-{{ message.tags }}">
                            {{ message }}
                        </div>
                    {% endfor %}
            {% endif %}
                <h3 class="pt-8 text-info" style="margin-top: 20px;">Your Password has been reset.</h3>
	        </header>
        <a href="{% url 'login' %}"><button type="button" class="templatemo-blue-button width-100">Login In Here</button></a>
		</div>
{% endblock content%}

