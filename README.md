# PQViewer
View [Apache Parquet](https://parquet.apache.org/) Files In Your Terminal  

![PQViewer](https://github.com/thread53/pqviewer/blob/main/pqviewer.png)

## Installing PQViewer

After installing Python 3.7 or above, install PQViewer using `pip` with:

```bash
pip install pqviewer
```

## Using PQViewer with local parquet files

From any shell run the command pqviewer and provide the exact path to the file

```bash
pqviewer "path/to/file.parquet"
```

## Navigation  
Arrow keys or mouse to move around the table  
Tab key to switch focus  
CTRL+C to Quit   

## Contributions
Any contributions, features and improvements are welcome. Please, open an issue so we can start discussion.

## Acknowledgements
PQViewer is build using 
[Textual](https://github.com/Textualize/textual)  
[Rich](https://github.com/Textualize/rich)  
[PyArrow](https://arrow.apache.org/docs/python/index.html)

## License
MIT