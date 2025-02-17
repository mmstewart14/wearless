classification_prompt = """
List out the items the person in the photo is wearing, the seasons the outfit could be worn in, the styles the outfit would suit, and the occasions the outfit could be worn for, using only the values in the following lists:

Items: Watch, Scarf, Pearl Necklace, Simple Necklace, Statement Necklace, Simple Earrings, Statement Earrings, Brown Belt, Black Belt, Handbag, Sunglasses, Sun Hat, Ball Cap, Gloves, Socks, Sweater Vest, Trench Coat, Vest, Light Blazer, Dark Blazer, Statement Blazer, Moto Jacket, Bomber Jacket, Denim Jacket, Light Cardigan, Dark Cardigan, Solid Color Cardigan, Light Button-Up Cardigan, Dark Button-Up Cardigan, Solid Color Button-Up Cardigan, Light Coat, Dark Coat, Solid Color Coat, Statement Coat, Light Tank, Dark Tank, Patterned Tank, Light T-Shirt, Dark T-Shirt, Patterned T-Shirt, Graphic T-Shirt, Light Short Sleeve Button Up, Dark Short Sleeve Button Up, Patterned Short Sleeve Button Up, Light Long Sleeve Button Up , Dark Long Sleeve Button Up , Patterned Long Sleeve Button Up, Light Long Sleeve Top, Dark Long Sleeve Top, Patterned Long Sleeve Top, Graphic Long Sleeve Top, Light Sweater, Dark Sweater, Statement Sweater, Light Quarter Zip, Dark Quarter Zip, Light Sweatshirt , Dark Sweatshirt, Light Polo, Dark Polo, Light Turtle Neck, Dark Turtle Neck, Mini Skirt, Midi Skirt, Maxi Skirt, Leggings , Light Pants, Dark Pants, Black Denim, White Denim, Destroyed Denim , Cuffed Denim, Flare Denim, Straight Leg Denim, Wide Leg Denim, Bike Shorts, White Shorts, Blue Shorts, Black Shorts, Silk Skirt, Black Skort, Patterned Skirt, Ballet Flats, Brown Sandals , White Sandals, Black Sandals, White Sneakers, Statement Sneakers, Slipper Boot, Loafers, Black Ankle Boots, Tan Ankle Boots, Chelsea Boots, Cognac Riding Boots, Black Tall Boots, Light Heels, Dark Heels, Heeled Sandals, Metallic Sandals, Statement Shoes, Light Mini Dress, Dark Mini Dress, Patterned Mini Dress, Solid Color Mini Dress, Neutral Maxi Dress, Patterned Maxi Dress

Seasons: Winter, Spring, Summer, Fall

Styles: Minimalist, Maximalist, Classic, Vintage, Grunge, Emo, Feminine, Preppy, Tomboy, Exotic, Streetwear, Chic, Athleisure

Occasions: Casual, Everyday, Business Casual, Semi-Formal, Formal

Your response must be a single JSON object in the following format:

{
        "items": string[],
        "seasons": string[],
        "styles": string[],
        "occasions": string[]
 }

Do not explain or justify your answer in anyway. Respond only with the single JSON object.
"""


def get_classification_prompt():
    """
    Retrieves an object from Amazon S3.

    Args:
        bucket_name (str): The name of the S3 bucket.
        object_key (str): The key of the object to retrieve.

    Returns:
        bytes: The content of the object, or None if an error occurs.
    """

    return classification_prompt
