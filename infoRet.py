import feedparser as fp
#  from time import gmtime, strftime


def get_data_rss():

    datUniver = fp.parse('http://www.eluniversal.com.mx/seccion/1/rss.xml')
    datJorn = fp.parse('http://www.jornada.unam.mx/rss/politica.xml?v=1')
    datCnn = fp.parse('http://expansion.mx/rss/politica')

    file = open('rss_univ.txt', 'a')

    file.write(str(datCnn['Date']) + ';\n')
    file.write(str(datCnn) + ';\n')
    file.write(str(datUniver.headers['Date']) + ';\n')
    file.write(str(datUniver) + ';\n')
    file.write(str(datJorn.headers['Date']) + ';\n')
    file.write(str(datJorn) + ';\n')

    file.close()

get_data_rss()

#  SOME COMMANDS OF FEEDPARSER

#  print(datUniver['feed']['link'] + '\n')
#  print(datJorn['feed']['title'] + '\n')

#  print(datUniver.headers['Date'])

#  print(len(datUniver.entries))
#  print(datUniver.entries[0])

#  print(datUniver)


#print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
