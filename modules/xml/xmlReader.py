#!/usr/bin/env python3.6
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
        elif type(item[key]) == list:
            for x in range(0, len(item[key])):
                xmlIterator(item[key][x])
        else:
            foundList.append(item[key])
    return foundList

def searchInXml(xml, search_pattern, foundList=[]):
    for item in xml:
        if search_pattern in str(item):
            return item

def xmlReader(xml_folder):
    for files in os.listdir(xml_folder):            # iterate through all xml files in given folder
        xml_file = xml_folder + files               # file path + file name
        with open(xml_file) as xml:                 # open xml file as xml
            xml_dict = xml2Dict(xml)                # convert xml <-> dictionary
            search = xmlIterator(xml_dict)
            print(searchInXml(search, 'SAP@'))
            input('######### ENTER #########')

def main():
    xml_folder = '/Users/f1b0/Workspace/AssuranceTriangle/xml_folder/'
    xmlReader(xml_folder)

if __name__ == '__main__':
    main()