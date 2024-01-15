## Hugging Face - NLP text2text translation models

# Prerequisite Windows environment

1. Install Anaconda
    a. Download: https://docs.anaconda.com/free/anaconda/install/windows/
    b. Install, configure and verify Anaconda: https://docs.anaconda.concom/free/anaconda/install/verify-install/

# Prepare Anaconda Prompt

1. Run: conda install pytorch torchvision torchaudio cpuonly -c pytorch
2. Run: pip install transformers
3. Run: pip install sentencepiece
    a. If errors occured, fix: pip install --upgrade transformers sentencepiece

# Run translations

1. Open in VSCode folder where Python scripts "translate.py" is located
2. Modify line with function "translate(source, target, text)"
3. Open Anaconda Prompt and goto folder where Python file "translate.py" is located
4. Run: python translate.py
    a. When errors occured. Please check your internet connection or verify required language model is available
5. Run: python translations.py
    notice: Python script read source csv-file, translate and produce target csv-file with preferred language

# References

- PyTorch: https://pytorch.org/get-started/locally/#windows-anaconda
- Helsinki-NLP: https://huggingface.co/Helsinki-NLP
