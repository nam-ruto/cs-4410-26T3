Task 1: (Exercise 16.1 - Textbook) (Image Recognition: The Fashion-MNIST Dataset)
(Check 16_06.ipynb for reference) 
- Keras comes bundled with the Fashion-MNIST database of fashion articles which, like the MNIST digits dataset, provides 28-by-28 grayscale images
- Fashion-MNIST contains clothing-article images labeled in 10 categories—0 (T-shirt/top), 1 (Trouser), 2 (Pullover), 3 (Dress), 4 (Coat), 5 (Sandal), 6 (Shirt), 7 (Sneaker), 8 (Bag), 9 (Ankle boot)—with 60,000 training samples and 10,000 testing samples.
- Modify this chapter’s convnet example to load and process Fashion-MNIST rather than MNIS - this requires simply importing the correct module, loading the data then running the model with these images and labels, then re-run the entire example.
- Question: How well does the model perform on Fashion-MNIST compared to MNIST? How do the training times compare?

Task 2: (Exercise 16.4 - Textbook) (Convnet Layers) Remove the first Dense layer in this chapter’s convnet model. How does this change the prediction accuracy? Several Keras pretrained convnets contain Dense layers with 4096 neurons. Add such a layer before the two Dense layers in this chapter’s convnet model. How does this change the prediction accuracy?