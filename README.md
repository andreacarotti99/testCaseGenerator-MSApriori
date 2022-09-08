# Generate a Test Case

You need to pass 4 parameters:

- num_of_items: the total number of items
- num_of_transactions: the total number of transactions
- max_items_per_tr: the maximum number of items that each transactions contains
- num_of_mis_defined: the total number of MIS(i) = ... defined before having MIS(rest) =  ... (it needs to be less than the number of items)

```
python TestCaseGenerator.py 20 100 15 10

```

will generate two files: input_data.txt and input_params.txt filled with the information above 