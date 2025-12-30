readings = [12.5, "Error", 18.2, 15.0, "Error", 22.1, 10.8]

# --- Task 1: The Cleaner (Search and Replace)---
for i in range(len(readings)):
    if readings[i] == "Error":
        readings[i] = 0.0
print(f"After Cleaning(Replacing ): {readings}")
# --- Task 2: The Multiplier  (In-place Modification)---
for i in range(len(readings)):
    readings[i] = readings[i] * 1.1
print(f"After Multiplication: {readings}")
# --- Task 3: The Filter (Selective Removal) & Extra Challenge  ---
low_quality_log = []
for i in range(len(readings) - 1, -1, -1):
    if readings[i] < 15.0:
        low_quality_log.append(readings[i])
        readings.pop(i)

# --- Final Output ---
print(f"Cleaned Readings: {readings}")
print(f"Low Quality Log: {low_quality_log}")