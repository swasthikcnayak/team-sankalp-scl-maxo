U
    ��_?  �                   @   s.   d dl mZmZ d dlZG dd� dej�ZdS )�    )�
migrations�modelsNc                   @   s  e Zd ZdZdddgZejddejdddd�d	�ejdd
ej	e
jjjjdd
d�d	�ejddej	de
jjjjddd�d	�ejddej	de
jjjjdd�d	�ejddej	e
jjjjddd�d	�ejdd
ej	de
jjjjdd
d�d	�ejddhd�ejddhd�gZdS )�	MigrationT)�
attendance�0001_initial)�	academicsr   )�usersr   �attendancelog�	absenteeszusers.StudentProfile)�blank�to�verbose_name)�
model_name�name�field�subjectzacademics.Subject)�	on_deleter   r   �teacherzusers.TeacherProfile)�nullr   r   r   r   �Classzacademics.Class)r   r   r   �student)�conducted_dater   r   )r   �unique_together)r   r   N)�__name__�
__module__�__qualname__�initial�dependenciesr   �AddFieldr   �ManyToManyField�
ForeignKey�django�db�deletion�CASCADE�SET_NULL�AlterUniqueTogether�
operations� r(   r(   �`E:\scl-maxo\team-sankalp-scl-maxo\djangoProject\attendance\migrations\0002_auto_20201224_1735.pyr      sX   ����������r   )�	django.dbr   r   �django.db.models.deletionr!   r   r(   r(   r(   r)   �<module>   s   