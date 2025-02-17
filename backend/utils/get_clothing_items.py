import csv


def get_clothing_items(csv_file_path: str):
    """
    Generates list of clothing items to use in classification prompt

    Args:
        csv_file_path (str): The file path to csv containing clothing items.

    Returns:
        bytes: The content of the object, or None if an error occurs.
    """
    data_list = []
    categories = []
    clothing_items = {}

    try:
        with open(csv_file_path, "r") as file:
            csv_reader = csv.reader(file)
            for row_index, row in enumerate(csv_reader):
                if row_index == 0:
                    for col in row:
                        if col:
                            category_name = col

                            categories.append(category_name)
                            clothing_items[category_name] = []
                else:
                    for col_index, col in enumerate(row):
                        if col:
                            category_name = categories[col_index]

                            clothing_items[category_name].append(col)

        for key in clothing_items:
            item_list = clothing_items[key]

            clothing_items[key] = ", ".join(item_list)

        print(clothing_items)
        return data_list
    except Exception as e:
        print(f"Error opening csv file: {e}")
        return []
