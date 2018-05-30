Title: Linux 趁手工具之剪贴板系列
Category: Learning
Tags: Linux
Slug: linux_clipboard
Date: Thu Mar 17 15:01:18 CST 2016

懂 Linux 的程序员朋友很多，但是把 Linux 当作日常桌面系统用的还是不多。我自己的小破笔记本上，350G 的机械硬盘跑着 Win7， 120G 的MSATA SSD 跑过Ubuntu，OpenSuse，Kali(基于 Debian )，现在跑着  Debian 8， 开机秒速，不比 Win10 的平板或是Chromebook 慢，且更功能更强大。

我个人也并没有把 Linux 完全取代 Windows 来用，毕竟很多时候还要用到微软的 Office 等工具，或者有些网站至今为止还是“IE6 Only”。但是日常大部分工作，Linux 已经完全可以代替 Windows；在开发方面，如果你是一个 Unix/Linux 平台的开发者，当然是直接使用 Linux 更好啊，那种在 Windows 上用 UE 写代码，用 SourceInsight 浏览代码，scp 到 Linux 上编译代码的方式既不方便也无效率。

我打算陆续总结和分享下 Linux 下好用的工具，这些工具要么是在 Windows 上 power tools 的同功能替代，要么是更加好用和有趣。我不打算写篇幅很多，很系统的 Linux 工具介绍，只是兴之所至，在一个小的分类或相关标签下做简短的介绍。日后有新的发现也许会在历史文章上做些更新。

另外，我推荐的工具基本是基于Debian，GNOME。

## Linux 剪贴板原理
对 Linux 剪贴板原理感兴趣的朋友可以参看这篇文章 [Linux 剪贴板原理](http://blog.51cto.com/laokaddk/945304) ，其中关于 “selection” 的概念，在之后介绍的一个工具中会用到。

### 终端与剪贴板的通道

#### xclip

xclip命令建立了终端和剪切板之间通道，可以用命令的方式将终端输出或文件的内容保存到剪切板中，也可以将剪切板的内容输出到终端或文件
不加选项时只在保存在X PRIMARY（终端剪贴板），加上选项 -selection c后保存在 X CLIPBOARD（外部程序剪贴板）。
参考：http://www.debian-administration.org/articles/565
安装 sudo apt-get xclip

__终端输出保存到剪切板中__
ls -al | xclip
此时ls -al的输出内容已经保存在剪切板中了，此时xclip -o可以看到剪切板的内容。
但此时还不可以粘贴到终端以外的程序中，此时需要用到： xclip -selection c
ls -al | xclip -selection c

__文件内容复制到剪切板中__
xclip /etc/apt/sources.list
xclip -selection c /etc/apt/sources.list

__剪切板内容输出到终端__
xclip -o
xclip -selection c -o

__剪切板内容输出到文件__
xclip -o > ~/test.txt
xclip -selection c -o > ~/test.txt

#### 剪贴板管理器

如果你在 Windows 上用过 clipx 之类的软件，一定会离不开，如果你从来没用过，建议看看这篇：https://xbeta.info/clipx-clcl-ditto.htm

简言之，系统自带的剪贴板功能只能保存一条记录，下次 “Ctrl + C” 就会把这条记录冲掉，这类软件能够保存一定数量剪贴记录，为你在进行多次 copy-paste 操作时不用担心记录冲掉，随时选择粘贴剪贴板历史记录里的内容。

Windows 平台的此类软件，上面的链接里有很好的综合比较。Linux 下此类软件也不少，我仅推荐两个我使用过的基于GNOME的：

- Parcellite
- diodon

这两个软件都很轻量，都可以apt-get install 来安装，Ubuntu 和 Debian 的源中都有。

使用都很简单，修改下呼出剪贴版历史的热键就可以用起来。但 diodon 在我的系统中，热键要按两次才能呼出不知道为何。

而 Parcellite 默认没有启用 AutoPaste，就是点选历史记录后，并没有直接粘贴到光标焦点位置上，还需要用户自己“Ctrl + V” 或右键菜单粘贴，这很不方便。配置里勾选 AutoPaste 后，提示必须要先安装 xdotool 才能启用。apt-get install xdotool 后就可以启用，用起来就方便了。

![](http://oc3b8hnrg.bkt.clouddn.com/2016-03-17-221500-%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)
