default:
	@echo Options:
	@echo 	run : run the project
	@echo 	ini : initialize the root user

run:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

ini:
	@echo When firstly deploy, please enter the admin info: 
	@echo 	name=root, email=any@qq.com, password=root
	python3 manage.py createsuperuser
