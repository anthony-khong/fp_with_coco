# Pythonic Functional Programming with Coconut

**Talk Format:** Short Talk (30 minutes)

**Audience Level:** Intermediate/Specialised

**Tags:** Python, ML

# Elevator Pitch

Writing functional-style Python can be challenging. The challenges range from minor nuisance such as verbose lambda syntax and clunky currying to more serious problems such as iterator chaining and pattern matching. Coconut is a functional superset of Python that aims to enable elegant and Pythonic functional-style code.

# Public Abstract

With functions being first-class citizens, Python allows us to build programmes with higher-order functions. However, it is often cumbersome to do something that would be bread-and-butter in a typical functional language. The lack of concise syntax for lambdas, currying and function compositions is a nuisance. The lack of boilerplate-less pattern matching and iterator chaining could be a deal breaker. This talk presents Coconut, a functional superset of Python, which aims to enable writing elegant functional code, whilst staying with the familiar Python environment and libraries. We will identify various pain points of writing functional code in Python, and demonstrates how Coconut addresses the problems. In particular, we will start with a basic coding problem, and move on to designing a machine-learning pipeline with a functional approach.

# Private Abstract and Timing Overview

- 0-5 minutes: Introduction to functional-style code
    - What is functional programming? Ans. Immutability and referential transparency.
    - What exactly do we mean by functional style? Ans. Higher-order functions and function compositions.
    - What are the benefits? Ans. Easier to reason about, parallelise and often more readable.
    - What is needed from the language? Ans. First class functions.
- 5-10 minutes: Show expressiveness of functional paradigm with basic example of Sieve of Eranthoses.
    - Compare Haskell and Python code.
    - Address Python pain points in Coconut:
        1. Verbose lambdas
        2. Hard-to-read function compositions
        3. Clunky currying
        4. No straightforward iterator chaining
        5. No pattern matching
        6. Bonuses: assignment functions, builtin higher-order functions, more concise names and declarative style.
- 10-15 minutes: Explain the use of the pipeline pattern in ML
    - Data types: transformers and estimators.
    - Functions: fit and transform.
    - Pipeline and pipeline stages.
    - Why? Ans. more readability and same level of abstraction.
- 15-20 minutes: Pipeline in Coconut
    - Haskell-style type tetris.
    - Pipeline stage as monoid, so we only need mempty and mconcat.
    - Example: one-hot encoder estimator.
- 20-25 minutes: Compare to Python version
    - No pattern matching means it's very inconvenient to do it with functions.
    - Notice boilerplates and conciseness.
    - We would not have noticed pipeline as monoid.
- 25-30 minutes: Taking Coconut even further:
    - Functor example: one-hot encoder coalescing.
    - Parallel example: parallel pipeline stage.
    - Static typing with MyPy.

# Biography

I am a data scientist working at Agoda, an innovative accommodation website that places a huge emphasis in machine learning algorithms. I have been using Python on a daily basis since 2013 as a freelance data scientist and algorithmic trader. I am also a functional programming enthusiast, and my experience mainly comes from writing Scala code in Agoda and using Haskell for scripting. I enjoy writing functional-style code in Python, and have been actively trying to marry the two for years. My other passion include high-performance computing, Bayesian statistics and Vim.

I have never spoken in a conference before. However, I have a number of public speaking experiences such as training in Agoda and giving undergraduate-level lectures in machine learning and economics. I have also been involved in a few pro-bono projects that required public speaking.
