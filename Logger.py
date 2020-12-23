#!/usr/bin/python
# -*- coding: UTF-8 -*-
def make_print_to_file(path='./'):
    '''
    path， it is a path for save your log about fuction print
    example:
    use  make_print_to_file()   and the   all the information of funtion print , will be write in to a log file
    :return:
    '''
    import sys
    import os
    import sys
    import datetime

    class Logger(object):
        def __init__(self, filename="Default.log", path="./"):
            self.terminal = sys.stdout
            self.log = open(os.path.join(path, filename), "a", encoding='utf8',)

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

        def flush(self):
            pass




    fileName = datetime.datetime.now().strftime('day'+'%Y_%m_%d')
    sys.stdout = Logger(fileName + '.log', path=path)

    #############################################################
    # 这里输出之后的所有的输出的print 内容即将写入日志
    #############################################################
    print(fileName.center(60,'*'))



if __name__ == '__main__':


    make_print_to_file(path='./')

    #############################################################
    # 这里输出之后的所有的输出的print 内容即将写入日志
    #############################################################
    print("1234124")
    print("--")
    print(":;;;")
    print("")
    print("阿斯顿发11111111111111111")
    print("zzzzz")