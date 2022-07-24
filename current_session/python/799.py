class Solution:
    def champagneTower_TLE(self, poured: int, query_row: int, query_glass: int) -> float:
        # use stack (TLE)
        # time complexity: O(pour)
        glass = [ [0 for _ in range(101)] for _ in range(101) ]
        st = [(0,0,1)]
        while poured:
            tmp = []
            while st:
                r, g, c = st.pop()
                # fill this cup
                if glass[r][g] >= 1.0:
                    st.append((r+1, g, 0.5*c))
                    st.append((r+1, g+1, 0.5*c))
                else:
                    glass[r][g] += c
                    if glass[r][g] >= 1.0:
                        tmp.append((r+1, g, 0.5*c))
                        tmp.append((r+1, g+1, 0.5*c))
                    else:
                        tmp.append((r,g,c))
            poured -= 1
            st = tmp
            if glass[query_row][query_glass] == 1.0: return 1.0
        return glass[query_row][query_glass]

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # simulation, in each glass we keep the amount of pour
        # time complexity: O(R^2)
        glass = [ [0 for _ in range(101)] for _ in range(101) ]
        glass[0][0] = poured
        
        for r in range(query_row+1):
            for g in range(r+1):
                q = (glass[r][g]-1) / 2
                if q > 0:
                    glass[r+1][g] += q
                    glass[r+1][g+1] += q
        
        return min(1, glass[query_row][query_glass])