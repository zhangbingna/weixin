import demjson


class Test(object):
    def textstart(self, text):
        if text.startswith("{"):
            print("{")
        else:
            text = text.split("{", 1)[1]
            print(type(text))

    def titlenone(self, title):
        if len(title) == 0:
            print(1)
        else:
            print(2)
    def text_split(self):
        m = self.path.split('_')[0]
        print(m)

    def write_file(self, filepath, newline):
        with open(filepath, "a", encoding='utf-8') as f:
            f.writelines(newline+"\n")
            f.close()

    def demjson(self):
        with open(self.path) as f:
            f = f.readline()
            print("½âÂë", demjson.decode(f))
            print("±àÂë", demjson.encode(f))


if __name__ == "__main__":
    data = Test()

