default:
	@echo Options:
	@echo 	run : run the project
	@echo 	ini : initialize the root user
	@echo 	test : import the database testcase
	@echo 	clean : clean the database testcase 

run:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

ini:
	@echo When firstly deploy, please enter the admin info: 
	@echo 	name=root, email=any@qq.com, password=root
	python manage.py createsuperuser
<<<<<<< HEAD
=======

test:
	python .\manage.py import_sql

clean:
	python .\manage.py clear_sql
>>>>>>> 48b74f5179aa582ffcf10e77a1531744ad15fcc4
