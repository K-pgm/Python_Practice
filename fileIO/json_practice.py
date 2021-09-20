import json

# json.load: jsonファイルをpythonのデータ構造で読み込み
with open("example.json") as f:
    data = json.load(f)

print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['ID'])

# json.dump: pythonのデータ構造をjsonファイルに書き込み
# ※タプルはJsonではリスト型に変換される
new_json = {'key1': 'value1', 'key2': (1, 'value2')}
with open("new_json.json", 'w') as f:
    json.dump(new_json, f)

# json.loads: json文字列をpythonのデータ構造に変換
with open("new_json.json", 'r') as f:
    new_json_reload = json.load(f)

print(new_json_reload)

# json.dumps: pythonのデータ構造をjson文字列に変換
json_str = json.dumps(new_json)
print(type(json_str))

python_data = json.loads(json_str)
print(python_data)
