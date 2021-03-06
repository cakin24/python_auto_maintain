#coding=utf-8
import os
import sys
if os.getuid() == 0:
    pass
else:
    print '当前用户不是root用户，请以root用户执行脚本'
    sys.exit(1)

version = raw_input('请输入你想安装的python版本（2.7/3.6）')
if version == '2.7':
    url = 'https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz'
elif version == '3.6':
    url = 'https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz'
else:
    print '您输入的版本号有误，请输入输入2.7或3.6'
    sys.exit(1)

cmd = 'wget '+url
res = os.system(cmd)
if res != 0:
    print '下载源码包失败，请检查网络'
    sys.exit(1)

if version == '2.7':
    package_name = 'Python-2.7.12'

else:
    package_name = 'Python-3.6.8'
cmd = 'tar xf ' + package_name+ '.tgz'
res = os.system(cmd)
if res != 0:
    os.system('rm '+package_name+'.tgz')
    print '解压源码包失败，请重新运行这个脚本下载源码'
    sys.exit(1)

cmd = 'cd '+ package_name+ ' && ./configure --prefix=/usr/local/python && make && make install'
res = os.system(cmd)
if res !=0:
    print '编译python源码失败，请检查是否缺少依赖库'
    sys.exit(1)