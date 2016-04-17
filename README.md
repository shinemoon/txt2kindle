# txt2kindle

To generate Kindle File (mobi) from txt file based on defined format.

Mainly focus on Chinese Novel

Usage:

*Better to add this script's path into sys environmental paramenter for convienience.*

python PathtoScript/txt2kindle.py **pathToRawTxtFile** **NovelName** *NovelAuthor*

Then, one mobi file will be generated in same folder where you execute this command.

Note:

- For chapter handling, by default using `h2re = re.compile(r'\s*第.*章\s+.*')`, please change in need in txt2kindle.py file
- Currenlty only check 1 layer chapter, and later MIGHT extend to 1 higher layer , e.g. Vol, etc.

## Req
- Python 2.7 installed
- kindlegen installed, and can be called in cmd with 'kindlegen'(or to modify txt2kindle.py to assign specified path to kindlegen)
- Tested in Unix/Linux/OSX/Windows
- Please replace the font for 'normal' and 'title' by your self based on your flavor.

# txt2kindle 说明

用于从单一的全文txt小说生成Kindle阅读的mobi文件.

主要适用于中文网络小说，仅在Kindle Paperwhite上测试过实际效果。

用法：

*建议将本脚本路径加入系统环境变量，以便使用*

python 脚本路径/txt2kindle.py **Txt文件路径** **小说名** *作者名*

执行后，mobi文件会在你执行命令的目录生成。

注意:

- 当前对于目录章节的辨识是用`h2re = re.compile(r'\s*第.*章\s+.*')`,如果有修改需求请自行修改txt2kindle.py
- 目前仅支持一级章节识别，以后可能会多扩展到上层

## 需求
- Python 2.7
- 安装kindlegen , 可以通过'kindlegen'直接调用（否则，请修改txt2kindle.py修改kindlegen为正确路径）
- Unix/Linux/OSX/Windows 测试后均可支持
- 请自行准备并替换normal和title对应的正文和标题字体


