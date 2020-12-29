U
    ���_�  �                   @   sP  d dl mZmZ d dlmZ d dlmZ d dlmZ	 d dl
mZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ dZdZd	Zd
Zededd�edee��ede	jjdd�dd�ede	jjdd�dd�ede	jjdd�dd�ede	jjdd�dd�edee��edee��edee��edee��g
Z ej!�rLe eej"ej#d �7 Z dS )!�    )�path�include)�settings)�static)�viewsN)�	home_viewzdjangoProject.views.handler404zdjangoProject.views.handler500zdjangoProject.views.handler400zdjangoProject.views.handler403� �home)�namezusers/zpassword-reset/zusers/password_reset.html)�template_nameZpassword_resetzpassword-reset/done/zusers/password_reset_done.htmlZpassword_reset_donez(password-reset-confirm/<uidb64>/<token>/z!users/password_reset_confirm.htmlZpassword_reset_confirmzpassword-reset-complete/z"users/password_reset_complete.htmlZpassword_reset_completezattendance/zmarks/zassignments/z
academics/)�document_root)$�django.urlsr   r   �django.confr   Zdjango.conf.urls.staticr   �django.contrib.authr   Z
auth_viewsZ
users.urls�urlsZuser_urlZattendance.urlsZattendance_urlZacademics.urlsZacademics_urlZ
marks.urlsZ	marks_urlZassignments.urlsZassignment_urlZdjangoProject.viewsr   Z
handler404Z
handler500Z
handler400Z
handler403ZPasswordResetView�as_viewZPasswordResetDoneViewZPasswordResetConfirmViewZPasswordResetCompleteView�urlpatterns�DEBUG�	MEDIA_URL�
MEDIA_ROOT� r   r   �EE:\scl-maxo\team-sankalp-scl-maxo\djangoProject\djangoProject\urls.py�<module>   sJ   �����