# Movie-Recommendation-System

# About this Project

Movie recommendation systems are designed to provide personalized movie suggestions to users, enhancing their entertainment experience by helping them discover movies tailored to their preferences. This project showcases the development of a Movie Recommendation System using various machine-learning models and techniques. 

The primary goal of this project is to build a robust movie recommendation system that can analyze user preferences and viewing history to make accurate movie suggestions. It utilizes popular machine-learning algorithms to classify movies and generate personalized recommendations.

## Built-With

 - Flask
 - Numpy
 - Scipy
 - Nltk
 - Scikit-learn==1.2.2
 - Pandas
 - Beautifulsoup4
 - tmdbv3api
 - DVC

 Anyways you can install all the libraries mentioned above at a glance by executing the following command:
 
  ```sh
  pip install -r requirements.txt
  ```

## Getting Started

This will help you understand how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Installation Steps

### Option 1: Installation from GitHub

Follow these steps to install and set up the project directly from the GitHub repository:

1. **Clone the Repository**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to install the project.
   - Run the following command to clone the GitHub repository:
     ```
     git clone https://github.com/KalyanMurapaka45/End-to-End-Movie-Recommendation-System.git
     ```

2. **Create a Virtual Environment** (Optional but recommended)
   - It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
     ```
     conda create -p <Environment_Name> python==<python version> -y
     ```

3. **Activate the Virtual Environment** (Optional)
   - Activate the virtual environment based on your operating system:
       ```
       conda activate <Environment_Name>/
       ```

4. **Install Dependencies**
   - Navigate to the project directory:
     ```
     cd [project_directory]
     ```
   - Run the following command to install project dependencies:
     ```
     pip install -r requirements.txt
     ```

5. **Run the Project**
   - Start the project by running the appropriate command.
     ```
     python app.py
     ```

6. **Access the Project**
   - Open a web browser or the appropriate client to access the project.
  
<br><br>
### Option 2: Installation from DockerHub

If you prefer to use Docker, you can install and run the project using a Docker container from DockerHub:

1. **Pull the Docker Image**
   - Open your terminal or command prompt.
   - Run the following command to pull the Docker image from DockerHub:
     ```
     docker pull kalyan45/movierecommend-app
     ```

2. **Run the Docker Container**
   - Start the Docker container by running the following command, and mapping any necessary ports:
     ```
     docker run -p 5000:5000 kalyan45/movierecommend-app
     ```

3. **Access the Project**
   - Open a web browser or the appropriate client to access the project.



   
# Contributing

Contributions make the open-source community such an amazing place to learn, inspire, and create. I would greatly appreciate any contributions you make.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch 
3. Commit your Changes 
4. Push to the Branch 
5. Open a Pull Request

<!-- LICENSE -->
# License

Distributed under the GNU General Public License v3.0. See `LICENSE.txt` for more information.

# Acknowledgements

This project was inspired by the Kaggle dataset on Spam Email Detection and the corresponding competition. We also acknowledge the open-source Python libraries used in this project and their contributors.

