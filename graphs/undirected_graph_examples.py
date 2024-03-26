slides_example =  { 1: [3, 5],
                    2: [4, 5],
                    3: [1, 4, 5],
                    4: [2, 3, 6],
                    5: [1, 2, 3],
                    6: [4]
                  }

slides_example_reordered =  { 4: [6, 2, 3],
                    1: [3, 5],
                    2: [4, 5],
                    3: [1, 4, 5],
                    5: [1, 2, 3],
                    6: [4]
                  }

western_canada = { 'BC': ['AB'],
                   'AB': ['BC', 'SK'],
                   'SK': ['AB', 'MB'],
                   'MB': ['SK'],
                 }


western_canada_plus2 = { 'BC': ['AB'],
                         'AB': ['BC', 'SK'],
                         'SK': ['AB', 'MB'],
                         'MB': ['SK'],
                         'XX': ['YY'],
                         'YY': ['XX']
                       }

dasgupta_book_fig3_2 = {'G': ['D', 'H'],
                        'H': ['G', 'D'],
                        'D': ['A', 'G', 'H'],
                        'A': ['B', 'C', 'D'],
                        'C': ['A', 'F'],
                        'B': ['A', 'E', 'F'],
                        'F': ['B', 'C'],
                        'E': ['B', 'I', 'J'],
                        'I': ['E', 'J'],
                        'J': ['E', 'I'],
                        'K': ['L'],
                        'L': ['K']
                       }

mostly_disconnected = { 1:[5],
                        2:[],
                        3:[4],
                        4:[3],
                        5:[1],
                        6:[],
                        7:[]
                      }
