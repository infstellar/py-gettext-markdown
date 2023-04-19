import gettext
import re
import os

class GeneratePot():
    LANG='zh_CN'
    def __init__(self, file_path):
        self.file_path = file_path
        self.origin_file = open(file_path, 'r').read()
        self.text_list = re.split('  \n|\n\n|<br>',self.origin_file)
        self.text_list = [i.replace('\n', '\\n') for i in self.text_list]
        self.text_list = [i.replace('\"', '\\"') for i in self.text_list]

    def _write_file(self):
        f = open(self.file_path.replace('.md','.py'), 'w')
        f.write(f'import gettext\n')
        f.write(f'l10n = gettext.translation("{self.LANG}", localedir = r"translation/locale", languages=["{self.LANG}"])\n')
        f.write('l10n.install()\n')
        f.write(f'_ = l10n.gettext\n')
        for i in self.text_list:
            f.write(f'_("{i}")\n')
        f.close()
            
      
if __name__ == "__main__":
    gp = GeneratePot('test.md')
    gp._write_file()