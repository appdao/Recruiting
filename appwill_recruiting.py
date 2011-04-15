# -*- coding: utf-8 -*-

"""
移动互联网公司Appwill招聘研发和运维护工程师:

"""


import sys
# Thanks to  http://code.activestate.com/recipes/577058/
def query_yes_no(question, default="no"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes":1,   "y":1,  "ye":1,
             "no":0,     "n":0}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")


must_have_list = [[
     "你身手敏捷，视墙如无物, 时常出去看看外面的世界如Facebook, Twitter, StumbleUpon?",
     "你可以熟练使用英语, 经常翻阅英文技术文档解决问题, 甚至浏览英文新闻站点获取第一手信息?",
     "你熟悉开源世界, 对GNU, FreeBSD, Linux耳熟能详, 也知道Mac OS X是怎么来的?",
     "你热爱技术, 富有激情, 做事主动, 相信技术可以让人们生活的更美好, 喜欢写程序来搞定单调乏味的工作?",
     "你思维活跃，富有想象力, 喜欢新奇的产品, 关注Geek相关产品新闻?",
     "你喜欢科幻小说,电影, 知道HHGTG, 喜欢美剧Star trek, StarGate...?",
     "你喜欢看美剧<生活大爆炸>?",
     "你现在的开发环境为Linux或Mac OS X?",
     "热爱Linux?",
     ],5]
 
pos_list = []
pos_list.append([[
    "你热爱编程,看到有趣的网站都要研究下怎么实现?",
    "你熟悉Python, 并且了解C,C++,Go,Ruby,PHP,Lisp,Erlang其中任意一种?",
    "你了解Web开发基本常识: XML, JSON, REST, COMET, Ajax?",
    "你熟悉MVC机制, 尝试过自己编写MVC开发框架(用其他语言尝试亦可)?",
    "你研究过列数据库, BigTable, Cassandra, Hadoop均可?",
    "你熟悉关系数据库,了解PostgreSQL?",
    "你了解Pylons框架?",
    "你熟悉Key-Value存储机制, 能够说出其优缺点?",
    "你熟悉常用的网站性能优化方案?",
    "你非常熟悉Linux或MacOSX常用命令行工具, 熟练使用Vim或Emacs做为开发工具?",
    "你喜欢并自信能实现易于扩展，能支撑海量并发访问的Web服务?",
    "你了解社会化推荐相关知识或对其有浓厚兴趣?"
    ],7])


pos_list.append([[
    "你参加过Velocity大会?",
    "你喜欢研究高并发网站架构, 对每个大型web站点(有公开分享过的)的技术方案、目前负载、服务器规模耳熟能详, 如Facebook, Youtube, Reddit?",
    "你研究过Amazon云算计相关服务, 使用过S3, EC2, Cloudfront等等?",
    "你订阅stevesouders.com并读过相关著作?",
    "你了解负载均衡的几种方案, 研究过HAProxy, LVS?",
    "你熟悉TCP/IP协议, 知道路由、交换机的工作机制, 以及网络相关参数的优化?",
    "你使用过tcpdump, traceroute, netstat, strace等工具分析调试系统及服务当前状况?",
    "你接触过各种编程语言, 脚本(bash, PHP, Python, Perl), 以及正则表达式?",#不会写程序的DBA不是好运维
    "你了解DBA相关的简单知识, 使用过PostgreSQL, MySQL, 了解负载均衡方案，主从模式?",
    "你熟悉Nginx, 熟练编写配置文件(rewrite, if判断, 反向代理等等), 了解有关性能调优相关参数?",
    "你熟悉服务端备份、同步、服务监控流程, 写过相关脚本?",
    "你了解iptables, SELinux, 知道如何防范常见的攻击并具备良好的运维习惯?"
    ],7])

pos_list.append([[
    "你熟读<精通Web Analytics>和<集体智慧编程>--Programming Collective Intelligence?",
    "你熟悉数据挖掘基本算法, 理解基本的统计学知识?",
    "你熟悉Linux, 精通一种或了解多种脚本语言(Python, PHP, Perl, Ruby, Shell, Ack,Sed等)，具有良好的编程功底?",
    "你熟练使用Google Analytics或类似工具, 了解常见的网站分析概念, 转化率, 路径分析?",
    "你熟悉SPSS或SAS等统计软件或者Weka、YALE 等数据挖掘软件?",
    "你熟练使用关系型数据库并了解NoSQL基本知识?",
    "你具备优秀的沟通和表达能力?",
    "你好奇心强, 非常想知道海量数据中到底蕴藏着哪些不为人知的秘密?"
    ],5])



about_us = """

关于我们:

我们是一个充满激情、处于高速发展阶段的移动互联网团队，现有产品在iPhone和Android平台上有数百万用户。

听说过我们团队的朋友可能知道我们做过一些大众产品(壁纸图片等)，我们的原则是
不管做什么，简单还是复杂，都要做到最好,做到用户满意(可以拿我们的产品和其他
同类的对比下), 并开发了广受好评的反馈系统来实现这个目的。

对于每个新加入的团队成员都有很高的要求, 倒不是说学历和技术, 学历可以造假, 技术可以培养,
我们最关心的是一个人学习和掌握新知识、适应变化的能力, 做事的主动性和追求完美的精神。

移动互联网领域日新月异，新的技术和可能性层出不穷, 没有很好的学习和应变能力，就没有办法跟随行业的脚步；
而没有做事的主动性和追求完美的精神, 则无法跟随团队的脚步。

通过考核后，我们会提供有竞争力的待遇，休闲的工作环境和灵活的工作时间，

融洽的工作气氛, 民主的、扁平化的管理方式，以及难得的成长机遇, 不只是技术，
也许是是市场，运营，策划, 你都可以提出自己的想法、实际参与，并很快得到
真实用户的反馈再进行调整，如此不断迭代的过程中了解移动互联网产品的工作流程。

如果你对移动互联网有浓厚兴趣，相信通过技术可以使人们的生活更加美好；
如果你充满激情同时又能非常踏实，愿意一步一个脚印将产品做到完美；
让我们一起努力，为移动互联网行业添砖加瓦，共同创造属于自己和大家的美好未来!

"""


def tranversal_q(pos_list):
    res = 0
    for item in pos_list:
        res = res + query_yes_no(item) 
    return res

def choose_pos():
    
    pos_info = """
    请选择您期望的职位:

        1): * 服务端Python开发工程师
            *
            * 负责:
            * 1, 维护云端代码，设计架构, 为移动终端提供良好支撑
            * 2, 未来各项服务的功能的设计和改进

        2): * Linux服务器运维工程师
            *
            * 负责让各个服务器有序、和谐、公平、轻松的运行, 并高效的协作

        3): * 数据挖掘工程师
            *
            * 负责从海量日志中分析移动终端用户行为、偏好、习惯，帮助产品定位、决策
    请选择[1,2,3]: 
    """
    pos = 0
    while pos not in [1,2,3]:
        print pos_info
        choice = raw_input()
        pos = 0
        try:
            pos = int(choice)
        except ValueError:
            pass 
    return pos-1 
    #print query_yes_no("hi")

def check_list(pos_list):
    res = tranversal_q(pos_list[0])
    if res > pos_list[1]:
        return True
    return False

def output(outstr):
    print_sep()
    print outstr
    print_sep()


def print_sep():
    print "*" * 60



if __name__ == '__main__':

    if query_yes_no("你没有工作经验?"):
        output("没关系, 继续!")

    if not check_list(must_have_list):
        output("您可能很优秀, 不过不是我们要找的类型, sorry...")
        sys.exit(0)

    pos = choose_pos()
    if(check_list(pos_list[pos])):
        output("\n\n太油菜了！ 心动不如行动,  赶紧发简历作品到hr#appwill.com, 期待与您一起携手共创美好未来! \n\n" + about_us)
        
    else:
        output("您可能很优秀, 不过不是我们要找的类型, sorry...")


