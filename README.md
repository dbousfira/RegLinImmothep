# Immothep

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Intermovie</h3>

  <p align="center">
    A study project, house price prediction
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)

<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* [Anaconda](https://www.anaconda.com/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo

    ```sh
    git clone https://github.com/diem-ai/Immothep.git
    ```

2. Create a conda virtual environment with

    ```sh
    conda create --name <env> --file requirements.txt
    ```

<!-- USAGE EXAMPLES -->
## Usage

* Run the server with:

    ```sh
    uvicorn src.modules.main:app --reload --port 5003
    ```

* Go to [http://localhost:5003/api/estimate](http://localhost:5003/api/estimate)
* Run immothep.ipynb
* Outputs
    1.
