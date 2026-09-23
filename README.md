# 🩺 Diabetes Prediction Model

A **Machine Learning-based web application** that predicts whether a person is likely to have diabetes based on important medical and personal health parameters.

The project uses **Python, Machine Learning, Scikit-learn, Flask, HTML, and CSS** to provide an easy-to-use web interface for diabetes prediction.

> **Disclaimer:** This project is developed for educational and demonstration purposes only. It is not a substitute for professional medical diagnosis or advice.

---

## 🚀 Project Overview

Diabetes is a common health condition that can be identified using various medical and demographic factors.

This project uses a trained Machine Learning model to analyze patient information and predict one of two outcomes:

* ✅ **Non-Diabetic**
* ⚠️ **Diabetic**

The trained model is integrated with a **Flask web application**, allowing users to enter their health information through a simple web form and receive a prediction.

---

## ✨ Features

* 🧠 Machine Learning-based diabetes prediction
* 🌐 Flask web application
* 📋 User-friendly prediction form
* 📊 Uses multiple medical parameters
* ⚡ Fast prediction results
* 🎨 Responsive HTML/CSS interface
* 💾 Pre-trained Machine Learning model
* 🔄 Real-time prediction through the web application
* 📱 Simple and accessible user interface

---

## 🛠️ Technologies Used

| Technology       | Purpose                          |
| ---------------- | -------------------------------- |
| **Python**       | Programming language             |
| **Pandas**       | Data processing                  |
| **NumPy**        | Numerical operations             |
| **Scikit-learn** | Machine Learning                 |
| **Flask**        | Web application framework        |
| **HTML5**        | Web page structure               |
| **CSS3**         | Web page styling                 |
| **Pickle**       | Saving and loading trained model |
| **Git & GitHub** | Version control                  |

---

## 📊 Dataset

The project uses the **PIMA Indians Diabetes Dataset**, which contains medical information used to predict diabetes.

### Input Features

The model uses the following parameters:

| Feature                        | Description                          |
| ------------------------------ | ------------------------------------ |
| **Pregnancies**                | Number of times pregnant             |
| **Glucose**                    | Plasma glucose concentration         |
| **Blood Pressure**             | Diastolic blood pressure             |
| **Skin Thickness**             | Triceps skin fold thickness          |
| **Insulin**                    | 2-Hour serum insulin                 |
| **BMI**                        | Body Mass Index                      |
| **Diabetes Pedigree Function** | Diabetes-related genetic information |
| **Age**                        | Patient's age                        |

### Target

The target variable is:

* `0` → Non-Diabetic
* `1` → Diabetic

---

## 🔄 Project Workflow

```text
                 ┌─────────────────────┐
                 │   Diabetes Dataset  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Data Preprocessing  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Feature Preparation │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Machine Learning    │
                 │ Model Training      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Trained Model     │
                 │     model.pkl       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Flask Web App    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ User Enters Medical │
                 │      Details        │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Diabetes Prediction │
                 └─────────────────────┘
```

---

## 📁 Project Structure

```text
diabetes-prediction-model/
│
├── static/
│   └── CSS and other static files
│
├── templates/
│   └── HTML templates
│
├── app.py
│   └── Flask application
│
├── model.py
│   └── Machine Learning model training
│
├── diabetes.csv
│   └── Diabetes dataset
│
├── model.pkl
│   └── Saved/trained Machine Learning model
│
└── README.md
    └── Project documentation
```

---

## 🧠 Machine Learning Process

The Machine Learning workflow consists of the following steps:

### 1. Data Collection

The diabetes dataset is loaded using Pandas.

### 2. Data Preprocessing

The dataset is prepared for Machine Learning by separating:

* Input features `X`
* Target variable `Y`

### 3. Feature Scaling

The numerical features are standardized so that the Machine Learning algorithm can process them effectively.

### 4. Train-Test Split

The dataset is divided into training and testing data.

### 5. Model Training

A Machine Learning classification model is trained using the prepared dataset.

### 6. Model Saving

After training, the model is saved using Python's `pickle` module.

```text
model.pkl
```

### 7. Flask Integration

The saved model is loaded into the Flask application.

### 8. Prediction

When the user submits the form, the entered values are passed to the trained model.

The application then displays the prediction:

```text
Diabetic
```

or

```text
Non-Diabetic
```

---

## 🌐 Flask Web Application

The Flask application provides a web interface where users can enter their medical information.

### Application Flow

```text
User
 │
 ▼
Web Form
 │
 ▼
Enter Health Parameters
 │
 ▼
Flask /predict Route
 │
 ▼
Machine Learning Model
 │
 ▼
Prediction
 │
 ├───────────────┐
 ▼               ▼
Diabetic      Non-Diabetic
```

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sudeepsagar1807/diabetes-prediction-model.git
```

### 2. Navigate to the Project

```bash
cd diabetes-prediction-model
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 5. Install Required Libraries

```bash
pip install flask pandas numpy scikit-learn
```

---

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

You should see the Flask server running locally.

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## 📌 Example Input

Example patient information:

```text
Pregnancies: 8
Glucose: 125
Blood Pressure: 96
Skin Thickness: 0
Insulin: 0
BMI: 0
Diabetes Pedigree Function: 0.232
Age: 54
```

The application processes these values through the trained Machine Learning model and displays the predicted result.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. To understand Machine Learning classification.
2. To work with real-world healthcare data.
3. To preprocess and prepare data for Machine Learning.
4. To train a diabetes prediction model.
5. To save and reuse a trained Machine Learning model.
6. To integrate Machine Learning with Flask.
7. To create a simple web interface for prediction.
8. To understand the deployment of ML models as web applications.

---

## 🔮 Future Improvements

Some possible improvements include:

* Improve model performance through hyperparameter tuning.
* Compare multiple Machine Learning algorithms.
* Add model performance visualizations.
* Add probability/confidence scores.
* Improve the user interface.
* Add input validation.
* Deploy the application using cloud services.
* Add a database for storing prediction history.
* Add authentication for users.
* Provide personalized health information based on prediction results.

---

## ⚠️ Disclaimer

This application is intended **only for educational and demonstration purposes**.

The prediction generated by this Machine Learning model should **not be considered a medical diagnosis**. Users should consult a qualified healthcare professional for medical advice, testing, and diagnosis.

---

## 👨‍💻 Author

### Sudeep Kumar

**B.Tech Computer Science Engineering Student**

GitHub:
[@sudeepsagar1807](https://github.com/sudeepsagar1807?utm_source=chatgpt.com)

Project Repository:
[Diabetes Prediction Model](https://github.com/sudeepsagar1807/diabetes-prediction-model?utm_source=chatgpt.com)

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

### 📜 License

This project is intended for educational purposes.
