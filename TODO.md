WX4399 Design & Todo
======

# 创建游戏界面    
    tab页：
    基本信息 | 奖项设置 | 素材定制 | 分享设置 |  完成

### 基本信息：
      游戏名称，单行TextField, Help: 不超过64个字
      开始时间，DatetimeFiled, Help: 必填
      结束时间，DatetimeFiled, Help: 必填，必须大于开始时间
      游戏规则，多行TextField, Help: 不超过400个字
      Button: 下一步

### 奖项设置：
      按钮组：无奖 | 按排名发奖 | 按分数级别发奖
        选完后：按钮变色或者打勾，以下内容伴随改变
      提示区：
        方式为：无奖 / 按排名发奖 / 按分数级别发奖
        请注意“基本信息 -> 游戏规则”的文字要与此相符
      操作区：
        无奖：操作区为空
        按排名发奖：操作区参考(创建活动2-奖项设置2.jpg)
        按分数发奖：同上，奖品数量改为领奖分数              
      Button: 下一步 | 完成
      
### 分享设置：
     分成3部分：称号设置、分享标题格式、分享描述格式
     称号设置类似奖项设置：无称号 | 按排名设称号 | 按分数设称号
     分享标题格式和分享描述格式中可以使用以下参数：
       %title% 称号 
       %score% 得分
     Button: 下一步 | 完成
     
### 素材定制：TBD
    每个游戏不同

### 完成:
    url
    二维码
    link: 下载
  

# Todo    
## 游戏创建页
1.4个tab页切换  
  1) 各页面点上/下一步切换  
  2) 点完成时post数据  
2. 奖项设置
  1) 按钮组  
  2) 点按钮出现相应操作区    
3. 素材定制
  1) 图片上传demo字段  
4. 分享设置
  1) 按钮组  
  2) 点按钮出现相应操作区
5.基本信息
  1) datetime picker
6.各页面invalidator
7.post返回，并在完成页面显示url和二维码  

## .php转.python

cantk.php

-- request --
GET /firefly0411B/cantk/js/cantk.php HTTP/1.1
Host: 192.168.1.120
Connection: keep-alive
Cache-Control: max-age=0
Accept: */*
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36
Referer: http://192.168.1.120/firefly0411B/index.html
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4
Cookie: PHPSESSID=sshibp64v752ovqi5r269808i2

-- response --
HTTP/1.1 200 OK
Date: Sun, 17 May 2015 13:38:43 GMT
Server: Apache/2.4.9 (Win64) PHP/5.5.12
X-Powered-By: PHP/5.5.12
Vary: Accept-Encoding
Expires: Sun, 17 May 2015 13:43:43 GMT
Cache-Control: public, max-age=300
Content-Encoding: gzip
Keep-Alive: timeout=5, max=99
Connection: Keep-Alive
Transfer-Encoding: chunked
Content-Type: application/x-javascript; charset=UTF-8

