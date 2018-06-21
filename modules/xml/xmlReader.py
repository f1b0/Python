#!/usr/bin/env python3.6
# -*- encoding: utf-8; py-indent-offset: 2 -*-

import os
import xmltodict
import json


def xml2_dict(xml):
    doc = xmltodict.parse(xml.read())
    j_dict = json.loads(json.dumps(doc))
    return j_dict


def xml_iterator(item, found_list=list()):
    for key in item.keys():
        if type(item[key]) == dict:
            xml_iterator(item[key])
        elif type(item[key]) == list:
            for x in range(0, len(item[key])):
                xml_iterator(item[key][x])
        else:
            found_list.append(item[key])
    return found_list


def search_in_xml(xml, search_pattern):
    for item in xml:
        if search_pattern in str(item):
            return item


def xml_reader(xml_folder):
    for files in os.listdir(xml_folder):            # iterate through all xml files in given folder
        xml_file = xml_folder + files               # file path + file name
        with open(xml_file) as xml:                 # open xml file as xml
            xml_dict = xml2_dict(xml)               # convert xml <-> dictionary
            search = xml_iterator(xml_dict)
            print(search_in_xml(search, 'SOME_SEARCH_PATTER'))
            input('######### ENTER #########')


def main():
    xml_folder = 'XML_FOLDER'
    xml_reader(xml_folder)


if __name__ == '__main__':
    main()