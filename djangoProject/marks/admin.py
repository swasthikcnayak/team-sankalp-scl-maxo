B
    ��_W  �               @   s   d dl mZmZ d dlmZ d dlmZ d dlmZ	 d dl
mZ d dlmZ d dlmZ d dlmZ dZdZdZd	Zed
ee��ede	jjdd�dd�ede	jjdd�dd�ede	jjdd�dd�ede	jjdd�dd�edee��edee��edee��gZej�reeejejd�7 ZdS )�    )�path�include)�settings)�static)�viewsNzdjangoProject.views.handler404zdjangoProject.views.handler500zdjangoProject.views.handler400zdjangoProject.views.handler403zusers/zpassword-reset/zusers/password_reset.html)�template_nameZpassword_reset)�namezpassword-reset/done/zusers/password_reset_done.htmlZpassword_reset_donez(password-reset-confirm/<uidb64>/<token>/z!users/password_reset_confirm.htmlZpassword_reset_confirmzpassword-reset-complete/z"users/password_reset_complete.htmlZpassword_reset_completezattendance/zmarks/znotes/)Zdocument_root) �django.urlsr   r   �django.confr   Zdjango.conf.urls.staticr   Zdjango.contrib.authr   Z
auth_viewsZ
users.urls�urlsZuser_urlZattendance.urlsZattendance_urlZacademics.urlsZacademics_urlZ
marks.urlsZ	marks_urlZ
handler404Z
handler500Z
handler400Z
handler403ZPasswordResetView�as_viewZPasswordResetDoneViewZPasswordResetConfirmViewZPasswordResetCompleteView�urlpatterns�DEBUG�	MEDIA_URL�
MEDIA_ROOT� r   r   �PC:\Users\tulsi\Desktop\team-sankalp-scl-maxo\djangoProject\djangoProject\urls.py�<module>   s8   