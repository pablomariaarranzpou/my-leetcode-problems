class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        max_pos = 0
        pos_x, pos_y = 0, 0
        dir_i = 1
        obst_f = False
        
        obstacles = {tuple(o) for o in obstacles}
        
        for i in commands:
            
            if i == -1:
                dir_i = (dir_i  + 1)% 4
                obst_f = False
                
            elif i == -2:
                dir_i = (dir_i  - 1) % 4
                obst_f = False
            else:
                
                if obst_f:
                    continue
                if dir_i == 0:
                    for i in range(i):                       
                        if (pos_x - 1, pos_y) in obstacles:
                            obst_f = True
                            break
                        pos_x -= 1
                    
                elif dir_i == 1:
                    for i in range(i):                       
                        if (pos_x, pos_y + 1) in obstacles:
                            obst_f = True
                            break
                        pos_y += 1
                    
                elif dir_i == 2:
                    for i in range(i):                       
                        if (pos_x + 1, pos_y) in obstacles:
                            obst_f = True
                            break
                        pos_x += 1
                    
                else:
                    for i in range(i):                       
                        if (pos_x, pos_y - 1) in obstacles:
                            obst_f = True
                            break
                        pos_y -= 1
                    
                max_pos = max(max_pos, pow(pos_y, 2) + pow(pos_x, 2))     
                
        return max_pos
                    
                    
                
            
        
        