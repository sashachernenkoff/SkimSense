# SkimSense

This repo is the home of `SkimSense`, a Python utility for predicting the nutrition of 
donor human milk after reduction (removal of skim) using a feedforward neural network 
implemented with TensorFlow.

![SkimSense](https://i.imgur.com/kpKFXlO.png)


## More Info

Human milk is preferred over formula because it contains optimal nutrition as well as 
immunoglobulins, hormones, oligosaccharides and other components that are crucial for infant 
development and health, particularly in premature or sick newborns. Thousands of infants, 
especially those in NICUs or with mothers unable to produce sufficient milk, rely on donor 
human milk for essential nutrition and biological components.

Milk banks screen, process, and distribute donated breast milk to ensure safe and nutritious 
feedings for infants in need, playing a vital role in public health care for newborns. Optimizing 
the nutrition of donor milk supports the specific needs of vulnerable infants, promoting better 
health outcomes and reducing the risks associated with premature birth and illness.

SkimSense is a tool developed to assist milk banks in optimizing the nutrition of donated 
breast milk to distribute to hospitals, pharmacies, and families. This tool reduces waste and 
improves nutrition profiles, ensuring vulnerable infants receive the best possible nourishment 
to support their health and development.


## Installation

Requirements can be installed by running `pip install -r requirements.txt`. These 
requirements have been verified for python version 3.11.0.


## Usage

### Making predictions

#### Input

The input should be a .csv file with each line representing a starting nutrition 
profile to make predictions on, as well as a desired reduction percentage. 
Thus, each line should contain five numerical features, detailed as:

* **Fat**: A positive numeric value representing the fat content (%).
* * **Protein**: A positive numeric value representing the protein content (g/dL).
* **Carbohydrates**: A positive numeric value representing the carbohydrate content.
* **Calories**: A positive numeric value representing the caloric content (cal/oz).
* **Percentage reduction**: A numeric value ranging from 0 to 100, representing the 
desired percentage reduction.

These features must be provided in the order specified above and separated by commas. 
Below is a sample of the expected input format:

```
2.85,1.09,7.48,18.07,10
2.27,1.05,7.27,16.2,50
1.35,0.96,7.07,13.35,20
```


#### Output

The prediction task can then be performed by running the following:

```
python SkimSense.py --file /path/to/input/file.csv --out /path/to/write/predictions/to.csv
```

This will read in the inputs from `/path/to/input/file.csv`, make a nutrition prediction 
for each line of text, and write it to `/path/to/write/predictions/to.csv`.

Alternatively, a single text snippet can be read from the command line:

```
python SkimSense.py --text 'fat,protein,carb,cals,%reduction' --out /path/to/write/predictions/to.csv
```

Which will write a single prediction to `/path/to/write/predictions/to.csv`.


#### Demo

For an example, run `sh demo.sh` in the `src/` directory. The script will execute the full 
predictive pipeline of SkimSense. Each line of input text will be run through the pre-trained 
neural network.

```bash
cd src/
sh demo.sh
```

This will read in the example input file from `data/example_input.csv` and write predictions 
to `out/example_output.csv`.


## Overview of Repository

Here, we list the files we have included as part of this repository.

* `bin/` - The fully trained neural network stored as an hdf5 (`.h5`) file and the trained 
scaler stored as a serialized Python object.
    * `bin/model.h5` - Fully trained neural network
    * `bin/scaler.save` - Trained scaler object
* `data/` - Example input file and the data file used to train the neural network.
    * `data/example_input.csv` - Example input file
    * `data/training_data.csv` - Experimental data used to train the neural network
* `src/` - Main source directory
    * `src/demo.sh` - Runs an example of the pipeline
    * `src/model_train.py` - Script for training the neural network
    * `src/SkimSense.py` - Primary file for making predictions on input
    * `src/utils.py` - Utility file containing tools for making predictions


## Additional Information

### Support
For support, please contact [Sasha Chernenkoff](http://www.sashachernenkoff.com/) at 
sasha.chernenkoff@ucalgary.ca.

### Inquiry
All general inquiries should be directed to [Sasha Chernenkoff](http://www.sashachernenkoff.com/) 
at sasha.chernenkoff@ucalgary.ca.

### License
This repository and all its contents are released under the 
[MIT License](https://opensource.org/licenses/MIT); See 
[LICENSE.md](https://github.com/sashachernenkoff/SkimSense/blob/main/LICENSE).