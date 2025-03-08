import json
from utils.get_clothing_items import get_clothing_items
from utils.s3.list_images_in_bucket import list_images_in_bucket
from utils.s3.get_encoded_image import get_encoded_image
from utils.dynamo.write_items_to_table import write_items_to_table
from classification.classify_outfit import classify_outfit
import csv
from pprint import pprint


bucket_name = "wearless"

if __name__ == "__main__":

    outfit_image_keys = list_images_in_bucket(bucket_name=bucket_name)

    outfits = []

    for key in outfit_image_keys:
        print(f"classifying {key}")

        encoded_outfit_image = get_encoded_image(
            bucket_name=bucket_name, object_key=key
        )

        outfit = classify_outfit(base64_image=encoded_outfit_image, image_key=key)

        if outfit:
            outfits.append(outfit)

    print("writing to DyanamoDB")

    write_items_to_table(table_name="outfits", items=outfits)

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
