# Workout Tracker

This Python script allows you to track your exercises and log the details in a Google Sheets document. It uses the Nutritionix API to get exercise details and the Sheety API to log the data into a Google Sheet.

## Prerequisites

- Python 3.x
- `requests` library (install with `pip install requests`)
- Nutritionix API credentials (`APP_ID` and `API_KEY`)
- Sheety API credentials (`USERNAME`, `PASSWORD`, and `TOKEN`)

## Environment Variables

Make sure you set the following environment variables:

- `USERNAME`: Your Sheety API username
- `PASSWORD`: Your Sheety API password
- `TOKEN`: Your Sheety API token (if using Bearer Token Authentication)
- `APP_ID`: Your Nutritionix API app ID
- `API_KEY`: Your Nutritionix API key

You can set environment variables in your terminal:

```bash
export USERNAME='your_username'
export PASSWORD='your_password'
export TOKEN='your_token'
export APP_ID='your_app_id'
export API_KEY='your_api_key'
