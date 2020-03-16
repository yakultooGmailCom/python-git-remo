# 引入 flask 套件下的類別和函式，注意不是 requests
from flask import Flask, request

# 使用 __name__ 代表目前運作的程式的模組名稱當作辨識名稱使用，下面產生一個網頁伺服器的實例物件
app = Flask(__name__)

# 此為 decorator 為當網址為 / 時由這個函式負責處理，若改為 @app.route('/hello') 則當網址 /hello 才給他處理
@app.route('/')
def hello():
    # request 為 flask 內建的網路請求物件，可以取出網路請求攜帶的資料，例如：網址參數，ex. name。get 方法取若網址中沒有 name 參數，則預設為 World 字串。例如：localhost:8080/?name=Jack
    name = request.args.get("name", "World")
    # 伺服器回傳 Hello, name 變數值
    return f'Hello, {name}!'

# 運行 Flask server，設定監聽 port 8080（網路 IP 位置搭配 Port 可以辨識出要把網路請求送到那邊 xxx.xxx.xxx.xxx:port，0.0.0.0 代表任何 IP）
app.run(host='0.0.0.0', port=8080)