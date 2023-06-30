# SoftwareEngineering
This is software engineering project in NKU.

## start
env:
- python 3.7 +
- mysql 5.6

1. execute the command below to install requirements
`pip install -r requirements.txt`
2. create a database below
```
        'NAME': 'cet',
        'HOST': '127.0.0.1', 
        'PORT': 3306, 
        'USER': 'root',
        'PASSWORD': '123456'
```
3. execute `make run` to start
4. execute `make ini` and follow the tips
5. execute `make test` to add testcases


### docker apply

You only need to have Docker and MySQL environments.

Then execute the following commands:

```sh
sudo docker build -t django_project .
sudo docker run -d --name django_pro -p 8000:8000 django_project /bin/sh -c "while true;do echo hello;sleep 5;done"
```

After that, enter the container and execute `make run`, then cancel it.

Next, execute `python manage.py runserver 0:8000` (to expose the port) to start.

PS: **Remember to change the database information in `setting.py`.**

## dev
If you have added new Python libraries, please include them in the `requirements.txt` file.

## debug
If you encounter database migration issues, you can execute the `rm` file in the root directory. Use `.bat` for Windows and `.sh` for Linux.