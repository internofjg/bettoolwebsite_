def hello():
    return "Hello, World!"

def content():
    return '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            '''
# @app.route("/")
def home():
    return '''
    <center><h1>JG說真的－加碼計算機</h1></center>
    <center><form action="/result" method="post">
        <label for="cost_price">庫存成本價:</label>
        <input type="text" id="cost_price" name="cost_price"><br><br>

        <label for="cost_amount">庫存張數:</label>
        <input type="text" id="cost_amount" name="cost_amount"><br><br>

        <label for="add_price">想加碼價位:</label>
        <input type="text" id="add_price" name="add_price"><br><br>

        <label for="expect_price">預期股價會上漲到多少:</label>
        <input type="text" id="expect_price" name="expect_price"><br><br>

        <label for="exit_money">加碼後獲利回吐，至少保有多少獲利離場:</label>
        <input type="text" id="exit_money" name="exit_money"><br><br>

        <input type="submit" value="計算">
    </form><center>
    '''

# @app.route("/result", methods=["POST"])
def result():
#   import numpy as np
#   import scipy.optimize
#
#    def add_lot_opt_sol(p0, x0, p1, final_return, p_exp, exp_return_loss_ratio):
#        def f(x):
#            x1 = x[0] #ADD LOT
#            p_final = x[1] #WORST CASE
#            r = p_final * (x0 + x1) - p0 * x0 - p1 * x1 #利潤
#            return_loss_ratio = (p_exp - p1) / (p_final - p1)
#            return (r - (final_return /1000)) ** 2 + (return_loss_ratio - exp_return_loss_ratio) ** 2
#        sol = scipy.optimize.minimize(f, [0, 0])
#        return(sol)
#
#    cost_price = float(request.form["cost_price"])
#    cost_amount = float(request.form["cost_amount"])
#    add_price = float(request.form["add_price"])
#    expect_price = float(request.form["expect_price"])
#    exit_money = float(request.form["exit_money"])
#
#    ans = add_lot_opt_sol(cost_price, cost_amount, add_price, exit_money, expect_price, -3)

    return f'''
    <center><div class="result">若想在價格 {add_price} 塊加碼，建議加碼 <h1 style="display: inline">{int(ans.x[0])}</h1> 張，出場價格 <h1 style="display: inline">{ans.x[1]}</h1>塊</div></center><br><br><center><button onclick='history.back()'>返回上一步</button></center>
    '''
