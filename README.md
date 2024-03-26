# TAMU Sea Level Rise Data Challenge
## Team Members: Shawn Chin and Daniel Chen
- IntialCSVFileCreation.ipynb/.py used to convert Mat files into CSV for easy data processing
- CSVFileIntegration (Program)
    - created to make CSV file readable for ML Model
    - Used GeoHashing to Hash Longitude and Latitude which reduces dimensionality, allows for spatial indexing and overall better understanding of spatial context
- ** initial_vector_autogregressionmodel.py/.ipynb **
    - settled on using a vector autoregression model that takes into account time and each variables relationship with each other
    - these files contain the intial model trained on only MSLR(Mean Sea Level Rise) and MGRD(Barystatid GRD)
    - ran the Augmented Dickey-Fuller test and adjusted the differenced value to make the data stationary
    - ran the Granger Causality Test to find the right number of lags for causation between the two variables
    - model ran well with a Root Mean Squared Error of 60 for MSLR and 17.87 for MGRD
