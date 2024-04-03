# Human milk nutrition prediction after reduction
#
# Corresponding Author: Sasha Chernenkoff, sasha.chernenkoff@ucalgary.ca
#
# demo.sh - demo for running SkimSense on an input file to make predictions using our model
#
# Author: Sasha Chernenkoff
# Date: 3 March, 2024
# Updated: 16 March, 2024


if [ ! -d ../out/ ]; then
    echo "Making directory ../out/ to send outputs to"
    mkdir ../out/
fi

# For a single line passed via args
python SkimSense.py --text 2.27,1.05,7.27,16.20,10 --out ../out/single_example_output.csv

# For a file of inputs
python SkimSense.py --file ../data/example_input.csv --out ../out/example_output.csv