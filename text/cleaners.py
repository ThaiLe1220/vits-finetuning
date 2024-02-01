# import re
from text.japanese import japanese_to_romaji_with_accent
from text.english import english_to_ipa2

import re
from unidecode import unidecode


def japanese_cleaners(text):
    text = f"[JA]{text}[JA]"
    text = re.sub(
        r"\[JA\](.*?)\[JA\]",
        lambda x: japanese_to_romaji_with_accent(x.group(1))
        .replace("ts", "ʦ")
        .replace("u", "ɯ")
        .replace("...", "…")
        + " ",
        text,
    )
    text = re.sub(r"\s+$", "", text)
    text = re.sub(r"([^\.,!\?\-…~])$", r"\1.", text)
    return text


def english_cleaners(text):
    text = text.lower()
    text = english_to_ipa2(text).strip()
    return text
