# Twitter Network Analysis

Welcome to the **Twitter Network Analysis** project! This project leverages **graph theory** and **network analysis techniques** to study the structure of **Twitter's social network**. The dataset includes **user connections** (followers and followees), and the project calculates various **network metrics**, such as **PageRank** and **strongly connected components**.

## Project Overview

The **main goals** of this project are to:

- Analyze **Twitter's follower-followee relationships** using **graph theory**.
- Visualize the **network structure** and **key metrics** like **PageRank**.
- Identify **strongly connected components** within the network.

## Features

- **Graph Visualization**: Visualizes the **Twitter network** using **nodes** (users) and **edges** (follower-followee relationships).
- **PageRank Calculation**: Computes the **PageRank** of users, indicating the **most influential users** in the network.
- **Strongly Connected Components**: Identifies **clusters of users** who are all **reachable from each other**.

## Setup & Installation

### Prerequisites

Make sure you have **Python 3.x** installed on your machine. You will also need **pip** to install the **required dependencies**.

### Installation Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Kushagra-maker/twitter-network-analysis.git

2. **Navigate to the project directory**:

   ```bash
   cd twitter-network-analysis

3. **Install dependencies**: Install the **required Python packages** by running:

   ```bash
   pip install -r requirements.txt

4. **Prepare the data**: Create a **`twitter_data.csv`** file with the following **columns**:

   - **`user_id`**: Unique identifier for the user.
   - **`username`**: The user's name.
   - **`follower_id`**: ID of the user following (if applicable).

   Example:

   ```csv
   user_id,username,follower_id
   1,User1,2
   2,User2,3
   3,User3,1

5. **Run the analysis**: Execute the script to perform **network analysis** and **visualize the results**:

   ```bash
   python main.py

6. **View the results**: The program will print the following:

   - **Number of strongly connected components**.
   - **PageRank scores** of **top users**.
   - A **graphical visualization** of the **Twitter network**.

## Results

- The program identifies **strongly connected components** (clusters of users who follow each other) and **prints them**.
- **PageRank values** are calculated for each user, highlighting the **most influential users** in the network.
- A **graphical visualization** of the network is generated, showcasing **users** and their **relationships**.

## Contributing

Feel free to **fork this repository**, make **improvements**, and create **pull requests**. **Contributions** are always welcome!

## License

This project is **open-source** and available under the **MIT License**.
