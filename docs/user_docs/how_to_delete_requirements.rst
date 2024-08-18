Deleting Requirements
=====================

.. Note::
   Super-Admin rights are required to add, modify, or delete Requirements.

Changes to the Requirements records must be done through the Super Powers > Database 
Maintence interface.

As is the case with most of the base record objects, a Requirements record can only be
deleted if **no other record** is referencing the one you are attempting to delete. 

References to Requirement records are typically:

* Coverage records

  -  In which case, the Requirement should probably be considered permanent and changed to
     inactive, rather than deleted.

* Other Requirement records

  - A Requirement record can not be deleted while there are children claiming it as a parent 
    requirement. Either delete the child(ren) or point them to a different parent.
  - A Requirement that has "Self" coverage delegation can not be deleted until the coverage 
    is delegated to somewhere other than itself, to remove the circular reference.

Once these references are removed, a Requirements should be able to be deleted normally.
