import random
import LatLon
import copy


class Delivery:
    def __init__(self, delivery_execs_list, orders_list, scoring_func):
        #convert lists to map
        self.delivery_execs = {}
        for d in delivery_execs_list:
            self.delivery_execs[d] = 1

        self.orders = {}
        for o in orders_list:
            self.orders[o] = 1

        self.scoring_func = scoring_func

        self.best_score = 0.0
        self.best_match = {}



    def delivery_helper(self, de_map, score_so_far):
        for de in self.delivery_execs:
            for order in self.orders:
                del self.delivery_execs[de]
                del self.orders[order]
                de_map[de] = order
                score_with_assignment = score_so_far + self.scoring_func(de, order)
                if score_with_assignment > self.best_score:
                    best_score = score_with_assignment
                    # can use cPickle instead of deepcopy for perf, but makes code less readable
                    self.best_match = copy.deepcopy(de_map)
                    self.best_score = score_with_assignment
                self.delivery_helper(de_map, score_with_assignment)

                # try without assignment
                self.delivery_execs[de] = 1
                self.orders[order] = 1
                del de_map[de]

        return self.best_score

    def assign(self):
        de_map = {}
        self.delivery_helper(de_map,0)
        return self.best_match, self.best_score
