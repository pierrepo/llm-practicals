# Tokens

Open OpenAI Tokenizer in a web browser: <https://platform.openai.com/tokenizer>

## Tokens are not words

1. Select “GPT-4o & GPT-4o mini”
2. Enter the sentence below:

    > You need to know bioinformatics.

3. Tokens are colored in various colors. One token = one colored block.
4. How many tokens are used to represent the sentence above?
5. Pay attention to token delimitations (color blocks). How are spaces handled?
6. How many tokens are used to represent the word “bioinformatics”?

```{note}
Large language models (LLMs) can use a limited set of words called tokens. When a word is not in a LLM vocabulary, it is chunked into multiple tokens. For instance, `bioinformatics` (actually ` bioinformatics`) is chunked into two tokens: ` bio` and `informatics`.
```

7. Keep the same sentence as above, and click on “GPT-3 (Legacy)”
8. How many tokens are used to represent the word “bioinformatics”?

Each LLM has its owns vocabulary (set of tokens). GPT-4o’s vocabulary has about 200,000 tokens, whereas GPT-4's has 100,000 tokens and GPT2’s vocabulary has 50,000 tokens. Complex words like “bioinformatics” are easier to represent with a large vocabulary. However, larger vocabularies require more memory and computation.

9. Find out other examples of words that are chunked into multiple tokens. Try with different tokenizers ("GPT-4o", "GPT-4", "GPT-3").


## Tokens are more than words

1. Switch back to “GPT-4o & GPT-4o mini”
2. Enter the sentences below: 
    > What is biology? Biology is the scientific study of life and living organisms.
3. Click on the “Token IDs” button (below the colored tokens). Each number corresponds to a given token. By clicking back and forth on the "Text" and "Token IDs" buttons, identify the tokens ids associated to the words “ biology” and “ Biology”? Are they identical?

```{note}
Tokens are context-dependent. A capital letter or a space could lead to very different tokens. 
```


## Tokens and languages

1. Enter a sentence (for instance, “What is DNA?”) and find out how many tokens are used to express this sentence.
2. Try the same sentence in different languages? What do you observe regarding the number of tokens used?

Most LLM vocabularies are based on the English language. Words and phrases in other languages could be represented with tokens, but usually with more tokens.
This is important given that the cost of LLM usage is per token. For instance, 1 million input tokens cost 5,00 $US with the GPT-4o model.

3. Find out other examples with different languages (for instance "J'aime la bioinfo") and tokenizers. Share your most interesting findings in a shared document.
