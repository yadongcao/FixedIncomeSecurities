#-*- coding: utf-8 -*-

import pandas as pd
import datetime

# 计算全价（full）跟净价(flat)
# 全价: 全价等与净价+累计利息
# 净价: 债券的市场报价

# 根据Table_1.2.csv 数据计算贴现因子
# 半年付息一次
# 2010年5月28日

def cacualte_discount_factor():
    print("根据Table_1.2.csv计算贴现因子")
    dataframe = pd.read_csv("./data/Table_1.2.csv")
    dataframe["Coupon"] = dataframe["Coupon"].apply(lambda x:float(x.split("%")[0]))
    dataframe["Maturity"] = dataframe["Maturity"].apply(lambda x: datetime.datetime.strptime(x, "%m/%d/%Y"))
    # 票面价格
    par_value = 100
    discount_factor = list()
    for i in range(dataframe.shape[0]):
        temp_coupon = dataframe["Coupon"][i]
        temp_maturity = dataframe["Maturity"][i]
        temp_price = dataframe["Price"][i]
        temp_discount_factor = 0
        discount_factor_len = len(discount_factor)
        temp_value = 0
        if discount_factor_len > 0:
            for i in range(discount_factor_len):
                temp_value = temp_value + temp_coupon / 2 * discount_factor[i]
        temp_discount_factor = (temp_price - temp_value)/(par_value + temp_coupon/2)
        temp_discount_factor = round(temp_discount_factor, 5)
        discount_factor.append(temp_discount_factor)
        print(temp_discount_factor)
    dataframe["DiscountFactor"] = discount_factor
    dataframe.to_csv("./data/Table_1.3.csv", index=False)

if __name__ == '__main__':
    cacualte_discount_factor()