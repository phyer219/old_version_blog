---
title: 说明
date: 2021-09-25
---

#  [html](./anime.html)

# 前言

今天是 2021.9.25.

就在昨天有一批动漫又消失了, 其中就有 Re0. 前些天发现 qq 音乐里有些专辑会莫名少一首歌. 还有各种扭曲的翻译, 大片删节及马赛克. 因此, 看正版没有一丝安全感.

校园网每月只有 25G 的流量, 实在是少得可怜. 超出之后 0.8元/GB, 有点贵呀! 但宿舍里的手机流量实在太慢, 根本没法看视频.

综上, 今后的主要的影音来源是各种ipv6 的 pt 网站, 然后在办公室用 emby 做服务器, 这样在校内就可以免流听歌看视频. 想有一起用的可以联系本人.

只有自己掌握原始数据才是最安全的.

以后大概再也不会给国内的视频音乐软件充会员了.

# 用 SQLite 记录

看过的动漫就记录在一个单个文件的 SQLite 的数据库里, 初始时可以用下面的 code 创建一个 table
```python
import sqlite3

conn = sqlite3.connect('hello.db')

print('open datebase yes!')

c = conn.cursor()
c.execute('''CREATE TABLE ANIME
            (MY_ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             MY_RANK        INT     NOT NULL,
             NAME_JP        TEXT,
             MY_COMMENT     TEXT,
             BGM_ID         INT,
             IMDB_ID        INT,
             FINISH_TIME    TEXT,
             WATCHT_TIME_START TEXT,
             WATCHT_TIME_END   TEXT
            );''')
print("Table created successfully")
conn.commit()
conn.close()
```

动漫表 `ANIME` 有如下字段

- `MY_ID` : 每个条目的编号, 由六位数字组成, 第一位代表评级, 后五位代表编号. 如 `100000` 为最高评级零号作品.
- `NAME` :  名字
- `MY_RANK` : 星级, 一位数字. 5 为最高, 1 为最低.
- `NAME_JP` : 日文名字
- `MY_COMMENT` :评论和感想
- `BGM_ID` : 在 bgm.tv 上的 ID
- `IMDB_ID` : IMDB 上的 ID
- `FINISH_TIME` :完结时间
- `WATCH_TIME_START` :何时开始观看
- `WATCH_TIME_END` :何时观看结束

# SQLiteStudio

添加记录可以用 SQLiteStudio 可视化添加, 之后导出 html 格式. SQLiteStudio下载地址:  https://sqlitestudio.pl/

# html 


导出的数据库: [html](./anime.html)

