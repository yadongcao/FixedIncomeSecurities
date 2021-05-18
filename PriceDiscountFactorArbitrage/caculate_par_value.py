#-*- coding: utf-8 -*-

import datetime
import pandas as pd

# 根据贴现因子（Table_1.3.csv）, 计算债券的价格。再将债券现值做对比。来寻找套利机会

# 示例:
# 2010年5月28日
# 2011年11月30日3/4债券


def caculate_par_value(caculate_date_str, bond_maturity_str, coupon_rate, price):
    pv = 0
    print("计算债券票面值")
    caculate_date = datetime.datetime.strptime(caculate_date_str, "%Y-%m-%d")

    bond_maturity = datetime.datetime.strptime(bond_maturity_str, "%Y-%m-%d")
    # 读取贴现因子数据集
    dateparse = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d')
    dataframe = pd.read_csv("./data/Table_1.3.csv",  parse_dates=['Maturity'], date_parser=dateparse)

    temp_dataframe = dataframe[(dataframe["Maturity"] > caculate_date) &(dataframe["Maturity"] <=bond_maturity)]
    rows = temp_dataframe.shape[0]
    for i in range(rows-1):
        pv = pv + temp_dataframe["DiscountFactor"][i] * coupon_rate/2
    pv = pv + (100 + coupon_rate/2) * temp_dataframe["DiscountFactor"][rows-1]
    pv = round(pv, 3)
    return pv

def sample():
    caculate_date_str = "2010-5-28"

    bond_maturity_str = "2011-11-30"
    coupon_rate = 0.75
    price = 100.190
    pv = caculate_par_value(caculate_date_str, bond_maturity_str, coupon_rate, price)
    print("3/4s11/30/11", "PV", pv, "Price", price, "PV-Price", round(pv - price, 3))


    bond_maturity_str = "2011-05-31"
    coupon_rate = 0.875
    price = 100.549
    pv = caculate_par_value(caculate_date_str, bond_maturity_str, coupon_rate, price)
    print("7/8s5/31/11", "PV", pv, "Price", price, "PV-Price", round(pv - price, 3))

    bond_maturity_str = "2012-05-31"
    coupon_rate = 0.75
    price = 99.963
    pv = caculate_par_value(caculate_date_str, bond_maturity_str, coupon_rate, price)
    print("7/8s5/31/11", "PV", pv, "Price", price, "PV-Price", round(pv - price, 3))



if __name__ == '__main__':
    sample()
