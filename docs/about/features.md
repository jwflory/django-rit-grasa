Features
========

This page references our application features based off system requirements.
All application features are identified by the following:

```
* **Status**:
    * Confirmed: Successfully tested items
    * Unconfirmed: Items not yet successfully tested
    * Skipped: "Old hat" items
* **Technology decision**
* **Summary of approach**
* **Completion criteria**
```

Features are organized below by user groups.


## Families

### Search for different events.

* **Status**: Implemented
* **Technology decision**: [Haystack](https://haystacksearch.org/), [Whoosh](https://whoosh.readthedocs.io/en/latest/intro.html)
* **Relevant domain(s)**: Database
* **Summary of approach**: Use Django Haystack to search the database of events using a keyword match search.
* **Completion criteria**:
    * Unauthenticated user runs successful search query to return results about after-school programs in an area.
    * Information is provided if it exists; the user is informed if it does not exist.

### Apply filters to better discover events that interest a user.

* **Status**: Implemented
* **Technology decision**: [Haystack](https://haystacksearch.org/), [Django Forms](https://docs.djangoproject.com/en/2.2/topics/forms/), [Jinja](https://palletsprojects.com/p/jinja/), YAML config files
* **Relevant domain(s)**: Database
* **Summary of approach**: Create Haystack search filters that mirror metadata we save in our database.
* **Completion criteria**:
    * Unauthenticated user alters search query by choosing from a list of preset filters.
    * More detailed information is discovered in search when filters are displayed.

### Find information to learn more about a specific event.

* **Status**: Implemented
* **Technology decision**: [Django Forms](https://docs.djangoproject.com/en/2.2/topics/forms/), [Jinja](https://palletsprojects.com/p/jinja/)
* **Relevant domain(s)**: Database, front-end
* **Summary of approach**: Create a unique, addressable page for every event by pulling data from the database and injecting it into front-end HTML with Jinja inclusions.
* **Completion criteria**:
    * Unauthenticated user is able to navigate to an event’s unique page from search UI.
    * Any user can share a direct link to event page details with another user.


## Program providers

### Add new events with specific metadata into system for approval by administrators.

* **Status**: Implemented
* **Technology decision**: [Django Forms](https://docs.djangoproject.com/en/2.2/topics/forms/)
* **Relevant domain(s)**: Full stack
* **Summary of approach**: Create Forms to validate user input and create new events in the events database table.
* **Completion criteria**:
    * Provider is able to log into application.
    * Provider submits new event for review with required details:
        * Title
        * Website
        * Address
        * Suggested age groups

### Update information for existing events in system for approval by administrators.

* **Status**: In progress
* **Technology decision**: [User authentication modules](https://docs.djangoproject.com/en/2.2/topics/auth/) provided in Django, [Django Forms](https://docs.djangoproject.com/en/2.2/topics/forms/) for basic user input
* **Relevant domain(s)**: Full stack
* **Summary of approach**: Allow an authenticated user to edit Forms for events they themselves have created.
* **Completion criteria**:
    * Provider is able to log into application.
    * Provider edits an existing event that they already contributed.
    * Event re-enters review queue for admin users.


## GRASA and Monroe County staff

### Review and approve submitted events.

* **Status**: Implemented
* **Technology decision**: [User authentication modules](https://docs.djangoproject.com/en/2.2/topics/auth/) provided in Django, [Django Forms](https://docs.djangoproject.com/en/2.2/topics/forms/) for managing event data, email (via [Mailgun](https://www.mailgun.com/pricing))
* **Relevant domain(s)**: Full stack
* **Summary of approach**: A status field in the database will be edited for an event depending if it is pending review, approved, or rejected; only approved events appear on the public site.
* **Completion criteria**:
    * Admin is able to log into application.
    * Admin is able to edit a pending event and change its status (approved or rejected).
    * Provider is emailed when their event status is changed.

### Confirm new provider accounts.

* **Status**: Implemented
* **Technology decision**: [User authentication modules](https://docs.djangoproject.com/en/2.2/topics/auth/) provided in Django, email (via [Mailgun](https://www.mailgun.com/pricing))
* **Relevant domain(s)**: Back-end, database
* **Summary of approach**: Allow anyone to self-register on the website using Django Forms to gather information about the user and saving the User object to the database when registration process completes.
* **Completion criteria**:
    * Admin is able to log into application.
    * Registered user is able to log in as a provider once admin confirms user's registration.


## All users

### Mobile-friendly user interface.

* **Status**: Implemented
* **Relevant domain(s)**: Front-end
* **Summary of approach**: Ensure web application appears correctly on modern smartphones and mobile devices by manual QA testing.
* **Completion criteria**:
    * Core functionality works smoothly on mobile device as it does computing device.
