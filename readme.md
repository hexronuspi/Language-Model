My first attempt in creating a language Model.

Note: This is heavily inspired by Andrej Karpathy's Makemore series and his works.

```Ongoing Work```
### Usage
`Language-Model\model`

The files are organized into two primary categories: `word` and `character`. These categories denote the type of encoding used in the text data.

- **Word**: The `word` category contains files that utilize word-level encoding. In this encoding scheme, each unique word in the text data is represented by a unique integer or vector. Word-level encoding is particularly useful for tasks where the semantic meaning of words is crucial.

- **Character**: The `character` category contains files that employ character-level encoding. In this encoding scheme, each unique character in the text data is represented by a unique integer or vector. Character-level encoding is beneficial for tasks where the structure and spelling of words are significant, such as in text generation or language modeling.

Within each of these primary categories, there are two types of files: `Bigram` and `LSTM`. These represent the algorithms used to process the encoded text data.

- **Bigram**: Files under this type utilize a bigram model. A bigram model is a type of language model that predicts the next word in a sequence based on the preceding word. While bigram models are simple and efficient, they are unable to capture long-term dependencies in the text data.

- **LSTM**: Files under this type employ a Long Short-Term Memory (LSTM) model. An LSTM model is a type of recurrent neural network (RNN) capable of learning and remembering patterns over time. Although LSTM models are more complex and computationally intensive than bigram models, they can capture long-term dependencies in the text data. This makes them useful for more complex tasks such as text generation or machine translation.
