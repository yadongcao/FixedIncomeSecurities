#-*- coding: utf-8 -*-

import numpy as np
import datetime
# 两个目的
# 1、利用债券组合来构建特定到日期，票息率的债券组合。
# 2、对已知组合去分析现金流。从而得到投资组合的成本


# 将三种债券：1(1/4)s 11/30/2010, 4(7/8)s 5/31/200, 4(1/2)s 11/30/2011
# 复制为: (3/4)s 11/30/2011到期的债券
# 输出为：三种债券的面值。正数做多，负数做空

# 子债券
child_bond_dict = {
        "Bond1": {"Name": "Bond1", "Coupon": 1.25, "Maturity": "2010-11-30", "Price": 100.550, "FaceAmount": -1.779},
        "Bond2": {"Name": "Bond2", "Coupon": 4.875, "Maturity": "2011-05-31", "Price": 104.513, "FaceAmount": -1.790},
        "Bond3": {"Name": "Bond3", "Coupon": 4.5, "Maturity": "2011-11-30", "Price": 105.856, "FaceAmount": 98.166}
    }

# 组合目标债券
targe_bond = {"Name": "TargeBond", "Coupon": 0.75, "Maturity": "2011-11-30", "Price": 100.19}

def create_bond_portfolio():


    child_cashflow_array = np.array([[100+1.25/2, 4.875/2, 4.5/2],
                                    [0, 100+4.875/2, 4.5/2],
                                    [0,0,100+4.5/2]])
    targe_cashflow_array = np.array([0.75/2, 0.75/2, 100 + 0.75/2])
    result = np.dot(np.matrix(child_cashflow_array).I, targe_cashflow_array.T)
    print(result)

# 根据投资组合去计算现金流，从现金流去进一步得到组合成本
def caculate_portolio_cashflow():
    maturity_str_list = ["2010-11-30", "2011-05-31", "2011-11-30"]
    maturity_list = list()
    for i in range(len(maturity_str_list)):
        temp_maturity_str  = maturity_str_list[i]
        temp_maturity = datetime.datetime.strptime(temp_maturity_str, "%Y-%m-%d")
        maturity_list.append(temp_maturity)
    maturity_list = sorted(maturity_list)
    bond_list = ["Bond1", "Bond2", "Bond3"]

    cash_flow_list = list()
    for i in range(len(maturity_list)):
        temp_cash_flow_list = list()
        temp_maturity = maturity_list[i]
        for j in range(len(bond_list)):
            temp_bond = bond_list[j]
            temp_bond_maturity_str = child_bond_dict[temp_bond]["Maturity"]
            temp_bond_coupon = child_bond_dict[temp_bond]["Coupon"]
            temp_bond_face_amount = child_bond_dict[temp_bond]["FaceAmount"]
            temp_bond_maturity = datetime.datetime.strptime(temp_bond_maturity_str, "%Y-%m-%d")
            temp_bond_cashflow = 0
            if temp_maturity<temp_bond_maturity:
                temp_bond_cashflow = temp_bond_face_amount * (temp_bond_coupon/2)/100
                #print(temp_bond_cashflow)
            elif temp_maturity==temp_bond_maturity:
                temp_bond_cashflow = temp_bond_face_amount * (100 + temp_bond_coupon / 2) / 100
                #print(temp_bond_cashflow)
            #else:
                #print(temp_bond_cashflow)
            temp_cash_flow_list.append(temp_bond_cashflow)
        cash_flow_list.append(temp_cash_flow_list)
    #print(cash_flow_list)
    portfolio_list = list()
    for i in range(len(cash_flow_list)):
        temp_portfolio_cachflow = np.sum(cash_flow_list[i])
        #print(temp_portfolio_cachflow)
        portfolio_list.append(temp_portfolio_cachflow)

    # 计算成本。面值*价格
    cost_list = list()
    for j in range(len(bond_list)):
        temp_bond = bond_list[j]
        temp_bond_face_amount = child_bond_dict[temp_bond]["FaceAmount"]
        temp_bond_price = child_bond_dict[temp_bond]["Price"]
        temp_cost = temp_bond_face_amount * temp_bond_price/100
        cost_list.append(temp_cost)
    #print(cost_list)
    portfolio_cost = np.sum(cost_list)

    # 净收入
    target_price = targe_bond["Price"]
    net_proceeds = portfolio_cost - target_price

    #现金流矩阵
    print("现金流矩阵\n", cash_flow_list)
    # 组合现金流
    print("组合现金流\n", portfolio_list)
    # 成本
    print("成本\n", cost_list)
    # 组合成本
    print("组合成本\n", portfolio_cost)
    # 净收入
    print("净收入\n", net_proceeds)

if __name__ == '__main__':
    #create_bond_portfolio()
    caculate_portolio_cashflow()
