"""1. Write a python program to add below matrices """


class Matrix:
    # constructor
    def __init__(self):
        self.mat_list1 = [[12, 7, 3],
                          [4, 5, 6],
                          [7, 8, 9]]

        self.mat_list2 = [[5, 8, 1],
                          [6, 7, 3],
                          [4, 5, 9]]

    # display matrix
    def read_matrix(self):
        print("mat_list:")
        for temp in self.mat_list1:
            print(temp)
        print("\nmat_list1:")
        for temp1 in self.mat_list2:
            print(temp1)


# object of class
obj = Matrix()

# call method
obj.read_matrix()


class Addition(Matrix):

    # constructor of subclass
    def __init__(self):
        super(Addition, self).__init__()

    # method for addition
    def add_matrix(self):
        while 1:
            print("\n 1. Get Matrix add""\n""2. Exit")
            ch = int(input("Enter choice"))
            try:
                if ch == 1:
                    result_list = [
                        [self.mat_list1[row][col] + self.mat_list2[row][col] for col in range(len(self.mat_list1[0]))]
                        for row in range(len(self.mat_list1))]
                    print("\n Addition Matrix:-")
                    for temp1 in result_list:
                        print(temp1)
                elif ch == 2:
                    exit()
                else:
                    print("Invalid choice")

            except Exception as e:
                print("Matrix is not conformable for addition", e)


# object of subclass
obj = Addition()

# call method
obj.add_matrix()
