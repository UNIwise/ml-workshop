## UNIwise ML workshop

The purpose of this workshop is for you to get hands on experience with how we at UNIwise use data for machine learning purposes.
You will learn about the types of data we handle, the challenges we face, and ponder how to overcome them.

## Getting Started

- Clone the repo with <code>git clone git@github.com:UNIwise/ml-workshop.git</code> or download the repo
- Check you have python installed by running <code>python -v</code> in your favourite terminal. \
If you do not have it installed:
  - Linux: <code>sudo apt-get install python3</code>
  - Windows: Download and install python from https://www.python.org/downloads/
  - MacOS: If you have homebrew installed, run <code>brew install python</code>. \
  Otherwise download and install python from https://www.python.org/downloads/.
  Or install homebrew by following this guide https://mac.install.guide/homebrew/3.html
- Navigate to the root of the project and run <code>pip install -r requirements.txt</code> to install the required packages.
- Run the example to make sure everything works:
    - Run <code>python example/visualize.py</code> to visualize the data.
    - Run <code>python example/predict.py</code> to predict & visualize outliers.

Now you're ready to go! 
To begin you should add your code to the <code>predict_outliers</code> function in <code>predict.py</code>, but feel free to add other functions or play with the visualization if you wish.

To predict with your implementation run <code>python \<difficulty\>/predict.py</code>. E.g <code>python hard/predict.py</code> to predict outliers on the hard dataste using your model.

To visualize run different variables run <code>python \<difficulty\>/visualize.py \<status_key\></code>, e.g. <code>python hard/visualize.py FACIAL_RECOGNITION</code> to visualize the facial recognition variable on your predictions on the hard dataset. \
For the datasets with only one variable (easy and example) just run <code>python \<difficulty\>/visualize.py</code>.

## Outlier Detection

The challenge of this workshop is detecting students acting suspicious during an exam i.e. outlier detection.
In outlier detection we do not have labels or 'ground truths' to guide the training of a model, nor the evaluation of it.
It should therefore be noted that outliers are not necessarily cheaters, but their data just looks different compared to their peers.
At UNIwise we never call students cheaters, but we provide insights for the institutions to draw their own conclusions. 

## Datasets

This repository contains three different datasets in increasing complexity and one used as an example, where we have supplied a simple model for outlier detection.
We recommend starting with the easy dataset, but depending on your level of experience and/or fighting spirit, feel free to start with any dataset.
Note that while results are cool, we would also love to talk with you about your considerations, potential problems you see with your methods or how you would handle hypothetical issues we might suggest. 

### Example

In the example dataset we have generated data for 10 students doing a 3-hour exam. \
The data is structured in the following manner:

| time                | user_id | status_key       | value  |
| ------------------- | ------- | ----------       | ------ |
| 2023-02-10 12:00:00 | 0       | CHARACTERS_TYPED | 6543   |
| 2023-02-10 12:05:00 | 0       | CHARACTERS_TYPED | 7534   |
| 2023-02-10 12:00:00 | 1       | CHARACTERS_TYPED | 3213   |

With columns: \
<code>time</code>: The timestamp of the datapoint. \
<code>user_id</code>: A unique student identifier. \
<code>status_key</code>: Variable the following column belongs to. In Example <code>status_key</code> is always <code>CHARACTERS_TYPED</code>, representing the character count up until this time. \
<code>value</code>: The value <code>status_key</code> had at this time.   
### Easy

This dataset is similar to the example dataset in that it only contains one measurement, <code>CHARACTERS_TYPED</code>, but this dataset contains data for more students. \
The data is structured in the following manner:

| time                | user_id | status_key       | value  |
| ------------------- | ------- | ----------       | ------ |
| 2023-02-10 12:00:00 | 0       | CHARACTERS_TYPED | 6543   |
| 2023-02-10 12:05:00 | 0       | CHARACTERS_TYPED | 7534   |
| 2023-02-10 12:00:00 | 1       | CHARACTERS_TYPED | 3213   |

With columns: \
<code>time</code>: The timestamp of the datapoint. \
<code>user_id</code>: A unique student identifier. \
<code>status_key</code>: Variable the following column belongs to. In Easy <code>status_key</code> is always <code>CHARACTERS_TYPED</code>, representing the character count up until this time. \
<code>value</code>: The value <code>status_key</code> had at this time.   

### Medium

For this dataset there are multiple possible values for <code>status_key</code>. Now students can be considered outliers just according to one variable or a combination of multiple.
The data is structured in the following manner:

| time                | user_id | status_key         | value  |
| ------------------- | ------- | ----------         | ------ |
| 2023-02-10 12:00:00 | 0       | CHARACTERS_TYPED   | 6543   |
| 2023-02-10 12:05:00 | 0       | CHARACTERS_TYPED   | 7534   |
| 2023-02-10 12:00:00 | 0       | FACIAL_RECOGNITION | 95     |
| 2023-02-10 12:05:00 | 0       | FACIAL_RECOGNITION | 93     |
| 2023-02-10 12:00:00 | 0       | VOICE_DETECTION    | 4      |
| 2023-02-10 12:05:00 | 0       | VOICE_DETECTION    | 2      |
| 2023-02-10 12:00:00 | 1       | CHARACTERS_TYPED   | 3213   |

With columns: \
<code>time</code>: The timestamp of the datapoint. \
<code>user_id</code>: A unique student identifier. \
<code>status_key</code>: Variable the following column belongs to. <code>CHARACTERS_TYPED</code> represents the character count up until this time, <code>FACIAL_RECOGNITION</code> represents a percentage match to a reference image of the student using facial recognition and <code>VOICE_DETECTION</code> represents a count of sentences of spoken words since last observation.\
<code>value</code>: The value <code>status_key</code> had at this time.  

Here you will have to be creative and use the new features to help you figure out, if more people should be considered outliers based on the extra variables.

### Hard

This dataset contains the same variables as the medium dataset, but this time, students from multiple exams are included and the exams were held at different times.
This means that comparing variables across exams is going to pose some problems. What is considered an outlier <code>CHARACTERS_TYPED</code> value in one exam at a given time, may be different than the value at an equivalent time in a different exam. 

| time                | user_id | exam_id | status_key         | value  |
| ------------------- | ------- | ------- | ----------         | ------ |
| 2023-02-10 12:00:00 | 0       |    0    | CHARACTERS_TYPED   | 6543   |
| 2023-02-10 12:05:00 | 0       |    0    | CHARACTERS_TYPED   | 7534   |
| 2023-02-10 12:00:00 | 0       |    0    | FACIAL_RECOGNITION | 95     |
| 2023-02-10 12:05:00 | 0       |    0    | FACIAL_RECOGNITION | 93     |
| 2023-02-10 12:00:00 | 0       |    0    | VOICE_DETECTION    | 4      |
| 2023-02-10 12:05:00 | 0       |    0    | VOICE_DETECTION    | 2      |
| 2023-02-10 12:00:00 | 1       |    0    | CHARACTERS_TYPED   | 3213   |
| 2023-02-10 12:00:00 | 0       |    1    | CHARACTERS_TYPED   | 3654   |

With columns: \
<code>time</code>: The timestamp of the datapoint. \
<code>user_id</code>: A unique student identifier for a given exam. \
<code>exam_id</code>: A unique exam identifier. \
<code>status_key</code>: Variable the following column belongs to. <code>CHARACTERS_TYPED</code> represents the character count up until this time, <code>FACIAL_RECOGNITION</code> represents a percentage match to a reference image of the student using facial recognition and <code>VOICE_DETECTION</code> represents a count of sentences of spoken words since last observation.\
<code>value</code>: The value <code>status_key</code> had at this time.  

### Questions to Ponder
We do not expect you to *solve* these questions, but they are important things to consider if one were to deploy a model for finding outlier students in real exams.
- How to handle student starting late? Or ending early?
- What if some students were given extra time?
- What if not all exams have the same <code>status_key</code>s available?
- How would you explain to an invigilator why a student is considered an outlier?
