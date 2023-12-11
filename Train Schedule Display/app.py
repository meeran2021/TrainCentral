from flask import Flask, render_template
import requests
import time

app = Flask(__name__)

@app.route('/train schedule')
def display_train_information():
    trains = get_details()
    print(trains)
    return render_template('index.html', trains=trains)


def get_access_token():
    url = "http://20.244.56.144/train/auth"
    parameters= {
        "companyName": "Train Central",
        "clientID": "bc141f09-2605-4996-aea6-c837647f7daa",
        "ownerName": "Fever Kumar",
        "ownerEmail": "feverkumar@gmail.com",
        "rollNo": "200101234",
        "clientSecret": "OmQBJTVsrIgXXlvE"
    }

    try:
        response = requests.post(url, json=parameters, headers= {'Content-Type': 'application/json'})
        token_generted_time= time.gmtime()
        response_data = response.json()
        print(response)
        if response.status_code == 200:
            print(response_data['access_token'])
            return response_data['access_token'], token_generted_time
        
        else:
            print("Failed to fetch data.")
            print("Error message:", response_data.get("error"))
            return ""

    except requests.exceptions.RequestException as e:
        print("Error occurred while making the API request:", e)
        return ""


def get_details():
    url = "http://20.244.56.144/train/trains"
    access_token, token_generted_time= get_access_token()

    try:
        response = requests.get(url, headers={'Authorization': 'token {}'.format(access_token)})
        response_data = response.json()

        if response.status_code == 200:
            return response_data
        else:
            print("Failed to fetch event details.")
            print("Error message:", response_data.get("error"))
            return []

    except requests.exceptions.RequestException as e:
        print("Error occurred while making the API request:", e)
        return []



if __name__ == '__main__':
    app.run(debug=True)





