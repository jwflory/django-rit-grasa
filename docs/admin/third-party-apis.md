Third-party APIs
================

This page describes third-party API services used in the application, how they are used, and how to set them up.


## Geocoding service: MapQuest API

An API token for this service is required for the map functionality of the Event Locator to work.

The MapQuest API translates an address provided by a Program Provider to a pair of latitude/longitude coordinates.
These coordinates are used in the front-end to create markers on the map for events.


### How it is used

The MapQuest API token is set in the configuration file (see `config.yml.example`).
The secret token is automatically used in front-end HTML files.
Administrators only need to maintain the API token in the production config file.

The API request is made when an address is added or changed on a new event or an edited event.

### How to acquire API access

Register for a [MapQuest Developer API key](https://developer.mapquest.com/plan_purchase/steps/business_edition/business_edition_free/register).

### Cost considerations

A free API key is limited to 15,000 requests a month.
The API is only used when a new event is created or an existing event is edited (explained above).
Therefore, it is highly unlikely for the API to graduate to a paid tier unless the application grows significantly.
The next price tier is 30,000 requests a month for $99/month; see [pricing and plans](https://developer.mapquest.com/plans) for more information.


## Email/SMTP service

The Event Locator also needs an SMTP server for dispatching email.
This information is managed in the config file (see `config.yml.example` for an example).
If an existing SMTP mail server already exists, it may be used in the application.

However, in the event that an on-premise SMTP server is not available, we suggest using any of the following services and their email APIs:

* [Mailgun](https://www.mailgun.com/) ([about](https://www.mailgun.com/email-api), [pricing](https://www.mailgun.com/pricing))
* [SendGrid](https://sendgrid.com/) ([about](https://sendgrid.com/use-cases/transactional-email/), [pricing](https://sendgrid.com/pricing/))
* [Mandrill](https://mandrill.com/) ([about](https://mandrill.com/features/), [pricing](https://mandrill.com/pricing/))
