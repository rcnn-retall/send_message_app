# send_message_app
安桌运行的一个实时通讯的app

1. #####  用户登入模块

   + kivy 界面

     ![96c9e3ed5bf3ee328dfcaf1a9a5f162f](https://github.com/rcnn-retall/send_message_app/blob/main/IMAGE/96c9e3ed5bf3ee328dfcaf1a9a5f162f.png)

   + 请求行：主机\login

   + 请求体：json

     ```json
     {
         username:"今生水月"，
         password:"admin"
     }
     ```

   + 请求方式：POST

   + 响应类型：JSON

     ```json
     {userauth:"GE3TGNRWHAYDGNJZFY3DEMRTGI3DTZF3RLTZJH7GWC2ONHEI"}
     ```

   + 服务端数据库：mysql

     + userinfo 

       + id  int auto not null

       + username text not null

       + passwodrod text not null

         

   + 服务端验证字段的存储：redis
     + setex
       + username
       + time
       + userauth
   + 客户端验证字段的存储:sqlite3
     + login_auth
     + id int not null (一直为一)
     + userauto text not null

2. 信息页面

   + \is_user（创建会话接口）

   + 请求行： 主机\is_user

   + 请求方式：GET

   + 请求体：JSON

     ```python
                 pua = {
                     "username": self.parent.parent.parent.parent.username,(验证用户名)
                     "userauth": self.parent.parent.parent.parent.userauth,(验证字符串)
                     "add_user": self.input.text(创建会话用户)
                 }
     ```

   + 响应体：
     + code:状态码
     + message:返回信息
