import networkx as nx
import itertools
import pprint
import matplotlib.pyplot as plt
from networkx import Graph


class Elimination:
    def __init__(self, in_path, in_file):
        self.max_current_w = None
        self.max_current_t = []
        self.t_lists = {}
        self.t_names = []
        self.in_path = in_path
        self.in_file = in_file
        self.team_select = None
        self.game_vertices = []
        self.team_vertices = []
        self.standings = None
        self.other_teams = []
        return

    def read_data(self):
        game_data = open(self.in_path + self.in_file, 'r')
        num_teams = game_data.readline()

        for g in game_data:
            t_temp = g.strip().split()
            self.t_lists[t_temp[0]] = t_temp
            self.t_names.append(t_temp[0])

        return self.t_lists

    def trivial_elimination(self):

        # Run data import
        Elimination.read_data(self)
        D = self.t_lists

        # Create some empty lists for parsed data
        possible_wins = []
        current_wins = []

        # Parse data and append to lists above
        for d in D:
            d_list = D[d]
            possible_wins.append(int(d_list[1]) + int(d_list[3]))
            current_wins.append(int(d_list[1]))

        #print(current_wins)

        # Find the max current win amount and team name
        self.max_current_w = max(current_wins)
        mct_indices = [i for i, x in enumerate(current_wins) if x == self.max_current_w]
        for t in range(len(mct_indices)):
            self.max_current_t.append(self.t_names[t])

        # Loop through teams and print who's trivially eliminated
        d_lists = list(D.values())
        te_list = []
        for d in range(len(d_lists)):
            if d != mct_indices:
                cw = current_wins[d]
                pw = possible_wins[d]
                t = d_lists[d][0]
                if pw < self.max_current_w:
                    te_list.append(t)

        return te_list

    def make_vertices(self):

        # Set up team lists
        all_teams = self.t_names
        team_select = self.team_select
        other_teams = all_teams.copy()
        del other_teams[other_teams.index(team_select)]

        # Take the team list and find combinations for matchups
        game_vertices = []
        for L in range(0, len(other_teams) + 1):
            l = 0
            for m in itertools.combinations(other_teams, L):
                if len(m) == 2:
                    game_vertices.append((f'{other_teams.index(m[0])}-{other_teams.index(m[1])}'
                                          , {"game_vertices": f'{other_teams.index(m[0])}-{other_teams.index(m[1])}'}))
                    l += 1

        # Create list for team vertices nodes
        team_vertices = []
        for t in range(len(other_teams)):
            team_vertices.append((t, {"team_vertices": f'{other_teams[t]}'}))

        # Store the vertices to corresponding attributes
        self.game_vertices = game_vertices
        self.team_vertices = team_vertices
        self.other_teams = other_teams


    def node_assignment(self):

        # Instantiate the graph object
        self.standings = nx.DiGraph()

        # Count the number of nodes in game vertices
        mc_node_ct = len(self.game_vertices)

        # Combine game and team vertices
        total_nodes = self.game_vertices + self.team_vertices

        # Add nodes for source, game / team vertices, and sink
        self.standings.add_node("source")
        self.standings.add_nodes_from(total_nodes)
        self.standings.add_node("sink")

    def make_edges(self):

        # Localize the selected team and other attributes
        team_select = self.team_select
        r_games_all = self.t_lists
        other_teams = self.other_teams
        game_vertices = self.game_vertices

        # Identify the index for team we're evaluating, and drop from data
        t_drop_index = self.t_names.index(team_select)
        r_games_x_node = r_games_all.copy()
        del r_games_x_node[team_select]

        g_edge_wt_sum = 0
        # Add edge weights from source to game vertices, and game to team vertices
        for L in range(0, len(other_teams) + 1):
            l = 0
            for m in itertools.combinations(other_teams, L):
                if len(m) == 2:
                    # Loop through game vertices to grab teams
                    t1 = int(game_vertices[l][1]['game_vertices'].split('-')[0])
                    t2 = int(game_vertices[l][1]['game_vertices'].split('-')[1])
                    gv = game_vertices[l][0]
                    # print(gv)

                    # Grab game counts for team matchups, starting with list for first team in game vertex
                    games_left_l = r_games_x_node[other_teams[t1]][4:]

                    # Drop count for team we're evaluating
                    del games_left_l[t_drop_index]
                    # print(games_left_l)

                    # Select games left for second team in game node (node)
                    #print(games_left_l)
                    #print(t2)
                    games_left = int(games_left_l[t2])
                    # print(r_games_x_node[other_teams[l]][4:])
                    # print(t1, t2)
                    # print(games_left)

                    # Set the edge weight for source to game vertices node
                    self.standings.add_edge("source", gv, capacity=games_left)
                    # print(f'games left is {games_left}')

                    # Calculate the sum of the edge weights
                    g_edge_wt_sum = g_edge_wt_sum + games_left

                    # Set the edge weight for game to team vertices to infinity
                    self.standings.add_edge(gv, t1, capacity=float('inf'))
                    self.standings.add_edge(gv, t2, capacity=float('inf'))

                    # Increment the loop count
                    l += 1

                    #print(f'gv node is {gv}')
                    #print(f'team 1 is {t1}')
                    #print(f'team 2 is {t2}')
                    #print(f'games_left edge weight is {games_left}')

        # Set final edge weights from team vertices to sink node
        for t in other_teams:
            # Pull data for selected team
            e_team_data = r_games_all[team_select]

            # Get values for wins and remaining games
            e_w = int(e_team_data[1])
            e_r = int(e_team_data[3])

            # Get values for wins for loop team
            l_team_data = r_games_all[t]
            l_w = int(l_team_data[1])

            #print('Flow edge weight is:')
            #print(e_w + e_r - l_w)

            self.standings.add_edge(other_teams.index(t), 'sink', capacity=e_w + e_r - l_w)

        return g_edge_wt_sum

    def output_results(self, team_select):

        self.team_select = team_select

        # Run process through edge creation
        Elimination.make_vertices(self)
        Elimination.node_assignment(self)
        Elimination.make_edges(self)

        """
        print('**********************************')
        print(f'RUNNING CODE FOR {self.team_select.upper()}')
        print('**********************************')
        print()
        print(f'REMAINING TEAMS ARE:')
        print(self.other_teams)
        print()
        print(f'NODES THAT ARE CREATED INCLUDE (source, matchups, teams, sink)')
        pprint.pprint(list(self.standings.nodes()))
        print()
        print(f'EDGES THAT ARE CREATED ARE (start, end):')
        pprint.pprint(list(self.standings.edges()))
        print()
        # Get the edge weights
        edge_weights = nx.get_edge_attributes(self.standings, 'capacity')
        print(f'THE EDGE CAPACITIES ARE:')
        pprint.pprint(edge_weights)
        """
        #print()
        flow_value = nx.maximum_flow_value(self.standings, 'source', 'sink')
        #print(Elimination.make_edges(self))
        g_edge_wt_sum = Elimination.make_edges(self)
        #print(f'flow value is {flow_value}')
        #print(f'edge wt sum is {g_edge_wt_sum}')

        #print()
        if flow_value < g_edge_wt_sum:
            print(f'{self.team_select} is eliminated')
        else:
            print(f'{self.team_select} is not eliminated')


def main():

    myfiles = ['ivy_league.txt', 'mlb.txt', 'potter.txt', 'world_cup.txt']

    for f in myfiles:

        e = Elimination('../../support/', f)
        te_print = e.trivial_elimination()

        # Instantiate elimination object
        for m in e.t_names:
            if m in te_print:
                pass
            else:
                e.output_results(m)
            if m in te_print:
                print(f'{m} has been trivially eliminated by {e.max_current_t[0]}')
            else:
                pass
        print()

if __name__ == '__main__':
    main()
