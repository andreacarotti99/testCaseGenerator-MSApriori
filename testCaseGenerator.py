import random
import sys

def create_transaction(max_items_trans, num_of_items):
    elements = 0
    tr = []
    created_element = random.randint(1, num_of_items)
    while elements < max_items_trans:
        while created_element in tr:
            created_element = random.randint(1, num_of_items)
        elements += 1
        tr.append(created_element)
    return tr

def check_param(num_of_items, num_of_transactions, max_items_per_tr, num_of_mis_defined):
    if max_items_per_tr > num_of_items:
        print("Error: provide less items than maximum number per transaction")
        return
    if num_of_mis_defined > num_of_items:
        print("Error: Provide a number of MIS defined < than the number of total items")
        return

def generate_input_data(num_of_transactions, max_items_per_tr, num_of_items, num_of_mis_defined):

    with open('input_data.txt', 'w') as f:
        for i in range(num_of_transactions-1):
            # max_items_per_tr = random.randint(1, max_items_per_tr)
            tr = create_transaction(max_items_per_tr, num_of_items)
            for j in range(len(tr)-1):
                f.write(str(tr[j]) + ", ")
            f.write(str(tr[-1]) + "\n")
            tr.clear()
        tr = create_transaction(max_items_per_tr, num_of_items)
        for j in range(len(tr)-1):
            f.write(str(tr[j]) + ", ")
        f.write(str(tr[-1]))



    with open('input_param.txt', 'w') as f:
        for i in range(num_of_mis_defined):
            f.write("MIS(" + str(i+1) + ") = " + str(random.randint(1, 50)/100) + "\n")
        f.write("MIS(rest) = " + str(random.randint(1, 50)/100) + "\n")
        f.write("SDC = " + str(random.randint(1, 100)/100))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num_of_items = int(sys.argv[1])
    num_of_transactions = int(sys.argv[2])
    max_items_per_tr = int(sys.argv[3])
    num_of_mis_defined = int(sys.argv[4])

    if len(sys.argv) is not 5:
        print("Incorrect number of parameters!")
        print("Please provide: num_of_items, num_of_transactions, max_items_per_transaction, num_of_mis")

    check_param(num_of_items, num_of_transactions, max_items_per_tr, num_of_mis_defined)
    generate_input_data(num_of_transactions, max_items_per_tr, num_of_items, num_of_mis_defined)
