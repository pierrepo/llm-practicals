# Embeddings

*In this section, we’re mentioning words, but in reality we are manipulating [tokens](tokens.md).*


## Explore the multidimensional space
Viewing embeddings in high-dimensional space is impossible for any human. The web app [Embedding Projector](https://projector.tensorflow.org/) projects many dimensions into only 3: it's easier to see but at the cost of a strong simplification.

1. Open the [Embedding Projector](https://projector.tensorflow.org/) app.
2. Keep default parameters (Word2Vec 10k). In this case, you’re viewing 10,000 words (tokens) from 200 dimensions projected into 3 dimensions.
3. In the right panel, search for a word (for instance, “biology”) and set the number of neighbors as “10”:

```{image} img/embedding_projector.png
:alt: Copie d'écran de l'application Embedding Projector
:class: bg-primary mb-1
:align: center
:width: 600px
```

4. Find the closest words (tokens).
5. Try with other words (for instance: “DNA”, “mouse”...).
6. Click on the “Clear selection” button (top-right corner).
7. Hover points and select one with a left click.
8. Find out closest words (tokens) listed on the right panel.
9. Repeat this operation several times.


## Do the (vector) math

1. Open the [Dash Word Embeddings Arithmetic](https://dash.gallery/dash-word-arithmetic/) app.
2. The idea is to:
    - Start from a word (for instance: “France”)
    - Subtract a word (for instance: “Paris”)
    - Add another a word (for instance: “Tokyo”)
    - Click the “Run” button.
    - Find the nearest word (not from the input word list) in yellow in the right panel. In this case: “Japan”
    - In the above example, we started with a country (“France”), subtracted its capital (“Paris”) and added a new country (“Japan”) to obtain its capital (“Tokyo”).
    - Note: top nearest words are often the ones taken as inputs. We are looking for the nearest word, **not provided as inputs**.


```{image} img/embeddings_arithmetic.png
:alt: Copie d'écran de l'application Embeddings Arithmetic
:class: bg-primary mb-1
:align: center
:width: 600px
```

3. Try out other word operations for yourself. Here are a few examples to get you started:
- uncle - man + woman = ?
- niece - woman + man = ?
- cars - car + bike = ?
- train - trains + pen = ?
- feet - foot + goose = ?
- mice - mouse + child = ?
- cucumber - vegetable + fruit = ?
- sushi - japan + germany = ?
- beer - bubble + grape = ?
4. Try to find out other word operations. Share your most interesting findings in a shared document.
