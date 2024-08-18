About Standards and Requirements
================================

Standards and Requirements are the primary record types for defining the primary objectives
ACME Co. hopes to achieve by our business processes.

Standard
--------
A `Standard` record is created to define the top-level controlling document, such as AS9100:D.

`Standard` record contents are straight-forward:

* Identifier

  * In the example of AS9100:D, the identifier should be "AS9100"

* Revision

  * "D" - to continue the above example

* Description

  * This is free-form text, and used to store the document title.
  * In the AS9100:D example, this would be: "Quality Systems - Aerospace - Model for Quality
    Assurance in Design, Development, Production, Installation and Servicing"
  * Not widely used, but can be included on some Reports, etc.

* Start Date and Stop Date

  * Currently, these fields are informative only, but could add logic in the future.

* Is Active?

  * True/False representing if this Standard is currently the in-use and being audited 
    against. 
  
  * Audits are created and conducted against active Standards.

Requirements
------------

`Requirement` defines a particular "rule" or directive contained in a `Standard`. These are
generally the **shall's** that dictate what the business must do to be in compliance with 
the `Standard`.  In the case of AS9100, these are typically the document's **clauses**.
IADB2 uses the term `Requirement` as it is possible to incorporate other documents in the 
future where the term `clause` may not be as appropriate as it is in the context of AS9100.

Requirements can be (read: should be) specified in a heirarchical manner when possible. When
adding a Requirement, there is drop down selector for choosing some other Requirement as
the new Requirement's **parent**. Note this implies that the order requirements are added
to IADB is important. Parent requirements must be created before the child(ren). 

It is only necessary to identify relationships by defining parent. Once that link is created,
the system will keep track of the reciprocal relationship (parent-to-children) automatically.

Requirements: Coverage Delegation
---------------------------------

When a Requirement is defined, you must specify **coverage delegation**.  This is a way 
to delegate the responsibility for covering this particular `Requirement` to either a 
parent or the children.  

.. NOTE::
   Coverage delegation is used to shift responsibility for covering the Requirement to the
   Questions that will be asked elsewhere. The implication here is that ACME Co. always has
   the responsibility to meet ALL Requirements contained in the Standard.

We use Coverage Delegation as a tool to better manage our Question pool, and to cope with
different ways the Standards are written. For example, the requirement may be be written:

1. Management shall:

   1. Enforce a four day work-week
   2. Provide designated nap times

In this case, Requirement 1 would Delegate Coverage to Requirements 1.1 and 1.2. This
means that if 1.1 and 1.2 are indeed found to be True, then Requirement 1 is also fulfilled.
Requirement 1 would be set to Delegate Coverage to it's children, and both 1.1 and 1.2 should 
be set to `Self` as they are the actual coverage points.

Note that coverage can be delegated upstream or downstream if needed, and can take as many
nested delegations as needed until it hits the Requirements that will actually be covered.

A requirement that has delegated it's coverage elsewhere will not be included in Coverage
calculations - only Requirements with `Self` coverage are counted towards coverage metrics.

.. TIP::
   Coverage Delegration graphs are available in IADB2, under Maintenance > Requirements.
   Look for a Button on that page to generate the graphs. They can be a useful visualization
   of how the current configuration is set up.
