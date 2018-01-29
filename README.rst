StackSphere
===========

Yet another troposphere helper lib

Overview
---------

The troposphere library provides an interface for generating Amazon
Cloudformation templates in python.  It also provides type-checking
and validation of a stack.

The goal of this library is to extend the functionality of troposphere to
better facilitate nesting templates, to perform type-checking on parameters
passed to nested templates, and to ease creation and update of
cloudformation stacks.

Specific Goals
--------------

* Generate template urls from Python module paths

* Type check parameters passed to nested templates

* Order resources by dependency and deploy stack incrementally
