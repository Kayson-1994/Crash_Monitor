# Crash_Monitor
Crash reports multiple devices collected and reported

> * 验证创建一个实例，这个实例，该实例提供start_service、stop_service对外接口
```python
g_obj = None


def start_service():
    global g_obj
    g_obj = Monitor()
    print("g_obj is {0}".format(g_obj))
    g_obj.start_monitor()


def stop_service():
    global g_obj
    if g_obj is not None:
        g_obj.stop_monitor()
```

> * 解析：
>> 调用start_service来创建一个Monitor()类的实例 \
>> 调用stop_service来销毁改实例
>> 其中实例是全局的变量

> * 疑惑：
>> 问题：别的模块或文件在调用这两个方法的时候，是否会影响？？\
>> 答案：不会

>> 问题：因为创建一个实例就开启了线程，调用stop就停止线程，那么我多次调用start也就是多吃创建实例，再最后调用stop是所有的实例的线程都被停止还是只是最后一个被销毁了？？？\
>> 答案：最后一个被销毁，其余的线程依旧在循环处理