# read csv file with text to translate and write translated text to csv file
import os, csv, time
from transformers import AutoTokenizer, MarianMTModel

# define variable folder location
folder = "C:\\Developments\\Python\\MLTranslate\\data"
source = "en"
target = "nl"

# Download the model and the tokenizer
model_name = f"Helsinki-NLP/opus-mt-{source}-{target}"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def translate(text):

    # Tokenize the text
    input_ids = tokenizer.encode(text, return_tensors="pt")
    
    # Perform the translation and decode the output
    translated = model.generate(input_ids)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    return translated_text

start_time = time.time()

# delete target file if exists
try:
    os.remove(f"{folder}\\target\\{source}-{target}.csv")
except:
    pass

# open csv file with text to translate
with open(f"{folder}\\source\\{source}.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        # translate text
        translated = translate(row[1])
        # print original and translated text
        print(f"{row[0]} > {translated}")
        # write original and translated text to csv file
        with open(f"{folder}\\target\\{source}-{target}.csv", 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
            writer.writerow([row[0], row[1], translated])

elapsed_time = round(time.time() - start_time)
print("--- %s seconds ---" % elapsed_time)