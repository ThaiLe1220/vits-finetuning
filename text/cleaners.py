import re
from text.japanese import japanese_to_romaji_with_accent
from text.english import english_to_ipa2


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


# Assuming imports are correctly set up as per your provided snippets.


def english_cleaners(text):
    text = f"[EN]{text}[EN]"  # Mark the text for processing, similar to the Japanese cleaner.

    # Replace the English text enclosed in markers with its IPA2 representation.
    # Additional replacements and formatting can be applied here as needed.
    text = re.sub(
        r"\[EN\](.*?)\[EN\]",
        lambda x: english_to_ipa2(x.group(1))
        .replace("...", "…")  # Normalize ellipsis
        .strip()  # Ensure no leading/trailing whitespace
        + " ",  # Add a space at the end for consistency
        text,
    )

    # Normalize multiple spaces to a single space.
    text = re.sub(r"\s{2,}", " ", text)

    # Clean up: remove any excess whitespace at the end of the string.
    text = re.sub(r"\s+$", "", text)
    text = re.sub(r"([?!.])", r"\1 ", text)  # Ensure space after punctuation.

    # Ensure punctuation: if the text doesn't end with common punctuation, add a period.
    # This mirrors the Japanese cleaner functionality for consistency.
    text = re.sub(r"([^\.,!\?\-…~])$", r"\1.", text)

    return text
