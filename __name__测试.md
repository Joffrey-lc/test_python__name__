# 测试if \__name\_\_ == ' \_\_main\_\_'

## 说明

python.py文件运行的方式有两种，一种是脚本运行，一种被import 导入运行。

## 脚本运行文件supNet

直接运行supNet结果如下

![image-20201207172509313](https://mymarkdown-pic.oss-cn-chengdu.aliyuncs.com/img/image-20201207172509313.png)

结果说明直接运行脚本，\_\_name\_\_ == '\_\_main\_\_' 恒成立，所以运行主程序之后运行了方法test()



## import 运行

![image-20201207172537786](https://mymarkdown-pic.oss-cn-chengdu.aliyuncs.com/img/image-20201207172537786.png) 

import执行会执行主程序+import后调用的方法。此处调用了main()。其\_\_name\_\_属性为import的文件名。



## 结论

无论脚本运行还是import，都会先执行主程序。（要import所有可能的库，所以这是合理的）。然后脚本运行\__name\_\_  为'\_\_main\_\_'；import的\_\_name\_\_为文件名。