# **SpaceX Launch Records Dashboard**

## **Overview**
The **SpaceX Launch Records Dashboard** is an interactive data visualization tool built using **Dash** and **Plotly**. It provides insights into SpaceX launch data, showcasing key metrics such as the success rates, payload masses, and booster versions used for different launch sites.

### **Features**
- **Launch Site Selection**: Users can choose between various SpaceX launch sites to view detailed launch success statistics.
- **Payload Range**: Filter launches based on payload mass to understand its correlation with mission outcomes.
- **Success vs Failure Visualization**: Display pie charts to visualize the success vs failure ratio for different launch sites and the entire dataset.
- **Scatter Plot**: Visualize the relationship between payload mass and launch success, color-coded by booster version.

## **Technologies Used**
- **Python**: Main programming language.
- **Dash**: Framework used for building the interactive dashboard.
- **Plotly**: Data visualization library used to generate the pie chart and scatter plot.
- **Pandas**: Data manipulation library to handle and process the SpaceX dataset.

## **Installation Instructions**
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/spacex-launch-dashboard.git
    ```
2. Navigate to the project directory:
    ```bash
    cd spacex-launch-dashboard
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    python spacex_dash_app.py
    ```
5. Open your browser and navigate to `http://127.0.0.1:8050/` to view the dashboard.

## **Dataset**
The dataset used is based on SpaceX's historical launch data, which includes the following columns:
- **Flight Number**: Unique identifier for each launch.
- **Launch Site**: The location from where the rocket was launched.
- **class**: Indicates the success (1) or failure (0) of the launch.
- **Payload Mass (kg)**: The weight of the payload carried during the launch.
- **Booster Version**: The version of the rocket booster used in the launch.
- **Booster Version Category**: A categorized version of the booster for more granular analysis.

## **Usage**
### **1. Select Launch Site:**
Choose from a dropdown to visualize launch statistics for different SpaceX launch sites.

### **2. Filter by Payload Range:**
Use the payload slider to filter the launches based on their payload mass, and observe its correlation with launch success/failure.

### **3. View Pie Chart:**
For each selected launch site or for all sites, a pie chart will show the ratio of successful vs failed launches.

### **4. View Scatter Plot:**
A scatter plot will show the relationship between payload mass and mission outcomes, color-coded by the booster version used.

## **Screenshots**
Include some screenshots of your dashboard here to give users a preview of what to expect.

## **Contributing**
Feel free to fork this repository and contribute! Any improvements or bug fixes are welcome. To contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **Acknowledgements**
- SpaceX for inspiring this project.
- Dash and Plotly for providing the frameworks and tools to build this dashboard.
- Pandas for data manipulation.

---

