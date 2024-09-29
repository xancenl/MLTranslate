# Hugging Face - NLP text2text translation models

## Prerequisite Windows environment

1. Install Anaconda
    a. Download: <https://docs.anaconda.com/free/anaconda/install/windows/>
    b. Install, configure and verify Anaconda: <https://docs.anaconda.concom/free/anaconda/install/verify-install/>

## Prepare Anaconda Prompt

1. Install pytorch:

    ```console
    conda install pytorch torchvision torchaudio cpuonly -c pytorch
    ```

2. Install python transformers:

    ```console
    pip install transformers
    ```

3. Install python sentencepiece:

    ```console
    pip install sentencepiece
    ```

    a. If installations errors occures, fix:

    ```console
    pip install --upgrade transformers sentencepiece
    ```

## Run translations

1. Open in VSCode folder where Python scripts "translate.py" is located
2. Modify line with function "translate(source, target, text)"
3. Open Anaconda Prompt and goto folder where Python file "translate.py" is located
4. Run: python translate.py
    a. When errors occured. Please check your internet connection or verify required language model is available
5. Run: python translations.py
    notice: Python script read source csv-file, translate and produce target csv-file with preferred language

## References

- PyTorch: <https://pytorch.org/get-started/locally/#windows-anaconda>
- Helsinki-NLP: <https://huggingface.co/Helsinki-NLP>

## CTranslate2 running (fast)

- Prerequisite:
  - CTranslate2 modules: pip install ctranslate2 OpenNMT-py==2.* sentencepiece
    - Download translation model: ct2-transformers-converter --model Helsinki-NLP/opus-mt-{source}-{target} --output_dir data/models/Helsinki-NLP/opus-mt-{source}-{taget}
- Run:
  - python translate2.py

## CTranslate2 references

- <https://opennmt.net/CTranslate2/guides/transformers.html#marianmt>
- <https://opennmt.net/CTranslate2/quickstart.html>

## Git rebuild and checkout

1. Open de Command Prompt of Git Bash
2. Verwijder de .git directory met:

    ```console
    rmdir /S /Q .git
    ```

3. Initialiseer een nieuwe Git-repository met:

    ```console
    git init
    ```

4. Voeg bestanden toe met:

    ```console
    git add .
    ```

5. Commit alle bestanden met:

    ```console
    git commit -m "Initial commit"
    ```

6. Push alle bestanden naar remote repository:

    ```console
    git remote add origin https://github.com/xancenl/MLTranslate.git
    ```

7. Verbind met GitHub en forceer de push met:

    ```console
    git push -f origin main
    ```
