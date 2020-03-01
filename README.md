# MyHarvest-Server

## 准备工作

- python 环境 
    - pip install pyenv 
    - pyenv install 3.7.5
    - pip install virtualenv 
    - virtualenv venv 3.7.5
    - source venv/bin/activate （deactivate 关闭虚拟环境）

## 开始

- 创建工程
    - django-admin.py startproject mysite
- 启动服务器
    - python manage.py runserver 8000
- 新建模块（django中叫做模块以app命名）
    - python manage.py startapp xxx(模块名称)
    - mysite/setting.py中INSTALL_APPS里，新增APP名称
- 创建超级用户,用于 server/admin 页面管理数据库
    - python manage.py createsuperuser
    - 比如sqlite的 admin-admin
- 同步数据库
    - python manage.py migrate   # 创建表结构
    - python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
    - python manage.py migrate TestModel   # 创建表结构
- 遇到端口号被占用
    - sudo losf -i :xxxx # xxxx为端口号
    - sudo kill -9 xxxx # xxxx为PID编号。在-9配置无效时，可以取消该配置即 sudo kill xxxx


## TODO

- [ ] 请求方式
    - GET
    - POST
- [ ] 请求参数的分析
- [ ] 相应参数的组装
- [x] 查询数据
- [ ] 修改数据
- [ ] JSON序列化
- [ ] 登录验证

## 参考链接

- [“被解放的姜戈”系列文章](http://www.cnblogs.com/vamei/archive/2012/09/13/2682778.html#section6)
    - [01 初试天涯](https://www.cnblogs.com/vamei/p/3528878.html)
    - [02 庄园疑云](https://www.cnblogs.com/vamei/p/3531740.html)
    - [03 所谓伊人](https://www.cnblogs.com/vamei/p/3538183.html)
    - [04 各取所需](https://www.cnblogs.com/vamei/p/3546090.html)
    - [05 黑面管家](http://www.cnblogs.com/vamei/p/3548762.html)
    - [06 假作真时](http://www.cnblogs.com/vamei/p/3550951.html)
    - [07 马不停蹄](http://www.cnblogs.com/vamei/p/3578718.html)
    - [08 远走高飞](http://www.cnblogs.com/vamei/p/5302943.html)
- [Python基础教程（RUNOOB）](https://www.runoob.com/python/python-built-in-functions.html)