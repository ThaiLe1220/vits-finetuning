# @title  Edit config
import json

BATCH_SIZE = 32  # @param {type:"number"}
EPOCHS = 4000
TRAINING_FILES = "filelists/miyu_train.txt.cleaned"  # @param {type:"string"}
VALIDATION_FILES = "filelists/miyu_val.txt.cleaned"  # @param {type:"string"}
TEXT_CLEANERS = ["english_cleaners"]


config = json.load(open("configs/config.json"))


config["train"]["batch_size"] = BATCH_SIZE
config["train"]["log_interval"] = BATCH_SIZE
config["train"]["epochs"] = EPOCHS

config["data"]["training_files"] = TRAINING_FILES
config["data"]["validation_files"] = VALIDATION_FILES
config["data"]["text_cleaners"] = TEXT_CLEANERS

with open("configs/config.json", "w+") as f:
    json.dump(config, f, indent=4)


# @title  Process the wav files of the dataset to make them meet the requirements (Optional)
import os
import librosa
from tqdm import tqdm

wav_path = "wav/ba/miyu"  # @param {type:"string"}
for file_name in tqdm(os.listdir(wav_path)):
    if file_name.endswith(".spec.pt"):
        os.remove(rf"{wav_path}/{file_name}")
        continue
    y, sr = librosa.load(rf"{wav_path}/{file_name}", sr=22050, mono=True)
    sf.write(rf"{wav_path}/{file_name}", y, 22050, subtype="PCM_16")


# # Define the input and output file paths
# input_file_path = "_eugene/obama2.txt"
# output_file_path = "_eugene/obama2_cleaned.txt"

# # Define the prefix to add to each filename
# prefix = "wav/obama2/"

# # Open the input file for reading and the output file for writing
# with open(input_file_path, "r", encoding="utf-8") as input_file, open(
#     output_file_path, "w", encoding="utf-8"
# ) as output_file:
#     # Iterate over each line in the input file
#     for line in input_file:
#         # Split the line into the filename part and the rest of the line
#         parts = line.split("|", 1)
#         if len(parts) == 2:
#             # Prepend the prefix to the filename part
#             modified_line = f"{prefix}{parts[0].strip()}|{parts[1]}"
#             # Write the modified line to the output file
#             output_file.write(modified_line)
#         else:
#             # If the line does not match the expected format, write it unchanged
#             output_file.write(line)

# print(f"Lines have been modified and written to {output_file_path}")
