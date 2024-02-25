# Steps for myself as I go...
# Set up with virtual environment and activated
# Take in a csv file of dependent and independent variables from https://www.kaggle.com/datasets/

# Linear regression algorithm b = mx + b
# Use scikit-learn library to perform linear regression calculation / storing of data to recognize the correlation based on input data
# Perform algorithmic functionality for program to correlate variables and able to make it's own predictions based on test cases
# Include results (variance between result and expected data) to visually depict in linear regression graph from seaborn lib
# Continue to feed/adjust program to adjust for variance and perform input operation to allow user to input house size and get result of predicted price
# Convert prgram to use my own functionality rather than libs

# numPy used for 

import data_related

def main():
    print("Test for python project")
    
    try:
        data_related.load_CSV()
    except Exception as e:
        print("An error occurred:", e)
    
    
if __name__ == "__main__":
    main()