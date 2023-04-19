import gettext
import re
import os

class GeneratePot():
    LANG='zh_CN'
    def __init__(self, folder_path):
        self.folder_path = folder_path
        

    def _write_file(self, file_path):
        origin_file = open(file_path, 'r').read()
        text_list = re.split('  \n|\n\n|<br>',origin_file)
        text_list = [i.replace('\n', '\\n') for i in text_list]
        text_list = [i.replace('\"', '\\"') for i in text_list]
        f = open(file_path.replace('.md','.py'), 'w')
        f.write(f'import gettext\n')
        f.write(f'l10n = gettext.translation("{self.LANG}", localedir = r"markdown_i18n/locale", languages=["{self.LANG}"])\n')
        f.write('l10n.install()\n')
        f.write(f'_ = l10n.gettext\n')
        f.write(f'f = open(r"{file_path}")\n')
        for i in text_list:
            f.write(f'f.write(_("{i}"))\n')
        f.write(f'f.close()')
        f.close()
    
    def run(self):
        for root, dirs, files in os.walk(self.folder_path):
            for f in files:
                if f.split('.')[-1] in ['md', 'markdown']:
                    self._write_file(f"{root}/{f}")
      
if __name__ == "__main__":
    gp = GeneratePot('md_test')
    gp.run()