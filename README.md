# Social-ly
A social calendar project in Software Engineering class

## A brief introduction
We are a team from Tsinghua University Software Engineering class. And this project is the group work product which we call Social历.  
This project, in the form of calendar, aims to help people manage their time, invite others to insert activities in their calendar and collect team schedule. 

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For detailed explanation on how things work, checkout the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

---

## 需求文档

### 0 说明

因为我们组采用的是增量模型，所以在元代软件的实现中，我们先考虑实现日历的基本功能，包括用户的登录、查看日程、新增日程、删除与编辑日程。另外，我们的用户之间不存在区别，所有的用户都可以实现相同的功能。

---

### 1 用户故事
#### 1.1 故事一：用户登录
故事序号：	1
故事标题：	用户登录
用户角色：普通用户
用户特征：登录app，进入主页
用户利益：进入app直接查看最近活动与月历

##### 1.1.1 场景1：已注册用户登录
场景标题：已注册用户登录
上下文：用户已注册过小程序
事件	
1. 用户进入小程序
2. 显示小程序主页，主页含有月历与最近日程安排

结果：用户日程数据从数据库存入本地缓存，用户进入小程序主页

##### 1.1.2 场景2：未注册用户登录
场景标题：未注册用户登录
上下文：用户未注册过小程序
事件	
1. 用户进入小程序
2. 用户点击注册对话框“确定”按钮
3. 显示小程序主页，主页含有月历（最近日程安排为空）

结果：数据库内建立该用户账户，用户进入小程序主页


#### 1.2 故事二：用户新增日程
故事序号：2
故事标题：用户新增日程
用户角色：普通用户
用户特征：希望能在制定时段添加日程，编辑时间、内容等要素
用户利益：将日程添加到指定时段，能设置时间、内容、地点
事件	
1. 用户点击左上按键，打开侧栏
2. 用户点击侧栏中“添加日程”
3. 用户选择时间，选填地点、内容
4. 用户点击“确定”按钮

结果：用户成功添加新日程；新日程数据传入数据库；跳转到新增日程该日页面，且新日程出现在相应时间；内容、地点显示在新日程中

#### 1.3 故事三：用户查看已有日程
故事序号：3
故事标题：用户查看已有日程
用户角色：普通用户
用户特征：希望查看已有日程安排，并查看详细信息
用户利益：进入app直接查看最近活动与月历
事件	
1. 用户点击“日”按钮
2. 点击想要查看的日程

结果：用户查看已有日程；显示日程信息页面

#### 1.4 故事四：用户编辑已有日程
故事序号：4
故事标题：用户编辑已有日程
用户角色：普通用户
用户特征：希望能更改或删除已有日程
用户利益：能更改或删除已有日程

##### 1.4.1 场景1：更改日程信息
场景标题：更改日程信息
上下文：用户已添加日程
事件	
1. 用户点击“日”按钮
2. 点击想要更改的日程
3. 点击“编辑”按钮
4. 更改日程时间/内容/地点
5. 点击“确认”按钮

结果：用户更改已有日程信息；日程数据更改传入数据库；跳转到更改的日程的日期页面，且日程出现在相应时间；内容、地点显示在新日程中

##### 1.4.2 场景2：删除日程
场景标题：删除日程
上下文：用户已添加日程
事件	
1. 用户点击“日”按钮
2. 点击想要删除的日程
3. 点击“删除”按钮（弹出确认窗口）
4. 点击“确认”按钮

结果：用户删除已有日程；日程数据更改传入数据库；跳转到月历页面

