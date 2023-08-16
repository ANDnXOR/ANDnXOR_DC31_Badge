#!/bin/bash

# Python Requirements: numpy==1.23.1, Pillow==9.2.0
# Linux Requirements: ffmpeg (sudo apt-get install ffmpeg)

input_folder="animated_input"
output_folder="animated_output"
FRAME_COUNT=10  # Change this value to set the desired number of frames
TERMINAL_HEIGHT=20

# Delete all .anm files in the output folder
rm "$output_folder"/*.anm 2>/dev/null

# Iterate over each GIF file in the input_folder
for gif_file in "$input_folder"/*.gif; do
    # Get the total number of frames in the current GIF
    frame_count=$(ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames -of csv=p=0 "$gif_file")

    # Calculate the step size for evenly selecting frames
    step_size=$((frame_count / FRAME_COUNT))

    # Convert animated GIF to individual frames (JPEG) using FFMPEG
    ffmpeg -i "$gif_file" -vf "select='not(mod(n\,$step_size))',setpts=N/TB" -vsync 0 "$output_folder/frame_%04d.jpg"

    # Iterate over each file in the output folder
    for ((i = 0; i < FRAME_COUNT; i++)); do
        # Construct the input file name
        input_file="$output_folder/frame_$(printf "%04d" $((i + 1))).jpg"

        # Construct the output file path with input file name and frame number
        output_file="$output_folder/$(basename "${gif_file%.*}")_$(printf "%02d" $i).anm"

        # Run the command for each file
        python3 art_andnxor_fork.py -i "$input_file" -y $TERMINAL_HEIGHT -f True > "$output_file"
    done

    # Remove the JPG files
    rm "$output_folder"/*.jpg
done

# Remove the text files
rm "$output_folder"/*.txt

