class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        def get_path_to_region(region, graph, curr_node, path):
            path.append(curr_node)
            if curr_node == region:
                return path[:]
            
            if curr_node in graph:
                for neig in graph[curr_node]:
                    result = get_path_to_region(region, graph, neig, path)
                    if result:
                        return result
            path.pop()
            return None
        
        tree = {}
        
        for lista in regions:
            parent = lista[0]
            if parent not in tree:
                tree[parent] = []
            for i in range(1, len(lista)):
                tree[parent].append(lista[i])
                

        path1 = get_path_to_region(region1, tree, regions[0][0], [])
        path2 = get_path_to_region(region2, tree, regions[0][0], [])
        

        i = min(len(path1) - 1, len(path2) - 1)
        while i > 0 and path1[i] != path2[i]:
            i -= 1
        
        if path1[i] == path2[i]:
            return path1[i]
        
        else:
            return None
