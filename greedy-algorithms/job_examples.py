from job import Job

example1 = [None, # for 1-based quicksort
        Job(15.5, 17, 'CMPUT 130'),
        Job(11, 14, 'CMPUT 131'),
        Job(9, 10.5, 'CMPUT 127'),
        Job(11, 12.5, 'CMPUT 128'),
        Job(13, 14.5, 'CMPUT 129'),
        Job(9, 12.5, 'CMPUT 125'),
        Job(14.5, 17.5, 'CMPUT 126'),
        Job(9, 10.5, 'CMPUT 122'),
        Job(13, 14.5, 'CMPUT 123'),
        Job(15.5, 17.5, 'CMPUT 124')
    ]

example2 = [None, # for 1-based quicksort
        Job(1, 7, 'Job1'), # time 1 corresponds to s1 in slide, 7 is f1
        Job(5, 8, 'Job2'), # 5 is s2, 8 is f2
        Job(3, 6, 'Job3'), # 3 is s3, 6 is f3
        Job(2, 4, 'Job4')  # 2 is s4, 4 is f4
    ]

# Example from problem 2 in http://cs.boisestate.edu/~jhyeh/cs421/activity-selection-example.pdf
# optimal solution should be {2,3,4,5}
example3 = [None, # for 1-based quicksort
        Job(3, 5, 'A1'),
        Job(0.1, 2, 'A2'),
        Job(6, 8, 'A3'),
        Job(2, 4, 'A4'),
        Job(4, 6, 'A5'),
        Job(1, 3, 'A6'),
        Job(1, 3, 'A7'),
        Job(5, 7, 'A8'),
        Job(5, 7, 'A9')    
    ]
