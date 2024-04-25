#!/bin/bash

# Base URL of your Flask application
BASE_URL="http://10.0.2.8:30497//add"

# Array of names
names=("Bartek" "Tomek" "Marysia" "Jakub" "Karolina" "Piotrek" "Lucyna" "Marek" "Jola" "Asia" "Basia" "Kasia" "Stasia" "Monika" "Ala" "Alicja" "Chewbacca")

# Array of descriptions
descriptions=(
    "A cheerful and optimistic friend, always brings light and laughter."
    "Known for his wit and humor, the life of every party."
    "Compassionate and caring, always there to support."
    "Loves to share the latest tech tips with friends."
    "Creative and artistic, inspires everyone with passion for the arts."
    "The adventurer, always planning his next travel adventure."
    "The wise mentor, offering insightful advice and guidance."
    "The sports fanatic who organizes weekend games."
    "Known for her delicious dishes and warm hospitality."
    "Passionate about sustainability and living green."
    "Motivates everyone with her infectious enthusiasm."
    "Helps friends stay trendy with her fashion advice."
    "Always ready to engage in deep conversations and expand horizons."
    "Known for her meticulous planning and ability to bring people together."
    "Always upbeat and smiling, the group's sunshine."
    "A gifted musician whose melodies are the soundtrack of gatherings."
    "Loyal and protective, always ready to stand up for friends."
)

# Loop through all names and descriptions
for i in "${!names[@]}"; do
    name="${names[$i]}"
    description="${descriptions[$i]}"

    # Using curl to POST data
    curl -X POST "$BASE_URL" -F "name=$name" -F "description=$description"
    echo "Posted $name and their description."
done

