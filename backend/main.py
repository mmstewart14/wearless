from utils.dynamo.get_item import get_item

from pprint import pprint


bucket_name = "wearless"
outfit_table_name = "outfits"

if __name__ == "__main__":

    item = get_item(table_name=outfit_table_name, item_id="756fc6c6-e35a-44ed-8ead-0b943ed42f2f")

    pprint(item)

    # ------ CSVVVVV -------

    # with open("data/results.csv", "w", newline="") as csvfile:
    #     writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

    #     for key in outfit_image_keys:
    #         print(f"classifying {key}")

    #         encoded_outfit_image = get_encoded_image(
    #             bucket_name=bucket_name, object_key=key
    #         )

    #         outfit = classify_outfit(base64_image=encoded_outfit_image)

    #         if outfit:
    #             outfit_name = outfit.name
    #             outfit_items = ", ".join(outfit.items)
    #             outfit_seasons = ", ".join(outfit.seasons)
    #             outfit_styles = ", ".join(outfit.styles)
    #             outfit_occasions = ", ".join(outfit.occasions)

    #             writer.writerow(
    #                 [
    #                     outfit_name,
    #                     outfit_items,
    #                     outfit_seasons,
    #                     outfit_styles,
    #                     outfit_occasions,
    #                 ]
    #             )
