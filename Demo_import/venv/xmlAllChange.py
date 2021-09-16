#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET
import os
import xml.dom.minidom
import urllib.request
# import os
# import xml.dom.minidom
# import xml.etree.ElementTree

#url = 'C:/Users/butel/Desktop/xml/'  # 你的xml文件的路經，注意最后一定要有'/'
tree = ET.ElementTree(file='strings.xml')
root = tree.getroot()
for elem in tree.iter(tag='string'):
    elem.text=str(1)
    tree.write("string.xml")

#root.text
# for child_of_root in root.text:
#     print(child_of_root)
    #print(child_of_root.tag, child_of_root)
    # sub1 = child_of_root.find('string')  # 找到filename标签，
    # sub1.text = 1  # 修改标签内容
# xmldata = '<resources>' + urllib.request.urlopen(url).read() + '</resources>'
# tree = ElementTree.fromstring(xmldata)
# codigo = tree.find('codigo').text
#
# print(codigo)
# for xmlfile in os.listdir(xmldir):
#     xmlname = os.path.splitext(xmlfile)[0]
#
#     # 读取 xml 文件
#     dom = xml.dom.minidom.parse(os.path.join(xmldir, xmlfile))
#     print(dom)
#     root = dom.documentElement
#
#     # 获取标签对的名字，并为其赋一个新值
#     root.getElementsByTagName('filename')[0].firstChild.data = xmlname + '.jpg'
#     root.getElementsByTagName('path')[0].firstChild.data = \
#         '/home/dulingwen/Pictures/road/' + xmlname + '.jpg'
#     root.getElementsByTagName('width')[0].firstChild.data = '2084'
#     root.getElementsByTagName('height')[0].firstChild.data = '2084'
#
#     # 修改并保存文件
#     xml_specific = xmldir + xmlfile
#     with open(xml_specific, 'w') as fh:
#         dom.writexml(fh)
# def change_xml(xml_path):
#     #upath = unicode(xml_path, 'utf-8')
#
#     filelist = os.listdir(xml_path)
#     print(filelist)
#     # 打开xml文档
#     for xmlfile in filelist:
#         #dom = xml.dom.minidom.parse(os.path.join(xml_path, xmlFile))
#         #print(dom)
#         doc = ET.parse(xml_path + xmlfile)
#         print(doc)
#         root = doc.getroot()
#         print(root)
#         sub1 = root.find('name')  # 找到filename标签，
#         sub1.text = 1  # 修改标签内容
#
#         doc.write(xml_path + xmlfile)  # 保存修改
#
#
# change_xml(r'C:/Users/butel/Desktop/xml/')