import yaml
from os import listdir
from os.path import isfile, join

template = 'generated/templates/requirement.tex'
sources  = 'generated/yaml/'
output   = 'generated/system_requirements_table.tex'

func_header = "\\subsection{Specifica dei Requisiti Funzionali}\n\n"
n_func_header = "\\subsection{Specifica dei Requisiti Non Funzionali}\n\n"
domain_header = "\\subsection{Specifica dei Requisiti di Dominio}"

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
        self.type = self.data['type']

    def build_id(self):
        info = ['REQ']
        info += [self.data['title'].replace(' ','').upper()[0:6]]
        info += [self.data['type'].upper()[0]]
        info += [self.data['priority'].upper()[0]]
        info += [str(index)]
        self.data['id'] = "\\code{{{}}}".format("\\_".join(info))

    def output(self):
        res = ''
        with open(template, 'r') as ft:
            t = ft.read()
            res = t.format(**self.data)
        return res

if __name__ == '__main__':
    files = [f for f in listdir(sources) if isfile(join(sources, f))]
    index = 0
    with open(output, 'w') as out:
        res_func = ""
        res_n_func = ""
        res_domain = ""
        for f in files:
            if f == "example.yaml": continue
            index += 1
            r = Requirement(sources + f, index)
            if r.type == 'Funzionale':
                res_func += r.output()
            elif r.type == 'Non Funzionale':
                res_n_func += r.output()
            elif r.type == 'Dominio':
                res_domain += r.output()
        out.write(func_header)
        out.write(res_func)
        out.write(n_func_header)
        out.write(res_n_func)
        out.write(domain_header)
        out.write(res_domain)

