# Next token prediction

1. Open the [Next token prediction](https://alonsosilva-nexttokenprediction.hf.space/) app by Alonso Silva Allende. You may need to wait a couple of seconds or minutes for the app to load.
2. Start with a sentence (for instance, "Biology is") and jump from the most probable token to the next. Do you get a meaningful sentence?
3. Start over with the same sentence and jump from one token to the next but don’t select the most probable (try with the second or third most probable). Do you get a meaningful sentence?
4. Enter this text exactly:
    > The doctor is a professional.
    
    What is the probability for "He" and "She"?
5. Enter this text exactly:
    > The nurse is a professional.

    What is the probability for "He" and "She"?
6. Any thoughts on these results?

The LLM model used here is GPT-2, a rather small (but open) model with *only* 124 million parameters. LLM like GPT-4 counts about 1.76 trillion (1,760 millions) parameters.

You can also take a look at the [TextSynth](https://textsynth.com/completion.html) app that will complete text from a short input ("Biology is", "My name is"...).
