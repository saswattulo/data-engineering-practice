import requests
import os
from zipfile import ZipFile
from datetime import datetime


download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def main():
    # your code here
    download_directory = 'downloads'
    # create a folder downloads, ignore if exists
    os.makedirs(download_directory, exist_ok = True)

    start_time = datetime.now()
    # iterate over all the element of the list
    for url in download_uris:

        # extract filename from the url
        file_name = url.split('/')[-1]

        output_file_path = os.path.join(download_directory, file_name)

        try:
            response = requests.get(url= url)
            if response.status_code == 200:
                with open(output_file_path, 'wb') as f:
                    f.write(response.content)
            print(f"File {file_name} saved successfully to {output_file_path}")
        except Exception as e:
            print(f"Error occured while downloading the file {file_name}")
            print("Error: e")
    print("File downloading operation is completed.")
    print(f"Downloading process took {(datetime.now() - start_time).total_seconds()} seconds.")

    for file in os.listdir(download_directory):
        if file.endswith('.zip'):
            zip_file_name = file.split('.')[0]
            zip_file_path = os.path.join(download_directory,file)
            extracted_file_location = os.path.join(download_directory, zip_file_name)

            with ZipFile(zip_file_path,'r') as zip_file:
                zip_file.extractall(extracted_file_location)
                print(f"{file} is extracted to {extracted_file_location} successfully.")
            os.remove(zip_file_path)
    print("Extraction operations is completed.")
    print("Operation is completed.")
    print(f"Whole process took {(datetime.now() - start_time).total_seconds()} seconds.")


if __name__ == "__main__":
    main()
