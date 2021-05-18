#-*- coding: utf-8 -*-

import datetime
#应计利息计算

# 净价即报价（quoted price 或者 flat price, clean price）: 即在交易屏幕上出现的价格
# 全价： 净价 + 应计利息。dirty price

# 应计利息有两种计算：actual/360 : 根据实际天数来，30/360 一个月按30天处理

# 举例: 3(5/8)s 8/15/19。 上一次票息支付日为: 2010-02-15,交割日：2010-06-01, 下一个付息日2010-08-15
def calculate_accrued_interest(amount, coupon_rate, last_coupon_date_str, next_coupon_date_str, delivery_date_str):
    # amount=10000
    # coupon_rate = 3.625
    #
    # last_coupon_date_str = "2010-02-15"
    # next_coupon_date_str = "2010-08-15"
    # delivery_date_str = "2010-06-01"
    last_coupon_date = datetime.datetime.strptime(last_coupon_date_str, "%Y-%m-%d")
    next_coupon_date = datetime.datetime.strptime(next_coupon_date_str, "%Y-%m-%d")
    delivery_date = datetime.datetime.strptime(delivery_date_str, "%Y-%m-%d")
    coupon_period_days = (next_coupon_date-last_coupon_date).days
    seller_coupon_period_days = (delivery_date-last_coupon_date).days
    buyer_coupon_period_days = (next_coupon_date-delivery_date).days
    coupon_payment = amount * coupon_rate/2
    seller_coupon_payment = coupon_payment * seller_coupon_period_days/coupon_period_days/100
    buyer_coupon_payment = coupon_payment * buyer_coupon_period_days / coupon_period_days/100
    accrued_interest = round(seller_coupon_payment, 2)
    return accrued_interest


def sample():
    amount = 10000
    coupon_rate = 3.625

    last_coupon_date_str = "2010-02-15"
    next_coupon_date_str = "2010-08-15"
    delivery_date_str = "2010-06-01"
    accrued_interest = calculate_accrued_interest(amount, coupon_rate, last_coupon_date_str,
                                                  next_coupon_date_str, delivery_date_str)

    print("示例中应计利息为：", accrued_interest)

if __name__ == '__main__':
    sample()