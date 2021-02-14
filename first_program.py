def zadachs():
	ask='Введите желаемый номер пункта (1 - просмотр текущих задач, 2 - запись новых задач, 3 - удаление существующей задачи, 4 - выход из программы): '
	vopros1='Напишите здесь Вашу новую задачу: '
	vopros2='Введите задачу, которую вы хотите удалить: '
	while True:
		b=input(ask)
		try:
			b=int(b)
		except ValueError:
			print("Введите номер пункта")
			continue
		if b==4:
			break
		if b==1:
			with open(r'C:\Users\nikit\test\zadachi.txt', 'r') as f:
				zd=f.read().strip()
				print(zd)
				if len(zd)==0:
					print("На текущий момент задач нет")
		elif b==2:
			zadacha = input (vopros1)
			with open(r'C:\Users\nikit\test\zadachi.txt', 'a') as f:
				f.write('\n' + zadacha)
		elif b==3:
			dell = input (vopros2)
			f=open(r'C:\Users\nikit\test\zadachi.txt', 'r')
			lines=f.readlines()
			f.close()
			f=open(r'C:\Users\nikit\test\zadachi.txt', 'w')
			f.truncate()
			for line in lines:
				if line.rstrip('\n') != dell:
					f.write(line)
			f.close()
		else:
			print('Такого пункта нет')
zadachs()