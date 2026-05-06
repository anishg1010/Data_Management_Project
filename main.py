import fastf1

# Use the same cache folder where your ff1pkl files are
fastf1.Cache.enable_cache(r'C:\Users\yuvra\Desktop\UNI\Data management\project\output')

# Reload session (this will USE the cached ff1pkl files)
session = fastf1.get_session(2023, 'Monza', 'R')
session.load()

# Extract datasets
laps = session.laps
results = session.results
weather = session.weather_data

# Convert to CSV
laps.to_csv('output/laps.csv', index=False)
results.to_csv('output/results.csv', index=False)
weather.to_csv('output/weather.csv', index=False)

print("CSV files created successfully!")