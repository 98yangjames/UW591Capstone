# UW591Capstone

## Flipkart MedOCR

### Introduction
With the growing demand for auto health delivery and e-pharmacy,
Flipkart Health Plus has been receiving a significant number of
40,000 medical uploads daily. However, due to the need for a
pharmacist to review and approve each upload before processing,
the company has been facing challenges in dealing with the high
volume of requests. To overcome this hurdle, Flipkart Health is
exploring the implementation of a machine-aided system that
leverages artificial intelligence to assist with the review and
approval process.

### Improving the OCR Model with Data
#### Digitized Text Generation
The given FlipKart prescription images have too much variation in them. The combination of different backgrounds mixed with different texts make it difficult to produce an generalizable and accurate OCR (Optical Character Recognition) model. 

* To counteract this, we used PaddleOCR to extract printed text and backgrounds from the given images to produce synthesized fake images. 
* These images are combinations of different texts and backgrounds put together to help reinforce the training data being put into the MedOCR model.
* We produced 30 different backgrounds with N different extracted texts from the images. 

#### Handwritten Text Generation
To improve an OCR model's performance, it is essential to have a large variation of images that could potentially be passed, including both digitized and handwritten text.  While there is a large number of solutions and datasets for digitized text, handwritten datasets are limited by number of labeled data points. For this reason, we explore generative models for creating synthetic handwritten data to capture various nuances of handwriting styles, strokes, and shapes. We did so by passing in medical text names (e.g., “Acilioc 150 mg”, “Rejulox od 10”) to the model for handwritten image generation (300x340 pixels png images). These were done with two different generative techniques: 
* Generating Handwriting Sequences (RNNs):  
LSTM-based RNNs can be used to generate realistic sequences of online handwriting. The approach works by training the network by predicting the next point in a sequence given previous points. At each time step, the network takes in previous points and the current hidden state to output the next point in the sequence. 
* Diffusion
Diffusion models are a class of generative models that start from Gaussian noise and gradually denoise to produce the desired output. The goal is to learn the probability distribution over the image space as the image is gradually denoised. At each step, the probability distribution is updated by applying a diffusion process to the current state of the image. This process is modeled by a Gaussian diffusion process, where the image is gradually smoothed by adding Gaussian noise to the pixels.

### Improving the Resolution System
#### Integrating 6 NIH APIs for populating Medical Data
The catalog had close to 100,000 product listings - each containing multiple salts in their composition.
Six APIs that the National Institute of Health made available to users to retrieve data from several drug information sources were integrated and run on the catalog data. This is in-line with the aim of building a chatbot-like model to answer customers' questions around medicines that can be used in the treatment of different diseases or to find out the physiological effects of a particular drug. This will also help improve the OCR model by listing down the exact drug/salt that helps treat a disease (that may be mentioned on a doctor's prescription). These APIs helped populate information for 30000 products and contributed significantly to improving the final model and building a functional chatbot.

#### Catalog Product Search with Vector Similarity Matching 
OCR outputs often contain errors which can cause issues with product identification. We aim to generate product name embeddings using BioBERT and utilize vector similarity matching for efficient OCR outputs.
We trained BioBERT, a pre-trained language model on a large corpus of biomedical text, to generate embedding vectors for product names. Then, we utilized vector similarity matching to find the closest product name to the OCR output. We calculated the cosine similarity between the OCR output embedding and each product name embedding, and selected the product name with the highest similarity score.

### Conclusion 
In conclusion, the MedOCR project addresses several challenges: identifying text segments on handwritten and digitized images, and improving the resolution system. Our team set out to accomplish these goals by augmenting our data via generative techniques, and adding semantic matching on a wider medical database for medical name resolution.
We believe our project has the potential to significantly reduce manual intervention in processing medical prescriptions, leading to better user experiences and improved efficiency.


