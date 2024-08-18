Developer Backlog
=================

Currently Working
-----------------

 * Need People Model
   * Employees? do we need separate model?
   * Auditors Model points to People for basic information
   * Consider extending Django User Model for Auditors

 * Template Stuff
   * Implement a basic Django form somewhere just to get better start on tempate system, etc.

Backlog
-------
 * Requirements Model - consider this:
   * Requirements coverage choices of Self, Parent, Child, N/A, (maybe Special)?
   * Auto-Add option
   * Consider way to handle grouping (related to / keep together / bundle )
   * Special Focus requirement. See end of 5.3 - how to handle?

 * On Processes Model
   * Consider adding a Process Owner one-to-many.  Would require implmenting people first.
   * Is there a better way to abstract Audit Frequency

 * Need Audits Model (near-last thing todo)
   * Start ID's at 4121100 - don't know what significance is

 * Consider some sort of yearly coverage record model - need to think this over
   * A home for managerial dispensation notes, etc.

 * Need Departmental model for areas audited

 * IS_TRAINING flag on things that can be used for training and should be cleaned up

 * Document substantial differences between iadb1 vs iadb2
   * Requirements vs Clauses and idea that coverage can trace to children, be covered by parent.

 * Reports that were in IADB1:
   * Auditor Audit History (by year quarter)
   * Auditor Assignment by Quarter
   * Clause Coverage
   * Delinquency
   * Dept Audit Count
   * Question Useage
   * Process Coverage

Wishlist Items
--------------

 * Implement in-app ticket system to replace this and be more useful for users to report
   issues. Django-helpdesk could be option once it supports Django 2
