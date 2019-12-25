import web
render = web.template.render('templates/')
urls = (
    '/', 'index',
    '/add', 'add'
)

db = web.database(dbn='postgres', user='exec', pw='webproj', db='webproj')

class index:
    def GET(self):

        # return render.index(i.name)
        todos = db.select('todo')
        return render.index(todos)

class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()