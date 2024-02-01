# @title  Edit config
import json

# batchsize = 16  # @param {type:"number"}
# training_files = "filelists/miyu_train.txt.cleaned"  # @param {type:"string"}
# validation_files = "filelists/miyu_val.txt.cleaned"  # @param {type:"string"}
# config = json.load(open("configs/config.json"))
# config["train"]["batch_size"] = batchsize
# config["data"]["training_files"] = training_files
# config["data"]["validation_files"] = validation_files
# with open("configs/config.json", "w+") as f:
#     json.dump(config, f, indent=4)


# @title  Check if your dataset meets the requirements (Optional)
import os
import soundfile as sf

all_meet = True
wav_path = "wav/obama1"  # @param {type:"string"}
for file_name in os.listdir(wav_path):
    if not file_name.endswith(".wav"):
        continue
    data, sr = sf.read(rf"{wav_path}/{file_name}")
    n_channels = data.shape[1] if data.ndim > 1 else 1
    subtype = sf.info(rf"{wav_path}/{file_name}").subtype
    if sr == 22050 and n_channels == 1 and subtype == "PCM_16":
        filesize = os.path.getsize(rf"{wav_path}/{file_name}") / 1024
        if filesize > 500 or filesize < 16:
            print(
                f"Warning: {file_name}: wav files larger than 500KB and smaller than 16KB will not be read in training"
            )
        continue
    else:
        print(
            f'\x1b[31m"Error: {file_name} does not meet the criteria because:"\x1b[0m'
        )
        if sr != 22050:
            print(" - sample rate is " + str(sr) + " instead of 22050")
        if n_channels != 1:
            print(" - number of channels is " + str(n_channels) + " instead of 1")
        if subtype != "PCM_16":
            print(" - subtype is " + subtype + " instead of PCM_16")
        all_meet = False
if all_meet:
    print("All files meet the requirements")


# # @title  Process the wav files of the dataset to make them meet the requirements (Optional)
# import os
# import librosa
# from tqdm import tqdm

# wav_path = "wav/ba/miyu"  # @param {type:"string"}
# for file_name in tqdm(os.listdir(wav_path)):
#     if file_name.endswith(".spec.pt"):
#         os.remove(rf"{wav_path}/{file_name}")
#         continue
#     y, sr = librosa.load(rf"{wav_path}/{file_name}", sr=22050, mono=True)
#     sf.write(rf"{wav_path}/{file_name}", y, 22050, subtype="PCM_16")


# # Define the input and output file paths
# input_file_path = "_eugene/obama1.txt"
# output_file_path = "_eugene/obama1_cleaned.txt"

# # Define the prefix to add to each filename
# prefix = "wav/obama1/"

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
