Proposal Plan
-------------

# Pythonic Functional Programming with Coconut

Talk Format: Short Talk (30 minutes)
Audience Level: Intermediate/Specialised
Tags: Python, ML

## Elevator Pitch

Ever tried writing functional-style Python? Did you wish that you had a less clunky lambda syntax and more straightforward currying? Or maybe you're just tired of importing reduce from functools? Find out how to comfortably write elegant functional code with Coconut, a functional superset of Python!

## Public Abstract

Writing functional code in Python can be both fun and frustrating at the same time. With functions being first-class citizens, Python allows us to build programmes with higher-order functions. However, it is often cumbersome to do something that would be bread-and-butter in a typical functional language. The lack of concise syntax for lambdas, currying and function compositions is a nuisance. The lack of boilerplate-less pattern matching and algebraic data types could be a deal breaker. This talk presents a functional superset of Python, Coconut, which allows you to write elegant functional code, whilst staying with the familiar Python environment. Since all Coconut code compiles to Python, it is straightforward to leverage existing Python libraries. This talk identifies various pain points of writing functional code in Python, and demonstrates how Coconut addresses the problems. In particular, we will start with a basic coding problem, and move on to designing a machine-learning pipeline by exploiting its monoidal structure.

## Private Abstract and Timing Overview

- 0-5 minutes: Introduction to why would we want to write code in a functional style?
    - What is functional programming? Immutability and referential transparency.
    - What are the benefits? Easier to reason about, to parallelise and often more readable.
    - What is needed from the language? First class functions.
- 5-10 minutes: Show expressiveness of functional paradigm with basic example of Sieve of Eranthoses.
    - Present Haskell and Python code.
    - Identify Python pain points one-by-one, and slowly address them in Coconut: lambda, pattern matching, composition, builtin functions.
- 10-15 minutes: Explain the concept of ML pipeline
    - Data types: transformers and estimators.
    - Functions: fit and transform.
    - Pipeline and pipeline stages.
    - Why would we write ML code like this?
- 15-20 minutes:
    - Haskell-style type tetris.
    - Pipeline stage as monoid, so we only need mempty and mconcat.
    - Example: one hot encoder estimator.
- 20-25 minutes: Compare to Python version
    - No pattern matching means it's very inconvenient to do it with functions.
    - We would not have noticed pipeline as monoid.
    - Notice boilerplates and conciseness.
- 25-30 minutes: Taking Coconut even further:
    - Add types with MyPy.
    - Define functors and monads.

## Biography

I am an avid Pythonista and a functional programming enthusiast. I have been using Python on a daily basis since 2013, where I worked on a machine learning and algorithmic trading project with Seamless Machine Learning. Nowadays, I work as a data scientist in Agoda, an online travel agency with a huge emphasis on intelligent application of machine learning. Despite being a company whose main production language is Scala, I still find every opportunity to use Python in my daily research. Although Haskell is often my go-to scripting language, Python remains to be my default machine learning language due to its libraries. This talk draws on my personal experience of writing Python in a style that is as functional as possible.

I have never spoken in a conference before. However, I have a number of public speaking experiences such as giving Agoda's AB testing training for product owners, giving supervisions in Cambridge University and teaching machine learning 101 in Universitas Nusantara PGRI Kediri.
