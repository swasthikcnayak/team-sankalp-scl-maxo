B
    ��_�
  �               @   s�   d dl mZ d dlmZmZ d dlmZ d dlmZ d dl	m
Z
mZmZ d dlmZmZ d dlmZ d dlmZ ed	d
� �Zedd� �ZdS )�    )�ceil)�render�redirect)�login_required)�
Attendance)�StudentProfile�TeacherProfile�Teach)�Subject�Class)�AttendanceUpdateForm)�messagesc             C   s�   | j jdkr:tjj| j d�}tjj|d�}t| dd|i�S | j jdksR| j jdkr�tjj| j d�}t	jj|d�}t| dd	|i�S t
d
�S )N�STD)�user)�studentzattendance/attendance.html�attendances�THR�ADM)�teacher�teachesz"/users/admin/attendance/attendance)r   �roler   �objects�getr   �filterr   r   r	   r   )�requestZstudentProfiler   �teacherProfiler   � r   �NC:\Users\tulsi\Desktop\team-sankalp-scl-maxo\djangoProject\attendance\views.py�view_attendance   s    r   c       
      C   sH  | j jdks| j jdk�rDtjj|d�}tjj|d�}t� }tjj||d�}| j	dkrht
| d||d��S | j	dk�rDtjj| j d	�}t| j�}|�� �rD|jd
d�}||_||_||_|�� }tjj||d�}xb|D ]Z}	|	jd |	_|	j|j�� k�r|	jd |	_t|	j|	j d �|	_|	��  tj| dd� q�W t
| d||d��S d S )Nr   r   )�id)�subjectZstudent__section�GETzattendance/attendance-edit.html)r   �form�POST)r   F)�commit)r   r    �   �d   z!Absentees registered successfully)�message)r   r   r
   r   r   r   r   r   r   �methodr   r   r#   �is_valid�saver   r    �classes_conductedr   �	absentees�all�classes_attendedr   �
percentager   �success)
r   ZclassIdZ	subjectIdr    Z	class_objr"   r   r   �log�
attendancer   r   r   �view_subject_attendance   s4    



r3   N)�mathr   �django.shortcutsr   r   �django.contrib.auth.decoratorsr   Zattendance.modelsr   �users.modelsr   r   r	   �academics.modelsr
   r   Zattendance.formsr   Zdjango.contribr   r   r3   r   r   r   r   �<module>   s   