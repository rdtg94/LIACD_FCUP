def transform(lst):
    result = []
    for sublist in lst:
        transformed_sublist = []
        for item in sublist:
            try:
                # Convert to integer if it's not an int
                n = int(item)
                # Check for division by zero
                if n == 0:
                    raise ZeroDivisionError("division by zero")
                # Perform transformation 1/n
                transformed_sublist.append(1 / n)
            except Exception as e:
                # Print the error message in the specified format
                print(f"Error: {type(e).__name__} for value \"{item}\": {e}.")
        # Only add non-empty sublists to the result
        if transformed_sublist:
            result.append(transformed_sublist)
    return result







lst = [[2, 8, 4], [4, -8, 'a'], [1, 5, 10]]
transformed_lst = transform(lst)
print("Transformed List:", transformed_lst)

lst = [[2, 0, 4], ["2", "4"], [1, 5, 10]]
transformed_lst = transform(lst)
print("Transformed List:", transformed_lst)

lst = [[2, 8, 4], [4, "abc", "8"], [1, 5, 10]]
transformed_lst = transform(lst)
print("Transformed List:", transformed_lst)