B
    ��_;  �               @   s(   d dl mZ edd� �Zedd� �ZdS )�    )�login_requiredc             C   s0   | j jdkrd S | j jdks(| j jdkr,d S d S )N�STD�THR�ADM)�user�role)�request� r	   �IC:\Users\tulsi\Desktop\team-sankalp-scl-maxo\djangoProject\marks\views.py�	view_list   s    r   c             C   s   d S )Nr	   )r   r	   r	   r
   �
view_notes   s    r   N)�django.contrib.auth.decoratorsr   r   r   r	   r	   r	   r
   �<module>   s   