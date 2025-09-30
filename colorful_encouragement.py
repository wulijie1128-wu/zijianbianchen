#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import datetime
import os
from typing import List

# Windows颜色代码
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def enable_colors():
    """启用Windows命令行颜色支持"""
    if os.name == 'nt':  # Windows
        os.system('color')
        # 启用ANSI转义序列支持
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except:
            pass

class ColorfulEncouragementCard:
    def __init__(self):
        enable_colors()

        self.encouragements = [
            "今天写的每一行代码，都让你更强大！",
            "bug不是失败，是学习的机会！",
            "每个程序员都曾是初学者，坚持就是胜利！",
            "代码的世界很大，你的潜力更大！",
            "今天解决的问题，明天就是你的经验！",
            "新的一天，新的开始，新的可能！",
            "你比你想象的更勇敢，更强大！",
            "每一个今天，都是改变的起点！",
            "相信自己，你已经走了很远的路！",
            "困难只是成长路上的垫脚石！",
            "今天的努力，是明天的骄傲！",
            "你的努力，时间都看得见！",
            "小步前进，也是进步！",
            "每一次尝试，都让你更接近成功！",
            "今天是创造美好的好日子！",
            "记得照顾好自己，你很重要！",
            "休息不是浪费时间，是为了走更远的路！",
            "你已经很棒了，继续保持！",
            "慢慢来，比较快！",
            "给自己一个拥抱，你辛苦了！",
        ]

        self.morning_quotes = [
            "早安！新的一天充满新的希望！",
            "晨光照耀，梦想启航！",
            "今天要做最好的自己！",
            "早起的鸟儿有虫吃，加油！",
        ]

        self.evening_quotes = [
            "今天辛苦了，为自己点个赞！",
            "夜深了，记得早点休息！",
            "今天的收获，是明天的基础！",
            "晚安，明天继续加油！",
        ]

    def get_daily_card(self) -> str:
        current_time = datetime.datetime.now()
        hour = current_time.hour
        date_str = current_time.strftime("%Y年%m月%d日")
        weekday = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"][current_time.weekday()]

        if 6 <= hour < 12:
            quote = random.choice(self.morning_quotes)
            time_period = "早上"
            quote_color = Colors.YELLOW  # 早上用黄色
        elif 18 <= hour < 24:
            quote = random.choice(self.evening_quotes)
            time_period = "晚上"
            quote_color = Colors.PURPLE  # 晚上用紫色
        else:
            quote = random.choice(self.encouragements)
            time_period = "今天"
            quote_color = Colors.GREEN  # 其他时间用绿色

        card = self._create_colorful_card(date_str, weekday, time_period, quote, quote_color)
        return card

    def get_random_encouragement(self) -> str:
        quote = random.choice(self.encouragements)
        return f"{Colors.CYAN}{quote}{Colors.END}"

    def _create_colorful_card(self, date: str, weekday: str, time_period: str, quote: str, quote_color: str) -> str:
        border = "=" * 50

        card = f"""
{Colors.CYAN}+{border}+{Colors.END}
{Colors.CYAN}|{Colors.END}{Colors.BOLD}{Colors.WHITE}                    每日鼓励卡片                    {Colors.END}{Colors.CYAN}|{Colors.END}
{Colors.CYAN}+{border}+{Colors.END}
{Colors.CYAN}|{Colors.END}                                                  {Colors.CYAN}|{Colors.END}
{Colors.CYAN}|{Colors.END}  {Colors.BLUE}日期:{Colors.END} {Colors.YELLOW}{date} {weekday}{Colors.END}                     {Colors.CYAN}|{Colors.END}
{Colors.CYAN}|{Colors.END}  {Colors.BLUE}时间:{Colors.END} {Colors.GREEN}{time_period}{Colors.END}                                           {Colors.CYAN}|{Colors.END}
{Colors.CYAN}|{Colors.END}                                                  {Colors.CYAN}|{Colors.END}
{Colors.CYAN}|{Colors.END}  {Colors.RED}今日鼓励:{Colors.END}                                       {Colors.CYAN}|{Colors.END}
{Colors.CYAN}|{Colors.END}                                                  {Colors.CYAN}|{Colors.END}
{Colors.CYAN}|{Colors.END}     {quote_color}{quote}{Colors.END}      {Colors.CYAN}|{Colors.END}
{Colors.CYAN}|{Colors.END}                                                  {Colors.CYAN}|{Colors.END}
{Colors.CYAN}|{Colors.END}  {Colors.GREEN}记住:{Colors.END} 每一天都是新的开始！                      {Colors.CYAN}|{Colors.END}
{Colors.CYAN}|{Colors.END}  {Colors.GREEN}相信:{Colors.END} 你比想象中更强大！                        {Colors.CYAN}|{Colors.END}
{Colors.CYAN}|{Colors.END}                                                  {Colors.CYAN}|{Colors.END}
{Colors.CYAN}+{border}+{Colors.END}
        """
        return card

def main():
    print(f"{Colors.BOLD}{Colors.GREEN}欢迎使用彩色每日鼓励卡片！{Colors.END}\n")

    card_generator = ColorfulEncouragementCard()

    while True:
        print(f"{Colors.YELLOW}选择功能:{Colors.END}")
        print(f"{Colors.WHITE}1.{Colors.END} {Colors.GREEN}获取今日鼓励卡片{Colors.END}")
        print(f"{Colors.WHITE}2.{Colors.END} {Colors.BLUE}获取随机鼓励语{Colors.END}")
        print(f"{Colors.WHITE}3.{Colors.END} {Colors.RED}退出{Colors.END}")

        try:
            choice = input(f"\n{Colors.CYAN}请选择 (1-3): {Colors.END}").strip()

            if choice == "1":
                print("\n" + "="*60)
                card = card_generator.get_daily_card()
                print(card)
                print("="*60)

                save = input(f"\n{Colors.YELLOW}是否保存今日记录？(y/n): {Colors.END}").strip().lower()
                if save in ['y', 'yes', '是']:
                    print(f"{Colors.GREEN}记录已保存！{Colors.END}")

            elif choice == "2":
                quote = card_generator.get_random_encouragement()
                print(f"\n{Colors.BOLD}随机鼓励: {quote}{Colors.END}\n")

            elif choice == "3":
                print(f"\n{Colors.PURPLE}愿你每天都充满正能量！再见！{Colors.END}")
                break

            else:
                print(f"{Colors.RED}无效选择，请重新输入{Colors.END}")

        except KeyboardInterrupt:
            print(f"\n\n{Colors.PURPLE}再见！记得每天鼓励自己哦！{Colors.END}")
            break
        except Exception as e:
            print(f"{Colors.RED}出现错误: {e}{Colors.END}")

if __name__ == "__main__":
    main()