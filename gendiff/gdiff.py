import copy
def test(a):
    subtree = {}
    
    def subtest(tree, level):
        copytree = copy.deepcopy(tree)
        subtree = {}
        print('tree =:', copytree, 'len = ', len(copytree), 'level -', level)
        for i in (copytree.values()):
            if type(i) is dict:
                subtree.update(i)

        print('subtree"', subtree)
        stroke = '**' * level
        print(stroke, subtree)
        
        if subtree != {}:
            level += 1
            subtest(subtree, level)
        return
    return subtest(a, 1)

a = {'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {'key': 'value', 'doge': {'wow': ''}}}

# b = {'setting1': 'Value 1', 'setting2': 100, 'setting3': True, 'setting6': {'key': 'va5lue', 'doge': {'wow': ''}}}

c = (test(a))

