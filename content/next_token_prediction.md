# Next token prediction

## GPT-2

1. Open the [Next token prediction](https://alonsosilva-nexttokenprediction.hf.space/) app by Alonso Silva Allende. You may need to wait a couple of seconds or minutes for the app to load.
2. Start with a sentence (for instance: "Biology is") and jump from the most probable token to the next. Do you get a meaningful sentence?
3. Start over with the same sentence and jump from one token to the next but don’t select the most probable (try with the second or third most probable token). Do you get a meaningful sentence?
4. Enter this text exactly:
    > The doctor is a professional.
    
    What is the probability for "He" and "She"?
5. Enter this text exactly:
    > The nurse is a professional.

    What is the probability for "He" and "She"?
6. Any thoughts on these results?

```{note}
The LLM model used here is GPT-2, a rather small (but open) model with *only* 124 million parameters. LLM like GPT-4 counts about 1.76 trillion (1,760 millions) parameters.
```

## GPT-2 vs Gemma 3

Open this other [next token prediction](https://cupnet.net/llm-practicals/next-token-prediction-gpt2-gemma3.html) application with wich you will be able to compare the next token prediction mechanism for two langage models:

- GPT-2, 2019 model, 124 millions parameters, 50,257-token vocabulary
- Gemma 3, 2025 model, 270 million parameters, 262,144-token vocabulary

```{warning}
These models run entirely in your web browser. Please leave enought time for the models to be downloaded
```

## TextSynth

You can also take a look at the [TextSynth](https://textsynth.com/completion.html) app that will complete text from a short input ("Biology is", "My name is"...). Many larger models are available.

## Moebio

Finally, open the interactive application [moebio.com](https://moebio.com/mind/). Set your web browser to full-screen mode and explore the construction of a sentence, token by token, from left to right. As the application is very responsive, move your mouse *very* slowly. On the far left, observe the path explored by the different tokens in the semantic space. ✨
