import feedparser as fp

datUniver = fp.parse('http://www.eluniversal.com.mx/seccion/1/rss.xml')
datJorn = fp.parse('http://www.jornada.unam.mx/rss/politica.xml?v=1')

#  print(datUniver['feed']['link'] + '\n')
#  print(datJorn['feed']['title'] + '\n')

#  print(datUniver.headers['Date'])

#  print(len(datUniver.entries))
#  print(datUniver.entries[0])

#  print(datUniver)

file = open('rss_univ.txt', 'a')

file.write(str(datUniver.headers['Date']) + ';\n')
file.write(str(datUniver) + ';\n')
file.write(str(datJorn.headers['Date']) + ';\n')
file.write(str(datJorn) + ';\n')

file.close()
