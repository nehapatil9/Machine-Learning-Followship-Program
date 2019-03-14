""" 2. Write a program to perform scalar multiplication of matrix and a number"""


class Matrix:
    # constructor

    def __init__(self):
        self.Num = 3
        self.mat_list1 = [[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]]

        self.scalar = 4

    # function for display matrix

    def read_matrix(self):
        print("mat_list:")
        for temp1 in self.mat_list1:
            print(temp1)


# object of class
obj = Matrix()

# call method
obj.read_matrix()


class ScalarMultiplication(Matrix):

    # constructor for subclass

    def __init__(self):
        super(ScalarMultiplication, self).__init__()

    # function for scalar product

    def scalar_Product_Mat(self):
        for row in range(self.Num):
            for col in range(self.Num):
                self.mat_list1[row][col] = self.scalar * self.mat_list1[row][col]

            return self.mat_list1
        # while 1:
        #     print("\n 1. Get Matrix ""\n""2. Exit")
        #     ch = int(input("\n Enter choice"))
        #     try:
        #         if ch == 1:
        #             for row in range(self.Num):
        #                 for col in range(self.Num):
        #                     self.mat_list1[row][col] = self.mat_list1[row][col] * self.scalar
        #
        #                 return self.mat_list1
        #             scalar_list = obj.scalar_Product_Mat()
        #             print("\n Scalar Product Matrix is : ")
        #             for temp in scalar_list:
        #                 print(temp)
        #
        #         elif ch == 2:
        #             exit()
        #         else:
        #             print("Invalid choice")
        #
        #     except Exception as e:
        #         print("Matrix is not conformable ", e)
# object of subclass
obj = ScalarMultiplication()

# call function
scalar_list = obj.scalar_Product_Mat()
# print("\n Scalar Product Matrix is : ")
# for temp in scalar_list:
#     print(temp)
while 1:
        print("\n 1. Get Matrix ""\n""2. Exit")
        ch = int(input("\n Enter choice"))
        try:
                if ch == 1:
                    # for row in range(self.Num):
                    #     for col in range(self.Num):
                    #         self.mat_list1[row][col] = self.mat_list1[row][col] * self.scalar
                    #
                    #     return self.mat_list1
                    scalar_list = obj.scalar_Product_Mat()
                    print("\n Scalar Product Matrix is : ")
                    for temp in scalar_list:
                        print(temp)

                elif ch == 2:
                    exit()
                else:
                    print("Invalid choice")

        except Exception as e:
                print("Matrix is not conformable ", e)


