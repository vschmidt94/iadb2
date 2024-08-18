== IADB2 To-Do List / Work log ==


1. Work on audit scheduling

3. Events help text is not aligned with actual page content.
   - Page Header missing also
 
* Consider django-threadedcomments module.

* Should be able to create abstract class for IADB list view that populates the context.  
  * Holding on this one, need to move the prototype forward and spend less time refactoring right now.

2018.03.25
----------
 - Started back in on Audits module, refactored that to match other apps setup.

2018.03.18
----------
 - Process update fixed using generic update page.

2018.03.16
----------
NEXT TIME: Do same thing to Processes that happened to Department today.
 - Department inquiry, update fixed by implementing it as a class based view.
 - Now have a common/generic_update_page.html template that can be reused for basic objects.

2018.03.14
----------
NEXT TIME:
 - Maintain department broken from department inquiry page
 - Edit link on processes goes nowhere

Today: walked through People, Processes, Requirements looking for consistency.

2018.03.09
----------
NEXT TIME: Walk through People, Processes, Requirements apps and make sure they are more or
less conforming to the general pattern that is developing. Check for consistency.
- Worked on People update form. Now allow blank department for person, shows heading.
- Removed dead code for person update view.

2018.03.08
----------
 NEXT TIME: Continue working on People - update view works, but ugly.
 - Working on Requirements models.
 - In Person app:
   - Changed to use the generic table
   - Partialized the add person modatl
