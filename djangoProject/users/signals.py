U
    ���_M
  �                   @   s`   d dl mZ G dd� dej�ZG dd� dej�ZdZdZG dd	� d	ej�ZG d
d� dej�ZdS )�    )�modelsc                   @   s<   e Zd Zejdddd�Zejdddd�Zdd� Zdd� Zd	S )
�
Department�2   T)�
max_length�null�unique�   c                 C   s   | j S �N)�department_short_form��self� r   �CE:\scl-maxo\team-sankalp-scl-maxo\djangoProject\academics\models.py�__str__   s    zDepartment.__str__c                 C   s   | j �� | _ | j�� | _d S r	   )r
   �upper�department_namer   r   r   r   �clean   s    zDepartment.cleanN)	�__name__�
__module__�__qualname__r   �	CharFieldr   r
   r   r   r   r   r   r   r      s   r   c                   @   sf   e Zd Zejeejdd�Zejddd�Z	ejddd�Z
ejddd�Zdd� ZG d	d
� d
�Zdd� ZdS )�SubjectT)�	on_deleter   r   �r   r   r   �   c                 C   s   | j jd | j S �N�+)�
departmentr
   �subject_short_formr   r   r   r   r      s    zSubject.__str__c                   @   s   e Zd ZdZdS )zSubject.Meta)r   r   N�r   r   r   �unique_togetherr   r   r   r   �Meta   s   r!   c                 C   s   | j �� | _ | j�� | _d S r	   )r   r   �subject_namer   r   r   r   r      s    zSubject.cleanN)r   r   r   r   �
ForeignKeyr   �SET_NULLr   r   r"   r   �creditsr   r!   r   r   r   r   r   r      s   r   ))�1r&   )�2r'   )�3r(   )�4r)   )�5r*   )�6r+   )�7r,   )�8r-   ))�Ar.   )�Br/   )�Cr0   )�Dr1   c                   @   sn   e Zd Zejdedd�Zejdedd�Zej	e
ejd�Zejdd�Ze�� Zd	d
� ZG dd� d�Zdd� ZdS )�Class�   r&   )r   �choices�defaultr   r.   )r   T)r   c                 C   s   | j �� | _ d S r	   )�section_namer   r   r   r   r   r   ;   s    zClass.cleanc                   @   s   e Zd ZdZdS )z
Class.Meta)�semesterr6   r   Nr   r   r   r   r   r!   >   s   r!   c                 C   s   | j jd | j d | j S r   )r   r
   r7   r6   r   r   r   r   r   A   s    zClass.__str__N)r   r   r   r   r   �SEM_CHOICESr7   �SECTION_CHOICESr6   r#   r   �CASCADEr   �URLField�linkZ	timetabler   r!   r   r   r   r   r   r2   4   s   r2   c                   @   sl   e Zd Zejeejddd�Zejeej	dd�Z
ejddd�Zejddd�Ze�� ZG d	d
� d
�Zdd� ZdS )�Noter   T)r   �verbose_namer   �subject)r   r>   �   r   r   c                   @   s   e Zd ZdZdS )z	Note.Meta)r   r?   �chapter_numberNr   r   r   r   r   r!   L   s   r!   c                 C   s   | j jd | jj d | j S r   )r   r
   r?   r   rA   r   r   r   r   r   O   s    zNote.__str__N)r   r   r   r   r#   r   r$   r   r   r:   r?   r   rA   Zchapter_namer;   r<   r!   r   r   r   r   r   r=   E   s   r=   N)	�	django.dbr   �Modelr   r   r8   r9   r2   r=   r   r   r   r   �<module>   s   