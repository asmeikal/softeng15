import yaml
from os import listdir
from os.path import isfile, join

fields = [
    'title',
    'id',
    'type',
    'priority',
    'description',
    'origin',
    'input',
    'output',
    'action',
    'pre',
    'post',
    'side'
]

class Requirement(object):
    def __init__(self, fname, index):
        with open(fname, 'r') as f:
            data = yaml.safe_load(f)
            self.data = {}
            for k, v in data.iteritems():
                self.data[str(k)] = str(v)
        self.index = index
        self.build_id()
        assert set(self.data.keys()) == set(fields)

    def build_id(self):
        info = ['REQ']
        info += [self.data['title'].replace(' ','').upper()[0:6]]
        info += [self.data['type']]
        info += [self.data['priority']]
        info += [str(index)]
        self.data['id'] = "\\code{{{}}}".format("\\_".join(info))

    def output(self):
        res = ''
        with open('requirement.tex', 'r') as template:
            t = template.read()
            res = t.format(**self.data)
        return res

if __name__ == '__main__':
    path = 'yaml/'
    files = [f for f in listdir(path) if isfile(join(path, f))]
    index = 0
    with open('system_requirements_table.tex', 'w') as out:
        for f in files:
            index += 1
            r = Requirement(path + f, index)
            out.write(r.output())

