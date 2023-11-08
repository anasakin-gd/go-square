#!/usr/bin/python

import os
import yaml
import re

original_file_path = "./go-square-chart/Chart.yaml"
# Save changes to temp file to minimize the risk of the yaml file corruption
temp_file_path = "./go-square-chart/Chart_temp.yaml"
# New version of the app is a new GIT_TAG env.var set via GHA workflow
new_version = os.environ.get("GIT_TAG")

# Cut "v" in vX.X.X tag
if new_version.startswith("v"):
    new_version = new_version[1:]

# Open Chart.file
with open(original_file_path) as f:
    y = yaml.safe_load(f)

# Get current version of the Chart
current_version = y['version']

# Splitting version on regexp groups. We need only patch version so major & minor are in one group
match = re.match(r'(\d+\.\d+)\.(\d+)', current_version)
major_minor_version, patch_version = match.groups()

# Increasing Chart version
new_patch_version = int(patch_version) + 1
new_chart_version = f"{major_minor_version}.{new_patch_version}"
y['version'] = new_chart_version

# Set appVersion
y['appVersion'] = new_version

# Saving to temporary file
with open(temp_file_path, 'w') as temp_file:
    yaml.dump(y, temp_file)

# Updating original Chart file
os.replace(temp_file_path, original_file_path)
