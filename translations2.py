# read csv file with text to translate and write translated text to csv file
import os, csv, time, ctranslate2
from transformers import AutoTokenizer

# define variable folder location
folder = "C:\\Developments\\Python\\MLTranslate\\data"
source = "en"
target = "nl"

# Download the model and the tokenizer
model_name = f"Helsinki-NLP/opus-mt-{source}-{target}"
translator = ctranslate2.Translator(f"data/models/{model_name}")
tokenizer = AutoTokenizer.from_pretrained(model_name)

def translate(text):

    # Tokenize the text
    sourceTokenized = tokenizer.convert_ids_to_tokens(tokenizer.encode(text))

    # Perform the translation and decode the output
    results  = translator.translate_batch([sourceTokenized])
    targetResults = results[0].hypotheses[0]

    # Perform the translation and decode the output
    translated_text = tokenizer.decode(tokenizer.convert_tokens_to_ids(targetResults))
    
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