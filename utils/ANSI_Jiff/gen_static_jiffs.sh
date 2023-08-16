#!/bin/bash

input_folder="static_input"
output_folder="static_output"
FRAME_COUNT=10  # Change this value to set the desired number of frames
TERMINAL_HEIGHT=23

# Delete all files in the output folder
rm "$output_folder"/*.* 2>/dev/null

# Iterate over each image file in the input_folder
for image_file in "$input_folder"/*; do
    # Check if the file is a valid image
    if file -b --mime-type "$image_file" | grep -q '^image/'; then
        # Convert the image to JPEG format using FFMPEG
        ffmpeg -i "$image_file" -vf "select='not(mod(n\,$FRAME_COUNT))',setpts=N/TB" -vsync 0 "$output_folder/$(basename "${image_file%.*}").jpg"

        # Iterate over each converted file in the output folder
        for converted_file in "$output_folder"/*; do
            # Check if the file is a valid image
            if file -b --mime-type "$converted_file" | grep -q '^image/'; then
                # Get the filename without the extension
                filename=$(basename "${converted_file%.*}")

                # Run the command for each file
                python3 art_andnxor_fork.py -i "$converted_file" -y $TERMINAL_HEIGHT -f True > "$output_folder/$filename.ans"

                # Remove the converted image file
                rm "$converted_file"
            fi
        done
    fi
done

# Remove the text files
rm "$output_folder"/*.txt
