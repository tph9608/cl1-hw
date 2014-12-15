The goal of this project is to predict whether the answer to a trivia
question is correct or not (these are the same questions you classified in an earlier homework).  The most important (and effective) route for success is to engineer
features and gather additional data to help your predictions of the right answer.

About the Data
==============

Quiz bowl is an academic competition between schools in
English-speaking countries; hundreds of teams compete in dozens of
tournaments each year. Quiz bowl is different from Jeopardy, a recent
application area.  While Jeopardy also uses signaling devices, these
are only usable after a question is completed (interrupting Jeopardy's
questions would make for bad television).  Thus, Jeopardy is rapacious
classification followed by a race---among those who know the
answer---to punch a button first.

Here's an example of a quiz bowl question:

Expanding on a 1908 paper by Smoluchowski, he derived a formula for
the intensity of scattered light in media fluctuating densities that
reduces to Rayleigh's law for ideal gases in The Theory of the
Opalescence of Homogenous Fluids and Liquid Mixtures near the Critical
State.  That research supported his theories of matter first developed
when he calculated the diffusion constant in terms of fundamental
parameters of the particles of a gas undergoing Brownian Motion.  In
that same year, 1905, he also published On a Heuristic Point of View
Concerning the Production and Transformation of Light.  That
explication of the photoelectric effect won him 1921 Nobel in Physics.
For ten points, name this German physicist best known for his theory
of Relativity.

*ANSWER*: Albert _Einstein_

Two teams listen to the same question. Teams interrupt the question at
any point by "buzzing in"; if the answer is correct, the team gets
points and the next question is read.  Otherwise, the team loses
points and the other team can answer.

Why we want to use Quiz Bowl Data for Classification
-----------------------------------------------

It's very easy to generate guesses (in fact, we could generate every
possible guess).  The challenge is knowing whether any given guess is
good or not.  We can treat this as a classification problem.  Every
guess can be described by features that measure how well it matches
the question.  The classifier tells us whether we got the question
wrong or right.

We will provide many different guesses for the question.  Your job is
to select (through classification or other means) which guess should
be treated as the the final guess.

Data Format
--------------------

Each line has a guess (page) and a correct answer (answer) given some
fraction of the question revealed so far (text).  Your goal is to
predict whether they match.  Each guess is the title of a Wikipedia
page.  To get you started, you have the following columns:

* _Question ID_: An ID for the question.

* _Answer_: The actual answer of the question (not always one of the guesses)

* _Sentence Position_: The index of the last question seen.  Smaller
  numbers are harder.  Together with the _Question ID_, this forms a
  unique identifier for the instance.

* _Question Text_: The text of the question.  It has been normalized to
  make parsing easier.

* _QANTA Scores_: Guesses generated by a [deep learning
  algorithm](http://www.cs.colorado.edu/~jbg/docs/2014_emnlp_qb_rnn.pdf)

* _IR_Wiki Scores_: Guesses generated by a [information
  retreival](https://pypi.python.org/pypi/Whoosh/) search through
  Wikipedia.

* _category_: The category of the question.

If you're using Python, make sure you use the [DictReader and
DictWriter classes](https://docs.python.org/2/library/csv.html).  For
both of the scores, you may find this code useful for forming a
dictionary:

<pre>
def form_dict(vals):
    d = defaultdict(float)
    for jj in vals.split(", "):
        key, val = jj.split(":")
        d[key.strip()] = float(val)
    return d
</pre>

Data are [available](https://github.com/ezubaric/cl1-hw/tree/master/project).  

You are welcome to use any *automatic* method to choose an answer.  It
need not be among the sets provided by our two guessers.  In addition to the data we provide, you are
welcome to use any external data *except* quiz bowl questions to improve your
methods.  You are welcome (an encouraged) to use any publicly
available software, but you may want to check on Piazza for
suggestions as many tools are better (or easier to use) than others.

Competition
==================

We will use [Kaggle InClass for this competition](https://inclass.kaggle.com/c/when-to-buzz).  This will be a
competition between students in the Colorado and Maryland graduate
courses on natural language processing and computational linguistics.
A large portion of your grade will be how you perform on this Kaggle
competition.  You must register with a UMD or Colorado address.  Please identify which school you're associated with when you register.

Proposal
==================

The project proposal is due 7. November.  This one page PDF document
should describe:

* Who is on your team

* What techniques you will explore 

* Your timeline for completing the project (be realistic; you should
  have your first Kaggle submission by 14. November)

Designate **one person** from your group to submit the proposal on
Moodle.  Late days cannot be used on this assignment.

Final Presentation
======================

The final presentation will be in class on Dec. 16 (at 13:30, not the
usual class time).  In the final presentation you will:

* Explain what you did

* Who did what

* What challenges you had

* Review how well you did (based on the Kaggle competition)

* Provide an error analysis.  An error analysis must contain examples from the
  development set that you get wrong.  You should show those sentences
  and explain why (in terms of features or the model) they have the
  wrong answer.  You should have been doing this all along as your
  derive new features (e.g., 2b), but this is your final inspection of
  your errors. The feature or model problems you discover should not
  be trivial features you could add easily.  Instead, these should be
  features or models that are difficult to correct.  An error analysis
  is not the same thing as simply presenting the error matrix, as it
  does not inspect any individual examples.

* The linguistic motivation for your features.  This is a
  computational linguistics class, so you should give precedence to
  features / techniques that we use in this class (e.g., syntax,
  morphology, part of speech, word sense, etc.).  Given two features
  that work equally well and one that is linguistically motivated,
  we'll prefer the linguistically motivated one.

* Presumably you did many different things; how did they each
  individually contribute to your final result?

Project Writeup
======================

By 23:55 16. December, have the person in your group whose last name
is alphabetically first submit their project writeup explaining what
you did and what results you achieved on Moodle.  This document should
make it clear:

* Why this is a good idea
* What you did
* Who did what
* Whether your technique worked or not

Please do not go over 2500 words unless you have a really good reason.
Images are a much better use of space than words, usually (there'��s no
limit on including images, but use judgement and be selective).

Grade
======================

The grade will be out of 25 points, broken into five areas:

* _Presentation_: For your oral presentation, do you highlight what
  you did and make people care?  Did you use time well during the
  presentation?

* _Writeup_: Does the writeup explain what you did in a way that is
  clear and effective?

* _Technical Soundness_: Did you use the right tools for the job, and
  did you use them correctly?  Were the relevant to this class?

* _Effort_: Did you do what you say you would, and was it the right
  ammount of effort.

* _Performance_: How did your techniques perform?