# Protein Predictor Server

This is the backend server for the Protein Predictor application. It is built using Flask and provides endpoints for processing protein data and making predictions.

---

## Prerequisites

Before running the server, ensure you have the following installed:

- Python (3.8 or later)
- pip (Python package manager)

---

## Installation and Setup

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/birehan/protein-predictor-server.git
   cd protein-predictor-server
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**  
   Create a virtual environment to isolate dependencies:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**  
   Install the required Python packages:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Server

1. **Start the Flask Server**  
   Run the following command in the terminal:  
   ```bash
   flask run
   ```

   By default, the server will start on `http://127.0.0.1:5000/`.

2. **Access the API**  
   You can now make requests to the API endpoints, all of which are prefixed with `/api`.

---

## API Details

### 1. Health Check  
**Endpoint**: `/api/health`  
**Method**: `GET`  
**Description**: Simple health check to verify the backend is running.  
**Response**:  
```json
{
  "status": "Backend is working fine!"
}
```

---

### 2. Get Available Models  
**Endpoint**: `/api/models`  
**Method**: `GET`  
**Description**: Retrieves a list of available prediction models.  
**Response**:  
```json
{
  "available_models": [
    "RandomForestClassifier",
    "GradientBoostingClassifier",
    "XGBClassifier",
    "LogisticRegression",
    "DecisionTreeClassifier",
    "KNeighborsClassifier"
  ]
}
```

---

### 3. Make a Prediction  
**Endpoint**: `/api/predict/<model_name>` - `http://127.0.0.1:5000/api/XGBClassifier`
**Method**: `POST`  
**Description**: Use a specific model to make a prediction. Requires a JSON payload with all 71 features.  

**Request Body**:  
A JSON object containing all 71 required features:  
```json
{
  "AAC_A": 0.1,
  "AAC_C": 0.2,
  "AAC_D": 0.3,
  "AAC_E": 0.4,
  "AAC_F": 0.5,
  "AAC_G": 0.6,
  "AAC_H": 0.7,
  "AAC_I": 0.8,
  "AAC_K": 0.9,
  "AAC_L": 0.10,
  "AAC_M": 0.11,
  "AAC_N": 0.12,
  "AAC_P": 0.13,
  "AAC_Q": 0.14,
  "AAC_R": 0.15,
  "AAC_S": 0.16,
  "AAC_T": 0.17,
  "AAC_V": 0.18,
  "AAC_W": 0.19,
  "AAC_Y": 0.20,
  "PCP_PC": 0.1,
  "PCP_NC": 0.2,
  "PCP_NE": 0.3,
  "PCP_PO": 0.4,
  "PCP_NP": 0.5,
  "PCP_AL": 0.6,
  "PCP_CY": 0.7,
  "PCP_AR": 0.8,
  "PCP_AC": 0.9,
  "PCP_BS": 0.10,
  "PCP_NE_pH": 0.11,
  "PCP_HB": 0.12,
  "PCP_HL": 0.13,
  "PCP_NT": 0.14,
  "PCP_HX": 0.15,
  "PCP_SC": 0.16,
  "PCP_SS_HE": 0.17,
  "PCP_SS_ST": 0.18,
  "PCP_SS_CO": 0.19,
  "PCP_SA_BU": 0.20,
  "PCP_SA_EX": 0.21,
  "PCP_SA_IN": 0.22,
  "PCP_TN": 0.23,
  "PCP_SM": 0.24,
  "PCP_LR": 0.25,
  "PCP_Z1": 0.26,
  "PCP_Z2": 0.27,
  "PCP_Z3": 0.28,
  "PCP_Z4": 0.29,
  "PCP_Z5": 0.30,
  "SEP": 0.31,
  "SER_A": 0.32,
  "SER_C": 0.33,
  "SER_D": 0.34,
  "SER_E": 0.35,
  "SER_F": 0.36,
  "SER_G": 0.37,
  "SER_H": 0.38,
  "SER_I": 0.39,
  "SER_K": 0.40,
  "SER_L": 0.41,
  "SER_M": 0.42,
  "SER_N": 0.43,
  "SER_P": 0.44,
  "SER_Q": 0.45,
  "SER_R": 0.46,
  "SER_S": 0.47,
  "SER_T": 0.48,
  "SER_V": 0.49,
  "SER_W": 0.50,
  "SER_Y": 0.51
}
```

**Response**:  

- If the prediction is successful:  
  ```json
  {
    "prediction": 1,
    "prediction_label": "Positive"
  }
  ```

---

## Configuration

- **Environment Variables**:  
  Flask can be configured using environment variables. Create a `.env` file in the root directory and add the following:  
  ```env
  FLASK_APP=app.py
  FLASK_ENV=development  # Set to "production" for deployment
  ```

- **Default Port**:  
  If you need to change the port, use the `--port` flag:  
  ```bash
  flask run --port=8080
  ```

---

## Troubleshooting

- If Flask is not recognized as a command, install Flask globally:  
  ```bash
  pip install flask
  ```
- If you encounter issues with dependencies, double-check the Python version and ensure all required libraries are installed.

---

