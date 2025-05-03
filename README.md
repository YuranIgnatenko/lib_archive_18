# lib_archive_18

`lib_archive_18` это библиотека Python для получения информации с сайта

## Установка из PyPI

```bash
pip install lib_archive_18
```

## Использование репозитория GitHub

```bash
git clone https://github.com/YuranIgnatenko/lib_archive_18.git
cd lib_archive_18
pip install .
```

## Пример использования

```python
# импорт парсера
from lib_archive_18 import Parser

# создание парсера
parser = Parser()

print(parser.get_count_all_files())
print(parser.get_count_pages())
print(parser.get_files(2))

for file in parser.get_files_iterator(10,2):
	print(file)
```
