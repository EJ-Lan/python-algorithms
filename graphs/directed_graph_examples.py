from reverse import reverse

simple =  {  'A': ['B', 'C'],
             'B': ['C'],
             'C': []
          }

lecture29_slide29 =  {  'A': ['B', 'G'],
                        'B': [],
                        'C': ['A', 'E'],
                        'D': ['H', 'J'],
                        'E': ['D', 'F', 'J'],
                        'F': ['G'],
                        'G': [],
                        'H': [],
                        'J': []
                     }
                     
# remove two out edges from E to disconnect the DAG 
# into two components, still a DAG
lecture29_slide29b =  {  'A': ['B', 'G'],
                        'B': [],
                        'C': ['A', 'E'],
                        'D': ['H', 'J'],
                        'E': ['F'],
                        'F': ['G'],
                        'G': [],
                        'H': [],
                        'J': []
                     }
                     
lecture29_slide30 =  {  'A': ['B', 'G'],
                        'B': [],
                        'C': ['A', 'E'],
                        'D': ['H', 'J'],
                        'E': ['D', 'F', 'J'],
                        'F': ['G'],
                        'G': ['H'],
                        'H': [],
                        'J': []
                     }

lecture29_slide32_cycle =  {  1: [2,3],
                              2: [],
                              3: [4],
                              4: [1,2,5],
                              5: [],
                              6: [3,5,7],
                              7: [3]
                           }

lecture30_slide18 = { 1: [3,4],
                      2: [1],
                      3: [2],
                      4: [5],
                      5: [6],
                      6: [4]
                    }

# Note: I sorted the adj. lists to match the dfs order in slide 19
lecture30_slide19 =  {  'C': ['D'],
                        'A': ['F'],
                        'B': ['K'],
                        'D': ['E', 'H', 'B'],
                        'E': [],
                        'F': ['G', 'C', 'E'],
                        'G': ['A', 'C'],
                        'H': ['B', 'C'],
                        'K': ['B']
                     }

# Sam graph, different dfs order (after D) as in slide 22
lecture30_slide22 =  {  'C': ['D'],
                        'A': ['F'],
                        'B': ['K'],
                        'D': ['H', 'E', 'B'],
                        'E': [],
                        'F': ['G', 'C', 'E'],
                        'G': ['A', 'C'],
                        'H': ['B', 'C'],
                        'K': ['B']
                     }


bookfigure3point7 =  {  'A': ['B', 'C', 'F'],
                        'B': ['E'],
                        'C': ['D'],
                        'D': ['A', 'H'],
                        'E': ['F', 'G', 'H'],
                        'F': ['B', 'G'],
                        'G': [],
                        'H': ['G']
                     }

bookfigure3point8 =  {  'A': ['C'],
                        'B': ['A', 'D'],
                        'C': ['E', 'F'],
                        'D': ['C'],
                        'E': [],
                        'F': []
                     }

bookfigure3point9 =  {  'A': ['B'],
                        'B': ['C','D','E'],
                        'C': ['F'],
                        'D': [],
                        'E': ['B', 'F', 'G'],
                        'F': ['C', 'H'],
                        'G': ['H', 'J'],
                        'H': ['K'],
                        'I': ['G'],
                        'J': ['I'],
                        'K': ['L'],
                        'L': ['J']
                     }

bookfigure3point10 = reverse(bookfigure3point9)