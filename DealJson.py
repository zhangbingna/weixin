#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import os
from time import sleep


class DealJson(object):
    def __init__(self, json_path):
        self.path = json_path

    def get_doc_id(self):
        doc_id_list = []
        f = open(self.path, encoding='utf-8')
        json_list = f.readlines()
        for read in json_list:
            if read[0] != "{":
                print("json文件格式错误")
                break
            else:
                json_text = json.loads(read)
                try:
                    itemtype = json_text["item_type"]
                    docid = json_text["docs"][0]["doc_item"]["doc_item_common"]["docid"]
                    vid = json_text["docs"][0]["doc_item"]["doc_item_common"]["vid"]
                    if itemtype == 4:
                        doc_id_list.append("vid:" + str(docid))
                    else:
                        doc_id_list.append(str(docid))
                except:
                    docid = ""
                    doc_id_list.append(docid)
                    print("json格式错误，找不到docid")
        print("docid列表", doc_id_list)
        return doc_id_list

    def get_line_json(self, value, new_path, line):
        f = open(self.path, encoding='utf-8')
        json_list = f.readlines()
        text = json_list[line]
        json_text = json.loads(text)
        for j in range(0, 4, 4):
            json_text["title"] = value[j]
            json_text["media_name"] = value[j+1]
            json_text["url"] = value[j+2]
            json_text["pic_url"] = value[j+3]
            with open(new_path, "a", encoding='utf-8') as fi:
                if os.path.getsize(new_path) > 0:
                    fi.write('\n')
                json.dump(json_text, fi, ensure_ascii=False)
            fi.close()
            print("标题《%s》写入成功" % value[j])
        f.close()

    def write(self, new_path, line):
        f = open(self.path, encoding='utf-8')
        json_list = f.readlines()
        text = json_list[line]
        with open(new_path, "a", encoding='utf-8') as fi:
            if os.path.getsize(new_path) > 0:
                fi.write('\n')
            fi.write(text)
        print("第%d行写入" % line+1)
        fi.close()
        f.close()


if __name__ == "__main__":
    filepath = "json_demo"
    data = DealJson(filepath)
    data.get_doc_id()
    data.get_line_json(["123", "456", "789", "abc"], "json_demo_1", 1)
