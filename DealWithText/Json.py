import json
import os


class Json(object):
    def __init__(self, json_path):
        self.path = json_path

    def rewrite_json_file(self, newfilepath, json_data):
        # json.dump���ļ��У�"a"��ʾ�����е��ı������ӣ�"w"��ʾ����д��
        with open(newfilepath, "a", encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False)
            # ensure_ascii=False����dumpĬ�ϱ�����ascii���ر��������д������
            f.close()

    def get_new_json(self, key, value):
        key_ = key.split(".")
        key_length = len(key_)
        with open(self.path, 'rb') as f:
            json_data = json.load(f)
            i = 0
            a = json_data
            while i < key_length:
                if i+1 == key_length:
                    a[key_[i]] = value
                    i = i + 1
                else:
                    a = a[key_[i]]
                    i = i + 1
        f.close()
        return json_data


if __name__ == "__main__":
    data = Json("1234")