import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the datasets
pitching_poi = pd.read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/poi_metrics.csv")
metadata = pd.read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/metadata.csv")

# Combine the dataframes on 'session_pitch' and 'session'
combined_data = pd.merge(pitching_poi, metadata, on=['session_pitch', 'session'])

# Clean the data by removing rows with NaN values for the variables of interest
clean_data = combined_data.dropna(subset=['lead_grf_z_max', 'session_mass_kg'])

# Define a function to find the best breakpoint for piecewise linear regression
def find_best_breakpoint(data, response, predictor, breakpoints):
    """
    Find the best breakpoint for a piecewise linear regression model.
    
    This function iterates over a set of potential breakpoints and fits two separate linear regression
    models for the data points on either side of each breakpoint. It calculates the sum of squared errors
    for the models at each breakpoint and returns the breakpoint with the smallest sum of squared errors, 
    indicating the best fit.
    
    :param data: DataFrame containing the data.
    :param response: The name of the response variable column.
    :param predictor: The name of the predictor variable column.
    :param breakpoints: A list or array of breakpoints to test.
    :return: The best breakpoint and the corresponding models.
    """
    best_sse = np.inf
    best_breakpoint = None
    best_models = None

    for breakpoint in breakpoints:
        # Divide the data around the current breakpoint
        lower_data = data[data[predictor] <= breakpoint]
        upper_data = data[data[predictor] > breakpoint]

        # Ensure there is enough data in each segment
        if lower_data.shape[0] > 1 and upper_data.shape[0] > 1:
            # Fit the models
            lower_model = LinearRegression().fit(lower_data[[predictor]], lower_data[response])
            upper_model = LinearRegression().fit(upper_data[[predictor]], upper_data[response])

            # Calculate predictions
            lower_predictions = lower_model.predict(lower_data[[predictor]])
            upper_predictions = upper_model.predict(upper_data[[predictor]])

            # Calculate the sum of squared errors
            sse = np.sum((lower_data[response] - lower_predictions) ** 2) + \
                  np.sum((upper_data[response] - upper_predictions) ** 2)

            # If this is the best sse, update the best breakpoint and models
            if sse < best_sse:
                best_sse = sse
                best_breakpoint = breakpoint
                best_models = (lower_model, upper_model)

    return best_breakpoint, best_models

# Define the range for potential breakpoints to avoid empty segments
min_mass = clean_data['session_mass_kg'].min() + 1e-2  # add a small epsilon to avoid the exact min value
max_mass = clean_data['session_mass_kg'].max() - 1e-2  # subtract a small epsilon to avoid the exact max value
breakpoints = np.linspace(min_mass, max_mass, 100)

# Find the best breakpoint
best_breakpoint, best_models = find_best_breakpoint(clean_data, 'lead_grf_z_max', 'session_mass_kg', breakpoints)

# Extract the models for plotting
lower_model, upper_model = best_models

# Generate a range of values for mass around the breakpoint for plotting the lines
mass_range_lower = np.linspace(clean_data['session_mass_kg'].min(), best_breakpoint, 100)
mass_range_upper = np.linspace(best_breakpoint, clean_data['session_mass_kg'].max(), 100)

# Predict the values using the models
predicted_lower = lower_model.predict(mass_range_lower.reshape(-1, 1))
predicted_upper = upper_model.predict(mass_range_upper.reshape(-1, 1))

'''
# Calculate R^2 values for the lower and upper models
r2_lower = lower_model.score(clean_data[clean_data['session_mass_kg'] <= best_breakpoint][['session_mass_kg']], 
                             clean_data[clean_data['session_mass_kg'] <= best_breakpoint]['lead_grf_z_max'])
r2_upper = upper_model.score(clean_data[clean_data['session_mass_kg'] > best_breakpoint][['session_mass_kg']], 
                             clean_data[clean_data['session_mass_kg'] > best_breakpoint]['lead_grf_z_max'])
'''
# Create the plot
plt.figure(figsize=(12, 8))
plt.scatter(clean_data['session_mass_kg'], clean_data['lead_grf_z_max'], alpha=0.5)
plt.plot(mass_range_lower, predicted_lower, 'r-', label='Model: Below Breakpoint')
plt.plot(mass_range_upper, predicted_upper, 'b-', label='Model: Above Breakpoint')
plt.axvline(x=best_breakpoint, color='black', linestyle='--', label=f'Breakpoint at {best_breakpoint:.2f} kg')

# Annotations and labels
plt.title('Piecewise Linear Regression: Session Mass vs Lead GRF Z Max')
plt.xlabel('Session Mass (kg)')
plt.ylabel('Lead Ground Reaction Force Z Max (N)')
#plt.text(0.05, 0.95, f'Lower Model R^2: {r2_lower:.2f}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))
#plt.text(0.05, 0.85, f'Upper Model R^2: {r2_upper:.2f}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))
plt.legend()
plt.show()
