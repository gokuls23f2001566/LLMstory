
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "aiohttp",
#   "httpx",
#   "matplotlib",
#   "numpy",
#   "pandas",
#   "requests",
#   "seaborn",
#   "scikit-learn",
#   "tabulate",
# ]
# ///

import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import math

# Set up AI proxy token and proxy configuration
proxy_token = os.getenv("AIPROXY_TOKEN")

if proxy_token is None:
    print("Error: AIPROXY_TOKEN not found in environment variables.")
    exit()

# Define the proxy URL and headers
proxy_url = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"  # Fixed the API path
headers = {
    "Authorization": f"Bearer {proxy_token}",
    "Content-Type": "application/json"
}
proxies = {
    "http": proxy_url,
    "https": proxy_url
}

def split_filename_and_path(file_path):
    directory, filename = os.path.split(file_path)
    return directory, filename

# Load dataset with fallback encoding and column cleanup
def load_data(file_path):
    """Loads the dataset with fallback encoding and column name cleanup."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        data = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        # Retry with a fallback encoding
        data = pd.read_csv(file_path, encoding='latin1')

    # Strip any leading/trailing whitespace in column names
    data.columns = data.columns.str.strip()
    print("Dataset loaded successfully!")
    return data


def create_histograms(data, outpath, filename="histograms.png"):
  
    # Filter numerical columns
    numerical_cols = data.select_dtypes(include=['number']).columns

    # Calculate the grid size
    num_cols = len(numerical_cols)
    cols = 3  # Number of columns in the grid
    rows = math.ceil(num_cols / cols)

    # Create the figure
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 5, rows * 4))
    axes = axes.flatten()  # Flatten the axes array for easy iteration

    for i, col in enumerate(numerical_cols):
        ax = axes[i]
        data[col].hist(ax=ax, bins=20, color='blue', edgecolor='black')
        ax.set_title(f"Histogram of {col}")
        ax.set_xlabel(col)
        ax.set_ylabel("Frequency")

    # Hide any unused subplots
    for j in range(i + 1, len(axes)):
        axes[j].axis("off")

    # Adjust layout and save the figure
    plt.tight_layout()
    plt.savefig(outpath + filename)
    append_image_to_readme(outpath + "README.md",outpath+filename,"Histograms")
    plt.close()
    print(f"Histograms saved to {filename}")


# Use proxy to call LLM API
def narrate_story(data, description, readmefile_path):

    print("Sending description stats to LLM to narrate story...")
    """Uses the proxy to send a request to the LLM API and narrate a story."""
    data_head = data.head(5).to_string()
    prompt = (
        "Analyze the following dataset description and visualization and narrate a story. "
        "The dataset summary is:\n\n"
        f"{description}\n\n"
        "The top 5 rows of the dataset are:\n\n"
        f"{data_head}\n\n"
        "Explain the patterns, trends, and insights in simple language suitable for a report. "
    )
    payload = {
        "model": "gpt-4o-mini",  # Updated model name
        "messages": [
            {"role": "system", "content": "You are a data analyst."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(
            proxy_url,
            headers=headers,
            json=payload,
            proxies=proxies
        )
        if response.status_code == 200:
            story = response.json()['choices'][0]['message']['content']
            print("Generated Story:\n")
            print(story)
            with open(readmefile_path + 'README.md', "w") as f:
                f.write(story)

        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error generating story: {e}")


def append_image_to_readme(readme_path, image_path, caption="Correlation Heatmap"):
    if not os.path.exists(readme_path):
        print(f"README file not found at {readme_path}. Creating a new one.")
        with open(readme_path, "w") as file:
            file.write("# Analysis Results\n\n")
    image_path=image_path.replace('./','/')
    # Prepare the Markdown image reference
    image_markdown = f"## {caption} \n\n" + f"![{caption}]({image_path})\n\n"

    # Check if the image is already in the README to avoid duplicates
    with open(readme_path, "r") as file:
        content = file.read()
        if image_markdown in content:
            print("Image reference already exists in README.md.")
            return

    # Append the image reference to the README
    with open(readme_path, "a") as file:
        #file.write('### Chart-1 - Correlation Matrix\n\n ###')
        file.write(image_markdown)
        print(f"Added image reference to {readme_path}.")

# Example usage
readme_path = "README.md"  # Path to your README file
image_path = "correlation_heatmap.png"  # Path to your image file
append_image_to_readme(readme_path, image_path)


# Function to create correlation heatmap with numeric data only
def plot_correlation_heatmap(data, output_file):
    # Select only numeric columns for correlation calculation
    numeric_data = data.select_dtypes(include=['number'])
    
    if numeric_data.empty:
        print("No numeric columns available for correlation.")
        return
    
    # Handle missing values (drop rows with missing data, or fill with mean)
    numeric_data = numeric_data.dropna()  # Drop rows with missing values
    # numeric_data = numeric_data.fillna(numeric_data.mean())  # Alternatively, fill missing with mean
    
    # Calculate the correlation matrix
    correlation_matrix = numeric_data.corr()
    
    # Plot the correlation matrix as a heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, cbar=True)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(output_file+"corr_heat_map.png")
    append_image_to_readme(image_path=output_file+"corr_heat_map.png",readme_path=output_file+"README.md", caption="Correlation Head Map")
    plt.close()


# Function to create boxplots for outlier detection
def plot_boxplots(data, output_file):
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=data.select_dtypes(include=['number']))  # Select numerical columns
    plt.title("Boxplot for Outlier Detection")
    plt.tight_layout()
    plt.savefig(output_file+"boxplot.png")
    append_image_to_readme(image_path=output_file+"boxplot.png",readme_path=output_file+"README.md", caption="BoxPlot")
    plt.close()


# Function to generate summary statistics
def generate_summary_stats(data):
    summary_stats = data.describe().to_markdown()
    return summary_stats


# Function to detect missing values
def detect_missing_values(data):
    missing_values = data.isnull().sum()
    missing_values_markdown = missing_values.to_markdown()
    return missing_values_markdown


# Function to generate the correlation matrix and highlights
def correlation_highlights(corr_matrix, threshold=0.75):
    strong_positive = set()
    strong_negative = set()
    for i, col in enumerate(corr_matrix.columns):
        for row in corr_matrix.index[i+1:]:  # Only traverse lower triangle
            value = corr_matrix.loc[row, col]
            if value >= threshold:
                strong_positive.add((row, col, value))
            elif value <= -threshold:
                strong_negative.add((row, col, value))
    return sorted(strong_positive), sorted(strong_negative)


def generate_correlation_matrix(data):
    numeric_data = data.select_dtypes(include=['number'])
    correlation_matrix = numeric_data.corr()
    return correlation_matrix


# Function to detect outliers in numerical columns
def detect_outliers(df, columns):
    outliers = {}
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers[col] = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col].count()
    return outliers


# Function for frequency analysis of categorical columns
def frequency_analysis(df):
    categorical_columns = df.select_dtypes(include=['object']).columns
    frequency_results = {}
    for col in categorical_columns:
        frequency_results[col] = df[col].value_counts().head(5)  
    return frequency_results



# Function to send data summary to LLM and get further analysis suggestions
def get_analysis_suggestions(summary_stats,sample,filename):
    try:
        response = requests.post(
            "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",  # Using proxy URL for the API
            headers=headers,
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "You are an intelligent assistant."},
                    {"role": "user", "content": f"Here are the summary statistics of a dataset:\n{summary_stats}\n\n Sample data:\n{sample}\n\n. Filename:{filename}\n Please suggest further analyses that could provide more insights.Also give advise on columns on which cluster analysis can be carried out"}
                ],
                "max_tokens": 150
            },
            proxies=proxies
        )

        # Check for successful response
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        else:
            print(f"Error in API call: {response.status_code}, {response.text}")
            return None

    except Exception as e:
        print(f"Error in API call: {e}")
        return None


# Main function to generate the README report and communicate with LLM
def generate_report(data, output_file,filename):

    # Check if the dataset is empty
    if data.empty:
        raise ValueError("The dataset is empty. Please provide a valid file.")

    print("Data loaded successfully!")

    # Generate numerical summary statistics
    print("Generating numerical summary statistics...")
    numerical_summary = data.select_dtypes(include=['number']).describe().to_markdown()

    # Generate categorical summary statistics
    print("Generating categorical summary statistics...")
    categorical_summary = data.select_dtypes(include=['object']).describe().to_markdown()

    # Print summaries for verification
    print("Numerical Summary:\n", numerical_summary)
    print("Categorical Summary:\n", categorical_summary)

    # Combine both numerical and categorical summaries into one string
    summary_stats = f"Numerical Summary:\n{numerical_summary}\n\nCategorical Summary:\n{categorical_summary}"

    # Get analysis suggestions from the LLM
    print("Sending summary statistics to LLM for suggestions...")
    suggestions = get_analysis_suggestions(summary_stats,data.sample(5),filename)

    # If suggestions are received, run them
    if suggestions:
        print(f"LLM suggests the following analyses:\n{suggestions}")
    else:
        print("No suggestions from LLM. Proceeding with generic analysis.")

    # Create README file and write report
    with open(output_file+"README.md", "a") as f:
        # Write header
        f.write("# Data Analysis Report\n\n")

        # 1. Numerical Summary Statistics
        print("Generating numerical summary statistics...")
        f.write("## Numerical Summary Statistics\n\n")
        f.write(numerical_summary + "\n\n")

        # 2. Categorical Summary Statistics
        print("Generating categorical summary statistics...")
        f.write("## Categorical Summary Statistics\n\n")
        f.write(categorical_summary + "\n\n")

        # 3. LLM Suggested Analyses
        print("Including LLM suggestions...")
        f.write("## LLM Suggested Analyses\n\n")
        if suggestions:
            f.write(f"### LLM suggests the following analyses:\n\n")
            f.write(f"{suggestions}\n\n")
        else:
            f.write("No suggestions provided.\n\n")

        # 4. Missing Values
        print("Detecting missing values...")
        f.write("## Missing Values\n\n")
        missing_values = detect_missing_values(data)
        f.write(missing_values + "\n\n")

        # 5. Correlation Matrix
        print("Generating correlation matrix...")
        f.write("## Correlation Matrix\n\n")
        correlation_matrix = generate_correlation_matrix(data)
        corr_markdown = correlation_matrix.to_markdown()
        f.write(corr_markdown + "\n\n")

        # Correlation Highlights
        strong_positive, strong_negative = correlation_highlights(correlation_matrix, threshold=0.75)
        
        f.write("### Strong Positive Correlations (>= 0.75)\n\n")
        for pair in strong_positive:
            f.write(f"- **{pair[0]} and {pair[1]}**: {pair[2]:.2f}\n")
        
        f.write("\n### Strong Negative Correlations (<= -0.2)\n\n")
        for pair in strong_negative:
            f.write(f"- **{pair[0]} and {pair[1]}**: {pair[2]:.2f}\n")
        
        f.write("\n\n")

        # 6. Outlier Detection
        print("Detecting outliers...")
        numerical_columns = data.select_dtypes(include=['number']).columns.tolist()
        outliers = detect_outliers(data, numerical_columns)
        f.write("## Outliers\n\n")
        for col, count in outliers.items():
            f.write(f"- **{col}**: {count} potential outliers\n")
        
        f.write("\n\n")

        # 7. Frequency Analysis
        print("Performing frequency analysis on categorical columns...")
        f.write("## Frequency Analysis (Top 5 Values for Categorical Columns)\n\n")
        frequency_results = frequency_analysis(data)
        for col, freq in frequency_results.items():
            f.write(f"### Column: {col}\n\n")
            f.write(freq.to_markdown() + "\n\n")

        print(f"Analysis complete. Report saved to {output_file}")



# Main function
def main(filename):
    
    cwd = os.getcwd()
    
    # Concatenate the CWD with the provided filename
    full_path = os.path.join(cwd, filename)
    
    if not os.path.exists(full_path):
        print(f"Error: The file '{full_path}' does not exist.")
        return
    
    print(f"Processing file: {full_path}")

    # Dataset 
    directory, filename = split_filename_and_path(full_path)
    
    #create directory in the filename if does not exist
    filename_withoutext = filename.split('.')[0]
    print("Creating output directory for the given dataset....",filename_withoutext)
   
    if not os.path.exists(filename_withoutext):
        os.makedirs(filename_withoutext)
        print(f"Directory '{filename_withoutext}' created successfully.")
    
    try:
        data = pd.read_csv(full_path, encoding='utf-8')
    except UnicodeDecodeError:
        # Retry with a fallback encoding
        data = pd.read_csv(full_path, encoding='latin1')

    # Strip any leading/trailing whitespace in column names
    data.columns = data.columns.str.strip()
    print("Dataset loaded successfully!")

    #print("Column names in the dataset:", data.columns) 
    description = data.describe(include="all")
    outfile_path  = os.getcwd().replace('\\','/')
    #output_readme_md_file = outfile_path + "/" + filename_withoutext +"/"
    output_readme_md_file = "./" + filename_withoutext +"/"

    narrate_story(data, description, output_readme_md_file)
    generate_report(data, output_readme_md_file,filename_withoutext)
    plot_correlation_heatmap(data,output_readme_md_file)
    plot_boxplots(data,output_readme_md_file)
    create_histograms(data,output_readme_md_file)


    

if __name__ == "__main__":

    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Process a file.")
    parser.add_argument("filename", help="The name of the file to process")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Call main with the filename argument
    main(args.filename)
