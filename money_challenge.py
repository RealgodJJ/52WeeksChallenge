# coding=utf-8
"""
    author: RealgodJJ
    function:
    version: 1.0
    date:
"""


def main():
    # 每周的存入金额
    money_per_week = 10
    # 记录周数
    week = 1
    # 递增金额
    increase_pace = 10
    # 存钱计划周数
    total_week = 52
    # 账户金额累计
    saving = 0

    while week <= 52:
        saving += money_per_week

        # 更新下一周的存钱金额
        money_per_week += increase_pace
        week += 1

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(week, money_per_week, saving))


if __name__ == '__main__':
    main()
