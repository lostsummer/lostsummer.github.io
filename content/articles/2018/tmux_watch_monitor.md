Title: 使用tmux和watch组合一个redis监控面板
Date: 2018-10-22
Modified: 2018-10-22
Category: Learning
Tags:
Slug: 201810221843
Author: Yushin

对于开发来说，有些特定服务器数据的实时监控可以不必大而全，比方阮一峰 [WebSocket 教程](http://www.ruanyifeng.com/blog/2017/05/websocket.html)中提到的使用Websocketd + 简单脚本实现的对服务器性能指标的监控服务程序。而我现在自己有个需求更加简单，只要验证redis中几个key的数据是否在不断更新。我既不想自己不断刷新桌面redis客户端，也不想不断在cli里敲回车，实际上借助几个命令也可以非常简单地满足：

- redis-cli：输出指定key的值
- watch：连续调用指定面命，并把输出刷新到屏幕上，类似top、tailf那样的效果，它是独占终端屏幕的
- tmux：会话保持、分屏。有了tmux就可以在一个平面查看多个watch命令的实时输出

于是有了下面的脚本：

```shell
HOST=127.0.0.1
PORT=6379
DB=1

R_CONN="redis-cli -h $HOST -p $PORT -n $DB"
R_MIN1_CMD="lrange min1:0600000 -1 -1"
R_CMINFO_CMD="get codemap:info"
R_CMLEN_CMD="hlen codemap:codes"
R_QUOTE_CMD="get quote:0600000"

WATCH_MIN1_CMD="watch \"$R_CONN $R_MIN1_CMD|python -m json.tool\""
WATCH_CMINFO_CMD="watch \"$R_CONN $R_CMINFO_CMD\""
WATCH_CMLEN_CMD="watch \"$R_CONN $R_CMLEN_CMD\""
WATCH_QUOTE_CMD="watch \"$R_CONN $R_QUOTE_CMD|python -m json.tool|grep time\""

SESS=monitor

tmux a -t $SESS
if [ $? -ne 0 ]
then
    tmux new-session -s $SESS -d "$WATCH_MIN1_CMD" \; \
    split-window -h -d "$WATCH_CMINFO_CMD" \; \
    split-window  "$WATCH_CMLEN_CMD" \; \
    select-pane -R \; \
    split-window  "$WATCH_QUOTE_CMD" \; \
    attach
fi
```

需要说明的是：

- watch 默认刷新的频率是2s，这个可以通过 -n 指定，watch 还有个 -d 选项会高亮刷新后的差异部分
- python -m json.tool 会把压缩的json格式化成美观可读的样式
- tmux 大家可能已经熟悉分屏操作的快捷键，这些操作其实在启动session时可以通过一连串的命令定义，这些命令之间需要`' \; '`分隔

脚本运行效果是这样的：

![mon](http://140.143.250.15/wiki-img/tmux_mon.png)
