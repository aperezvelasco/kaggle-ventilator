# Kaggle competition: Google Brain - Ventilator Pressure Prediction

## Description

What do doctors do when a patient has trouble breathing? They use a ventilator to pump 
oxygen into a sedated patient's lungs via a tube in the windpipe. But mechanical
ventilation is a clinician-intensive procedure, a limitation that was prominently 
on display during the early days of the COVID-19 pandemic. At the same time, 
developing new methods for controlling mechanical ventilators is prohibitively 
expensive, even before reaching clinical trials. High-quality simulators could 
reduce this barrier.

Current simulators are trained as an ensemble, where each model simulates a single lung 
setting. However, lungs and their attributes form a continuous space, so a parametric 
approach must be explored that would consider the differences in patient lungs.

Partnering with Princeton University, the team at Google Brain aims to grow the 
community around machine learning for mechanical ventilation control. They believe 
that neural networks and deep learning can better generalize across lungs with varying 
characteristics than the current industry standard of PID controllers.

In this competition, you’ll simulate a ventilator connected to a sedated patient's lung.
The best submissions will take lung attributes compliance and resistance into account.

If successful, you'll help overcome the cost barrier of developing new methods for 
controlling mechanical ventilators. This will pave the way for algorithms that adapt 
to patients and reduce the burden on clinicians during these novel times and beyond. 
As a result, ventilator treatments may become more widely available to help patients 
breathe.

# Installation

First clone the repository:

```
git clone https://github.com/aperezvelasco/kaggle-ventilator.git
```

Create the directory where the data and submissions will be stored:

```
cd kaggle-ventilator
mkdir data
mkdir submission
```

Download the zip file with the data to be stored. For doing so, you need to have a .json
file with the credentials defined in it (/home/username/.kaggle/kaggle.json):

```
pip install kaggle
cd data
kaggle competitions download -c ventilator-pressure-prediction
unzip ventilator-pressure-prediction.zip 
rm ventilator-pressure-prediction.zip 
cd ..
mv data/sample_submission.csv submission/sample_submission.csv
```

There will be 3 different files. One for train, one for test, and one example of how a 
submission is expected to be. The features given in train and test files are:

- id - globally-unique time step identifier across an entire file
- breath_id - globally-unique time step for breaths
- R - lung attribute indicating how restricted the airway is (in cmH2O/L/S). Physically, this is the change in pressure per change in flow (air volume per time). Intuitively, one can imagine blowing up a balloon through a straw. We can change R by changing the diameter of the straw, with higher R being harder to blow.
- C - lung attribute indicating how compliant the lung is (in mL/cmH2O). Physically, this is the change in volume per change in pressure. Intuitively, one can imagine the same balloon example. We can change C by changing the thickness of the balloon’s latex, with higher C having thinner latex and easier to blow.
- time_step - the actual time stamp.
- u_in - the control input for the inspiratory solenoid valve. Ranges from 0 to 100.
- u_out - the control input for the exploratory solenoid valve. Either 0 or 1.
- pressure - the airway pressure measured in the respiratory circuit, measured in cmH2O.
