#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

header = """
<html>
<head>
    <title>google</title>
    <style >
    .icon {
        display: inline-block;
        width: 95px;
        height: 35px;
        border: 1px solid #eee;
        margin: 1px;
    }
    </style>
</head>
<body>
    <h1>Google 全球 IP 地址库</h1>
"""
footer = """
</body>
</html>
"""

def render(host):
    return """<a href="http://%s" target="_blank"><div class="icon" style="background: url('http://%s/images/nav_logo195.png') 0px -42px"></div></a>""" %(host, host)

def main(src, dest):
    data = open(src, "r").read()
    des = open(dest, "w+")
    des.write(header)

    m = re.findall(r">(\d+\.\d+\.\d+\.\d+)<", data) # m is a list
    for item in m:
        #print render(item)
        des.write(render(item)+"\n")
    des.write(footer)

if __name__ == '__main__':
    main('./README.md', './index.html')
