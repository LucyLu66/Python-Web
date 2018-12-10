import webbrowser
urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return 'Hello World!'

if __name__ == '__main__':
    app = webbrowser.application(urls, globals())
    app.run()