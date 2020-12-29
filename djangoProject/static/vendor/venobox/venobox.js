U
    ��_C  �                   @   s.   d dl mZmZ d dlZG dd� dej�ZdS )�    )�
migrations�modelsNc                   @   s�   e Zd ZdZg Zejddejddddd�fdej	dd	�fd
e�
� fde�
� fdej	dd	�fde�� fgd�ejddejddddd�fde�� fde�
� fdejdd�fdejejjjjddd�fgd�gZdS )�	MigrationT�
Assignment�idF�ID)�auto_created�primary_key�	serialize�verbose_name�assignment_name�   )�
max_length�
start_time�end_time�maximum_marks�   �question)�name�fields�
Submission�answer�time_submitted�marks_obtained)�null�
assignmentzassignments.Assignment)�	on_delete�tor   N)�__name__�
__module__�__qualname__�initial�dependenciesr   �CreateModelr   �	AutoField�	CharField�DateTimeField�URLField�IntegerField�
ForeignKey�django�db�deletion�CASCADE�
operations� r/   r/   �VE:\scl-maxo\team-sankalp-scl-maxo\djangoProject\assignments\migrations\0001_initial.pyr      s,   


��

���r   )�	django.dbr   r   �django.db.models.deletionr*   r   r/   r/   r/   r0   �<module>   s   