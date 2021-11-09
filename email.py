# Извлечение адресов электронной почты из текстового документа
import re

file = open("expressions.txt", encoding="utf-8").readlines()
car = '\n'.join(file)


email = re.compile(
	r'''(
	[a-zA-Z0-9_-]+
	@
	([a-zA-Z0-9_-]+)?
	\.[a-zA-Z0-9]{2,4}
	)''', re.VERBOSE
)

list_email = []
for i in email.findall(car):
	if i[0] not in list_email:
		list_email.append(i[0])


print(list_email)

