from utils.s3.get_encoded_image import get_encoded_image
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import json
import os
import uuid


load_dotenv()


class Outfit:
    def __init__(
        self,
        id: str,
        items: list[str],
        seasons: list[str],
        styles: list[str],
        occasions: list[str],
        sourceImageKey: str,
        name: str,
        createdOn: str,
    ):
        self.id = id
        self.items = items
        self.seasons = seasons
        self.styles = styles
        self.occasions = occasions
        self.sourceImageKey = sourceImageKey
        self.name = name
        self.createdOn = createdOn

    def to_json(self):
        return self.__dict__


def classify_outfit(base64_image: str, image_key: str) -> Outfit | None:
    """
    Classifies the items, seasons, styles, and occassions of an image depicting an outfit.

    Args:
        base64_image (str): The encoded outfit image.

    Returns:
        outfit (Outfit): An object containing the outfit's classifications
    """

    if not base64_image:
        return None

    openai_api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=openai_api_key)

    prompt = """
    List out the items the person in the photo is wearing, the seasons the outfit could be worn in, the styles the outfit would suit, and the occasions the outfit could be worn for, using only the values in the following lists:

    Items: Watch, Scarf, Pearl Necklace, Simple Necklace, Statement Necklace, Simple Earrings, Statement Earrings, Brown Belt, Black Belt, Handbag, Sunglasses, Sun Hat, Ball Cap, Gloves, Socks, Sweater Vest, Trench Coat, Vest, Light Blazer, Dark Blazer, Statement Blazer, Moto Jacket, Bomber Jacket, Denim Jacket, Light Cardigan, Dark Cardigan, Solid Color Cardigan, Light Button-Up Cardigan, Dark Button-Up Cardigan, Solid Color Button-Up Cardigan, Light Coat, Dark Coat, Solid Color Coat, Statement Coat, Light Tank, Dark Tank, Patterned Tank, Light T-Shirt, Dark T-Shirt, Patterned T-Shirt, Graphic T-Shirt, Light Short Sleeve Button Up, Dark Short Sleeve Button Up, Patterned Short Sleeve Button Up, Light Long Sleeve Button Up , Dark Long Sleeve Button Up , Patterned Long Sleeve Button Up, Light Long Sleeve Top, Dark Long Sleeve Top, Patterned Long Sleeve Top, Graphic Long Sleeve Top, Light Sweater, Dark Sweater, Statement Sweater, Light Quarter Zip, Dark Quarter Zip, Light Sweatshirt , Dark Sweatshirt, Light Polo, Dark Polo, Light Turtle Neck, Dark Turtle Neck, Mini Skirt, Midi Skirt, Maxi Skirt, Leggings , Light Pants, Dark Pants, Black Denim, White Denim, Destroyed Denim , Cuffed Denim, Flare Denim, Straight Leg Denim, Wide Leg Denim, Bike Shorts, White Shorts, Blue Shorts, Black Shorts, Silk Skirt, Black Skort, Patterned Skirt, Ballet Flats, Brown Sandals , White Sandals, Black Sandals, White Sneakers, Statement Sneakers, Slipper Boot, Loafers, Black Ankle Boots, Tan Ankle Boots, Chelsea Boots, Cognac Riding Boots, Black Tall Boots, Light Heels, Dark Heels, Heeled Sandals, Metallic Sandals, Statement Shoes, Light Mini Dress, Dark Mini Dress, Patterned Mini Dress, Solid Color Mini Dress, Neutral Maxi Dress, Patterned Maxi Dress

    Seasons: Winter, Spring, Summer, Fall

    Styles: Minimalist, Maximalist, Classic, Vintage, Grunge, Emo, Feminine, Preppy, Tomboy, Exotic, Streetwear, Chic, Athleisure

    Occasions: Casual, Everyday, Business Casual, Semi-Formal, Formal

    Then, give the outfit a unique name of your choosing, that describes the essense of the outfit and is only a few words long.

    Your response must be a single JSON object in the following format:

    {
            "items": string[],
            "seasons": string[],
            "styles": string[],
            "occasions": string[]
            "name": string,
    }

    Do not explain or justify your answer in anyway. Respond only with the single JSON object.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            store=True,
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
        )

        if response.choices[0].finish_reason == "stop":
            # The model has successfully finished generating the JSON object according to the schema

            message_content = json.loads(response.choices[0].message.content)
            # total_tokens = response.usage.total_tokens

            return Outfit(
                id=str(uuid.uuid4()),
                items=message_content["items"],
                seasons=message_content["seasons"],
                styles=message_content["styles"],
                occasions=message_content["occasions"],
                sourceImageKey=image_key,
                name=message_content["name"],
                createdOn=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            )

        else:
            return None

    except Exception as e:
        print(f"Error classifying outfit: {e}")
        return None
