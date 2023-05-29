# 软件工程
此项目为NKU软件工程课程设计

## 开始
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

## 开发
如果使用了新的python库，请在`requirements.txt`中添加此项