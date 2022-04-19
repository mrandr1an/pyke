import click
import requests as r
from bs4 import BeautifulSoup
import sys
import datetime
from termcolor import colored, cprint
from pyfiglet import Figlet
from log import Log


site = "https://www.wordreference.com/engr/"


def request_word(word):
    url = site+word
    page = r.get(url)
    status = page.status_code
    #print(url)
    log = Log("pykelog")
    log.write_to_log(url)
    #Write datetime to log
    log.write_to_log("#################" + str(datetime.datetime.now()) + "###################")
    #Check if site is up
    if str(status) == "200":
        cprint(page.status_code, 'green', attrs=['bold','blink'])
        cprint("Status is valid grabbing word", 'grey', attrs=['bold' ])
        path = click.prompt("Please enter the file you want to write the examples to", type=str)
        soup = BeautifulSoup(page.text, 'html.parser')
        tables = soup.findChildren('table')
        table = tables[0]
        #getting table row
        rows = table.findChildren(['tr'])
        for row in rows:
            tr_cls = row.attrs.get("class")
            #print(str(tr_cls))
            log.write_to_log(str((tr_cls)))
            if str(tr_cls) == "['even']":
                td =  row.find("td",class_="FrEx")
                if td != None:
                     example = td.find('span').text
                     print(example)
                     log.write_to_log(example)
                     log.write_example(path, example)
                     log.make_exercise(path, word)
                else:
                     #print("Did NOT find example")
                     log.write_to_log("Did NOT find example")
            else:
              #print("Even td not found")
               log.write_to_log("Even td not found")
    else:
        cprint(page.status_code, "red", attrs=['bold', 'blink'])
        cprint("Pyke has encountered an error, please check your internet connection", "grey", attrs=['bold'])

def convert_args_to_str(args):
    str = ''
    seperator = '!/'
    for item in args:
        str = str + item + seperator

    str = str.split(seperator)
    return str

@click.command()
@click.argument('word',nargs=-1)
def grab_word(word):
    start_pyke()
    str_word = convert_args_to_str(word)
    for query in word:
        request_word(query) #function only gets strings

def start_pyke():
    f = Figlet(font='isometric2')
    print(colored(f.renderText("PYKE"),'red'))

if __name__ == '__main__':
    grab_word()









