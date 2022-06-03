import yaml
from yaml import CLoader as Loader, CDumper as Dumper
print("Welcome!!!!")
with open('file1.yml') as file:
    data = file.read()
    print('Data read:', data)
a = (yaml.load(data, Loader=Loader))
b = yaml.dump(a, Dumper=Dumper)
print('yaml load:', a)
print('yaml dump:', b)
print(set(a))
