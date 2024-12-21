## App Description &#128209;

This is a simple MPA project, based on Django4 and postgreSQL. The app provides different data reports.

## Launch instructions &#128190;

&#9881;**Frontend**:

- Bootstrap5;
- HTML/SCSS;
- Webpack + prettier + eslint.
  
&#9881;**Backend**:

- Django 4;
- Docker;
- PostgresQL.

<div style="display: flex; justify-content: end;">
  <p>Git and Docker should be installed locally on Your PC.</p>
</div>

---

1. Clone repository to Your local path:

    ```sh
    cd <your_local_path> && git clone <http/ssh-link>
    ```

2. Run compose:

    ```sh
    cd CompanyAndSales && docker compose --env-file ./.env.public up --build
    ```

3. After the installation is complete the web-app will start on `0.0.0.0:8001`;

- Open web-app in browser using URL: <http://0.0.0.0:8001/>

4. The superuser(admin) is NOT created automatically. To create it by yourself follow the instructions below in the new terminal (related docker containers must be in use):

    4.1 Create superuser:

    ```sh
    docker exec -it server python manage.py createsuperuser --noinput --username admin --email admin@example.com
    ```

    4.2 Note, that default password is already preset in the script above. Default credentials are:

    ```js
        {
          username: admin;
          email: admin@example.com;
          password: admin;
        }
    ```

    - for another password preset it should be **changed FIRST** in ./.env.public `DJANGO_SUPERUSER_PASSWORD=` and then run point 4.1.

    4.3 For changing already existing superuser's password (not password preset):

    ```sh
    docker exec -it server python manage.py changepassword admin
    ```

    - you will be prompted to set another password.

5. Stop the web-app press in current terminal:

    ```sh
    Ctrl + C
    ```

    or

    ```sh
    docker compose --env-file ./.env.public stop
    ```

6. Start again the web-app:

    ```sh
    docker compose --env-file ./.env.public start
    ```

7. To completely remove all related docker containers, docker images, volumes and related data:

    ```sh
    docker compose --env-file ./.env.public down --volumes --rmi all
    ```

    <span style="color: rgb(255, 0, 0)">After this step, it is need to go back to point №2 to run web-app again.</span>

---

### p.s

- Local environment variables can be changed in the `./.env.public`<br/>
- Outer ports of both django-server & postgresql are `8001` & `5433` respectively and could not be changed via environment.

## Screenshots &#127745;

1. Main page (not authenticated users)

<div align="center">
  <img src="./screenshots/ScreenShot_1.png" width="75%" heigth="75%" alt="Main page">
</div>

2. SignUp & signIn forms:

<div align="center">
  <img src="./screenshots/ScreenShot_2.png" width="75%" heigth="75%" alt="SignUp form">
  <img src="./screenshots/ScreenShot_3.png" width="75%" heigth="75%" alt="SignIn form">
</div>

3. Description page

<div align="center">
  <img src="./screenshots/ScreenShot_4.png" width="75%" heigth="75%" alt="Description">
</div>

4. Data presentation:

<div align="center">
  <img src="./screenshots/ScreenShot_5.png" width="75%" heigth="75%" alt="Data presentation">
</div>

5. Add/Edit data:

<div align="center">
  <img src="./screenshots/ScreenShot_6.png" width="75%" heigth="75%" alt="Add/edit data form">
</div>

6. Reports presentation:

<div align="center">
  <img src="./screenshots/ScreenShot_7.png" width="75%" heigth="75%" alt="Reports presentation">
</div>

<br>

---
