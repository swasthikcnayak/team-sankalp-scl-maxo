U
    �:�_�  �                   @   s�   d dl mZ d dlmZmZ d dlmZ d dlmZ d dl	m
Z
mZmZ d dlmZmZmZ edd� �Zed	d
� �Zedd� �Zedd� �ZdS )�    )�login_required)�render�get_object_or_404��Class)�
Submission)�StudentProfile�TeacherProfile�Teach)�
is_student�
is_teacher�is_adminc                 C   sb   t | �r6tt| jd�}tjj|jd�}t| dd|i�S t	| �r^tjj| jd�}t| dd|i�S d S )N��userr   zmarks/subject-list.html�subjects)�teacher__user�teaches)
r   r   r   r   r
   �objects�filter�sectionr   r   )�request�student_profiler   r   � r   �>E:\scl-maxo\team-sankalp-scl-maxo\djangoProject\marks\views.py�	view_list
   s    r   c                 C   s8   t | �r4tt|d�}tjj|d�}t| d||d��S d S )N��id)r   zmarks/student-list.html)�students�	subjectId)r   r   r   r   r   r   r   )r   r   �classId�	class_obj�students_this_sectionr   r   r   �students_list   s    r"   c                 C   s8   t | �r4tt|d�}tjj||d�}t| dd|i�S d S )Nr   ��studentZassignment__subject__id�marks/subject-marks-detail.html�submissions)r   r   r   r   r   r   r   )r   r   r   Z	studentIdr   r&   r   r   r   �student_marks_detail   s    r'   c                 C   s:   t | �r6tt| jd�}tjj||d�}t| dd|i�S d S )Nr   r#   r%   r&   )r   r   r   r   r   r   r   r   )r   r   r   r&   r   r   r   �marks_detail(   s    r(   N)�django.contrib.auth.decoratorsr   �django.shortcutsr   r   �academics.modelsr   Zassignments.modelsr   �users.modelsr   r	   r
   �djangoProject.utilsr   r   r   r   r"   r'   r(   r   r   r   r   �<module>   s   


