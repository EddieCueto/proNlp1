import feedparser as fp
#  from time import gmtime, strftime


def get_data_rss():

    datUniver = fp.parse('http://www.eluniversal.com.mx/seccion/1/rss.xml')
    datJorn = fp.parse('http://www.jornada.unam.mx/rss/politica.xml?v=1')
    datAri = fp.parse('http://aristeguinoticias.com/category/mexico/feed/')

    file = open('rss_univ.txt', 'a')

    # file.write(str(datAri.headers['Date']) + ';\n')
    file.write(str(datAri) + ';\n')
    # file.write(str(datUniver.headers['Date']) + ';\n')
    file.write(str(datUniver) + ';\n')
    # file.write(str(datJorn.headers['Date']) + ';\n')
    file.write(str(datJorn) + ';\n')

    file.close()

#  SOME COMMANDS OF FEEDPARSER

#  print(datUniver['feed']['link'] + '\n')
#  print(datJorn['feed']['title'] + '\n')

#  print(datUniver.headers['Date'])

#  print(len(datUniver.entries))
#  print(datUniver.entries[0])

#  print(datUniver)


#print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
