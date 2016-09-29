from flask import Flask, request,render_template,redirect, url_for, abort, session
from flask.ext.admin import Admin, BaseView, expose
app = Flask(__name__)

@app.route("/generate_204")
def generate_204():
    return render_template("204.html")

@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username in user_list:
            response = make_response(redirect('/home'))
            response.set_cookie('username', value=username, max_age=300)
            session['islogin'] = '1'
            return response
        else:
            session['islogin'] = '0'
            return redirect('/about')
    else:
        return render_template('login.html')

    
@app.route("/home")
def home():
    return render_template('/home/home.html')

@app.route("/feihua")
def feihua():
    return render_template('/feihua/feihua.html')

@app.route("/archive")
def archive():
    return render_template('archive.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/read_more")
def read_more():
    return render_template('read_more.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/zw")
def zw():
    return render_template('/row/love/zw.html')

@app.route("/row/2016/04/27/test")
def test():
    return render_template('/row/2016/04/27/test.html')

@app.route("/row/2016/05/21/10086")
def android_10086():
    return render_template('/row/2016/05/21/10086.html')

@app.route("/row/2016/05/25/xiaoqing")
def xiaoqing_60():
    return render_template('/row/2016/05/25/⁮xiaoqing_60.html')

@app.route("/row/2016/05/28/socket")
def socket_test():
    return render_template('/row/2016/05/28/socket.html')

@app.route("/row/2016/06/22/androidFile")
def androidFile():
    return render_template('/row/2016/06/22/androidFile.html')

@app.route("/row/2016/06/27/shixun")
def shixun():
    return render_template('/row/2016/06/27/shixun.html')

@app.route("/row/2016/07/09/mywebsite")
def mywebsite():
    return render_template('/row/2016/07/09/mywebsite.html')

@app.route("/row/2016/08/24/sdutinfo")
def sdutinfo():
    return render_template('/row/2016/08/24/sdutinfo.html')

@app.route("/row/2016/09/13/facerecognition")
def facerecognition():
    return render_template('/row/2016/09/13/FaceRecognition.html')

@app.route("/row/2016/09/14/androidn")
def androidn():
    return render_template('/row/2016/09/14/androidN.html')

@app.route("/webscan_360_cn.html")
def webscan_360_cn():
    return render_template('webscan_360_cn.html')
sdutinfo
if __name__ == "__main__":
    app.run()
