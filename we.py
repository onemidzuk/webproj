import web
import random

render = web.template.render('templates/')
urls = (
    '/', 'index',
    '/add', 'add'
)

db = web.database(dbn='postgres', user='exec', pw='webproj', db='webproj')


openers = []
def start():
    global openers
    acts = db.select('todo')
    openers = [i['title'] for i in acts]


class index:

    start()

    def GET(self):
        a = openers[random.randint(0, len(openers) - 1)]
        return render.index(a)

class add:

    def GET(self):
        return render.add()

    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        start()
        raise web.seeother('/')
        #return index.GET(self)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
