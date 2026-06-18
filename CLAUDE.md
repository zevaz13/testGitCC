# Data visualization

## Folder structure
TESTGITCC/
  data/
    eeg/
      raw/
    hue/
    lux/
    ....            
  src/
    eeg/
    hue/
    ....
  notebooks/            #.ipynb
    eeg/  # further separation can exist at this level depending on the type of analysis and if it improves functionality
    hue/
    ...
  scripts/
    eeg/              #.py files (we will start with this later)
    hue/
    ....     
  docs/               # for documentation of each kind of data
    EEG/

## Requirements

- This is going to be a set of python notebooks and scripts that allow to organize, visualize and explore data from different domains  
- The scafolding should allow to differentiate the different types of data we will use: hue, lux, beh, eeg, standarized scores. For each we will have a folder in data, one in notebooks, a src for modules of data of each kind
- raw data is to be stored in data/typeOfdata/raw
- We can include .md files to describe better each type of data
- Firs priorities are to allow the user to explore the data, and create functionalities that can be modularized later
- We will use python notebooks
- Create a python environment that has data analysis in mind
- Always keep a document called PLAN.md where we can communicate about the current plan of action.

## Technical Decisions

- IMPORTANT: Use "uv" as the package manager for python. ONLY UV.
- create a new virtual environment that adds the needed packages to check the data. Like: matplotlib, pandas, numpy, seaborn etc..
- You have a github tool access. You can create issues at your discression, but you will always need to ask for permission to add, commit and push changes
- create notebooks that allow the user to test functionality
- The user should be able to explore data by themselves looking at the documentation and creating scripts or notebooks of their own, calling the module fdunctions exposed in src/eeg

## Strategy

1. Write plan with success criteria for each phase to be checked off. Include project scaffolding, including .gitignore, and rigorous unit testing. 
2. Create issues as needed in the github repository
3. Execute the plan ensuring all critiera are met
4. Update issues as needed
5. Carry out extensive integration testing with Playwright or similar, fixing defect

## Coding standards

1. Use latest versions of libraries and idiomatic approaches as of today
2. Keep it simple - NEVER over-engineer, ALWAYS simplify, NO unnecessary defensive programming. No extra features - focus on simplicity.
3. Be concise. Keep README minimal. IMPORTANT: no emojis ever
