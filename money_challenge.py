# coding=utf-8
"""
    author: RealgodJJ
    function:
    version: 1.0
    date:
"""
import math

saving = 0


def save_money_in_n_weeks(money_per_week, increase_pace, total_week):
    """
    计算n周内的存款金额
    :return: null
    """
    # 账户金额累计
    global saving
    # 记录每周存款数的列表
    money_list = []

    for week in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        # 输出信息
        print('第{}周：存入{}元，账户累计{}元'.format(week + 1, money_per_week, saving))
        # 更新下一周的存钱金额
        money_per_week += increase_pace


def main():
    # 每周的存入金额
    money_per_week = float(input('请输入每周存入的金额：\n'))
    # 递增金额
    increase_pace = float(input('请输入每周的递增金额：\n'))
    # 存钱计划周数
    total_week = int(float(input('请输入总共的周数：\n')))

    save_money_in_n_weeks(money_per_week, increase_pace, total_week)
    print("存款金额为：{}元".format(saving))


if __name__ == '__main__':
    main()
