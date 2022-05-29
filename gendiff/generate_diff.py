def generate_diff(a, b):
    print(a)
    print(b)
    old_keys = set(a.keys())
    new_keys = set(b.keys())
    # added — ключ отсутствовал в первом словаре, но был добавлен во второй
    added = new_keys - old_keys

    # deleted — ключ был в первом словаре, но отсутствует во втором
    deleted = old_keys - new_keys

    # changed — ключ присутствовал и в первом и во втором словаре,
    # но значения отличаются
    intersept = new_keys & old_keys
    changed = set({})
    for i in intersept:
        if a[i] != b[i]:
            changed.add(i)

    # unchanged — ключ присутствовал и в первом и во втором словаре
    # с одинаковыми значениями
    intersept = new_keys & old_keys
    unchanged = set({})
    for i in intersept:
        if a[i] == b[i]:
            unchanged.add(i)

    # формируем отличия:
    all_keys = sorted(old_keys | new_keys)
    diff = {}
    for i in all_keys:
        if i in changed:
            diff[i] = {'attrib': 'changed',
                       'old_value': a[i],
                       'new_value': b[i]}
        elif i in unchanged:
            diff[i] = {'attrib': 'unchanged', 'new_value': b[i]}
        elif i in deleted:
            diff[i] = {'attrib': 'deleted', 'old_value': a[i]}
        elif i in added:
            diff[i] = {'attrib': 'added', 'new_value': b[i]}

    return make_json(diff)


def make_json(d):
    tab = ' '
    # diff_json = {}
    stroke = '{\n'

    for i in d:

        if d[i]['attrib'] == 'unchanged':
            add = f"  {i}: {d[i]['new_value']}"

        if d[i]['attrib'] == 'changed':
            add1 = f"- {i}: {d[i]['old_value']}"
            add = add1 + ',\n' + tab + f"+ {i}: {d[i]['new_value']}"

        if d[i]['attrib'] == 'deleted':
            add = f"- {i}: {d[i]['old_value']}"

        if d[i]['attrib'] == 'added':
            add = f"+ {i}: {d[i]['new_value']}"
        stroke += tab + add + ',\n'

    stroke = stroke[:-2] + '\n}'
    return stroke
