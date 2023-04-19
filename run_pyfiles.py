import os
command_head_en = f"python pygettext.py -k t2t -d en_US -p markdown_i18n\\locale\\en_US\\LC_MESSAGES"
command_head_zh = f'python pygettext.py -k t2t -d zh_CN -p markdown_i18n\\locale\\zh_CN\\LC_MESSAGES'

class RunPYFlies():
    def __init__(self, folder_path) -> None:
        self.folder_path = folder_path
    
    def run(self):
        command=''
        for root, dirs, files in os.walk(self.folder_path):
            for d in dirs:
                if '__pycache__' in root or d == '__pycache__':
                    continue
                print(os.path.join(root,d))
                command += f"{os.path.join(root,d)}\\*.py "
        command += f"{os.path.join(root)}\\*.py "
        print(f'{command_head_en} {command}')
        os.system(f'{command_head_en} {command}')
        print(f'{command_head_zh} {command}')
        os.system(f'{command_head_zh} {command}')

if __name__ == "__main__":
    rf = RunPYFlies(r"md_test")
    rf.run()