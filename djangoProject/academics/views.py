{% extends 'users/main.html' %}
{% load crispy_forms_filters %}
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
              <h1>Reset your Password!!!</h1>
	        </header>
	        <form class="templatemo-login-form" method="POST">
                {% csrf_token %}
		              	{{ form | crispy }}
				<div class="form-group">
					<button type="submit" class="templatemo-blue-button width-100">Submit</button>
				</div>
	        </form>
		</div>
{% endblock content%}

