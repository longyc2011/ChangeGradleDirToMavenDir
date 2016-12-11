# ChangeGradleDirToMavenDir
  将gradle的缓存目录结构，转换为maven的缓存目录结构
由于公司的网络安全限制，无法直接通过软件访问公网的maven 仓库中心，所以最近在弄本地搭建maven私有仓库。

##maven私库的搭建
使用Nexus 2.17搭建，傻瓜式的，直接启动脚本，就可以了，网上例子很多，这里不赘述。有一句话我一直没有看懂，就是使用maven代理的时候，会缓存通过私有仓库下载的jar包等文件，我的一直没有弄成功，所以如果有知道的请回复一下，多谢。
 
##jar包上私有仓库的结果方案
###将完整的 maven缓存目录中的结构拷贝到目录：
```
nexus-2.14.1-01-bundle\sonatype-work\nexus\storage\thirdparty
```
 就可以了

###将gradle缓存目录中的结构拷贝到上述目录
遇到了一个问题，既然无法访问公共网络，那么，只能在外网下载好jar包，然后，发送会内网，然后放到搭建好的maven仓库中，让开发人员使用。 对于Android 开发，使用gradle进行构建，背后还是使用maven的方式来管理和使用jar包，但是，查看gradle的jar包缓存目录~/.gradle，可以发现，目录结构与maven并不完全一致，让人头疼，不能直接拿来使用。

gradle 目录结构如下所示
```
\.gradle\caches\modules-2\files-2.1\org.hamcrest\hamcrest-core\1.3\1dc37250fbc78e23a65a67fbbaf71d2e9cbc3c0b\hamcrest-core-1.3-sources.jar
```

 maven 目录结构如下所示：
```
org\hamcrest\hamcrest-core\1.3\hamcrest-core-1.3-sources.jar
```
 
 可以看出，gradle的目录中，一些目录是直接带"."的，同时还有一串随机字符串组合。经过分析，使用python写了一个脚本

```
https://github.com/longyc2011/ChangeGradleDirToMavenDir
```

 使用方法很简单，将脚本拷贝到
 ```
 \.gradle\caches\modules-2\files-2.1
 ```
 目录，然后在cmd中，切换到该目录下，执行脚本
```
>python FileOpration.py
```
 最后在当前目录下生成一个out目录，这个目录下就是转换好的maven目录。我们就可以将out目录下的结构直接拷贝到nexus的storage目录下，如以上所示。

###这个目前只是我自己的一种实现方式，应该有更简单的方式，如果哪位大神无意间看到了我的解决方案，如果他有跟好的方案，请分享一下，多谢

 
 

 
