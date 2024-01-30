# PQViewer
View [Apache Parquet](https://parquet.apache.org/) Files In Your Terminal  

![PQviewer](./pqviewer.svg)

## Installing PQviewer

After installing Python 3.7 or above, install PQviewer using `pip`:

```bash
pip install PQviewer
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
PQViewer is build using [textual](https://github.com/Textualize/textual) and [rich](https://github.com/Textualize/rich)

## License
MIT