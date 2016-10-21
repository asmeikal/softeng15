
import yaml
from os import listdir
from os.path import isfile, join

template_path = 'generated/templates/'
sources  = 'generated/yaml/'
output   = 'generated/test-plan-tables.tex'
output_macro   = 'generated/test-plan-macros.tex'

header = "\\input{test-plan/" + output_macro.replace('.tex','') + "}\n\n\\subsection{Specifica dei Test Funzionali}"

fields = [
    'title',
    'mnemo',
    'shortid',
    'id',
    'prerequisites',
    'description',
    'action'
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

    def set_index(self, index):
        self.index = index;
        self.build_id()

    def build_id(self):
        info = ['TP']
        short_info = ['TP']
        info += [self.data['mnemo']]
        info += [str(self.index)]
        short_info += [str(self.index)]
        self.data['id'] = "{}".format("\\_".join(info))
        self.data['shortid'] = "{}".format("\\_".join(short_info))

    def output(self):
        res = ''
        template = template_path
        template += 'test-plan.tex'
        with open(template, 'r') as ft:
            t = ft.read()
            res = t.format(**self.data)
        return res

    def output_macro(self):
        res = ''
        template = template_path + 'macro.tex'
        with open(template, 'r') as ft:
            t = ft.read()
            res = t.format(**self.data)
        return res

if __name__ == '__main__':
    files = [f for f in listdir(sources) if isfile(join(sources, f))]
    index = 1
    with open(output, 'w') as out:
    	res = ""
        res_macro = ""
        for f in files:
            if f == "example.yaml": continue
            if f[0] == '.': continue
            r = Requirement(sources + f, index)
            index += 1
            r.set_index(index)
            res += r.output()
            res_macro += r.output_macro()
        out.write(header)
        out.write(res)
        with open(output_macro, 'w') as out_macro:
            out_macro.write(res_macro)
