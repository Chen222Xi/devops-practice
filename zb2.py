import os
import time

print('starting')

ret_val = os.fork()  # 创建子进程

if ret_val:
    # 父进程分支
    print('in parent')

    # 等待任意子进程结束（-1 表示任意子进程，1 表示挂起父进程等待）
    result = os.waitpid(-1, 1)  # 不挂起（非阻塞模式）

    print(result)  # 打印返回的 pid 和状态
    time.sleep(10)
    print('parent done')

else:
    # 子进程分支
    print('in child')
    time.sleep(5)
    print('child done')
