# PQViewer

[![PyPI](https://img.shields.io/pypi/v/pqviewer)](https://pypi.org/project/pqviewer/)  
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pqviewer)  

View [Apache Parquet](https://parquet.apache.org/) Files In Your Terminal  

![PQViewer](https://github.com/thread53/pqviewer/blob/main/pqviewer.png)

## Installing PQViewer

After installing Python 3.8 or above, install PQViewer using `pip` with:

```bash
pip install pqviewer
```

## Using PQViewer with local parquet files

From any shell run the command pqviewer and provide the exact path to the file

```bash
pqviewer "path/to/file.parquet"
```

## Navigation  
<kbd>&#8592;</kbd> <kbd>&#8594;</kbd> <kbd>&#8593;</kbd> <kbd>&#8595;</kbd> Move around the table  
<kbd>PgUp</kbd> <kbd>PgDn</kbd> Scroll up or down  
<kbd>T</kbd> Change Theme  
<kbd>Tab</kbd> Switch focus  
<kbd>Ctrl</kbd> + <kbd>C</kbd> Quit  


## Contributions
Any contributions, features and improvements are welcome. Please, open an issue so we can start discussion.

## Acknowledgements
PQViewer is built using  
[Textual](https://github.com/Textualize/textual)  
[Rich](https://github.com/Textualize/rich)  
[PyArrow](https://arrow.apache.org/docs/python/index.html)

## License
MIT