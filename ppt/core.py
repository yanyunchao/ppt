from __future__ import unicode_literals

import json
import six


def ppt(obj, filter='.', with_print=True, normal_path_print=False):
    base_string = str if six.PY3 else basestring
    obj = json.loads(obj) if isinstance(obj, base_string) else obj
    find_str, find_map = '', ['["%s"]', '[%s]', '%s', '.%s']
    for im in filter.split('.'):
        if not im:
            continue

        if isinstance(obj, (list, tuple, base_string)):
            if im.startswith('[') and im.endswith(']'):
                im = im[1:-1]
            if ':' in im:
                slice_default = [0, len(obj), 1]
                obj, quota = obj[slice(
                    *[int(sli) if sli else slice_default[i] for i, sli in
                      enumerate(im.split(':'))])], 1
            else:
                obj, quota = obj[int(im)], 1
        else:
            if im in obj:
                obj, quota = obj[im], 0
            elif im.endswith('()'):
                obj, quota = list(getattr(obj, im[:-2])()), 3
            else:
                if im.isdigit():
                    obj, quota = obj[int(im)], 1
                else:
                    raise KeyError(im)
        find_str += find_map[quota] % im

    if with_print:
        print(obj if isinstance(obj, base_string) else
              json.dumps(obj,
                         indent=4,
                         sort_keys=True,
                         ensure_ascii=False))
    if normal_path_print:
        print('get it normally with: <obj>%s' % find_str)
    return obj
