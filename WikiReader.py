from random import randint
import wikipediaapi

def read(day, month):
    wiki_wiki = wikipediaapi.Wikipedia('es')
    pageName = ("Plantilla:Efemérides - "+str(day)+" de "+parse_month(month))
    page_py = wiki_wiki.page(pageName)
    if page_py.exists():
        print("Wikipedia page ["+pageName+"] succesfully loaded.")
        return randomEfemeride(page_py)
    else:
        print("The Wikipedia page ["+pageName+"] could not be found.")
        return ("BuhoSabiondo parece estar fallando ——por culpa de Wikipedia——. Meper d0nas¿")


def parse_month(month):
    months = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
              "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    return months[month-1]


def randomEfemeride(wikiPage):
    contents = wikiPage.text
    contentsList = contents.split('\n')
    randIndex = randint(0, len(contentsList)-1)
    #print(contents)
    #print(randIndex)
    #print(contentsList[randIndex])
    return contentsList[randIndex].replace(' (en la imagen)', '')