# Prompts

## Prompt engineering

1. Create an account on:
    - a commercial platform ([ChaGPT](https://chatgpt.com/) from OpenAI or [Le Chat](https://chat.mistral.ai/) from Mistral AI)
    - an open-source platform (https://llm.mi.parisdescartes.fr/)
2. Try the same prompt on both platforms. Do some models need more context (i.e. explanations) than others to give expected results?
3. Evaluate the different models for:
    - Text production ("Write a 10-line text about...")
    - Text summarization ("Summarize the following text in 5 lines...")
    - Code production ("Write a Python function that extracts and prints sequence length from a FASTA file named 'sequences.fasta'. Add comments to explain how the function works.") Share your code in a shared document.
4. Challenge various LLM with common math problems you could find in the [gsm8k dataset](https://huggingface.co/datasets/openai/gsm8k):

    ```
    Betty is saving money for a new wallet which costs $100.
    Betty has only half of the money she needs. Her parents
    decided to give her $15 for that purpose, and her 
    grandparents twice as much as her parents. How much more 
    money does Betty need to buy the wallet?
    ```

    ```
    Julie is reading a 120-page book. Yesterday, she was able to
    read 12 pages and today, she read twice as many pages as 
    yesterday. If she wants to read half of the remaining pages 
    tomorrow, how many pages should she read?
    ```

    ```
    John buys 10 packs of magic cards. Each pack has 20 cards
    and 1/4 of those cards are uncommon. How many uncommon cards
    did he get?
    ```

    ```
    Paul went to a shop to buy some groceries. He bought some 
    bread for $2, butter for $3, and juice for two times the 
    price of the bread. He had $15 for his shopping. How much 
    money did Paul have left?
    ```

    ```
    Mr. Grey is purchasing gifts for his family. So far he has 
    purchased 3 polo shirts for $26 each; 2 necklaces for $83 
    each; and 1 computer game for $90. Since Mr. Grey purchased 
    all those using his credit card, he received a $12 rebate. 
    What is the total cost of the gifts after the rebate?
    ```


Most LLMs should succeed in these challenges, mostly because they come from a well-known problem database they could have already been trained on. Try to create your own math problem and find out how LLMs behave. Share your most interesting problems in a shared document.
