# Prompts

## Prompt engineering

1. Create an account on:
    - a commercial platform ([ChatGPT](https://chatgpt.com/) from OpenAI or [Le Chat](https://chat.mistral.ai/) from Mistral AI)
    - an open-source platform (https://llm.mi.parisdescartes.fr/)
2. Try the same prompt on both platforms. Do some models need more context (i.e. explanations) than others to give expected results?
3. Evaluate the different models for:
    - Text production ("Write a 10-line text about...")
    - Text summarization ("Summarize the following text in 5 lines...")
    - Code production ("Write a Python function that extracts and prints sequence length from a FASTA file named 'sequences.fasta'. Add comments to explain how the function works.") Share your code in a shared document.


## Success and failure with math problems

Challenge various LLM with common math problems you could find in the [gsm8k dataset](https://huggingface.co/datasets/openai/gsm8k):

```
Betty is saving money for a new wallet which costs $100.
Betty has only half of the money she needs. Her parents
decided to give her $15 for that purpose, and her 
grandparents twice as much as her parents. How much more 
money does Betty need to buy the wallet?
```

```{admonition} Answer
:class: tip, dropdown
5
```

```
Julie is reading a 120-page book. Yesterday, she was able to
read 12 pages and today, she read twice as many pages as 
yesterday. If she wants to read half of the remaining pages 
tomorrow, how many pages should she read?
```

```{admonition} Answer
:class: tip, dropdown
42
```

```
John buys 10 packs of magic cards. Each pack has 20 cards
and 1/4 of those cards are uncommon. How many uncommon cards
did he get?
```

```{admonition} Answer
:class: tip, dropdown
50
```

```
Paul went to a shop to buy some groceries. He bought some 
bread for $2, butter for $3, and juice for two times the 
price of the bread. He had $15 for his shopping. How much 
money did Paul have left?
```

```{admonition} Answer
:class: tip, dropdown
6
```

```
Mr. Grey is purchasing gifts for his family. So far he has 
purchased 3 polo shirts for $26 each; 2 necklaces for $83 
each; and 1 computer game for $90. Since Mr. Grey purchased 
all those using his credit card, he received a $12 rebate. 
What is the total cost of the gifts after the rebate?
```

```{admonition} Answer
:class: tip, dropdown
322
```


Most LLMs should succeed in these challenges, mostly because they come from a well-known problem database they could have already been trained on. Try to create your own math problem and find out how LLMs behave. Share your most interesting problems in a shared document.


## Difficult questions

Since LLMs are not able to reason, they can fail on simple questions. Challenge various LLMs with the following ones:

- Give me 10 sentences that end in the word "Apple"
- Écris 10 phrases qui se terminent par le mot "clavier"
- How many Rs are in the word "strawberry"?
-  I have 5 shirts that will take 6 hours to dry in the sun. How long will it take 30 shirts to dry?
- How many words are in your response to this prompt? (by [Matthew Berman](https://x.com/matthewberman/status/1834295485773054312))


## Jailbreaking

Jailbreaking a LLM is a technique that consists of designing a prompt to bypass the safety mechanisms of the LLM to reveal information it should not.

[Gandalf](https://gandalf.lakera.ai/) is a web application that allows you to test your prompt injection skills by trying to force a LLM to reveal a password. Give it a try.

