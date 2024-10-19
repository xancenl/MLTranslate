# Helsinki NLP + CTranslate2

## Download and install Anaconda

1. Download: <https://docs.anaconda.com/free/anaconda/install/windows/>
2. Install, configure and verify Anaconda: <https://docs.anaconda.concom/free/anaconda/install/verify-install/>

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

    a. If installations errors occurs, fix:

    ```console
    pip install --upgrade transformers sentencepiece
    ```

## Run translations

1. Open in VSCode folder where Python scripts "translate.py" is located
2. Modify line with function "translate(source, target, text)"
3. Open Anaconda Prompt and goto folder where Python file "translate.py" is located
4. Run: python translate.py
    a. When errors occurred. Please check your internet connection or verify required language model is available
5. Run: python translations.py
    notice: Python script read source csv-file, translate and produce target csv-file with preferred language

## References

- PyTorch: <https://pytorch.org/get-started/locally/#windows-anaconda>
- Helsinki-NLP: <https://huggingface.co/Helsinki-NLP>

## CTranslate2 running (fast)

- Prerequisite:
  - CTranslate2 modules: pip install ctranslate2 OpenNMT-py==2.* sentencepiece
    - Download translation model: ct2-transformers-converter --model Helsinki-NLP/opus-mt-{source}-{target} --output_dir data/models/Helsinki-NLP/opus-mt-{source}-{target}
- Run:
  - python translate2.py

## CTranslate2 references

- <https://opennmt.net/CTranslate2/guides/transformers.html#marianmt>
- <https://opennmt.net/CTranslate2/quickstart.html>

## Git rebuild and checkout

1. Open a command prompt in the folder where the repository is located.
2. Remove the .git folder:

    ```console
    rmdir /S /Q .git
    ```

3. Initialize the repository:

    ```console
    git init
    ```

4. Add files to the repository:

    ```console
    git add .
    ```

5. Commit all files to the repository:

    ```console
    git commit -m "Initial commit"
    ```

6. Push all files to remote the repository:

    ```console
    git remote add origin https://github.com/xancenl/MLTranslate.git
    ```

7. Command to force push all files to remote the repository:

    ```console
    git push -f origin main
    ```
