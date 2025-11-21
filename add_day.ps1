param(
    [string]$Year,
    [int]$Day
)

# Ensure the day is zero-padded to two digits
$DayPadded = "{0:D2}" -f $Day

# Define paths
$SourceFile = "src/solutions/template.py"
$DestinationDir = "src/solutions/y$Year"
$DestinationFile = "$DestinationDir/day$DayPadded.py"

# Check if the source file exists
if (-Not (Test-Path $SourceFile)) {
    exit 1
}

# Ensure the destination directory exists
if (-Not (Test-Path $DestinationDir)) {
    New-Item -ItemType Directory -Path $DestinationDir -Force | Out-Null
}

# Copy the file
Copy-Item -Path $SourceFile -Destination $DestinationFile -Force
