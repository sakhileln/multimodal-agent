# Learning Notes
## Quick Takeaway: Limited Accuracy with a Small Model
- As part of building this Simple Multimodal Agent, one key lesson learned is that using a lightweight model like `MobileNet` comes with trade-offs in accuracy. `MobileNet`, while efficient and suitable for running on a standard CPU, is a small, pre-trained model optimized for speed and low resource usage rather than top-tier precision. During testing, it correctly identified common objects (e.g., "dog" in dog.jpg), but its predictions can be less reliable for complex or ambiguous images compared to larger models like `ResNet` or `Vision Transformers`. This reflects a broader principle in AI: model size and complexity often correlate with accuracy, but simplicity was prioritized here for learning purposes and local execution. Future iterations could explore larger models or fine-tuning to improve performance, though that would require more computational resources.


#### Image Classification Results

| Image         | Prediction        | Actual          |
|--------------|------------------|----------------|
| cat.jpg      | tiger_cat        | cat            |
| dog.jpg      | German_shepherd  | German_shepherd |
| girl.jpg     | jean             | girl           |
| poeple.jpeg  | volleyball       | students       |
| woman.jpg    | rapeseed         | lady           |
| woman2.jpg   | sweatshort       | lady           |
| woman4.jpeg  | hair_slide       | lady           |
| woman6.jpg   | bathing_cap      | lady           |
| woman7.jpg   | bikini           | lady           |


