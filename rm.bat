@echo off
setlocal enabledelayedexpansion

rem 设置要删除的文件名
set "file_name=*.*"
set "exclude_file=__init__.py"

rem 遍历当前目录及其子目录下的所有migrations目录
for /r %%d in (migrations) do (
    rem 判断是否为目录
    if exist "%%d\" (
        rem 切换到目录
        pushd "%%d"
        rem 遍历目录下的所有文件
        for %%f in (%file_name%) do (
            rem 判断是否为要排除的文件
            if not "%%~nxf"=="%exclude_file%" (
                rem 删除文件
                del "%%f"
            )
        )
        rem 切换回上级目录
        popd
    )
)