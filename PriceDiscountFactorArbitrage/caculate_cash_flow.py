#-*- coding: utf-8 -*-
import datetime
from dateutil.relativedelta import relativedelta

# 根据面值（face amount, principal amount, per value）, 票息（coupon rate）, 到期日（maturity date）
# 计算票息支付
# 以2010年5月美国财政部发行票面利息为2(1/8)%, 到期日为2015年5月31日的债券
# 承诺每半年（6个月付息一次）

def caculate_cash_flow(issue_date, maturity_date, amount, coupon_rate, period):
    print("计算债券现金流")
    cash_flow_dict = dict()
    pay_interest_cash = amount * coupon_rate * period
    #time = issue_date +  datetime.timedelta(months=6)
    i = 1
    pay_interest_time = get_pay_inerest_time(issue_date, period, i)
    while pay_interest_time < maturity_date:
        #print(pay_interest_time, pay_interest_cash)
        cash_flow_dict[pay_interest_time] = pay_interest_cash
        i = i+1
        pay_interest_time = get_pay_inerest_time(issue_date, period, i)
    #print(pay_interest_time, pay_interest_cash+amount)
    cash_flow_dict[pay_interest_time] = pay_interest_cash + amount
    return cash_flow_dict



def get_pay_inerest_time(issue_date, period, i):
    pay_interest_time = issue_date + relativedelta(months=12 * period * i+1) - datetime.timedelta(days=1)
    return pay_interest_time


if __name__ == '__main__':
    # 发行时间
    issue_date = datetime.datetime(2010, 5, 1)
    # 到日期
    maturity_date = datetime.datetime(2015, 5, 31)
    # 面值
    amount = 1000000
    # 票息
    coupon_rate = 0.02125
    # 付息时间间隔，以年为单位
    period = 0.5
    cash_flow_dict = caculate_cash_flow(issue_date, maturity_date, amount, coupon_rate, period)
    # 打印债券现金流
    for key, value in cash_flow_dict.items():
        print(key, value)