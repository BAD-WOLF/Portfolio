import os
from flask import render_template
from flask import redirect
from flask import request
from flask import Flask

class BackEnd:
    def __init__(self):
        self.app = Flask(__name__)
        self.name = 'Portfolio'
        self.address = ['127.0.0.1', 4000]
        self.list_lang = ['python','html', 'css']
        self.list_cursos = {
                'Python':'https://www.youtube.com/watch?v=Ay-MakuSg08&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR',
                'JavaScript':'https://www.youtube.com/watch?v=E4DBTqgxHGM&list=PLx4x_zx8csUg_AxxbVWHEyAJ6cBdsYc0T',
                'PHP':'https://www.youtube.com/watch?v=O73xbQvGhHk&list=PL0N5TAOhX5E9eJ9Ix6YUIgEw3lNmaIEE9',
                'HTML & CSS':'https://www.youtube.com/watch?v=CZPa3-1BKnY&list=PLirko8T4cEmzrH3jIJi7R7ufeqcpXYaLa'
                }
        self.contat = {
                'name':'Paulo Pelecer',
                'numero': '+5562993386905',
                'GitHub': 'https://github.com/SenhorLoock'
                }

    def RunPage(self):
        @self.app.route('/', methods=['GET','POST'])
        def index():
            if request.method == 'GET':
                return render_template('index.html', langs=self.list_lang, cursos=self.list_cursos, links=self.list_cursos.values())
            else:
                return redirect('/404')
        @self.app.route('/<error>')
        def notfold(error):
            return render_template('404.html')

        self.app.run(debug=True, host=self.address[0], port=self.address[1])

if __name__ == '__main__':
    BackEnd().RunPage()
