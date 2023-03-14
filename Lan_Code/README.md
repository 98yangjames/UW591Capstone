# UW591Capstone - Catalog Product Search with Vector Similarity Matching

OCR outputs often contain errors which can cause issues with product identification. We aim to generate product name embeddings using BioBERT and utilize vector similarity matching for efficient OCR outputs.

> We trained BioBERT, a pre-trained language model on a large corpus of biomedical text, to generate embedding vectors for product names. Then, we utilized vector similarity matching to find the closest product name to the OCR output. We calculated the cosine similarity between the OCR output embedding and each product name embedding, and selected the product name with the highest similarity score.


OCR Prediction: propysic nf6
Ground-truth: propysalic nf6
Best Vector Similarity matching:  pqten
Cosine Similarity Score: 0.94
