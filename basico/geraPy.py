def geraPy(qtd_files):
  for index in range(1, qtd_files + 1):
    file = 'aula-' + str(index) + '.py'

    with open(file, 'w+') as f:

      subject = '"""\n\n\n\n"""\n'

      f.write(subject)

geraPy(10)
