# py-gettext-markdown
generate gettext file from markdown docs. Base on python and gettext module.

## Generate pot files
```powershell
cd py-gettext-markdown
python gettext-markdown.py pot -l zh_CN,en_US -f ../doc -c true
cd ../
```

## Generate markdowns
```powershell
cd py-gettext-markdown
python gettext-markdown.py md -l zh_CN,en_US -f ../doc -c true
cd ../
```