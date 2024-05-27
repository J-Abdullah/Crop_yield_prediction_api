# Yield Prediction API

This is a FastAPI application that predicts the yield of a crop based on various factors. It uses a machine learning model trained with the Bagging Regressors algorithm.

## Features

- Predict crop yield based on area, item, average rainfall, pesticides used, and temperature.
- Utilizes machine learning for accurate predictions.
- FastAPI for quick and efficient API responses.

## API Endpoints

- POST `/predict/`: Predicts the yield based on the provided parameters.

## Request Body

The request body should be a JSON object with the following properties:

- `area`: The area where the crop is grown (string).
- `item`: The type of crop (string).
- `avg_rain`: The average rainfall in the area (float).
- `pesticides`: The amount of pesticides used (float).
- `temperature`: The average temperature in the area (float).

## Response

The response will be a JSON object with the following properties:

- `predicted_yield`: The predicted yield of the crop (float).

## Error Handling

If there is an error during the prediction process, the API will return a 400 status code along with a message detailing the error.

## Setup

1. Clone the repository.
2. Install the dependencies.
3. Run the FastAPI server using the command: `uvicorn yield_predictor_api:app --reload`

## Testing

After running the FastAPI server, execute the `test_api` script to test the API.

## Dependencies

- FastAPI
- Pydantic
- Joblib
