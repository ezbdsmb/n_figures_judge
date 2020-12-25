from client.parsing import parse_agents
from client.udpclient import UDPClient
import random
import operator


class Judge(UDPClient):
    def __init__(self, server_addr):
        super().__init__()

        self.server_addr = server_addr
        self.agents_addr = None
        self.positions = {}

    def find_new_position(self, agent):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        while (x, y) in self.positions.values():
            x = random.randint(0, 8)
            y = random.randint(0, 8)

        self.positions[agent] = (x, y)
        return x, y

    def run(self):
        # send init
        self.sendto('init_judge', self.server_addr)
        print('send init_judge')


        # receive init ok
        data, addr = self.recvfrom()
        print('received:', data)
        # TODO: check ok

        # receive agents
        data, addr = self.recvfrom()
        self.agents_addr = parse_agents(data)
        print('received:', data)

        # send init positions
        mes = 'change_pos '
        for agent in self.agents_addr:
            x, y = self.find_new_position(agent)
            mes += f'({agent} {x} {y})'
        self.sendto(mes, self.server_addr)
        print('send:', mes)

        while True:
            # receive collisions
            collisions = {}
            for i in range(len(self.agents_addr)):
                data, addr = self.recvfrom()
                print('received:', data)

                coll_key = list(self.agents_addr.keys())[list(self.agents_addr.values()).index(addr)]
                coll_val = len(data.split(' '))

                collisions[coll_key] = coll_val

            # send agent to move
            max_idx = [k for k, v in collisions.items() if v == max(collisions.values())]

            agent = max_idx[random.randint(0, len(max_idx))]
            x, y = self.find_new_position(agent)
            self.sendto(f'change_pos ({agent} {x} {y})', self.server_addr)
            print('send:', f'change_pos ({agent} {x} {y})')


if __name__ == '__main__':
    judge = Judge(("localhost", 9998))
    judge.run()
