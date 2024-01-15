from transformers import AutoTokenizer, MarianMTModel
import time

def translate(srcLanguage, trgLanguage, text):

    # Download the model and the tokenizer
    model_name = f"Helsinki-NLP/opus-mt-{srcLanguage}-{trgLanguage}"
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Tokenize the text
    input_ids = tokenizer.encode(text, return_tensors="pt")
    
    # Perform the translation and decode the output
    translated = model.generate(input_ids)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    return translated_text

# execute the translation
start_time = time.time()

#fr-en = "où est l'arrêt de bus ?" 
#translated = translate("fr", "en", "où est l'arrêt de bus ?")

#fr-de = "wo ist die bushaltestelle ?"
translated = translate("fr", "de", "où est l'arrêt de bus ?")

#fr-nl = "waar is de bushalte ?"
#translated = translate("fr", "nl", "où est l'arrêt de bus ?")

#fr-es = "¿dónde está la parada de autobús ?"
#translated = translate("fr", "es", "où est l'arrêt de bus ?")

elapsed_time = round(time.time() - start_time)

# print the translated text results
print("--- %s seconds ---" % elapsed_time)
print(translated)