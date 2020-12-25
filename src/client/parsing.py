import re
import operator


def parse_board_size(message):
    message = message.replace('(', '').replace(')', '').replace(',', '').split(' ')
    return int(message[1]), int(message[2])


def parse_agents(message):
    agents = {}
    fig_info = re.findall(r'\([a-zA-Z]*\d* [a-zA-Z0-9.-]* \d*\)', message)
    for info in fig_info:
        info = info.replace('(', '').replace(')', '').split()
        agents[info[0]] = (info[1], int(info[2]))
    return agents


if __name__ == '__main__':
    print(parse_agents('agents (Q1 localhost 1234)(Q2 127.0.0.1 1221)(R3 pox-xx 245)'))
    #
    # stats = {'a': 3000, 'b': 3000, 'c': 100, 'd': 3000}
    # print([k for k, v in stats.items() if v == max(stats.values())])
