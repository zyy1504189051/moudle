调度服务-API
======

|接口 |备注 |
|:--- |:--- |
|[账号创建接口](#账号创建接口) |创建账号 |
|[账号修改接口](#账号修改接口) |修改账号 |
|[按ID查询接口](#按ID查询接口) |按ID查询 |
|~~[账号查询接口](#账查询除接口)~~ |（暂不实现） |
|~~[账号删除接口](#账号删除接口)~~ |只做禁用，不做删除。（暂不实现） |
|[修改密码接口](#修改密码接口) |需要调用client lib，实际修改密码，需要**独立端口** |
|[登录接口](#登录接口) |执行账号登录，需要**独立端口** |
|~~[加密接口](#加密接口)~~ |敏感字段加密 |
|~~[解密接口](#解密接口)~~ |敏感字段解密 |

## 账号创建接口
> [POST]
> /api/v1/account/add

**request 请求**
```json
{
    "request_token": "12123sdfafsf12313",
    "account": {
        "username": "SH123333",
        "password": "123adsasd",
        "vpn_username": "us133",
        "vpn_password": "1111333",
        "ins_company": "pinga",
        "login_type": 1,
        "area": "shangh",
		"is_bank": 0,  # 是否银行,
		"proxy": "代理地址:port",
    }
}
```

**response 返回**

```json
{
    "request_token": "12123sdfafsf12313",
    "status": "success",
    "data": {
        "account_id": 1012
    }
}
```

## 账号修改接口
> [POST]
> /api/v1/account/modify
> 
> 此接口的密码修改<font color=red>**仅**</font>修改本地数据库记录，<font color=red>**不会**</font>调用client。
> 请求参数输入哪个字段修改哪个字段

**request 请求**
```
{
    "request_token": "12123sdfafsf12313",
    "account": {
        "account_id": 1012,
        "username": "SH123333",
        "password": "123adsasd",
        "vpn_username": "us133",
        "vpn_password": "1111333",
        "ins_company": "pinga",
        "login_type": 1,
        "area": "shangh",
		"is_bank": 0,  # 是否银行
		"proxy": "代理地址:port",
		"pre_url": "直销报价前预访问地址",
		"pre_verify": "直销报价后是否调用预核保 -1 否 1是",
    }
}
```

**response 返回**

```json
{
    "request_token": "12123sdfafsf12313",
    "status": "success",
    "data": {
        "account_id": 1012
    }
}
```


## 按ID查询接口
> [GET]
> /api/v1/account/detail
> 
> 接口返回的密码为密文形式

**request 请求**
```
{
    "request_token": "12123sdfafsf12313",
    "need_password": true/false,  # 是否返回密码，默认false
    "account": {
        "account_id": 1012
    }
}
```

**response 返回**

```json
{
    "request_token": "12123sdfafsf12313",
    "status": "success",
    "data": {
        "account_id": 1012,
        "username": "SH123333",
        "password": "123adsasd",
        "vpn_username": "us133",
        "vpn_password": "1111333",
        "ins_company": "pinga",
        "login_type": 1,
        "area": "shangh",
        "cookies": "base64编码后的字符串，解码后为字典格式",
		"is_bank": 0,  # 是否银行,
        "proxy": "host:port",
        "host": "host",
		"pre_url": "直销报价前预访问地址",
		"pre_verify": "直销报价后是否调用预核保 -1 否 1是",
    }
}
```

## 修改密码接口
> [POST]
> /api/v1/account/password/modify
> 
> 该接口会请求底层保险公司页面，进行实际的密码修改动作
> 该功能需要使用独立端口提供服务

**request 请求**
```
{
    "request_token": "12123sdfafsf12313",
    "account": {
        "account_id": 1012,
        "old_password": "123asdQWE",
        "password": "ZXCqwe123",
        "old_vpn_password": "123asdQWE",
        "vpn_password": "ZXCqwe123"
    }
}
```

**response 返回**

```json
{
    "request_token": "12123sdfafsf12313",
    "status": "success",
    "data": {
        "account_id": 1012
    }
}
```

## 登录接口
> [POST]
> /api/v1/account/login
> 
> 该接口会请求底层保险公司页面，进行实际的密码修改动作
> 该功能需要使用独立端口提供服务

**request 请求**
```
{
    "request_token": "12123sdfafsf12313",
    "account": {
        "account_id": 1012
    }
}
```

**response 返回**

```json
{
    "request_token": "12123sdfafsf12313",
    "status": "success",
    "data": {
        "account_id": 1012,
        "cookies": "base64编码后的字符串"
    }
}
```
