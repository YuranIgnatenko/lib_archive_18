import lib_archive_18.parser as lib

url = lib.URL_GAME

parser = lib.Parser(url)
print(parser.get_count_all_files())
print(parser.get_count_pages())
# print(parser.get_files(2))

for file in parser.get_files_iterator(10,2):
	print(file)