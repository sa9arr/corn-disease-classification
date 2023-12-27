# Corn Disease Classification

This project is a corn disease classification system that utilizes Convolutional Neural Networks (CNNs) to classify leaf images of corn plants into one of four classes: 'Blight', 'Common_Rust', 'Gray_Leaf_Spot', and 'Healthy'. The model has been trained on 4188 images belonging to 4 classes for 60 epochs, achieving an impressive accuracy of 98.80% on the training data and a validation accuracy of 97%.

## Features

- **High Accuracy**: The model boasts a high accuracy rate, making it reliable for corn disease classification.
- **FastAPI Backend**: The backend is built using FastAPI, a modern, fast, web framework for building APIs with Python.
- **React Frontend**: The user interface is developed using React, providing an interactive and responsive experience.

## Demo
### Landing page
![Landingpage](https://github.com/sa9arr/corn-disease-classification/blob/master/screenshots/screenshot1.png)

### Prediction
![Prediction](https://github.com/sa9arr/corn-disease-classification/blob/master/screenshots/prediction.png)



## How to Run Locally

To run this project locally, follow the steps below:

### Prerequisites

- [Python](https://www.python.org/) installed on your machine.
- [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/) installed for the React frontend.

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sa9arr/corn-disease-classification.git
   cd corn-disease-classification

2. **Setup Virtual Environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
   
3. **Change to api directory:**
   ```bash
   cd api

4. **Install the requirements.txt file:**
   ```bash  
   pip install requirements.txt

5. **Run the fastapi server:**
   ```bash
   python main.py
 
   
6. **Setup and Run the frontend(React) server:**
   ```bash
   npm install
   npm start

 The React server will be running at http://localhost:3000/.
 The fastapi server will be running at http://localhost:8000/.

## Model Info Screenshots:
### Training Epochs and corresponding accuracy
![Epochs](https://github.com/sa9arr/corn-disease-classification/blob/master/screenshots/epochs.png)

### Losses and Accuracy
![loss](https://github.com/sa9arr/corn-disease-classification/blob/master/screenshots/losses%20and%20accuracy.png)

## Datasets

The dataset comprises images of corn leaves categorized into four classes:

Common Rust: 1306 images
Gray Leaf Spot: 574 images
Blight: 1146 images
Healthy: 1162 images
This diverse collection has been sourced from a publicly available Kaggle dataset. For access to the dataset, please follow this [link](https://www.kaggle.com/datasets/smaranjitghose/corn-or-maize-leaf-disease-dataset) 

  
## Contributing:
Contributions are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request.


## Acknowledgements

I extend my sincere appreciation to [Codebasics](https://github.com/codebasics) for their invaluable contribution to this project. The meticulously crafted and insightful video lecture series on deep learning offered by Codebasics played a pivotal role in guiding me through the intricacies of this project. The clarity and depth of their explanations have significantly influenced and enhanced my comprehension of the underlying concepts.

- GitHub: [Codebasics](https://github.com/codebasics)

## Future Development:

In subsequent phases of this project, there is a plan to extend its accessibility and usability by developing a mobile application. This application will facilitate on-the-field classification of corn diseases, providing a user-friendly and efficient tool for immediate disease identification in real-world agricultural settings. This strategic expansion aims to enhance the practical utility of the corn disease classification system, bringing the benefits directly to those involved in crop monitoring and management.

## License:
This project is licensed under the MIT License.

