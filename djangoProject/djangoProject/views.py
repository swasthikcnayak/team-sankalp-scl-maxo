U
    ��_�  �                   @   s.   d dl mZmZ d dlZG dd� dej�ZdS )�    )�
migrations�modelsNc                   @   s�   e Zd ZdZdddgZejddeje	j
jjjddd�d	�ejdd
eje	j
jjjdd
d�d	�ejddejde	j
jjjddd�d	�ejddhd�gZdS )�	MigrationT)�	academics�0001_initial)�usersr   )�marksr   �mark�studentzusers.StudentProfile)�	on_delete�to�verbose_name)�
model_name�name�field�subjectzacademics.Subject�teacherzusers.TeacherProfile)�nullr   r   r   )r
   r   �	exam_name)r   �unique_togetherN)�__name__�
__module__�__qualname__�initial�dependenciesr   �AddFieldr   �
ForeignKey�django�db�deletion�CASCADE�SET_NULL�AlterUniqueTogether�
operations� r$   r$   �[E:\scl-maxo\team-sankalp-scl-maxo\djangoProject\marks\migrations\0002_auto_20201224_1735.pyr      s2   ������r   )�	django.dbr   r   �django.db.models.deletionr   r   r$   r$   r$   r%   �<module>   s   