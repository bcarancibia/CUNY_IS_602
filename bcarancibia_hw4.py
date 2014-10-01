__author__ = 'bcarancibia'

from bs4 import BeautifulSoup
import urllib
from alchemyapi import AlchemyAPI


#begin exercise

if __name__ == "__main__":
    link = "http://www.newyorker.com/magazine/2014/06/30/stepping-out-3"
    f = urllib.urlopen(link)
    page = f.read()

    #BeautifulSoup
    soup = BeautifulSoup(page)
    str = ""
    def textOf(soup):
        return str.join(soup.findAll(text=True)).encode('ascii','ignore')

    visible_texts = [textOf(n) for n in soup.findAll(["p"])]
    visible_texts.pop()

    #Make String
    allimportanttext = "".join(visible_texts)

    #alchemyAPI
    alchemyapi = AlchemyAPI()
    response = alchemyapi.keywords("text", allimportanttext)

    
    print('Top 10 Keywords')

    #results
    index = 1;
    for keyword in response['keywords'][:10]:
        print(index)
        print('text: ', keyword['text'].encode('utf-8'))
        print('relevance: ', keyword['relevance'].encode('ascii', 'ignore'))
        print('')
        index = index+1



	
