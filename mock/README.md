##api相关

###相关api
+ 返回结果
    + 无资源和无权限直接404与403返回
    + 200情形下需要含有数据：
    ```
{
      error : 0,
      msg : "",
      data : {}
}
```

###api细分
+ 有关表的之间的步骤审批等操作，以一个字段形式放在表中，以修改UPDATE字段数据的形式来呈现。

####表数据，以equipment为例
+ (GET/POST/PUT/DELETE) api/equipment [source设备数据]
    + GET为请求
        + 可以考虑增加count及page参数的需求接口，目前可以先不理会，直接回传整个表即可
        + 结果需要含有两个数据:
            + title ：object，描述列属性
                + 每一列包含一些自身属性 :
                    + name ：字段显示名
                    + modifiable ：可修改与否
                    + options ：Array 如果修改的话需要从中选择
            + content ：array，每一个里的key与titleObject对应，前端靠key来对齐
        + ~~api/equipment/:id 暂不需求~~
    + POST为修改
        + api/equipment/:id
            + post内容数据里包含id编号，需*检测确认*或者*无视*
        + ~~api/equipment~~
            + post内容数据本身携带有id编号，选择项目也以字符串形式回传，后端需要*check是否与title.options匹配*
    + PUT为新建
        + id字段忽略，全字符串回传，options选项需要check
    + DELETE为删除
        + api/equipment/:id

+ api/sourcecompany [source公司数据]
+ api/sinkcompany [sink公司数据]
+ api/logistic [物流数据]
+ api/buyorder [采购单数据]
+ api/saleorder [销售单数据]

#### log数据
+ GET api/log/equipment or api/equipment/log
    + 需要权限
    + 可酌情只返回最新部分数据
+ 其他操作


#### 登录相关
+ api/user [用户数据]
    + GET
    + 需要兼容api/user/:id的操作
        + *权限check留意*
    + 增加api/user/me
        + 返回结果与相应的api/user/myid一致
+ api/action/login
+ api/action/register
+ api/auth






#####api查看
+ 按照项目整体的方案启动 ` npm run dev ` ，
经由express 与mock 来对外提供api服务。
+ 所有api相关内容位于api路径下
+ 如需屏蔽api服务，在 build/dev-server.js中注释掉 ` mockConfig(app) `一句再重启即可

#####todo
+ 目前未找到如何从express里顺利获取req.body的方法，express 4.1x中间api变更，有点头疼，后置。
