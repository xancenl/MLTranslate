import ctranslate2, transformers, time

def translate(srcLanguage, trgLanguage, text):

    # Download the model and the tokenizer
    model_name = f"Helsinki-NLP/opus-mt-{srcLanguage}-{trgLanguage}"
    translator  = ctranslate2.Translator(f"data/models/{model_name}")
    tokenizer = transformers.AutoTokenizer.from_pretrained(f"{model_name}")

    # Tokenize the text
    source = tokenizer.convert_ids_to_tokens(tokenizer.encode(text))

    # Perform the translation and decode the output
    results  = translator.translate_batch([source])
    target = results[0].hypotheses[0]

    # Perform the translation and decode the output
    translated_text = tokenizer.decode(tokenizer.convert_tokens_to_ids(target))
    
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