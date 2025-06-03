from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello(): 
    return 'Hello, kubig!'

if __name__ == '__main__':
    app.run(debug=True)

#git pull
#git push
#git checkout
#git commit
#git add
#git merge

#git branch
#git push --set-upstream origin practice
#git branch -d 
#git push origin --delete 
#git log
#.......