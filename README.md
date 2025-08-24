# 🍷 Wine Quality Prediction Pipeline

![Python](https://img.shields.io/badge/python-v3.10-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Framework](https://img.shields.io/badge/framework-Flask-orange.svg)

## 📋 Description

A complete end-to-end Machine Learning pipeline for predicting wine quality scores. This project implements a modular and production-ready ML system that includes data ingestion, validation, transformation, model training, and evaluation stages.

### Key Features

- Automated data ingestion and validation
- Configurable data transformation pipeline
- Model training with hyperparameter optimization
- Model evaluation and metrics tracking
- Web interface for easy interaction

## 🛠️ Tech Stack

- **Python 3.10**
- **Web Framework:** Flask
- **ML Libraries:**
  - scikit-learn
  - pandas
  - numpy
- **Development Tools:**
  - Dagshub
  - Mlflow
  - Jupyter Notebooks
- **Other Dependencies:** See requirements.txt

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/FullMLPipe.git
cd FullMLPipe
```

2. Create a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables (create .env file):

```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
MLFLOW_TRACKING_URI=your_mlflow_uri
```

## 💻 Usage

### Running the Pipeline

1. Execute the complete pipeline:

```bash
python main.py
```

2. Run the Flask application:

```bash
python app.py
```

## 📁 Project Structure

```
FullMLPipe/
├── src/FullMLPipe/          # Core ML pipeline components
│   ├── components/          # Individual pipeline stages
│   ├── config/             # Configuration management
│   ├── pipeline/           # Pipeline orchestration
│   └── utils/              # Utility functions
├── artifacts/              # Generated artifacts
├── config/                 # Configuration files
├── research/               # Jupyter notebooks for experimentation
├── templates/              # Web interface templates
└── logs/                   # Application logs
```

## ⚙️ Configuration

Configuration is managed through YAML files:

- `config/config.yaml`: Main configuration
- `params.yaml`: Model parameters
- `schema.yaml`: Data validation schema

### Required Environment Variables

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `MLFLOW_TRACKING_URI`

## 🔄 API Documentation

### Endpoints

`POST /predict`

- Accepts wine characteristics as JSON
- Returns predicted quality score

Example request:

```json
{
  "fixed_acidity": 7.4,
  "volatile_acidity": 0.7,
  "citric_acid": 0.0,
  "residual_sugar": 1.9,
  "chlorides": 0.076,
  "free_sulfur_dioxide": 11.0,
  "total_sulfur_dioxide": 34.0,
  "density": 0.9978,
  "pH": 3.51,
  "sulphates": 0.56,
  "alcohol": 9.4
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file
