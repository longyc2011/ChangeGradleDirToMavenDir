#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 创建时间 2016-12-11
import os
import shutil
import string

__author__ = "Stevens Sun"


def list_all_sub_files(directory):
    """
    列出指定目录下所有的文件。
    :param directory: 指定的目录
    :return: 返回指定目录下所有的文件相对指定目录的全路径
    """
    sub_files_list = []
    if os.path.isfile(directory):
        print directory
        dir_array = os.path.split(directory)
        file_full_name = str(dir_array[1])
        if not directory.startswith("./.") and not file_full_name.startswith("."):
            sub_files_list.append(directory)
    else:
        sub_path_list = os.listdir(directory)
        for files in sub_path_list:
            sub_path = os.path.join(directory, files)
            sub_files_list.extend(list_all_sub_files(sub_path))

    return sub_files_list


def make_dirs_and_copy_file_to_dest_dirctory(src_file_full_name):
    """
    根据源文件目录，创建目的文件目录，并拷贝源文件到，目的文件目录中，完成该操作
    :param src_file_full_name: 源文件，将要拷贝的文件全路径
    :return: null
    """
    if str(src_file_full_name).startswith("./."):
        print "this is a illeagle directory %s" % (src_file_full_name)
        return

    src_path_array = os.path.split(src_file_full_name)
    print src_path_array

    src_path = src_path_array[0]
    src_file_name = src_path_array[1]

    src_path_list = src_path.split(os.path.sep)

    if len(src_path_list) <= 1:
        return

    dest_path_list = []

    index = len(src_path_list) - 1
    src_path_list.pop(index)
    version_name = src_path_list.pop(index - 1)
    src_path_list.remove(src_path_list[0])

    print src_path_list

    dest_path_list.append("out")
    for path in src_path_list:
        if string.find(path, ".") != -1:
            print path
            dest_path_list.extend(path.split("."))
            pass
        else:
            dest_path_list.append(path)
    dest_path_list.append(version_name)
    print dest_path_list

    dest_dir = reduce(os.path.join, dest_path_list)

    print dest_dir

    if not os.path.exists(dest_dir):
        print os.makedirs(dest_dir)

    dest_file_full_name = os.path.join(dest_dir, src_file_name)

    print 'cp %s %s' % (src_file_full_name, dest_file_full_name)
    if os.path.exists(src_file_full_name) and not os.path.exists(dest_file_full_name):
        print 'cp %s %s' % (src_path, dest_file_full_name)
        shutil.copy(src_file_full_name, dest_file_full_name)


def change_gradle_dirs_to_maven_dirs():
    """
    将gradle的缓存目录结构，转换为maven的缓存目录结构
    :return: null
    """
    print "current directory : " + os.getcwd()
    print "list all sub files start:"
    sub_files = list_all_sub_files(".")
    print sub_files
    print '---- result -----'
    map(make_dirs_and_copy_file_to_dest_dirctory, sub_files)


if __name__ == '__main__':
    change_gradle_dirs_to_maven_dirs()
