import lib_archive_18.parser as lib
import asyncio
url = lib.URL_ABSTRAKT

parser = lib.Parser(url)
print(parser.get_count_all_files())
print(parser.get_count_pages())
# print(parser.get_files(2))

for file in parser.get_files_iterator(10,11):
	print(file)

async def main():
	parser = lib.Parser(url)
	res = await parser.get_random_file()
	if res:
		print(f"\n{res}\n")

asyncio.run(main())


