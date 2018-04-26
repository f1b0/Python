#!/usr/bin/env python2.7
# -*- encoding: utf-8; py-indent-offset: 2 -*-

import os
import xmltodict
import json

def xml2Dict(xml):
    doc = xmltodict.parse(xml.read())
    jdict = json.loads(json.dumps(doc))
    return jdict

def xmlIterator(item, foundList=[]):
    for key in item.keys():
        if type(item[key]) == dict:
            xmlIterator(item[key])
        else:
            foundList.append(item[key])
    return foundList

def searchInXml(xml, search_pattern='INC0', foundList=[]):
    for item in xml:
        if search_pattern in str(item):
            if type(item) == list:
                searchInXml(item[0])
            else:
                print(item)

def xmlReader(xml_folder):
    for files in os.listdir(xml_folder):
        f = xml_folder + files
        with open(f) as fd:
            xml_dict = xml2Dict(fd)
            search = xmlIterator(xml_dict)
            searchInXml(search)
            input('######### ENTER #########')

def main():
    xml_folder = '/Users/f1b0/Workspace/AssuranceTriangle/xml_folder'
    xmlReader(xml_folder)

if __name__ == '__main__':
    main()