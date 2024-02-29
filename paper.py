from flask import Flask, render_template, request
import random
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data_list = []
    if request.method == 'POST':
        usernum = request.form['usernum']
        wdl = [0, 0, 0]
        print(usernum)

        ran_rock = random.randint(1, 3)

        if usernum == "가위":
            user_num = 1  # 1, 3
            print(user_num)

        elif usernum == "바위":
            user_num = 2  # 2 ,1
            print(user_num)

        elif usernum == "보":
            user_num = 3  # 3 ,2
            print(user_num)

        if user_num == ran_rock:
            message="비겼습니다."
            wdl[1] += 1
            return render_template('paper.html',message = message)
        elif (user_num == 1 and ran_rock == 3) or (user_num == 2 and ran_rock == 1) or (user_num == 3 and ran_rock == 2):
            message="이겼습니다."
            wdl[0] += 1
            return render_template('paper.html',message = message)
        else:
            message="졌습니다."
            wdl[2] += 1
            return render_template('paper.html',message = message)
            
    return render_template('paper.html',)
if __name__ == '__main__':
    app.run(debug=True)
