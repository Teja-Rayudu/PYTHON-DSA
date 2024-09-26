from queue import SimpleQueue as sq
def bfs(self):
    if self.root:
        visited_nodes = []
        bfs_q = sq()
        bfs_q.put(self.root)
        while not bfs_q.empty():
            current_node = bfs_q.get()
            visited_nodes.append(current_node.data)
            if current_node.left_child:
                bfs_q.put(current_node.left_child)
            if current_node.right_child:
                bfs_q.put(current_node.right_child)

        return visited_nodes
