# Num-Eng Machine Translation

I have trained and fine-tuned the **[Text-to-Text Transfer Transformer (T5)](https://huggingface.co/transformers/model_doc/t5.html)** on custom dataset that I have downloaded from [here](https://www.calculatorsoup.com/calculators/conversions/numberstowords.php)

Here, I used **huggingface's** `t5-small` model (66 million parameters). I set `batch_size=128` and `learning_rate=0.001` (as they propossed in the [literature](https://arxiv.org/pdf/1910.10683.pdf)) without any `warmup` or `lr_schedule`.

1. 
    * Input text: `392665`

    * Pre-processed text: `"number to english: 3 9 2 6 6 5"`

    * Predicted output text: `"three hundred ninety-two thousand six hundred sixty-five"`

2. 
    * Input text: `"four hundred ninety-eight thousand one hundred forty-two"`

    * Pre-processed text: `"english to number: four hundred ninety-eight thousand one hundred forty-two"`

    * Predicted output text: `"4 9 8 1 4 2"`

3. 
    * Input text: `92923`

    * Pre-processed text: `"number to english: 9 2 9 2 3"`

    * Predicted output text: `"ninety-two thousand nine hundred twenty-three"`

4. 
    * Input text: `"eight hundred ninety-four thousand nine hundred sixty-five"`

    * Pre-processed text: `"english to number: eight hundred ninety-four thousand nine hundred sixty-five"`

    * Predicted output text: `"8 9 4 9 6 5"`

4. 
    * Input text: `"four hundred ninety-three"`

    * Pre-processed text: `"english to number: four hundred ninety-three"`

    * Predicted output text: `"4 9 3"`