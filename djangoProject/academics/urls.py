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
                <h3 class="pt-8 text-info" style="margin-top: 20px;">An email has been sent to your email. Follow the steps as directed.</h3>
	        </header>
		</div>
{% endblock content%}

