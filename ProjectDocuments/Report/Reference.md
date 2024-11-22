# Team Report Assignment

Student IDs: 2203484, 2313658, 2316783, 2312997, 2316662

The University Of Essex CSEE
CE101: Team Project Challenge

https://cseejira.essex.ac.uk/projects/D101019
https://github.com/RossJamesUK/Heart-Disease

24/03/2024
Team Report Assignment


# Chapter 1: Executive Summary

This report will cover the process of developing, training, and testing
an AI model for the diagnosis and prevention of cardiovascular disease.
We will go into detail on our initial plans for the model's development
cycle as well as our advanced planning methods to ensure the project
goes smoothly. Over the past few weeks, as a team, we have discussed
ideal methods for producing the code needed to run the model and set
targets for what would make this project successful with teamwork and a
final result.

We wanted this project to be a major step towards making AI more common
in healthcare to make links between factors that humans cannot see
without the power of computers. We hope this model stands as a good sign
for other conditions that could be helped through the use of computer
programs and AI such as cancer research and more. Primarily, this
project uses Python which the entire team is confident in allowing us to
quickly build prototypes and test the results as laid out in this
report. Our main focus was systematic development through prioritisation
and transparency that shined through while planning, developing, and
testing.

Jira played a major part in our success as we used sprints to progress
weekly with different objectives that our team found key to each step of
development. Each week that we worked on the project, we had an assigned
list of tasks that allowed us to limit time for each objective while
maintaining quality and avoiding over-development. Later, we will
discuss exactly how Jira contributed to the project components.

Furthermore, we also discussed many different outcomes of the project
such as ethical implications and possible biases generated from the
datasets which allowed us to implement as many safeguards as possible.
While presenting our work to potential investors, we were transparent
about the model's dataset and possible issues with the limited size of
patient data we had access to (303 people). Our presentation allowed us
to nicely conclude this product with an overall outline of what we did,
why we did it, and how we could improve with investments.

Overall, this report should serve as an interesting look into the world
of AI development and how it could potentially help to further medical
research and cure development.

# Chapter 2: The team working

2.1: A literature review of team working

Throughout our project, we made use of a variety of literature provided
to us both by the university during the lectures and within the extra
reading materials outside of the lectures themselves. For instance,
during one of the early lectures we read in part through the provided
reading book by James Dyson on his ethos of product development and then
further read through some of his other outings such as his 2011 Wired
interview with James Dyson: in praise of failure. The latter of which
had a notable quote we took to heart, and tried to follow throughout the
project.

> "By fostering an environment where failure is embraced, even those of
> us far from our student days have the freedom to make mistakes - and
> learn from them still"
>
> \- J. Dyson, \"James Dyson: In Praise of Failure\" \[1\].

This quote reflected in our work ethic quite predominantly with all of
our team being encouraged to try new and unexplored ideas in the pursuit
of progress without the fear of shame from failure. We as a team ensured
that each member\'s work was recognised and respected regardless of the
objective usefulness/functionality of the idea. This in turn drove
progress forward at an increased rate with more distinct ideas.

Another brilliant read was the book referenced in the reading material,
the literary piece "How to Solve It: A New Aspect of Mathematical
Method" by George Polya. This book is itself a very very useful tool to
reference for problem solving, as it offers great insights and puts a
lot of emphasis on three general aspects; understanding the problem,
devising and executing a plan, and reviewing the solution. One section
from this book that I thought applied to us very nicely was as follows.

> \"Understand the problem. Find the connection between the data and the
> unknown. You may be obliged to consider auxiliary problems if an
> immediate connection cannot be found\" - G. Polya, How to Solve It: A
> New Aspect of Mathematical Method \[2\].

According to Polya, when faced with a mathematical problem, it is
crucial to fully understand the problem, and then find the connection.
Even if that connection at first may be hard to find. This was apparent
in our research of the problem where the ultimate conclusion of our
work, in short, determining if an individual had Cardiovascular diseases
based on a multitude of variables, was similarly hard to find a
connection in. This was due to the seemingly complete disconnect between
the CVD value of the individuals in the dataset and any one of their
values for the other corresponding variables. However, following the
ideology of Polya, we eventually, through our research, learning, and
understanding, would come to make use of machine learning to make this
bridge in the otherwise unknown.

Through our project we would find ourselves diving head first, reading
up on many articles to find inspiration, learning, and progressing to
complete this and that. Ultimately all of the resources we used
contributed, in their respect, to our collective advancements in this
project, and to that end, we were thankful to have been able to access
them.

2.2: Contribution Claims

Oliver Keefe

-   Validated Model using Cross Validation

-   Train Model using SVC (Support Vector Classifier) Algorithm

-   Implemented Accessibility for Colour Blindness

-   Refactored Code to Avoid Using Deprecated Libraries / Methods

-   Wrote functions for data visualisations

-   Wrote Unit Tests

Mohammad Mahir Karim

-   Calculate the Percentage of People with and without Cardiovascular
    > Disease (CVD / Heart Disease)

-   Write a final summary of the key risk factors identified through
    > correlation and graphs

-   Validate model with ROC Curve as well as make improvement

-   Write Observations of Results of Training / Testing

-   Plan and prepare for a presentation

-   Explore feature variable \'Age\'

Anthony Calvin Kazibwe

-   Examined the risk factors for cholesterol

-   Examined the risk factors for heart rate

-   Wrote summary of use of project management

Adam Kenning

-   Analysed percentages of people with CVD in the dataset

-   Investigated male/female distribution

-   Examined age distribution within the dataset.

-   Conducted observations for my contributed analysis

-   Generated confusion matrix

-   Created, Organized and managed team report.

Ross James

-   Created and configured GitHub Repository

-   Wrote code to explore raw data and remove null values

-   Improved and optimised N-Fold Validation

-   Identified links between age and condition

# Chapter 3: The product development chapter

3.1: Product development literature review

Considering statistics, heart disease remains the primary cause of death
throughout the world, implying the urgent necessity for improved
diagnostic techniques. The development of machine learning in heart
disease prediction thus offers a stepping stone to boosting diagnostic
levels and, hence, ensuring better patient care. This review will
contribute to the understanding that it is vital to focus on heart
disease, as it's possible to use the ML method to find out the risk
factors.

Due to numerous factors, the majority of such diseases are preventable
through the management of an individual\'s risk, which includes both
modifiable and unmodifiable elements. \"CVD is responsible for an
estimated 31% of all global deaths,\" according to the World Health
Organisation. \"Of these deaths, heart attack and stroke account for
85%.\" \[3\] CVD is caused by numerous risk factors, including
hypertension, cholesterol, tobacco use, diabetes, and immutable
heredity. Early identification and management of these factors are of
the utmost importance in order to mitigate their prevalence and adverse
effects. This demonstrates the need for more sophisticated diagnostic
and predictive methods.

**Machine Learning and Its Effects on the Prediction of Heart Disease**

Machine learning is considered a subdivision of computing technology
that has a lot of potential in CRS predictive diagnosis. By analysing
large amounts of historical health data, ML algorithms can uncover
patterns and relationships that can be difficult for humans to identify.
For instance, as ScienceDirect writes in their article "Machine
learning-based approach for diagnosing cardiovascular diseases using a
combined data set,"\[4\] ML can help predict cardiac problems. This
demonstrates its potential to revolutionise the field as well as deepen
the understanding of the risk factors and the link between them.
Moreover, the different ML tools, including Support Vector Machine
(SVM), Random Forest, and Gradient Boosting, further prove the potential
of ML. However, even with the use of ML, it is necessary to visualise it
at some stages of the data analysis process, which can be done through
data visualisation. Such an approach will facilitate the reading of the
complex data set. These visualisation methods help to see the likelihood
of getting a disease based on other factors present in the data. The
thing is, the results of ML will remain at a speculative level without
the visualisation of data. Data visualisation can be a critical aspect
of ML models based on an individual's health data. Also, visualisation
can help in improving the quality of a solution, and it is quite
straightforward to understand by practitioners.

**Data Visualisation**

It is also a vital point in the context of ML. This is because Data
visualisation helps turn difficult data files or findings from analysis
into perspectives that are easy to read. If the data were not
visualised, ML would not make any significant improvements.
Visualisations will be implemented on complicated data files,
demonstrating patterns that would be impossible to find by visualising
the original data file by itself. Data visualisation may, from this
perspective, be the 'missing component' needed to enhance an ML model
based on health information.

There is no question that Anything© has the potential to profoundly
transform the struggle against heart disease. Our initiative is the
epitome of technology, poised to redefine how scientists forecast,
control, and address heart disease at last. Your commitment to funding
ensures that this revolution happens. With your help, we will not only
reach our mission and realise our goals but also bring about a future in
which heart disease is no longer the number one killer. Together, we can
conquer this global health crisis.

3.2: Context

Riding on the coattails of the ongoing global epidemic of heart
diseases, our young health-tech startup, Anything©, is on the cusp of a
medical breakthrough. This project is determined to attain the highest
power in machine learning to develop a heart disease-predicting model.
We submit this project, which is innovative, supported by a pertinent
dataset, and governed by well-established goals, to seek funding.

**The Sense of Urgency**

Heart diseases continue to be the leading cause of death globally, with
people dying from heart-related issues every year. This calls for
immediate validation of the critical work already done by other
researchers, complemented by a powerful tool to predict the chances of
developing the disease. By making this model available to the public, as
we intend, everyone, regardless of their geographical location, will
have a chance at life, courtesy of the sound preventive measures
guaranteed by the model.

**The ultimate development of the model will serve two key purposes:**

predicting whether there is a chance of an individual developing heart
disease in cases where there are no clinical signs and providing
healthcare personnel with a tool to aid in decision-making on whether to
intervene or which intervention to implement. The project is, therefore,
envisaged to transform the healthcare sector from a curative approach to
a preventive paradigm where new cases will be minimised significantly,
therefore curbing the morbidity currently suffered.

**Dataset and its Justification**

The dataset combines the outcomes from the three sources, which, when
integrated, provide cardiovascular health information that may indicate
the presence of heart disease. Apart from the patient's age and sex,
other health factors examined included resting blood pressure,
cholesterol, fasting blood sugar, resting electrocardiographic results,
the maximum heart rate during the patient\'s tests, the presence of ST-T
waves indicating abnormality, and exercise-induced angina. The variables
analysed covered all the known risk factors associated with heart
disease. It is the minimization of these risks that the predictive model
will use as parameters to develop a determination. The data provided
here simulates the real-world profile expected and the prediction. The
data ensures the model is fed with data that is relevant and applicable
across populations.

**Improved Decision-Making for Healthcare Practitioners:\
**Our project models could be a significant tool by enabling better
decision-making among healthcare practitioners. Better still, such
practitioners can intervene more quickly and more proactively and
optimise their patient's outcomes while minimising other adverse health
risks.

Some steps we take:\
Model Accuracy and Validation: You ensure that the risk models your
project will develop are validated in new datasets and in actual
clinical practice. Beyond their current capacities, genetics, lifestyle,
and environmental data may be gathered in more ways than we can
currently imagine.

User-centred Design: Computers should be naturally created with
usability in mind. We make sure the model is as simple to navigate as
possible for all levels of medical personnel, even those less
experienced with computers.

Integration with Healthcare Systems: Our tool must be fully integrated
with the existing Healthcare IT infrastructure or an electronic health
record; in that way, we have the most chance of success. The majority of
existing healthcare IT systems are built on an integrated approach, and
an additional layer of software will be beneficial.

**Drive preventive healthcare measures:\
**With the implementation of our model, we can achieve unprecedented
coverage of preventive healthcare among the most affected populations.
The population will be able to initiate the preventive measures on their
own before a situation gets out of hand, reducing the burden of heart
disease.

Anything© is an idea whose time has come. As such, the project is on the
brink of creating innovations that will revolutionise how heart disease
is predicted, prevented, and managed. We need your support and
partnership to transform this vision into a reality. Working together,
we can make a world where heart disease is not as widespread as it is
today.

3.3: The team product Technical documentation

This technical documentation shows an overview of the heart disease
prediction model that we developed as a team. The introduction for this
section will discuss a basic description of the product, why we made it,
and its intended uses. It will also go into detail about the standards,
limitations, performance metrics, and how we tested it.

The heart disease model that our team produced was made for predicting
how likely it is that someone would develop heart disease given we had
key metrics about their health. As this model is aimed at use in a
medical environment, it would be used by doctors, researchers, and
scientists to both test for cardiovascular disease and train the model
on other datasets that could be suitable. With this model in place, we
could, in theory, have better early detection systems in place to
identify those vulnerable to the condition and help prevent its
development. On top of this, we can potentially identify key risk
factors to minimise their risk in the long term.

We were given several requirements for this project to ensure that it
worked as expected and gave valid and useful outputs. For example, the
model had to utilise input data from 303 patients who had previously
been diagnosed with CVD to train the model. This input data had key
fields such as Age, Sex, Cholesterol, Resting blood pressure, and
Maximum heart rate. It was also important to us that we be able to add
more data to the model when needed to improve accuracy. Of course, the
other key requirement for this model is the function where it must be
able to take input data and predict if a person is at risk of/has been
diagnosed with CVD. This process involved preparing the input data,
training the model, and then using it to correctly predict CVD.

For the model to be successful, we also had to consider various other
topics such as the model's limitations, success rate, and how it
performs when used for its functions. Processing large amounts of
personal data with an artificial intelligence model might be classed as
unethical without expressed permission from each patient that the data
belongs to and so the data we used was sourced ethically.

It was also very important to consider the ethical standards of
predicting CVD with a computer program that could potentially make
mistakes which is why we tried to ensure the accuracy was as high as
possible. Furthermore, it was important to consider the limitations of
what predictions an AI model could make as well as check if it would
even be possible to make accurate predictions based on the limited input
data we had. There is also the possibility of bias in the dataset
through certain groups being larger than others since 303 input items
are very small compared to the population with CVD.

When measuring the performance of the model, it was important to define
how it would be measured and what counted as successful. Through the use
of ROC curves, confusion matrix, and percentage accuracy, we were able
to say the model was 87% accurate which is a great insight into the
model's sensitivity and performance when grouping those with and without
CVD. With this accuracy, we also did a lot of testing and validation to
ensure the model was being trained correctly, as well as outputting
expected results given input data to check for anomalous results. We
found it very important to validate the reliability across large
demographics that we were targeting with the research.

This documentation will go further into detail about the stages of
development, why we chose specific options, and most importantly, how
well it works. One of the key parts of this section is accuracy which
has a lot of key points about what could happen with incorrect results.

3.3.1: Design

During our project, we made use of a systematic routined approach to end
up with our design solution. This systematic approach involved us, each
week, convening at a communal computer lab space where we worked to
progress our understanding, allowing us to refine our design approach
iteratively. Initially, during the first few weeks, we familiarised
ourselves with the project scope, and tools and provided resources like
Jira, Kaggle and GitHub (we made use of GitHub as opposed to GoogleColab
due to members already being familiar with the software). We looked into
data handling resources, such as Python libraries like Numpy, Matplotlib
and Sklearn etc, conducted exploratory data analysis to familiarise
ourselves with the provided dataset, and researched\[5\] machine
learning, culminating in the final choice of our machine learning model
we would end up using; Support Vector Machines (SVMs), a type of
supervised learning algorithm used for classification and regression
tasks.\
\
Our choice of solution was informed by evaluating possible designs for
our project, taking both qualitative and quantitative research into
account. Under the category of support vector machines, we initially
trained several unique models, including the Linear Kernel, Polynomial
Kernel, RBF (Radial Basis Function) Kernel, and Sigmoid Kernel, to
determine which would work most suitably for our dataset.

> Linear Kernel Weighted average score: 0.72 F1 Score
>
> Polynomial Kernel Weighted average score: 0.74 F1 Score
>
> RBF Kernel Weighted average score: 0.85 F1 Score
>
> Sigmoid Kernel Weighted average score: 0.87 F1 Score

After assessing the performance of each model in terms of accuracy by
comparing them across some metrics, including precision, recall,
f1-score, and support, we found that the Sigmoid Kernel produced the
highest results. The Sigmoid Kernel is a non-linear kernel function that
maps input space into a higher-dimensional feature space. It works by
transforming the input data into a binary format, making it suitable for
classification tasks. With this model, we feed in a dataset to train it,
and then, given a new entry, it will predict the corresponding class
label based on its learned patterns and features. This process of
experimentation and elimination of poorer models ultimately finalised
our selection for the model we would use.

3.3.2: Implementation

Our model was implemented utilising the binary classification algorithm
Support Vector Classifier (SVC) written in Python 3.10 and adhered to
the agile methodology, specifically, SCRUM.

This approach allowed our team to adapt to changing requirements and
incorporate feedback rapidly throughout the development process.

3.3.2.1: Agile Methodology

The team organised the project planning timeline into bi-weekly sprints.
During sprint planning meetings, tasks were identified, estimated, and
finally assigned to team members based on their strengths and
weaknesses. weekly stand-ups, conducted virtually on Google Hangouts,
facilitated regular communication, ensuring each team member was
conscious of what they were required to achieve and how to achieve it,
along with the identification of any impediments ensuring that they
could be quickly addressed. The end of each sprint featured a sprint
review to acquire a retrospective on each task to refine our process
going forward.

3.3.2.2: Implementation Breakdown

Each stage of product development can be broken down into phases as
follows:

The **Data Preprocessing Phase** was crucial in preparing the dataset
for consumption. Its main objectives were the handling of missing / NULL
values, encoding categorical variables, and normalising numerical
variables to ensure that the data fed into the model is clean and
properly formatted. This was achieved using the ***pandas*** library for
data manipulation and ***scikit-learn*** for encoding and normalisation
tasks. Meticulous data preparation is instrumental in enhancing the
model\'s performance and accuracy by providing a solid foundation for
the subsequent stages of the machine-learning pipeline.

Following the data preparation phase, the **Feature Selection Phase**
played a vital role in the development process. Its purpose was to sift
through the various available features and select those that have the
most significant impact on the model's final prediction. By employing
techniques like Recursive Feature Elimination (RFE) implemented using
the method ***sklearn.feature_selection.RFE*** \[6\] from
***scikit-learn***, each feature was ranked based on its importance.
This reduced the complexity of the model while retaining the model\'s
predictive capability by focusing on the most informative attributes
within the dataset, for example, placing more weight on the resting
blood pressure of an individual and less emphasis on their sex/gender.

Once the features are selected, the **Model Training and Validation
Phase** begins. Within this phase, the Support Vector Classifier /
Machine (SVC / SVM) model is trained using the chosen features, then its
performance is subsequently validated. This stage utilises the
***scikit-learn*** library\'s SVC implementation with a Sigmoid Kernel,
complemented by K-Fold Cross-Validation. The primary aim here was to
train the model in such a way as to maximise accuracy while preventing
overfitting, ensuring that the model generalises well to unseen data by
accurately estimating its performance across various subsets of the
data.\
\
Finally, the **Model Evaluation Phase** includes the assessment of the
trained model\'s predictive accuracy and its generalisation capabilities
to new data. This is carried out through a comprehensive list of
evaluations using tools such as the Receiver Operating Characteristic
(ROC) curve and confusion matrix plots. The latter of which is useful in
generating key performance metrics including Precision, Recall, Accuracy
and F1 score. These metrics allow for the fine-tuning of the model, such
as by measuring the effectiveness of different Kernels based on their
accuracy, precision, recall and F1-Scores.\
\
This phase not only provides a detailed analysis of the model\'s
performance but also highlights its strengths and potential weaknesses
in predicting the risk of the development of cardiovascular disease
(CVD) within a human. Through this rigorous evaluation, insights were
gained into how well the model can be expected to perform in real-world
scenarios.

3.3.3: Testing

The primary advantage of using Jupyter Notebooks is that code can be
easily divided into cells for prototyping. This allows for a degree of
flexibility when prototyping code, such as the capability to run each
section independently of one another. Different parts included importing
the data, preprocessing to remove null values, exploring the dataset,
training the model, and then finally getting output results from the
model. This was important as we would add new parts to the code with no
possibility of breaking existing functionality.

In addition to the flexibility afforded by the use of Jupyter Notebooks,
the approach to testing outlined in this report encompassed three
distinct testing methodologies: Unit Testing, Integration Testing, and
Acceptance Testing.

Firstly, unit testing was conducted on each individual component to
verify its functionality, utilising Python's ***unittest*** framework
\[7\]. This testing methodology is imperative for the identification and
addressing of any anomalies in data preprocessing, feature selection and
data visualisations.

Next, integration testing was conducted. This was also a very important
part of the model so we could check how different parts of the model
worked with each other vs normal testing. The use of separate components
was a major part of our testing strategy to ensure each part would still
run individually even with new components. Our team also made use of
acceptance testing where we validated the performance and functionality
of the overall model such as tests to evaluate the actual model accuracy
which was 87%. This accuracy is very good for a start on the project,
especially for a medical context that could be saving lives - but it's
also important to note the possibility of wrong predictions and the
impact they can have on someone's life. For example, if this model
predicts the results of someone's test incorrectly, it could tell
someone with CVD that they are not at risk, or otherwise, someone
without CVD that they have CVD. This is the primary reason that the
model should be used as a baseline assessment, not a final conclusion.

Finally, acceptance testing was conducted. It is the final phase of
testing and constitutes the assessment of the entire system against our
project\'s specified requirements. The goal of this testing phase was to
confirm the model\'s overall performance and its capability to predict
cardiovascular disease risk (CVD) effectively. Notably, our initial
acceptance tests highlighted a variation in performance across different
demographic groups. This insight prompted further adjustments to the
feature selection process, enhancing the model\'s sensitivity and
specificity.

In this stage, the metrics that we employed to determine accuracy
included Precision, F1-Score, Recall and Accuracy generated by the
confusion matrix specified in the Model Evaluation Phase in section
3.3.2.2 of this report. On top of that, we tested the model against a
"model" that would produce a random output for the given results and
observed that our CVD model varied significantly showing accurate
results. During this phase, we encountered issues surrounding the
identification of false positives and false negatives and a series of
sub-80% accuracy scores, which prompted the team to trial different
Kernels. Thus concluding that Sigmoid was the most optimal Kernel for
this use case. Through these adjustments and retraining, we are now
confident that the model is accurate enough for use in the field.

We made use of testing methods such as K-Fold validation, ROC Curve and
Confusion Matrices that would confirm our results to be useful and allow
us to identify ways of improving the accuracy further. It's also
possible that there are limits to the potential accuracy and
generalizability of the model where there is a degree of unknown where
the amount of training we do cannot improve the real accuracy any
further.

Ultimately, through thorough testing and an adherence to agile
methodologies, the project successfully developed a machine learning
model capable of predicting CVD risk with 87% accuracy. The iterative
approach enabled continuous improvement, ensuring the product met its
requirements and goals. and demonstrating its potential as a valuable
tool within the healthcare space.

# Chapter 4: The project management chapter

4.1: A literature review of project management

We employed diverse project management methodologies during the
project\'s development to guarantee the smooth operation of the
workflow. From the first start, it was emphasised how important it is to
handle each assignment in a way that maximises efficiency. Our team\'s
comprehension of project management was crucial to completing the task
at hand, as our objective was to construct a model that could forecast
an individual\'s risk of developing heart disease.\
\
Project planning, when applied to the development of a model for
predicting heart disease, is more than the simplicity of to-do lists.
The monitoring and controlling phase is crucial for tracking the
project\'s progress, promptly addressing any arising issues, and
managing changes effectively. This structured project planning approach
ensures that the development of a heart disease prediction model is
executed efficiently, with the flexibility to adapt to new insights and
findings, thereby laying the foundation for a successful and impactful
model.\
\
A work breakdown structure breaks the work to be undertaken to achieve
the project goals into a set of functions, sub-functions, and
activities. Observing the progress of a project is very vital to its
success. Having regular meetings outlining what has been completed and
what needs to be completed goes a long way.

When conducting project planning and management, there are a wide
variety of planning tools that you may already be using or may utilise
in the future. It can be something as simple as reminders in a calendar
or sticky notes. With sticky notes, you may also utilise a whiteboard
and coloured marker pens to give further dimensions to the project\'s
planning and management representation. This may be a good option for a
smaller team or a smaller project as everyone might be working in the
same location. However, in our circumstance, we are a team of 5 working
on different parts of the project. It made more sense to utilise
technology to maximise potential by using Jira. By using Jira, it
allowed us to keep track of what everyone was doing whilst we spent time
in and out of the lab. A variety of software tools are also available,
including PlanBox and Microsoft Project.

The use of Jira facilitated seamless collaboration among us. It enabled
real-time tracking of progress and identification of issues and sprints.
Through the strategic application of Jira Software, we not only sped up
our development timeline but also made sure the quality of our project
remained high.

A task at this scale requires a lot of attention and time. Time
management is a skill which was mentioned throughout lectures and
PowerPoint. Time management skills were essential to the creation of our
model for predicting heart disease. We were able to monitor our progress
and reach deadlines by communicating with each other. Giving timeframes
to complete certain tasks helped maintain organisation. As a consequence
the project was finished on schedule, allowing us to concentrate on
improving our overall work.

Ultimately, [employing diverse project management methodologies and
tools like Jira, our team efficiently developed a heart disease
prediction model. Through structured planning, regular monitoring, and
seamless collaboration, we met our deadlines and maintained high
quality, demonstrating the crucial role of effective project management
in achieving objectives.]{.mark}

4.2: Team project management report

In the development of our project, we utilised a variety of project
management techniques to ensure that the workflow was managed
seamlessly. From the very first lecture, it was reiterated how essential
it is to manage each task in a manner that increases efficiency. With
our goal being to create a model that was made for predicting how likely
it is that someone would develop heart disease, it was vitally important
that as a team we understood the aspects of project management to get
the job done.\
\
The university provided us with many PowerPoint and documents defining
ways in which the project could be managed. 'Jira' was something that
was mentioned many times within lectures and plastered throughout most
of the resources from the module. Jira lets you break down the complex
model development process into objectives of large or smaller tasks.
This helps provide clarity and an approach which is structured and
focused.\
\
Jira's Scrum boards promote iterative development in the use of sprints.
This allowed us to create short development cycles with feedback loops
in the development of our product. Features such as real-time
developments meant that team members could update the status of their
tasks which provided a real-time view of the progress of the project.
Throughout our project, we used Jira to identify over 30 different
issues in the development of our model.\
As well as highlighting issues, you can define the priority in which the
problem is. Ranking it from lowest to highest.

In our development, our lowest priority issue was ranked medium, which
truly shows how vital every detail can affect the progress of our
project. This was for 'plotting variables'. By doing this it helped us
understand the dataset better which lies within the greater goal of
increasing efficiency.

In contrast to this, we had 5 issues that held the highest priority. An
example of one was 'Upload Dataset to Github Repository'. The reason
that this had great significance was because it was what our whole
project is based around. Having the dataset uploaded allowed us to deal
with other issues such as creating correlation notes, calculating risk
factors and analysing the data further. Within identifying an issue, it
is then assigned to a member of the team. It grants you the option to
add comments and create a work log. Once it is completed, it is logged
which then marks the resolution as 'done' and the time in which it took
to be completed is tracked and noted.\
\
We made sure to make the most of the agile methodology support on Jira
by using sprints. In the end, we made 5 sprints each including different
phases of our development. We made sure to regularly update each sprint
stemming from creating the GitHub Repository to planning and preparing
for the presentation.\
\
Overall, our project successfully illustrated the significance of the
use of Jira to help organise work, apply agile sprints and communicate
effectively. The emphasis on issue identification, prioritisation and
resolution reinforced the idea that every detail counts in achieving a
successful outcome.

# Chapter 5: The conclusion chapter

Cardiovascular Disorder (CVD) is a globally recognised plaguing issue
amongst the people unfortunate enough to have it, and extending to the
close family with the depression of one\'s passing. We at Anything©
sought to change this. Or at the very least provide a foundation for
people to more easily tackle it. We decided on a goal, we would attempt
to train a machine learning model, to be able to identify prevalence of
CVD, given a set of characteristics.

At the start of the project, we sourced a publicly available dataset of
individuals which listed their attributes alongside if they had been
recognised as having CVD. With this dataset, we meticulously analysed
it, cleaning it for any anomalies such as null values, prepping for our
use. Using this data we conducted exploratory data analysis including
constricting appropriate visual graphs and showcases allowing us to more
easily draw conclusions of trends within the dataset, determine features
such as correlation between various aspects such as age and sex, and
thus focusing us on what aspects were most relevant and needing of our
attention, and research.

Once we had the dataset cleaned, and a good understanding of the
architecture of it, we focused our efforts towards the training of the
model which we would come to use as the solution for the project. This
involved comparing various pre-existing machine learning solutions with
similar data analysing contexts as our own, creating relevant metrics
against which to stage them, and taking the greatest, the Sigmoid Kernel
Model. Once again with the dataset, we split it into two sets; a
training set, and a testing set. The training would be the ground on
which our model would be trained, and the latter would be the one
against which it is tested. The untouched testing set would give us the
ability to determine various attributes of our model such as its
accuracy, f1 score and other characteristics of it.\
\
The culmination of all of this resulted in a model with an accuracy of
87%, and reaching the most generalised to random new entries it can be.
This was what we had set out to do; given some characteristics of a
person, determine their unknown attribute of CVD. To this end, we
succeeded.

In summary, our project stands as an example of the incredible potential
of machine learning, namely at its incorporation into such fields as
healthcare and diagnosing diseases. By making use of data powered
insights and modern techniques, we have been able to take a monumental
step forwards towards a better less sorrowing future, wherein diseases
such as CVD can be recognised quicker and in turn treated sooner.

# References

2.1: A literature review of the team working

\[1\] \"James Dyson: In Praise of Failure,\" wired.com. \[Online\].
Available:
[[https://www.wired.com/story/james-dyson-failure/]{.underline}](https://www.wired.com/story/james-dyson-failure/).
\[Accessed: 23-Mar-2024\]

\[2\] "How to Solve It: A New Aspect of Mathematical Method," George
Pólya. Princeton University Press.

3.2: Context

\[3\] "Cardiovascular diseases (CVDs)," who.int. \[Online\]. Available:
[[https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)]{.underline}](https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds))
\[Accessed: 23-Mar-2024\]

\[4\] "Machine learning-based approach to the diagnosis of
cardiovascular vascular disease using a combined dataset,"
sciencedirect.com. \[Online\]. Available:
[[https://www.sciencedirect.com/science/article/pii/S2666521223000145?via%3Dihub]{.underline}](https://www.sciencedirect.com/science/article/pii/S2666521223000145?via%3Dihub).
\[Accessed: 23-Mar-2024\]

3.3.1: Design

\[5\] "Understanding Support Vector Machine Example Code," Analytics
Vidhya. \[Online\]. Available:
[[https://www.analyticsvidhya.com/blog/2017/09/understaing-support-ector-machine-example-code/]{.underline}](https://www.analyticsvidhya.com/blog/2017/09/understaing-support-ector-machine-example-code/).
\[Accessed: 24-Mar-2024\].

3.3.2: Implementation

\[6\] \"sklearn.feature_selection.RFE --- scikit-learn 0.24.1
documentation,\" scikit-learn. \[Online\]. Available:
<https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html>.
\[Accessed: 24-Mar-2024\].

\[7\] \"unit test --- Unit testing framework --- Python 3.10.4
documentation,\" Python.org. \[Online\]. Available:
[[https://docs.python.org/3/library/unittest.html]{.underline}](https://docs.python.org/3/library/unittest.html).
\[Accessed: 24-Mar-2024\].
