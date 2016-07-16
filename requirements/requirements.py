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

field_names = {
        'title' : 'Titolo',
        'id'   : 'ID',
        'type' : 'Tipologia',
        'priority' : 'Priorit\`a',
        'description' : 'Descrizione requisito',
        'origin' : 'Origine requisito',
        'input' : 'Input',
        'output' : 'Output',
        'action' : 'Descrizione azione',
        'pre' : 'Pre-condizioni',
        'post' : 'Post-condizioni',
        'side' : 'Side-effects'
}

# TODO make this better
def build_output(k, v):
    res = """\pline
\ptitlerow{{{k}}}
\prow{{
    {v}
}}
"""
    return res.format(k = field_names[k], v = v)

def build_id(data, index):
    info = ['REQ']
    info += [str(index)]
    return "$\\code{{{0}}}$".format("\\_".join(info))

class Requirement(object):
    def __init__(self, fname, index):
        with open(fname, 'r') as f:
            data = yaml.safe_load(f)
            self.data = {}
            for k, v in data.iteritems():
                self.data[str(k)] = str(v)
        self.data['id'] = build_id(self.data, index)
        assert set(self.data.keys()) == set(fields)
        self.index = index

    def output(self):
        res = ''
        res += '''\\begin{ptable}{1}\n'''
        for k in fields:
            res += build_output(k, self.data[k])
        res += '''\\end{ptable}\n'''
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

