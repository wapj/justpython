import json

txt = """
{
  "a" : 1,
  "b" : 2,
  "c": true,
  "d" : ["가", "나", "다"]
}
"""


def read_json():
    my_dict = json.loads(txt)
    print(my_dict)
    print(type(my_dict))

    for k, v in my_dict.items():
        print(k, v)
    return my_dict


def write_json():
    my_json = read_json()
    with open('test.json', 'w') as f:
        f.write(json.dumps(my_json))


def read_json_from_file():
    f = open('test.json')
    my_dict = json.loads(f.read())
    print(my_dict)


read_json_from_file()
