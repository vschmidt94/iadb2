IADB2 Introduction
==================

The Internal Audit Database v2 (IADB2) is a tool developed to assist Acme Co.'s
Internal Audit proccesses.  At it's core, IADB2 is used to manage, track, and
record the activities of auditors and audit teams as they conduct periodic
audits of Acme Co.'s processes and proceedures.

Infrastructure
--------------
IADB2 is currently implemented as follows:
 * Using Django 2.0 Framework (Python 3)
 * PostgreSQL as back-end database

   * Database would be easy change out as Django's ORM abstracts the data layer.
 * JQuery in support of theming
 * Bootstrap

   * Specifically, theming is provided by the SB-Admin2 theme under the MIT License
 * Sphinx for this documentation

REST API
--------
IADB2 offers `some` REST API functionality to retrieve the data from 
backend datastore without having to utilize the existing interface.
In theory this should make it easier to extend the overall functionality
or build really cool things into the front-end. As of this writing,
there is no known use of this API.  But hey, it's there.

Disambiguation: IADB2 `Apps`
----------------------------
New users may notice the word `App` used throughout this documentation is
used somewhat differently than the common concept of an `App`.
  

Django uses the concepts of `Projects` and `Apps`, which are not always
intuitive.  In these terms, IADB2 is the `Project` - the shell
which contains a collection of smaller Apps.  A Django `App` is a 
smaller, more granular chunck of functionality.

The IADB2 `Project` is built from the following `Apps`:
 * Audit `App`
 * Auditor `App`
 * Attendance `App`
 * Dashboard `App`
 * Question `App`
 * Requirements `App`
 * (and possibly other, more esoteric apps not mentioned here)

In actual use, these details are transparent to the end users. However, the
apps may be individually mentioned within this documentation - so it is
useful to have a basic awareness of this details.


  
