from tasksalesman import TaskSalesman


inf = float("inf")

matrix_C = [[inf, 68,  73,  24,  70,  9],
            [58,  inf, 16,  44,  11,  92],
            [63,  9,   inf, 86,  13,  18],
            [17,  34,  76,  inf, 52,  70],
            [60,  18,  3,   45,  inf, 58],
            [16,  82,  11,  60,  48,  inf]]

slsman = TaskSalesman(matrix_C)

way = slsman.solve_salesman()
