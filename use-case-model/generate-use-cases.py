import yaml
from os import listdir
from os.path import isfile, join

template_path = 'generated/templates/'
sources  = 'generated/yaml/'
output   = 'generated/use_case_table.tex'
output_macro   = 'generated/use_case_macro.tex'

output_header = "\\input{use-case-model/" + output_macro.replace('.tex','') + "}\n\n"

use_cases = {}

fields = [
    'title',
    'mnemo',
    'id',
    'shortid',
    'actors',
    'origin',
    'description',
    'pre',
    'flow',
    'post',
    'side',
]

alt_fields = fields + [
    'alt-flow',
    'alt-post',
    'alt-side',
]

class UseCase(object):
    def __init__(self, fname, index):
        self.alt = False
        with open(fname, 'r') as f:
            data = yaml.safe_load(f)
            self.data = {}
            for k, v in data.iteritems():
                if str(k).find('alt') >= 0: self.alt = True
                self.data[str(k)] = str(v)
        self.index = index
        self.build_id()
        if self.alt:
            assert set(self.data.keys()) == set(alt_fields), 'Use case in file "{}" is missing some fields.'.format(fname)
        else:
            assert set(self.data.keys()) == set(fields), 'Use case in file "{}" is missing some fields.'.format(fname)
    def get_subindex(self):
        self.subindex +=1
        return self.subindex

    def set_index(self, index):
        self.index = index;
        self.build_id()

    def build_id(self):
        info = ['UC']
        short_info = ['UC']
        info += [self.data['mnemo']]
        info += [str(self.index)]
        short_info += [str(self.index)]
        self.data['id'] = "{}".format("\\_".join(info))
        self.data['shortid'] = "{}".format("\\_".join(short_info))

    def output(self):
        res = ''
        template = template_path
        if self.alt:
            template += 'use-case-alt.tex'
        else:
            template += 'use-case.tex'
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
            r = UseCase(sources + f, index)
            index += 1
            res += r.output()
            res_macro += r.output_macro()
        out.write(output_header)
        out.write(res)
        with open(output_macro, 'w') as out_macro:
            out_macro.write(res_macro)

