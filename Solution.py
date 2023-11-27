from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys

class Solution:

    def __init__(self, problem, isp, graph, info):
        self.problem = problem
        self.isp = isp
        self.graph = graph
        self.info = info

    def output_paths(self):
        paths, updated_bandwidths, priorities = {}, {}, {}
        bfspaths = bfs_path(self.graph, self.isp, self.info["list_clients"])
        i = 0
        for client in self.info["list_clients"]:
            i += 1
            paths[client], updated_bandwidths[client] = self.newbfs(client, bfspaths[client], self.info)
            print("done with client: ", i)

        return (paths, updated_bandwidths, priorities)

    def newbfs(self, client, bfspath, info):
        visited = set()
        q = deque([(self.isp, [self.isp], 0)])
        tolerance = info["alphas"][client] * len(bfspath)
        path = None
        updated_bandwidth = info["bandwidths"].copy()  # Start with the original bandwidths

        while q:
            node, current_path, timestep = q.popleft()

            if node == client and timestep <= tolerance:
                path = current_path
                break

            if node in visited:
                continue

            visited.add(node)

            for neighbor in self.graph.get(node, []):
                newtime = timestep + 1

                if newtime > tolerance:
                    continue

                newpath = list(current_path)
                newpath.append(neighbor)
                q.append((neighbor, newpath, newtime))

                # Add logic to update bandwidths based on the solution
                # Here, you can check if the neighbor is a router and update its bandwidth
                if neighbor != client and neighbor in updated_bandwidth:
                    updated_bandwidth[neighbor] += 1  # Update bandwidth by 1 (you can adjust this based on your solution)

        return path, updated_bandwidth
        # """
        # This method must be filled in by you. You may add other methods and subclasses as you see fit,
        # but they must remain within the Solution class.
        # """

        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        # return (paths, bandwidths, priorities)
