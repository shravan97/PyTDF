from .Operation import Operation

class CallableGenerator(object):
    """
    Class that generates
    mapper and reducer functions

    """
    def __init__(self, root_node):
        self.root_node = root_node

    def _dfs(self, node, prev = 't', ops = []):
        """
        Method that does a depth-first
        traversal and takes note of the 
        necessary operations to carry out

        """

        ops_copy = list(ops)

        if not node.operation: # If root
            for n in node.next_nodes:
                self._dfs(n)
            return

        if node.operation.is_action():
            self.actions+=1
            
            ops_copy.append(node.operation)
            
            new_var_name = "ta"+str(self.actions)
            self.operations.append((new_var_name, prev, ops_copy))
            self.action_node_map[new_var_name] = node

        else:
            if len(node.next_nodes) != 1:
                self.tfs+=1

                ops_copy.append(node.operation)
                
                cur = 'tt'+ str(self.tfs)
                self.operations.append((cur, prev, ops_copy))
                new_tuple = (cur, [])
            
            else:
                ops_copy.append(node.operation)
                new_tuple = (prev, ops_copy)

            for n in node.next_nodes:
                self._dfs(n, *new_tuple)


    def get_callable(self):
        """
        Function that converts a given
        graph onto a mapper function and 
        returns the same

        """

        self.root_node._graph_prune()

        def mapper(t, node=None, return_vals=[], return_nodes=[]):
            ## TODO : Somehow remove references to any Node object 
            ## for this to work on Spark

            if not node:
                node = self.root_node
            else:
                t = getattr(t, node.operation.name)(*node.operation.args, **node.operation.kwargs)
                if node.operation.is_action():
                    return_vals.append(t)
                    return_nodes.append(node)

            for n in node.next_nodes:
                mapper(t, n, return_vals)

            return (return_vals, return_nodes)

        return mapper

    def get_reducer_callable(self):
        """
        A method that returns a 
        generalized reducer function 

        TODO(shravan97)

        """
        pass