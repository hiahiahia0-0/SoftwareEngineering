# 软件工程
此项目为NKU软件工程课程设计

## 开始
### 经典安装
1. 执行如下命令安装python依赖
`pip install -r requirements.txt`
2. 创建如下的数据库(也可以自己更改setting.py)
```
        'NAME': 'cet', # 数据库名称
        'HOST': '127.0.0.1', # 数据库地址，本机 ip 地址 127.0.0.1 
        'PORT': 3306, # 端口 
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456', # 数据库密码
```
3. 执行 `make run` 启动
4. 执行 `make ini` .根据提示创建root
5. 执行 `make test` 加入测试用例


### docker部署
仅需要有docker环境即可

然后执行如下命令
`docker build -t django_project .`
`docker run -d --name django_pro -p 8000:8000 django_project /bin/sh -c "while true;do echo hello;sleep 5;done"`
`docker exec <container_id> python manage.py runserver`
即可启动

PS：需要提前更改setting.py的数据库信息，以及
## 开发
如果使用了新的python库，请在`requirements.txt`中添加此项