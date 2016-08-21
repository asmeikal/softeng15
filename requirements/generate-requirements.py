import yaml
from os import listdir
from os.path import isfile, join

template_path = 'generated/templates/'
sources  = 'generated/yaml/'
output   = 'generated/system_requirements_table.tex'

func_header = "\\subsection{Specifica dei Requisiti Funzionali}\n\n"
n_func_header = "\\clearpage\n\n\\subsection{Specifica dei Requisiti Non Funzionali}\n\n"
domain_header = "\\clearpage\n\n\\subsection{Specifica dei Requisiti di Dominio}"

fields = [
    'title',
    'mnemo',
    'id',
    'shortid',
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

    def set_index(self, index):
        self.index = index;
        self.build_id()

    def build_id(self):
        info = ['REQ']
        short_info = ['REQ']
        info += [self.data['mnemo']]
        info += [self.data['type'].upper()[0]]
        short_info += [self.data['type'].upper()[0]]
        info += [self.data['priority'].upper()[0]]
        info += [str(self.index)]
        short_info += [str(self.index)]
        self.data['id'] = "{}".format("\\_".join(info))
        self.data['shortid'] = "{}".format("\\_".join(short_info))

    def output(self):
        res = ''
        template = template_path
        if self.type == 'Funzionale':
            template += 'requirement_func.tex'
        elif self.type == 'Non Funzionale':
            template += 'requirement_n_func.tex'
        elif self.type == 'Dominio':
            template += 'requirement_domain.tex'
        with open(template, 'r') as ft:
            t = ft.read()
            res = t.format(**self.data)
        return res

if __name__ == '__main__':
    files = [f for f in listdir(sources) if isfile(join(sources, f))]
    index_func = 1
    index_n_func = 1
    index_domain = 1
    with open(output, 'w') as out:
        res_func = ""
        res_n_func = ""
        res_domain = ""
        for f in files:
            if f == "example.yaml": continue
            if f[0] == '.': continue
            r = Requirement(sources + f, 0)
            if r.type == 'Funzionale':
                r.set_index(index_func)
                index_func += 1
                res_func += r.output()
            elif r.type == 'Non Funzionale':
                r.set_index(index_n_func)
                index_n_func += 1
                res_n_func += r.output()
            elif r.type == 'Dominio':
                r.set_index(index_domain)
                index_domain += 1
                res_domain += r.output()
        out.write(func_header)
        out.write(res_func)
        out.write(n_func_header)
        out.write(res_n_func)
        out.write(domain_header)
        out.write(res_domain)

