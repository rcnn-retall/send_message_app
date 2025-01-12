# send_message_app
安桌运行的一个实时通讯的app

1. #####  用户登入模块

   + kivy 界面

     ![96c9e3ed5bf3ee328dfcaf1a9a5f162f](C:\Users\iewv-nyaj\Desktop\keice\send_message_app\IMAGE\96c9e3ed5bf3ee328dfcaf1a9a5f162f.png)

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
