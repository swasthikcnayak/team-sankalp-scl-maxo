U
    ;~�_  �                   @   sT   d dl mZ d dlmZmZ d dlmZmZ G dd� dej�Z	G dd� dej�Z
dS )	�    )�models)�Subject�Class)�StudentProfile�TeacherProfilec                   @   sv   e Zd Zejeejdd�Zejeej	ddd�Z
ejeej	dd�Zejdd�Zejdd�Zejdd�ZG d	d
� d
�ZdS )�
Attendance�student)�	on_delete�verbose_name�subjectT�r	   r
   �null)r	   r   r   )�defaultc                   @   s   e Zd ZdZdS )zAttendance.Meta)r   r   N)�__name__�
__module__�__qualname__�unique_together� r   r   �DE:\scl-maxo\team-sankalp-scl-maxo\djangoProject\attendance\models.py�Meta   s   r   N)r   r   r   r   �
ForeignKeyr   �CASCADEr   r   �SET_NULLr   r   �IntegerFieldZclasses_conductedZclasses_attended�
percentager   r   r   r   r   r      s   r   c                   @   st   e Zd Zejeddd�Zejeej	ddd�Z
ejeej	ddd�Zejeejddd�Zejdd	d
�Zejddd�ZdS )�AttendanceLog�	absenteesT)r
   �blankr   Fr   �class�teacher�conducted_date)r   r
   �logged_date)�auto_now_addr
   N)r   r   r   r   �ManyToManyFieldr   r   r   r   r   r   r   r   r   r   �	DateFieldr    �DateTimeFieldr!   r   r   r   r   r      s   r   N)�	django.dbr   �academics.modelsr   r   �users.modelsr   r   �Modelr   r   r   r   r   r   �<module>   s   