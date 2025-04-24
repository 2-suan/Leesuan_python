def display_multiplication_table() :
        block_table(2)
        print()
        block_table(6)

        
def block_table(n):
        for i in range(1,10):
                for j in range(n, n+4):
                        print(f'{j} x {i} = {j*i:2d}\t',end = '')
                print()


display_multiplication_table()
