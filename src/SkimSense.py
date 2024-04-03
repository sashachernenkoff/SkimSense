# Human milk nutrition prediction after reduction
#
# Corresponding Author: Sasha Chernenkoff, sasha.chernenkoff@ucalgary.ca
#
# SkimSense.py - script to make predictions on new milk data using our model
#
# Author: Sasha Chernenkoff
# Date: 3 March, 2024
# Updated: 16 March, 2024


import numpy as np
import pandas as pd
import sys

from argparse import ArgumentParser as AP
from utils import predict_nutrition


if __name__ == "__main__":
    # Create structure for reading file/text from the command line and writing output to file
    parser = AP()
    parser.add_argument("--text", metavar="Input Text",
                        help="Starting nutrition of milk in form fat,protein,carbohydrates,calories,%reduction.")
    parser.add_argument("--file", metavar="/path/to/file/in_file.txt", type=str,
                        help="Path to file containing starting nutritions of milk to make prediction for. " +
                             "One prediction will be made for each line in input file.")
    parser.add_argument("--out", metavar="/path/to/file/out_file.txt", type=str,
                        help="Path to write predictions to.", required=True)
    args = parser.parse_args()

    # Check to make sure that either --text or --file was passed
    # If neither, raise ValueError
    if args.text is None and args.file is None:
        raise ValueError("Must either pass text or file containing milk starting nutrition.")

    # Check to make sure that both --text and --file was not passed
    # Must be one or the other
    if args.text is not None and args.file is not None:
        raise ValueError("Must pass --text _or_ --file. Cannot pass both.")

    # Check to make sure that an output file was specified
    if args.out is None:
        raise ValueError("Must specify output file with --out.")

    # If only a single string was passed using --text, then make prediction and write to file
    if args.text:
        print("Making prediction for input text...")

        # Parse input text
        # Check that 5 features were given (fat, carbohydrates, protein, calories, % reduction)
        try:
            features = np.array([float(x) for x in args.text.split(',')]).reshape(1, -1)
            if features.shape[1] != 5:
                raise ValueError("Expected 5 features")
        except ValueError as e:
            print(f"Error: {e}")
            exit(1)

        # Make prediction
        predicted_nutrition = predict_nutrition(features)

        # Convert predicted_nutrition to a single string
        formatted_prediction = ",".join(["%.3f" % number for number in np.round(predicted_nutrition,
                                                                                3)])

        # Write the formatted string to the output file
        with open(args.out, 'w') as f:
            f.write(formatted_prediction)

        print(f"Prediction successfully written to {args.out}")

    # If a file containing multiple lines is passed, make all predictions and write to file
    if args.file:
        print("Making predictions for input file...")
        all_predictions = []  # To store predictions for each line

        with open(args.file, 'r') as file:
            for line in file:
                # Parse input line
                # Check that 5 features were given (fat, carbohydrates, protein, calories, % reduction)
                try:
                    features = np.array([float(x) for x in line.strip().split(',')]).reshape(1, -1)
                    if features.shape[1] != 5:
                        raise ValueError("Each line must contain exactly 5 features")
                except ValueError as e:
                    print(f"Error processing line: {line.strip()} - {e}")
                    continue  # Skip to the next line

                # Make prediction for the current line
                predicted_nutrition = predict_nutrition(features)

                # Format the prediction
                formatted_prediction = ",".join(["%.3f" % number for number in np.round(predicted_nutrition, 3)])
                all_predictions.append(formatted_prediction)

        # Write all formatted predictions to the output file
        with open(args.out, 'w') as f:
            for prediction in all_predictions:
                f.write(prediction + "\n")

        print(f"Predictions successfully written to {args.out}")
