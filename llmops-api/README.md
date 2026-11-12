# python -m venv venv(环境名)

# 当前项目下 执行  venv\Scripts\activate  以激活当前的项目环境 （注意：这里是反斜杠）

# python -m pip install 包名    虚拟环境安装包到了系统环境下，可用此执行

# 「 依赖包检查导出列表
#  pip install --no-deps pipreqs
#  pip install yarg==0.1.9 docopt==0.6.2
#  pipreqs . --encoding=utf8  --ignore venv --force  # 生成统计当前项目依赖的包存入requirements.txt
#  pip install -r requestment.txt 自动读取并安装依赖
# 」
# 


## postgres
# postgres开启服务
#  D:\Application\Development\PostgreSQL\1842\bin>  pg_ctl.exe start -D  "D:\Application\Development\PostgreSQL\1842\data"
# postgres关闭服务
# D:\Application\Development\PostgreSQL\1842\bin>  pg_ctl.exe stop -D  "D:\Application\Development\PostgreSQL\1842\data"

# bat  启动服务， 关闭服务把参数start 改为 stop 即可
# [
# @echo off
# set PG_PATH="D:\Application\Development\PostgreSQL\1842\bin"
# set PG_DATA="D:\Application\Development\PostgreSQL\1842\data"

# echo  Starting  PostgreSQL...
# %PG_PATH%\pg_ctl.exe start -D %PG_DATA%
# echo   PostgreSQL  started.
# ]