# Python Web

## ORM
对象关系映射

### `flask-sqlalchemy`
用来实现ORM 

使用数据库 `URI` 的方式来配置，统一名称标识符用于指向某一互联网资源，此处名字不能改变
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/flask_db'



### `flask-wtf`
集成 wtforms
CSRF保护

- 默认开启的保护

与 Flask-Uploads 一起支持文件上传



分页查询

- 使用 `offset` 和 `limit`
- `paginate` 分页支持

图片上传
- 不使用 wtf
  - 设置 <form> 的 enctype="multipart/form-data"
  - 获取文件对象，`request.files`


