Title: 浅谈Python生成器的妙处
Date: 2018-11-28
Modified: 2018-11-28
Category: Learning
Tags: Python
Slug: 201811281543
Author: Yushin

大多数使用Python的同学应该都了解生成器语法，不知道大家使用场合是什么，我想结合自己的一点粗浅经验谈谈它给我的代码带来的好处。

### 1. 不浪费内存的的逻辑分层

   一个大家熟悉的例子是python2 的xrange 和 python3 的range函数，生成器的“惰性求值”特性使得不用开辟一个list，而只是在迭代中“现取现用”。

   我在使用中更有体验的经历是：写一个特殊格式的数据文件的parser，这种文件按特定大小的块增长，而每一条数据记录，存储在一条文件块的链表中。解析一条数据记录的逻辑是：现按照链表顺序拼合出连续缓存，再再缓存基础上解析数据记录，这样逻辑上是清晰的，但要再代码上照写逻辑，就是要单拿出一块很大的buffer，或者说拼合一个很大的列表，浪费空间，有效率的方法是，读到一个块，就可以解析此块上的数据记录，不过这样写，块的解析和记录的解析掺和到一个函数中，看上去很混乱（实际上原本有个C实现就是这样）。好的方法是，在解析block层面的函数ReadBlocks() 中 yield block，在解析数据记录的函数ReadRecs()中一个迭代中 `for block in ReadBlocks():`处理Record的解析就好。我写这个工具中文件解析的实际代码在 https://github.com/lostsummer/emdfparse/blob/master/emdfparse/datafile.py



### 2. 递归结构中减少全局变量

   比方某一类算法问题需要你对图作深度或广度遍历，得出所有符合条件的路径，这不避免的需要一个全局或者闭包的List存储这些路径，而有了 yield 和 yield from，大可不用这个全局变量，写出的函数更有“状态机”的意味。这里有我为两个算法题写的代码 https://github.com/lostsummer/fun 。一个是连接奶牛的路径问题，一个是组合问题，对这类问题，我很愿意把 yield from 当作一个范式来用，代码行数更少，思路更简明。

### 3. 协程范式

   早在2009年，David Beazley 就写了 A Curious Course on Coroutines and Concurrency （http://www.dabeaz.com/coroutines/）我觉得读透所有技巧和思想对现在的写python程序也是很有帮助，尤其是理解复杂的asyncio。我觉得，不管是 `yield` 还是 `x = yield`都可以算是协程，了解golang的同学会说，这不就是只读channel和只写channel吗？但是，单一个yield还构不成协程管理的全部，单靠协程，asyncio，还构不成完整的并发模型。在CSP、actor都整合到GoLang和ErLang语言层面的时代，Py界还在犹豫到底拥抱asyncio还是愉快的用着gevent。我觉得，还是先用go吧。但是作为py异步编程的未来，asyncio值得研究，即使不学asyncio，那些使用协程解决问题的思路，也能给我们很多新的启发。关于py的协程，有很多可说，来日再开篇幅。

