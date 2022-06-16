# ###################Task 14/06/2022########################
# def high_and_low(numbers):
#     list_of_numbers = numbers.split()
#     checked_numbers = []
#     while list_of_numbers:
#         current_number = list_of_numbers.pop()
#         checked_numbers.append(int(current_number))
#     return str(max(checked_numbers)) + ' ' + str(min(checked_numbers))
# print(high_and_low('1 9 3 4 -5'))
####################################################################
# def high_and_low(numbers):
#     numbers = [int(x) for x in numbers.split(" ")]
#     return str(max(numbers)) + " " + str(min(numbers))
# print(high_and_low('1 9 3 4 -5'))
###################################################################################################################

# sandwich_orders = ['safish', 'sameat', 'pastrami', 'sacheese', 'satomato', 'pastrami', 'saremba', 'pastrami']
# finished_sandwiches = []
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
#
# for sandwich in sandwich_orders:
#     finished_sandwiches.append(sandwich)
# print(finished_sandwiches)
# print("Sorry, we haven't pastrami anymore")
######################################################
def tower_builder(n_floors):
    n = n_floors

    if n == 1:
        list = ['*']
        for i in range(1, n, 2):
            a = i * '*'
            list.append(a.center(n))
    elif n == 2:
        list = []
        for i in range(n - 1, 2 * n, 2):
            a = i * '*'
            list.append(a.center(2 * n - 1))
    elif n > 2 or n % 2 != 0:
        list = []
        for i in range(1, 2 * n, 2):
            a = i * '*'
            list.append(a.center(2 * n - 1))
    elif n > 2 or n % 2 == 0:
        list = []
        for i in range(1, 2 * n, 2):
            a = i * '*'
            list.append(a.center(2 * n - 1))
    return list
print(tower_builder(3))





