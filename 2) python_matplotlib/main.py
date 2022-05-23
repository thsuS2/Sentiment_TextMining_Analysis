import russelCsvRead

rdr = russelCsvRead.run()

for line in rdr:
    print(line)