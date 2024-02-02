# @title  Edit config
import json

BATCH_SIZE = 32  # @param {type:"number"}
EPOCHS = 5000
TRAINING_FILES = "filelists/miyu_train.txt.cleaned"  # @param {type:"string"}
VALIDATION_FILES = "filelists/miyu_val.txt.cleaned"  # @param {type:"string"}
TEXT_CLEANERS = ["english_cleaners", "japanese_cleaners"]


config = json.load(open("configs/config.json"))


config["train"]["batch_size"] = BATCH_SIZE
config["train"]["log_interval"] = BATCH_SIZE
config["train"]["epochs"] = EPOCHS

config["data"]["training_files"] = TRAINING_FILES
config["data"]["validation_files"] = VALIDATION_FILES
config["data"]["text_cleaners"] = TEXT_CLEANERS

with open("configs/config.json", "w+") as f:
    json.dump(config, f, indent=4)
