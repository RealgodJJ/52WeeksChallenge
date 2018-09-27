# coding=utf-8
"""
    author: RealgodJJ
    function:
    version: 1.0
    date:
"""
import math
import datetime

num = 1


def num_change(num):
    """
    change the number in local not global
    :param num: number
    :return: null
    """
    num = 2


def save_money_in_n_weeks(money_per_week, increase_pace, total_week):
    """
    计算n周内的存款金额
    :return: null
    """
    # 记录每周存款数的列表
    money_list = []
    # 每周账户累计金额
    saved_money_list = []

    for week in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)
        # 输出信息（用于调试）
        # print('第{}周：存入{}元，账户累计{}元'.format(week + 1, money_per_week, saving))
        # 更新下一周的存钱金额
        money_per_week += increase_pace

    return saved_money_list


def main():
    # 每周的存入金额
    money_per_week = float(input('请输入每周存入的金额：\n'))
    # 递增金额
    increase_pace = float(input('请输入每周的递增金额：\n'))
    # 存钱计划周数
    total_week = int(float(input('请输入总共的周数：\n')))

    saved_money_list = save_money_in_n_weeks(money_per_week, increase_pace, total_week)
    print("总存款金额为：{}元".format(saved_money_list[saved_money_list.__len__() - 1]))

    input_date_str = input('请输入日期(yyyy/mm/dd)：\n')
    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')
    week_num = input_date.isocalendar()[1]
    # week_num = int(input('请输入第几周：\n'))
    print('第{}周的存款金额为{}元'.format(week_num, saved_money_list[week_num - 1]))

    print('=================关于全局变量和局部变量的测试===================')
    num_change(num)
    print(num)


if __name__ == '__main__':
    main()
