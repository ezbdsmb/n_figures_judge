import re
import operator

def parse_agents(message):
    agents = {}
    fig_info = re.findall(r'\([a-zA-Z]*\d* \d*\)', message)
    for info in fig_info:
        info = info.replace('(', '').replace(')', '').split()
        agents[info[0]] = int(info[1])
    return agents


if __name__ == '__main__':
    print(parse_agents('agents (Q1 1234)(Q2 1221)(R3 245)'))

    stats = {'a': 3000, 'b': 3000, 'c': 100, 'd': 3000}
    print([k for k, v in stats.items() if v == max(stats.values())])