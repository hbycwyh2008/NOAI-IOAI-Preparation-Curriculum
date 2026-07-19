# Phase 3 — Neural Networks and CNN Foundations

Sessions 27–34. Standard duration: 90 minutes.

---

## Session 27 — Perceptrons, Neurons, Weights, Bias, and Activations

### Resource segment

3Blue1Brown Neural Networks: **But what is a neural network?**; teacher note on the perceptron.

### Essential teaching content

- A neuron forms a weighted sum plus bias: `z = w·x + b`.
- An activation transforms `z`; without nonlinear activations, stacked linear layers remain linear.
- Weights control feature influence; bias shifts the decision boundary.
- A perceptron creates a linear separator and cannot solve XOR with a single layer.

### Worksheet

1. Calculate `z` for `x=[2,-1]`, `w=[.5,3]`, `b=1`.
2. Apply step, sigmoid, and ReLU to supplied values.
3. Explain the role of bias geometrically.
4. Why do multiple linear layers without activations collapse into one linear transformation?
5. Draw a separator for AND and explain why XOR is not linearly separable.
6. Identify inputs, weights, bias, activation, and output in a diagram.

### Guided practice

Students calculate outputs for four binary inputs using a perceptron configured for AND, then attempt XOR and document failure.

### Independent task

Design perceptron weights for OR or NAND and verify all truth-table rows.

---

## Session 28 — Multilayer Networks and Forward Propagation

### Resource segment

3Blue1Brown: **What are the hidden layers doing?**; PyTorch basics conceptual preview of `nn.Linear` and activations.

### Essential teaching content

- Layers transform representations, not merely “store answers.”
- Forward propagation applies affine transformation and activation layer by layer.
- Tensor shapes must align: batch × input features, weight output × input, output batch × output features.
- Hidden units can combine multiple linear boundaries into nonlinear regions.

### Worksheet

1. State the output shape for input `(32,10)` through `Linear(10,6)`.
2. Calculate a two-neuron hidden layer for one supplied input.
3. Apply ReLU, then calculate the output neuron.
4. Explain hidden representation in your own words.
5. Find the matrix-shape error in a supplied network.
6. Count parameters in `Linear(10,6)` and `Linear(6,3)` including biases.

### Guided practice

Pairs complete a full numerical forward pass through a 2–2–1 network and compare intermediate activations.

### Independent task

Implement the same network using NumPy only and verify it against hand calculation.

---

## Session 29 — Loss, Gradient Descent, and Computational Graphs

### Resource segment

3Blue1Brown: **Gradient descent, how neural networks learn**; IOAI Academy: **Loss and Gradients Intuition**.

### Essential teaching content

- Loss evaluates one prediction; cost/objective aggregates losses and may include regularisation.
- A computational graph records dependencies required for derivatives.
- Partial derivatives measure local sensitivity while other variables are held fixed.
- Gradient descent updates every trainable parameter opposite its gradient.

### Worksheet

1. Calculate squared loss for prediction 4 and target 7.
2. For `L=(wx-y)^2`, calculate `dL/dw` at `w=2,x=3,y=5`.
3. Draw a graph for `z=wx+b`, `a=ReLU(z)`, `L=(a-y)^2`.
4. Explain why zero gradient can stop learning.
5. Apply one update with a supplied learning rate.
6. Distinguish loss value from gradient value.

### Guided practice

Students trace a scalar graph forward to compute values, then backward to compute local derivatives.

### Independent task

Implement numerical gradient checking for one scalar parameter and compare with an analytic derivative.

---

## Session 30 — Backpropagation and Chain-Rule Tracing

### Resource segment

3Blue1Brown: **Backpropagation calculus**; teacher chain-rule worksheet.

### Essential teaching content

- Backpropagation efficiently applies the chain rule from loss to earlier parameters.
- Each node multiplies incoming gradient by its local derivative.
- Gradients from multiple downstream paths add.
- ReLU derivative is zero for negative input and one for positive input, excluding the convention at zero.

### Worksheet

For `x=2`, `w=3`, `b=-1`, `z=wx+b`, `a=z^2`, `L=(a-20)^2`:

1. Calculate the full forward pass.
2. Calculate `dL/da`.
3. Calculate `da/dz`.
4. Calculate `dz/dw` and `dz/db`.
5. Calculate `dL/dw` and `dL/db`.
6. Explain the direction of a small gradient-descent update.
7. Identify one arithmetic checkpoint for catching mistakes.

### Guided practice

Pairs use different coloured arrows for values, local derivatives, and accumulated gradients. One student explains each multiplication aloud.

### Independent task

Trace a new graph containing ReLU. Verify with PyTorch autograd only after finishing the paper derivation.

---

## Session 31 — Momentum, RMSprop, Adam, and AdamW

### Resource segment

Deep Learning Specialization: optimisation algorithms overview; PyTorch optimizer documentation for SGD and AdamW.

### Essential teaching content

- Momentum averages past gradient direction and reduces zigzagging.
- RMSprop scales updates using recent squared gradients.
- Adam combines momentum-like first moments and RMS-like second moments.
- AdamW decouples weight decay from the adaptive gradient update.
- Optimizer choice does not replace learning-rate validation.

### Worksheet

1. Explain momentum with a physical analogy and then with an update concept.
2. Why can different parameter scales motivate adaptive methods?
3. State the two moving statistics used by Adam.
4. Distinguish L2 penalty from decoupled weight decay at an introductory level.
5. Predict what happens with a learning rate 100 times too high.
6. Design a fair comparison between SGD+momentum and AdamW.
7. List which settings and random factors must remain fixed.

### Guided practice

Students inspect optimisation paths on an elongated contour plot and match plain SGD, momentum, and adaptive behaviour.

### Independent task

Train the same small network with SGD, SGD+momentum, and AdamW using identical splits and seeds; compare convergence, validation score, and stability.

---

## Session 32 — Convolution Kernels and Feature Maps

### Resource segment

Deep Learning Specialization, Course 4: **Convolutional Neural Networks — Edge Detection and Convolution Operation**.

### Essential teaching content

- A kernel slides across local image regions and computes weighted sums.
- Weight sharing reduces parameters and detects the same pattern across locations.
- Multiple filters create multiple output channels/feature maps.
- Early filters often respond to local edges/textures; later representations combine them.

### Worksheet

1. Apply a 2×2 kernel to one 2×2 image patch.
2. Calculate a full valid convolution on a 3×3 image with a 2×2 kernel.
3. Explain weight sharing.
4. If a layer has 16 filters, how many output channels result?
5. Why is convolution better suited than a fully connected layer to local image structure?
6. Compare correlation as implemented in libraries with mathematically flipped convolution; explain why the learned-filter interpretation still works.

### Guided practice

Students manually apply horizontal and vertical edge kernels to simple binary images and interpret positive/negative responses.

### Independent task

Use NumPy to implement single-channel valid correlation and test it on two patterns.

---

## Session 33 — Padding, Stride, Pooling, and Tensor Shapes

### Resource segment

Deep Learning Specialization: **Padding, Strided Convolutions, Pooling**; PyTorch Conv2d/MaxPool2d shape documentation.

### Essential teaching content

For one spatial dimension:

`output = floor((input + 2*padding - dilation*(kernel-1) - 1)/stride + 1)`.

- Padding controls border treatment and spatial size.
- Stride controls movement and downsampling.
- Pooling summarises local regions but discards detail.
- Shape errors are among the most common CNN implementation failures.

### Worksheet

1. Calculate output size for input 32, kernel 3, padding 1, stride 1.
2. Repeat for stride 2.
3. Calculate output shape for input `(16,3,64,64)` through `Conv2d(3,8,3,padding=1)`.
4. Continue through `MaxPool2d(2)`.
5. Calculate flattened features before a dense layer.
6. Explain when excessive downsampling is harmful.
7. Diagnose a supplied `Linear` input-size mismatch.

### Guided practice

Students complete a shape ledger for a five-layer CNN before seeing any code execution.

### Independent task

Write a PyTorch CNN whose comments state every tensor shape; verify with one dummy batch.

---

## Session 34 — CNN Architecture, Softmax, and Cross-Entropy

### Resource segment

PyTorch Learn the Basics: **Build Model** and **Optimization Loop**; Google MLCC multi-class classification introduction.

### Essential teaching content

- Classification networks usually output logits, not probabilities, during training.
- Softmax converts logits into a distribution across classes.
- Cross-entropy combines log-softmax and negative log-likelihood in common libraries.
- Do not apply Softmax before PyTorch `CrossEntropyLoss`.
- Train/eval mode matters for dropout and batch normalization.

### Worksheet

1. Define a logit.
2. Softmax logits `[0,0]`; explain the result.
3. Which logit vector gives greater confidence: `[1,0]` or `[10,0]`?
4. Why should labels for `CrossEntropyLoss` usually be integer class indices?
5. Explain why applying Softmax twice is incorrect.
6. State the difference between `model.train()` and `model.eval()`.
7. Identify the correct order: zero gradients, forward, loss, backward, optimizer step.
8. Explain top-1 accuracy and one limitation.

### Guided practice

Students connect an architecture diagram to code, output shapes, logits, loss input, and predicted class.

### Independent task

Build a compact CNN for a small synthetic image dataset. Demonstrate a clean training/validation loop and analyse at least five errors.

### Phase 3 exit gate

Students must complete a numerical forward pass, a chain-rule backpropagation trace, optimizer comparison explanation, convolution calculation, CNN shape ledger, and cross-entropy workflow without notes.