import web
import random

render = web.template.render('templates/')
urls = (
    '/', 'index',
    '/add', 'add'
)

db = web.database(dbn='postgres', user='exec', pw='webproj', db='webproj')



class index:

    r_old = -1
    def GET(self):

        # return render.index(i.name)
        todos = db.select('todo')

        while True :
            r = random.randint(0, len(todos))
            if r != r_old.index:
                r_old = r
                break
        # return render.index(todos)
        a = (todos[r]['title'])
        return render.index(a)

    def randomize(self):
        r = random.randint(0, len(todos))
        return r

class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')
        #return index.GET(self)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
