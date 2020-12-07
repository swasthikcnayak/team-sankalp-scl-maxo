# team-sankalp-scl-maxo

#### Project description

1. Backend Framework: **Django**
2. Front-end Framework: **Bootstrap**

## Installation 

1. 
    Only collaborators are allowed to send PR's for now. 
    Clone the repository in your local machine.
2. Checkout to your branch
     ```git
    git status
    git pull
    git checkout -b 'new branch name'
    ```
   Start applying your changes in this new  branch
3. update `setting.py` in `project/project/`
   
    Change the following parameters,
    ```python
    
   EMAIL_HOST_USER = 'YOUR EMAIL HERE'  
	EMAIL_HOST_PASSWORD = 'YOUR PASSWORD HERE'

4. Make migrations/ Create db.sqlite3

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Create a super user.
    In django if you want to access admin page, you need to create an account first.
    ```djangotemplate
    python manage.py createsuperuser
    ```
   Then select your username, email and password.
   
6. Run server
    ```bash
    python manage.py runserver
    ```
7. Do the Development
8. Push your changes
     ```git
    git push origin 'new branch name'
    ```
10. Send PR to the development branch using github website.
