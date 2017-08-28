# Table of contents

### Getting Started

* [Description](#description)
* [Requirements](#requirements)
* [Concepts description](#concepts)

### API

* [Listing](#listing)
* [Disruptions](#disruptions)
* [Impacts](#impacts)
* [Traffic_reports](#traffic)
* [Severities](#severities)
* [Categories](#categories)
* [Channels](#channels)
* [Properties](#properties)
* [Channel Types](#channeltypes)

## <a id="description" name="description"></a>Description

Chaos is the web service which can feed [Navitia](https://github.com/CanalTP/navitia) with real-time [disruptions](http://doc.navitia.io/#traffic-reports).
It can work together with [Kirin](https://github.com/CanalTP/kirin) which can feed [Navitia](https://github.com/CanalTP/navitia) with real-time delays.

Chaos manage disruptions and help you to communicate with your travellers on the best.


## <a id="requirements" name="requirements"></a>Requirements

Before using Chaos, you will need few things:
- a Navitia token, allowing you to request navitia on a data coverage
- a customer ID
- a contributor ID

Your usual Kisio Digital interlocutor can provide you these elements, and an access to the production or pre-production platform.
Before using the API in production, you will need to provide:
- integration specifications
- expected load your application will generate.

These two points are recquired to help us managing the Chaos platform.

## <a id="concepts" name="concepts"></a>Concepts description
Chaos uses some concepts, here are the essentials.

| Name                                                                   | Name (navitia) | Definition                 |
------------------------------------------------------------------------------ | -------- | ----------------------- |
| Disruption | Disruption | The event (planned, or not) you want to communicate to travellers. |
| Impact | Impact | The way an event affects the travellers (by blocking lines, closing station, ...). |
| Object | pt_object | The network objects (lines, stop area, stop points, or full network) affected by an impact. |
| Channel | channel | The way you speak to the traveller (SMS, web, mobile, notification, email, ...). |
| Severity | severity | How bad the impact is. |
| Cause | Cause | Description of the cause of the perturbation (strike, accident). |
| Localisation | Localisation | The Stop Area where the disruption happens. Useful to show it on map. |
| Tag | Tag | A tag on a description. |
| Effect | Effect | The effect of a severity. Only "No service" is implemented. |
| Color | Color | The color of a severity. |
| Priority | Priority | A number to order severities. |
| Pattern | N/A | A combination of days, dates and time to build a time pattern: "from 1 janv. 2016  to 1 janv. 2017 , only monday and tuesday, every day from 08:00 am to 10:00 am". |
| Application | Application | The effective duration of an impact. |
| Publication | Publication | The duration of the communication of a disruption to travellers (useful for planned disruptions). |

# Root [/]

## <a id="listing" name="listing"></a>List Api [GET]

- Response 200 (application/json)
    * Body
```json
{
    "status": {
        "href": "https://.../status"
    },
    "tags": {
        "href": "https://.../tags"
    },
    "severities": {
        "href": "https://.../severities"
    },
    "channels": {
        "href": "https://.../channels"
    },
    "disruption": {
        "href": "https://.../disruptions/{id}",
        "templated": true
    },
    "properties": {
        "href": "https://.../properties"
    },
    "categories": {
        "href": "https://.../categories"
    },
    "impactsbyobject": {
        "href": "https://.../impacts"
    },
    "disruptions": {
        "href": "https://.../disruptions"
    },
    "channeltypes": {
        "href": "https://.../channel_types"
    },
    "traffic_reports": {
        "href": "https://.../traffic_reports"
    },
    "causes": {
        "href": "https://.../causes"
    }
}
```

## <a id="headers" name="headers"></a>Headers

| Name                 | description                                                                    | required | default                 |
| -------------------- | ------------------------------------------------------------------------------ | -------- | ----------------------- |
| Content-Type         | input text type                                                                | true     | application/json        |
| Authorization        | token for navitia services                                                     | true     |                         |
| X-Customer-Id        | client code. A client is owner of cause, channel, severity and tag             | true     |                         |
| X-Contributors       | contributor code. A contributor is owner of a disruption                       | true     |                         |
| X-Coverage           | coverage of navitia services                                                   | true     |                         |

# <a id="categories" name="categories"></a>List of categories [/categories]

## Retrieve the list of all categories [GET]

### Headers ([here](#headers))

### Parameters
None

- Response 200 (application/json)
    * Body
```json
{
    "categories": [
        {
            "id": "ad24d203-9723-4318-bbaa-f025a7301044",
            "name": "meteo",
            "self": {
                "href": "https://.../categories/ad24d203-9723-4318-bbaa-f025a7301044"
            },
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "null"
        },
        {
            "id": "28bd0932-c2d5-43e0-8d7e-9f391da17c85",
            "name": "probleme",
            "self": {
                "href": "https://.../categories/28bd0932-c2d5-43e0-8d7e-9f391da17c85"
            },
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z"
        },
        {
            "id": "9917eebe-3c4a-443e-9b28-7f808a181b87",
            "name": "rer",
            "self": {
                "href": "https://.../categories/9917eebe-3c4a-443e-9b28-7f808a181b87"
            },
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z"
        }
    ],
    "meta": {}
}
```
## Create a category [POST]

### Headers ([here](#headers))

### Request (application/json) -> __Delete comments before POST__
- Body
```javascript
{
    // REQUIRED. string. maxLength 250.
    "name": "meteo"
}
```
- Response 201 (application/json)
    * Body
```json
{
    "category": {
        "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
        "name": "meteo",
        "self": {
            "href": "https://.../categories/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
        },
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": null
    }
}
```
# Category [/categories/{id}]

## Retrieve one category [GET]

Retrieve an existing category.

### Headers ([here](#headers))

### Parameters
None

- Response 200 (application/json)
    * Body
```json
{
    "category": {
        "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
        "self": {
            "href": "https://.../categories/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
        },
        "name": "rer",
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": null
    }
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No category"
    }
}
```
## Update a category [PUT]

### Headers ([here](#headers))

### Request (see POST part for required elements)

### Exemple of a request
```
    * Url
        /categories/3d1f42b3-e8df-11e3-8c3e-0008ca8617ea

    * Headers
        Content-Type: application/json
        Authorization: navitia_token
        X-Customer-Id: customer_id
        X-Contributors: contributor_id
        X-Coverage: navitia_coverage

    * Body
        {
            "name": "rer"
        }
```
- Response 200 (application/json)
    * Body
```json
{
    "category": {
        "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
        "self": {
            "href": "https://.../categories/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
        },
        "name": "rer",
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": "2014-04-31T16:55:18Z"
    }
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No category"
    }
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'name' is a required property"
    }
}
```
## Delete a category [DELETE]

Archive a category.

### Headers ([here](#headers))

### Parameters
None

- Response 204 (category archived)

- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No category"
    }
}
```
# List of causes [/causes]

## Retrieve the list of all causes [GET]

### Headers ([here](#headers))

### Parameters

| Name                 | description                                                                               | required | default                 |
| -------------------- | ----------------------------------------------------------------------------------------- | -------- | ----------------------- |
| category             |  filter by category (id of category)                                                      | false    |                         |


- Response 200 (application/json)
    * Body
```json
{
    "causes": [
        {
            "id": "95c916ba-b824-47c4-9fe9-99e8803dc493",
            "self": {
                "href": "https://.../causes/95c916ba-b824-47c4-9fe9-99e8803dc493"
            },
            "wordings": [{"key": "msg", "value": "accident voyageur1"}],
            "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "test"},
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z"
        },
        {
            "id": "6ebb24f5-6e02-4926-83f5-74002ac1bd1a",
            "self": {
                "href": "https://.../causes/6ebb24f5-6e02-4926-83f5-74002ac1bd1a"
            },
            "wordings": [{"key": "msg", "value": "accident voyageur2"}],
            "category": {"id": "ce1c4c79-5d5d-40e6-a3bb-1b1eb9cb0025", "name": "category-1"},
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z"
        },
        {
            "category": null,
            "id": "4fb9f90f-90b5-4ea1-91ad-f297f04debc6",
            "self": {
                "href": "https://.../causes/4fb9f90f-90b5-4ea1-91ad-f297f04debc6"
            },
            "wordings": [{"key": "msg", "value": "accident voyageur3"}],
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z"
        }
    ],
    "meta": {}
}
```
## Create a cause [POST]

### Headers ([here](#headers))

### Request -> __Delete comments before POST__
- Body
```javascript
{
    // OPTIONAL. object.
    "category": {
        // REQUIRED. regexp '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'.
        "id": "32b07ff8-10e0-11e4-ae39-d4bed99855be"
    },
    // REQUIRED. array. uniqueItems. minItems 1.
    "wordings": [
        {
            // REQUIRED. string. minLength 1. maxLength 250.
            "key": "msg_interne",
            // REQUIRED. string. maxLength 250.
            "value": "Bebert a encore laissé une locomotive en double file"
        },
        {
            // REQUIRED. string. minLength 1. maxLength 250.
            "key": "msg_media",
            // REQUIRED. string. maxLength 250.
            "value": "train delayed"
        },
        {
            // REQUIRED. string. minLength 1. maxLength 250.
            "key": "msg_sms",
            // REQUIRED. string. maxLength 250.
            "value": "prenez le bus"
        }
    ],
    // OPTIONAL. string. default wording displayed in navitia.
    "wording": "train delayed"
}
```
- Response 201 (application/json)
    * Body
```json
{
    "cause": {
        "category": {
            "created_at": "2017-02-21T09:30:09Z",
            "id": "32b07ff8-10e0-11e4-ae39-d4bed99855be",
            "name": "test",
            "self": {
                "href": "https://.../categories/32b07ff8-10e0-11e4-ae39-d4bed99855be"
            },
            "updated_at": null
        },
        "created_at": "2017-02-21T09:38:59Z",
        "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
        "self": {
            "href": "https://.../causes/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
        },
        "wordings": [
            {
                "key": "msg_interne",
                "value": "Bebert a encore laissé une locomotive en double file"
            },
            {
                "key": "msg_media",
                "value": "train delayed"
            },
            {
                "key": "msg_sms",
                "value": "take the bus"
            }
        ]
    }
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'wordings' is a required property"
    }
}
```
# Cause [/causes/{id}]

## Retrieve one cause [GET]

Retrieve one existing cause

### Headers ([here](#headers))

### Parameters
None

- Response 200 (application/json)
    * Body
```json
{
    "cause": {
        "id": "95c916ba-b824-47c4-9fe9-99e8803dc493",
        "self": {
            "href": "https://.../causes/95c916ba-b824-47c4-9fe9-99e8803dc493"
        },
        "wordings": [{"key": "msg", "value": "accident voyageur1"}],
        "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "test"},
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": "2014-04-31T16:55:18Z"
    }
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No cause"
    }
}
```

## Update a cause [PUT]

### Headers ([here](#headers))

### Request (see POST part for required elements)

### Exemple of a request
```
    * Url
        /causes/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea

    * Headers
        Content-Type: application/json
        Authorization: navitia_token
        X-Customer-Id: customer_id
        X-Contributors: contributor_id
        X-Coverage: navitia_coverage

    * Body
        {
            "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be"},
            "wordings": [{"key": "msg_interne", "value": "Bebert va déplacer sa locomotive"}, {"key": "msg_media", "value": "train delayed"}, {"key": "msg_sms", "value": "le train va arriver"}],
            "wording": "train delayed"
        }
```
- Response 200 (application/json)
    * Body
```json
{
    "cause": {
        "category": {
            "created_at": "2017-02-21T09:30:09Z",
            "id": "32b07ff8-10e0-11e4-ae39-d4bed99855be",
            "name": "test",
            "self": {
                "href": "https://.../categories/32b07ff8-10e0-11e4-ae39-d4bed99855be"
            },
            "updated_at": null
        },
        "created_at": "2017-02-21T09:38:59Z",
        "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
        "self": {
            "href": "https://.../causes/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
        },
        "wordings": [
            {
                "key": "msg_interne",
                "value": "Bebert va déplacer sa locomotive"
            },
            {
                "key": "msg_media",
                "value": "train delayed"
            },
            {
                "key": "msg_sms",
                "value": "le train va arriver"
            }
        ]
    }
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No cause"
    }
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'wordings' is a required property"
    }
}
```
## Delete a cause [DELETE]

Archive a cause.

### Headers ([here](#headers))

### Parameters
None

- Response 204 (cause archived)

- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No cause"
    }
}
```
# <a id="severities" name="severities"></a>List of severities [/severities]

## Retrieve the list of all severities [GET]

Return all the severities ordered by priority.

### Headers ([here](#headers))

### Parameters
None
- Response 200 (application/json)
    * Body
```json
{
    "severities": [
        {
            "self": {
                "href": "https://.../severities/e8d95fcb-e0cf-4c11-855a-4f9feb837002"
            },
            "id": "e8d95fcb-e0cf-4c11-855a-4f9feb837002",
            "wordings" : [{"key": "msg", "value": "Normal"}],
            "effect": null,
            "priority": 1,
            "color": "#123456",
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z"
        },
        {
            "self": {
                "href": "https://.../severities/8cb3fbc2-1c73-4bf0-8b85-dbd58760a39f"
            },
            "id": "8cb3fbc2-1c73-4bf0-8b85-dbd58760a39f",
            "wordings" : [{"key": "msg", "value": "Majeur"}],
            "effect": null,
            "priority": 2,
            "color": "#123456",
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z"
        },
        {
            "self": {
                "href": "https://.../severities/356c82ad-dda7-4aee-86c3-a31bcde67b45"
            },
            "id": "356c82ad-dda7-4aee-86c3-a31bcde67b45",
            "wordings" : [{"key": "msg", "value": "Bloquant"}],
            "effect": "no_service",
            "priority": 3,
            "color": "#123456",
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z"
        }
    ],
    "meta": {}
}
```
## Create a severity [POST]

### Headers ([here](#headers))

### Request -> __Delete comments before POST__
- Body
```javascript
{
    // REQUIRED. array. uniqueItems. minItems 1.
    "wordings" : [
        {
            // REQUIRED. string. minLength 1. maxLength 250.
            "key": "msg",
            // REQUIRED. string. maxLength 250.
            "value": "Normal"
        }
    ],
    // OPTIONAL. string. maxLength 20.
    "color": "#123456",
    // OPTIONAL. integer.
    "priority": 1,
    // OPTIONAL. enum ['no_service','reduced_service','significant_delays','detour','additional_service','modified_service','other_effect','unknown_effect','stop_moved'] | null.
    "effect": null
}
```
- Response 201 (application/json)
    * Body
```json
{
    "severity": {
        "color": "#123456",
        "created_at": "2014-04-31T16:52:18Z",
        "effect": null,
        "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
        "priority": 1,
        "self": {
            "href": "https://.../severities/3d1f42b3-e8df-11e3-8c3e-0008ca8617ea"
        },
        "updated_at": null,
        "wording": "Normal",
        "wordings": [
            {
                "key": "msg",
                "value": "Normal"
            }
        ]
    }
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'wordings' is a required property"
    }
}
```
# Severity [/severities/{id}]

## Retrieve one severity [GET]

Retrieve one existing severity.

### Headers ([here](#headers))

### Parameters
None
- Response 200 (application/json)
    * Body
```json
{
    "severity": {
        "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
        "wordings" : [{"key": "msg", "value": "Normal"}],
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": null,
        "color": "#123456",
        "priority": 1,
        "effect": null
    }
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No severity"
    }
}
```
## Update a severity [PUT]

### Headers ([here](#headers))

### Request (see POST part for required elements)

### Exemple of a request
```
    * Url
        /severities/3d1f42b3-e8df-11e3-8c3e-0008ca8617ea

    * Headers
        Content-Type: application/json
        Authorization: navitia_token
        X-Customer-Id: customer_id
        X-Contributors: contributor_id
        X-Coverage: navitia_coverage

    * Body
        {
            "wordings" : [{"key": "msg", "value": "Bonne nouvelle"}],
            "color": "#123456",
            "effect": null
        }
```

- Response 200 (application/json)
    * Body
```json
{
    "severity": {
        "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
        "wordings" : [{"key": "msg", "value": "Bonne nouvelle"}],
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": "2014-04-31T16:55:18Z",
        "color": "#123456",
        "priority": 1,
        "effect": null
    }
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No severity"
    }
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'wordings' is a required property"
    }
}
```
## Delete a severity [DELETE]

Archive one severity.

### Headers ([here](#headers))

### Parameters
None

- Response 204 (severity archived)

- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No severity"
    }
}
```
# <a id="channeltypes" name="channeltypes"></a>List of channel types [/channel_types]

## Retrieve the list of all channel types [GET]

### Headers ([here](#headers))

### Parameters
None

- Response 200 (application/json)
    * Body
```json
{
    "channel_types": ["web", "sms", "email", "mobile", "notification", "twitter", "facebook","title","beacon"]
}
```

# <a id="channels" name="channels"></a>List of channels [/channels]

## Retrieve the list of all channels [GET]

### Headers ([here](#headers))

### Parameters
None

- Response 200 (application/json)
    * Body
```json
{
    "channels": [
        {
            "id": "8a00aeb5-1704-4035-85de-6e4c329115cb",
            "name": "court",
            "self": {
                "href": "https://.../channels/8a00aeb5-1704-4035-85de-6e4c329115cb"
            },
            "max_size": 140,
            "content_type": "text/plain",
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z",
            "types": ["sms", "notification"]
        },
        {
            "id": "54933d0f-af4a-4ae0-a11a-71cdc7e6ca45",
            "name": "long",
            "self": {
                "href": "https://.../channels/54933d0f-af4a-4ae0-a11a-71cdc7e6ca45"
            },
            "max_size": 512,
            "content_type": "text/plain",
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z",
            "types": ["mobile"]
        },
        {
            "id": "a12a9681-3c0d-4ce8-9e7b-33ec58853666",
            "name": "long riche",
            "self": {
                "href": "https://.../channels/a12a9681-3c0d-4ce8-9e7b-33ec58853666"
            },
            "max_size": null,
            "content_type": "text/markdown",
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z",
            "types": ["web"]
        }
    ],
    "meta": {}
}
```
## Create a channel [POST]

### Headers ([here](#headers))

### Request (application/json) -> __Delete comments before POST__
- Body
```javascript
{
    // REQUIRED. string. maxLength 250.
    "name": "beacon",
    // REQUIRED. integer.
    "max_size": 140,
    // REQUIRED. string. maxLength 250.
    "content_type": "text/plain",
    // REQUIRED. array of enum (channel_types) ["web","sms","email","mobile","notification","twitter","facebook","title","beacon"]. uniqueItems. minItems 1.
    "types": ["beacon"]
}
```
- Response 201 (application/json)
    * Body
```json
{
    "channel": {
        "id": "ab73ada6-51ba-4f51-b68a-42bdd1555fbf",
        "name": "beacon",
        "self": {
            "href": "https://.../channels/ab73ada6-51ba-4f51-b68a-42bdd1555fbf"
        },
        "max_size": 140,
        "content_type": "text/plain",
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": null,
        "types": ["beacon"]
    }
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'name' is a required property"
    }
}
```
# Channel [/channels/{id}]

## Retrieve one channel [GET]

Retrieve one existing channel.

### Headers ([here](#headers))

### Parameters
None
- Response 200 (application/json)
    * Body
```json
{
    "channel": {
        "id": "ab73ada6-51ba-4f51-b68a-42bdd1555fbf",
        "name": "beacon",
        "self": {
            "href": "https://.../channels/ab73ada6-51ba-4f51-b68a-42bdd1555fbf"
        },
        "max_size": 140,
        "content_type": "text/plain",
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": null,
        "types": ["beacon"]
    }
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No channel"
    }
}
```
## Update a channel [PUT]

### Headers ([here](#headers))

### Request (see POST part for required elements)

### Exemple of a request
```
    * Url
        /channels/ab73ada6-51ba-4f51-b68a-42bdd1555fbf

    * Headers
        Content-Type: application/json
        Authorization: navitia_token
        X-Customer-Id: customer_id
        X-Contributors: contributor_id
        X-Coverage: navitia_coverage

    * Body
        {
            "name": "twitter",
            "max_size": 50,
            "content_type": "text/plain",
            "types": ["twitter"]
        }
```

- Response 200 (application/json)
    * Body
```json
{
    "channel": {
        "id": "ab73ada6-51ba-4f51-b68a-42bdd1555fbf",
        "name": "twitter",
        "self": {
            "href": "https://.../channels/ab73ada6-51ba-4f51-b68a-42bdd1555fbf"
        },
        "max_size": 50,
        "content_type": "text/plain",
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": "2014-04-31T17:30:44Z",
        "types": ["twitter"]
    }
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No channel"
    }
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'content_type' is a required property"
    }
}
```
## Delete a channel [DELETE]

Archive one channel.

### Headers ([here](#headers))

### Parameters
None

- Response 204 (channel archived)

- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No channel"
    }
}
```
# <a id="properties" name="properties"></a>List of properties [/properties]

## Retrieve the list of all properties [GET]

### Headers ([here](#headers))

### Parameters

| Name                 | description           | required |
| -------------------- | --------------------- | -------- |
| key                  | filter list by key    | false    |
| type                 | filter list by type   | false    |

- Response 200 (application/json)
    *Body
```json
{
    "properties": [
        {
            "created_at": "2016-04-12T12:00:00Z",
            "id": "10216aec-00ad-11e6-9f6d-0050568c8380",
            "key": "almost-special",
            "self": {
                "href": "https://.../properties/10216aec-00ad-11e6-9f6d-0050568c8380"
            },
            "type": "not_a_comment",
            "updated_at": "2016-04-12T13:00:00Z"
        },
        {
            "created_at": "2016-04-12T12:01:00Z",
            "id": "10216aec-00ad-11e6-9f6d-0050568c8382",
            "key": "special",
            "self": {
                "href": "https://.../properties/10216aec-00ad-11e6-9f6d-0050568c8382"
            },
            "type": "comment",
            "updated_at": "2016-04-12T13:01:00Z"
        }
    ]
}
```
## Create a property [POST]

### Headers ([here](#headers))

### Request (application/json) -> __Delete comments before POST__
- Body
```javascript
{
    // REQUIRED. string. minLength 1. maxLength 250.
    "key": "test",
    // REQUIRED. string. minLength 1. maxLength 250.
    "type": "test"
}
```
- Response 201 (application/json)
    * Body
```json
{
    "property": {
        "id": "0542d8f1-ff75-4035-89df-cd335b3cab5d",
        "self": {
            "href": "https://.../properties/0542d8f1-ff75-4035-89df-cd335b3cab5d"
        },
        "key": "test",
        "type": "test",
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": null
    }
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'key' is a required property"
    }
}
```
- Response 409 (application/json) -> duplicate
    * Body
```json
{
    "error": {
        "message": "..."
    }
}
```
# Property [/properties/{id}]

## Retrieve one property [GET]

Retrieve one existing property.

### Headers ([here](#headers))

### Parameters
None
- Response 200 (application/json)
    * Body
```json
{
    "property": {
        "id": "0542d8f1-ff75-4035-89df-cd335b3cab5d",
        "self": {
            "href": "https://.../properties/0542d8f1-ff75-4035-89df-cd335b3cab5d"
        },
        "key": "test",
        "type": "test",
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": null
    }
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "Property {id} not found"
    }
}
```
## Update a property [PUT]

### Headers ([here](#headers))

### Request (see POST part for required elements)

### Exemple of a request
```
    * Url
        /properties/0542d8f1-ff75-4035-89df-cd335b3cab5d

    * Headers
        Content-Type: application/json
        Authorization: navitia_token
        X-Customer-Id: customer_id
        X-Contributors: contributor_id
        X-Coverage: navitia_coverage

    * Body
        {
            "key": "test1",
            "type": "test2"
        }
```

- Response 200 (application/json)
    * Body
```json
{
    "property": {
        "id": "0542d8f1-ff75-4035-89df-cd335b3cab5d",
        "self": {
            "href": "https://.../properties/0542d8f1-ff75-4035-89df-cd335b3cab5d"
        },
        "key": "test1",
        "type": "test2",
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": "2014-04-31T16:55:10Z"
    }
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "Property {id} not found"
    }
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'type' is a required property"
    }
}
```
- Response 409 (application/json) -> duplicate
    * Body
```json
{
    "error": {
        "message": "..."
    }
}
```
## Delete a property [DELETE]

Delete one property. Can be used only if the property is not used.

### Headers ([here](#headers))

### Parameters
None

- Response 204 (property deleted)

- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "Property {id} not found"
    }
}
```
- Response 409 (application/json)
    * Body
```json
{
    "error": {
        "message": "The current {property} is linked to at least one disruption and cannot be deleted"
    }
}
```
# List of tags [/tags]

## Retrieve the list of all tags [GET]

### Headers ([here](#headers))

### Parameters
None
- Response 200 (application/json)
    * Body
```json
{
    "tags": [
        {
            "id": "cdb874a6-ab42-4058-b97b-1e95408372f1",
            "name": "meteo",
            "self": {
                "href": "https://.../tags/cdb874a6-ab42-4058-b97b-1e95408372f1"
            },
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z"
        },
        {
            "id": "ac5638c3-d086-4549-bc4b-40480b027d0c",
            "name": "probleme",
            "self": {
                "href": "https://.../tags/ac5638c3-d086-4549-bc4b-40480b027d0c"
            },
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z"
        },
        {
            "id": "5b9b1a2d-cf7c-40aa-80e4-ff1cbd17a658",
            "name": "rer",
            "self": {
                "href": "https://.../tags/5b9b1a2d-cf7c-40aa-80e4-ff1cbd17a658"
            },
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z"
        }
    ],
    "meta": {}
}
```
## Create a tag [POST]

### Headers ([here](#headers))

### Request (application/json) -> __Delete comments before POST__
- Body
```javascript
{
    // REQUIRED. string. maxLength 250
    "name": "traffic"
}
```
- Response 201 (application/json)
    * Body
```json
{
    "tag": {
        "id": "4295b733-b732-4794-81f5-e60b6553e026",
        "name": "traffic",
        "self": {
            "href": "https://.../tags/4295b733-b732-4794-81f5-e60b6553e026"
        },
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": null
    }
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'name' is a required property"
    }
}
```

# Tag [/tags/{id}]

## Retrieve one tag [GET]

Retrieve one existing tag.

### Headers ([here](#headers))

### Parameters
None
- Response 200 (application/json)
    * Body
```json
{
    "tag": {
        "id": "5b9b1a2d-cf7c-40aa-80e4-ff1cbd17a658",
        "self": {
            "href": "https://.../tags/5b9b1a2d-cf7c-40aa-80e4-ff1cbd17a658"
        },
        "name": "rer",
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": null
    },
    "meta": {}
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No tag"
    }
}
```
## Update a tag [PUT]

### Headers ([here](#headers))

### Request (see POST part for required elements)

### Exemple of a request
```
    * Url
        /tags/5b9b1a2d-cf7c-40aa-80e4-ff1cbd17a658

    * Headers
        Content-Type: application/json
        Authorization: navitia_token
        X-Customer-Id: customer_id
        X-Contributors: contributor_id
        X-Coverage: navitia_coverage

    * Body
        {
            "name": "rer bis"
        }
```
- Response 200 (application/json)
    * Body
```json
{
    "tag": {
        "id": "5b9b1a2d-cf7c-40aa-80e4-ff1cbd17a658",
        "self": {
            "href": "https://.../tags/5b9b1a2d-cf7c-40aa-80e4-ff1cbd17a658"
        },
        "name": "rer bis",
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": "2014-04-31T16:55:18Z"
    }
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No tag"
    }
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'name' is a required property"
    }
}
```
## Delete a tag [DELETE]

Archive a tag.

### Headers ([here](#headers))

### Parameters
None

- Response 204 (tag archived)

- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No tag"
    }
}
```
# <a id="disruptions" name="disruptions"></a>List of disruptions [/disruptions]

## Retrieve disruptions [GET]

Return all visible disruptions.

### Headers ([here](#headers))

### Parameters

| Name                 | description                                                                    | required | default                 |
| -------------------- | ------------------------------------------------------------------------------ | -------- | ----------------------- |
| start_page           | index of the first element returned (start at 1)                               | false    | 1                       |
| items_per_page       | number of items per page                                                       | false    | 20                      |
| publication_status[] | filter by publication_status, possible value are: past, ongoing, coming        | false    | [past, ongoing, coming] |
| ends_after_date    | start-date restriction for end_publication date     | false    |                     |
| ends_before_date      | end-date restriction for end_publication date       | false    |                     |
| current_time         | parameter for settings the use by this request, mostly for debugging purpose   | false    | NOW                     |
| tag[]                | filter by tag (id of tag)                                                      | false    |                         |
| uri                  | filter by uri of ptobject                                                      | false    |                         |
| line_section         | if uri is a line id, filter also on related line_section(s)                    | false    | False                   |
| status[]             | filter by status                                                               | false    | [published, draft]      |
| depth                | with depth=2, you could retrieve the first page of impacts from the disruption | false    | 1                       |


- Response 200 (application/json)
    * Body
```json
{
    "disruptions": [
        {
            "id": "d30502d2-e8de-11e3-8c3e-0008ca8657ea",
            "self": {"href": "https://.../disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ea"},
            "reference": "RER B en panne",
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z",
            "note": "blablbla",
            "status": "published",
            "publication_status": "ongoing",
            "contributor": "contrib.tn",
            "version": 1,
            "cause": {
                "id": "3d1f34b2-e8df-11e3-8c3e-0008ca8657ea",
                "wordings": [{"key": "msg", "value": "accident voyageur"}],
                "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "category-1"}
            },
            "tags": [
                {
                    "created_at": "2014-07-30T07:11:08Z",
                    "id": "ad9d80ce-17b8-11e4-a553-d4bed99855be",
                    "name": "rer",
                    "self": {
                        "href": "https://.../tags/ad9d80ce-17b8-11e4-a553-d4bed99855be"
                    },
                    "updated_at": null
                }
            ],
            "localization": [
                {
                    "id": "stop_area:RTP:SA:3786125",
                    "name": "HENRI THIRARD - LEON JOUHAUX",
                    "type": "stop_area",
                    "coord": {
                        "lat": "48.778867",
                        "lon": "2.340927"
                    }
                },
                {
                    "id": "stop_area:RTP:SA:3786123",
                    "name": "DE GAULLE - GOUNOD - TABANOU",
                    "type": "stop_area",
                    "coord": {
                        "lat": "48.780179",
                        "lon": "2.340886"
                    }
                }
            ],
            "publication_period" : {
                "begin":"2014-04-31T17:00:00Z",
                "end":"2014-05-01T17:00:00Z"
            },
            "impacts": {
                "pagination": {
                    "start_page": 0,
                    "items_per_page": 20,
                    "total_results": 3,
                    "prev": null,
                    "next": {"href": "https://.../disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ea/impacts?start_page=1&item_per_page=20"},
                    "first": {"href": "https://.../disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ea/impacts?start_page=1&item_per_page=20"},
                    "last": {"href": "https://.../disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ea/impacts?start_page=1&item_per_page=20"}
                }
            }
        },
        {
            "id": "d30502d2-e8de-11e3-8c3e-0008ca8657eb",
            "self": {"href": "https://.../disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657eb"},
            "reference": "RER A en panne",
            "created_at": "2014-05-31T16:52:18Z",
            "updated_at": null,
            "note": null,
            "status": "published",
            "publication_status": "coming",
            "contributor": "contrib.tn",
            "cause": {
                "id": "3d1f34b2-e8ef-11e3-8c3e-0008ca8657ea",
                "wordings": [{"key": "msg", "value": "accident voyageur"}],
                "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "category-1"}
            },
            "tags": [
                {
                    "created_at": "2014-07-30T07:11:08Z",
                    "id": "ad9d80ce-17b8-11e4-a553-d4bed99855be",
                    "name": "rer",
                    "self": {
                        "href": "https://.../tags/ad9d80ce-17b8-11e4-a553-d4bed99855be"
                    },
                    "updated_at": null
                }
            ],
            "properties": {
                "comment": [
                    {
                        "property": {
                            "created_at": "2014-04-12T12:49:58Z",
                            "id": "10216aec-00ad-11e6-9f6d-0050568c8382",
                            "key": "special",
                            "self": {
                                "href": "https://.../properties/10216aec-00ad-11e6-9f6d-0050568c8382"
                            },
                            "type": "comment",
                            "updated_at": "2014-04-12T13:00:57Z"
                        },
                        "value": "This is a very nice comment !"
                    }
                ]
            },
            "localization": [],
            "publication_period" : {
                "begin": "2014-04-31T17:00:00Z",
                "end": null
            },
            "impacts": {
                "pagination": {
                    "start_page": 0,
                    "items_per_page": 20,
                    "total_results": 5,
                    "prev": null,
                    "next": {"href": "https://.../disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657eb/impacts?start_page=1&item_per_page=20"},
                    "first": {"href": "https://.../disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657eb/impacts?start_page=1&item_per_page=20"},
                    "last": {"href": "https://.../disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657eb/impacts?start_page=1&item_per_page=20"}
                }
            }
        },
        {
            "id": "d30502d2-e8de-11e3-8c3e-0008ca8657ec",
            "self": {"href": "https://.../disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ec"},
            "reference": "Chatelet fermé",
            "created_at": "2014-05-17T16:52:18Z",
            "update_at": "2014-05-31T06:55:18Z",
            "note": "retour probable d'ici 5H",
            "status": "published",
            "publication_status": "past",
            "contributor": "contrib.tn",
            "cause": {
                "id": "3d1f34b2-e2df-11e3-8c3e-0008ca8657ea",
                "wordings": [{"key": "msg", "value": "accident voyageur"}],
                "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "category-1"}
            },
            "tags": [
                {
                    "created_at": "2014-07-30T07:11:08Z",
                    "id": "ad9d80ce-17b8-11e4-a553-d4bed99855be",
                    "name": "rer",
                    "self": {
                        "href": "https://.../tags/ad9d80ce-17b8-11e4-a553-d4bed99855be"
                    },
                    "updated_at": null
                }
            ],
            "localization": [
                {
                    "id": "stop_area:RTP:SA:378125",
                    "name": "Chatelet",
                    "type": "stop_area",
                    "coord": {
                        "lat": "48.778867",
                        "lon": "2.340927"
                    }
                }
            ],
            "publication_period" : {
                "begin": "2014-04-31T17:00:00Z",
                "end": null
            },
            "impacts": {
                "pagination": {
                    "start_page": 0,
                    "items_per_page": 20,
                    "total_results": 25,
                    "prev": null,
                    "next": {"href": "https://.../disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ec/impacts?start_page=1&item_per_page=20"},
                    "first": {"href": "https://.../disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ec/impacts?start_page=1&item_per_page=20"},
                    "last": {"href": "https://.../disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ec/impacts?start_page=21&item_per_page=20"}
                }
            }
        }

    ],
    "meta": {
        "pagination": {
            "start_page": 1,
            "items_per_page": 3,
            "total_results": 6,
            "prev": null,
            "next": {"href": "https://.../disruptions/?start_page=4&item_per_page=3"},
            "first": {"href": "https://.../disruptions/?start_page=1&item_per_page=3"},
            "last": {"href": "https://.../disruptions/?start_page=4&item_per_page=3"}
        }
    }

}
```

## Create a disruption [POST]

Create one valid disruption with impacts

### Headers ([here](#headers))

### Parameters

- Request (application/json) -> __Delete comments before POST__
    * Body
```javascript
{
    // REQUIRED. string. maxLength 250.
    "reference": "foo",
    // OPTIONAL. string. Default: null.
    "note": null,
    // REQUIRED. string.
    "contributor": "contrib.tn",
    // OPTIONAL. enum ["published", "draft"].
    "status": "published",
    // REQUIRED.
    "cause": {
        // REQUIRED.
        "id": "3d1f34b2-e8df-1ae3-8c3e-0008ca8657ea"
    },
    // OPTIONAL. array.
    "tags":[
        {
            // REQUIRED.
            "id": "ad9d80ce-17b8-11e4-a553-d4bed99855be"
        }
    ],
    // OPTIONAL. array. uniqueItems.
    "localization": [
        {
            "id": "stop_area:RTP:SA:3786125",
            "type": "stop_area"
        },
        {
            "id": "stop_area:RTP:SA:3786123",
            "type": "stop_area"
        }
    ],
    // OPTIONAL.
    "publication_period" : {
        // REQUIRED. string. regexp '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$'.
        "begin": "2014-04-31T17:00:00Z",
        // REQUIRED. string. regexp '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$' | null.
        "end": null
    },
    // OPTIONAL. array. uniqueItems.
    "impacts": [
        {
            // REQUIRED.
            "severity": {
                // REQUIRED. string. regexp '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'.
                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ea"
            },
            // OPTIONAL. array. uniqueItems.
            "application_periods": [
                {
                    // REQUIRED. string. regexp '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$'.
                    "begin": "2014-04-31T16:52:00Z",
                    // REQUIRED. string. regexp '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$' | null.
                    "end": "2014-05-22T02:15:00Z"
                }
            ],
            // OPTIONAL. array. uniqueItems.
            "messages": [
                {
                    // REQUIRED. string.
                    "text": "ptit dej à la gare!!",
                    // REQUIRED. object.
                    "channel": {
                        // REQUIRED. string. regexp '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'.
                        "id": "3d1f42b6-e8df-11e3-8c3e-0008ca8657ea"
                    }
                },
                {
                    // REQUIRED. string.
                    "text": "#Youpi\n**aujourd'hui c'est ptit dej en gare",
                    // REQUIRED. object
                    "channel": {
                        // REQUIRED. string. regexp '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'.
                        "id": "3d1f42b6-e8df-11e3-8c3e-0008ca8657ea"
                    }
                }
            ],
            // OPTIONAL. array. uniqueItems.
            "objects": [
                {
                    // REQUIRED. string. maxLength 250.
                    "id": "stop_area:RTP:SA:3786125",
                    // REQUIRED. enum ["network","stop_area","line","line_section","route","stop_point"].
                    "type": "stop_area"
                },
                {
                    // REQUIRED. string. maxLength 250.
                    "id": "line:RTP:LI:378",
                    // REQUIRED. enum ["network","stop_area","line","line_section","route","stop_point"].
                    "type": "line"
                },
                {
                    // REQUIRED. string. maxLength 250.
                    "id": "line_section:20:20:200",
                    // REQUIRED. enum ["network","stop_area","line","line_section","route","stop_point"].
                    "type": "line_section",
                    // REQUIRED if type "line_section". object.
                    "line_section":
                    {
                        // REQUIRED. object
                        "line":
                        {
                            // REQUIRED. string. maxLength 250.
                            "id": "line:RTP:LI:379",
                            // REQUIRED. enum ["line"].
                            "type": "line"
                        },
                        // REQUIRED.
                        "start_point":
                        {
                            // REQUIRED. string. maxLength 250.
                            "id": "stop_area:RTP:SA:3786198",
                            // REQUIRED. enum ["stop_area"].
                            "type": "stop_area"
                        },
                        // REQUIRED.
                        "end_point":
                        {
                            // REQUIRED. string. maxLength 250.
                            "id": "stop_area:RTP:SA:3783576",
                            // REQUIRED. enum ["stop_area"].
                            "type": "stop_area"
                        },
                        // OPTIONAL. array. uniqueItems.
                        "routes": [
                            {
                                // REQUIRED. string. maxLength 250.
                                "id": "route:GFH:RO:522",
                                // REQUIRED. enum ["route"].
                                "type": "route"
                            }
                        ],
                        // OPTIONAL. array. uniqueItems. minItems 1.
                        "metas": [
                            {
                                // REQUIRED. string. minLength 1. maxLength 250.
                                "key": "test",
                                // REQUIRED. string. maxLength 250.
                                "value": "meta de test"
                            }
                        ]
                    },
                }
            ]
            // OPTIONAL. boolean.
            "send_notifications": false,
            // OPTIONAL. string. regexp '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$' | null.
            "notification_date": null
        }
    ],
    // OPTIONAL. array.
    "properties": [
        {
            // REQUIRED. string. regexp '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'.
            "property_id": "10216aec-00ad-11e6-9f6d-0050568c8382",
            // REQUIRED. string. minLength 1. maxLength 250.
            "value": "This is a very nice comment !"
        }
    ]
}
```
- Response 201 (application/json)
    * Body
```json
{
    "disruption":{
        "id": "3d1f32b2-e8df-11e3-8c3e-0008ca8657ea",
        "self": {"href": "https://.../disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea"},
        "reference": "foo",
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": null,
        "note": null,
        "status": "published",
        "publication_status": "ongoing",
        "contributor": "contrib.tn",
        "version": 2,
        "cause": {
            "id": "3d1f34b2-e8df-1ae3-8c3e-0008ca8657ea",
            "wordings": [{"key": "msg", "value": "accident voyageur"}],
            "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "category-1"}
        },
        "tags": [
            {
                "created_at": "2014-07-30T07:11:08Z",
                "id": "ad9d80ce-17b8-11e4-a553-d4bed99855be",
                "name": "rer",
                "self": {
                    "href": "https://.../tags/ad9d80ce-17b8-11e4-a553-d4bed99855be"
                },
                "updated_at": null
            }
        ],
        "localization": [
            {
                "id": "stop_area:RTP:SA:3786125",
                "name": "HENRI THIRARD - LEON JOUHAUX",
                "type": "stop_area",
                "coord": {
                    "lat": "48.778867",
                    "lon": "2.340927"
                }
            },
            {
                "id": "stop_area:RTP:SA:3786123",
                "name": "DE GAULLE - GOUNOD - TABANOU",
                "type": "stop_area",
                "coord": {
                    "lat": "48.780179",
                    "lon": "2.340886"
                }
            }
        ],
        "publication_period" : {
            "begin": "2014-04-31T17:00:00Z",
            "end": null
        },
        "impacts": {
            "pagination": {
                "start_page": 0,
                "items_per_page": 20,
                "total_results": 1,
                "prev": null,
                "next": null,
                "first": {"href": "https://.../disruptions/1/impacts?start_page=1&item_per_page=20"},
                "last": null
            }
        },
        "properties": {
            "comment": [
                {
                    "property": {
                        "created_at": "2014-04-12T12:49:58Z",
                        "id": "10216aec-00ad-11e6-9f6d-0050568c8382",
                        "key": "special",
                        "self": {
                            "href": "https://.../properties/10216aec-00ad-11e6-9f6d-0050568c8382"
                        },
                        "type": "comment",
                        "updated_at": "2014-04-12T13:00:57Z"
                    },
                    "value": "This is a very nice comment !"
                }
            ]
        }
    },
    "meta": {}
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'reference' is a required property"
    }
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "..."
    }
}
```
- Response 503 (application/json)
    * Body
```json
{
    "error": {
        "message": "An error occurred during transferring this disruption to Navitia. Please try again"
    }
}
```
- Response 500 (application/json)
    * Body
```json
{
    "error": {
        "message": "..."
    }
}
```
# Disruption [/disruptions/{id}]

## Retrieve one disruption [GET]

Retrieve one existing disruption

### Headers ([here](#headers))

### Parameters

| Name                 | description                                                                    | required | default                 |
| -------------------- | ------------------------------------------------------------------------------ | -------- | ----------------------- |
| depth                | with depth=2, you could retrieve the first page of impacts from the disruption | false    | 1                       |

- Response 200 (application/json)
    * Body
```json
{
    "disruption": {
        "id": "3d1f32b2-e8df-11e3-8c3e-0008ca8657ea",
        "self": {"href": "https://.../disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea"},
        "reference": "RER B en panne",
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": "2014-04-31T16:55:18Z",
        "note": "blablbla",
        "status": "published",
        "publication_status": "ongoing",
        "contributor": "contrib.tn",
        "version": 2,
        "cause": {
            "id": "3d1e32b2-e8df-11e3-8c3e-0008ca8657ea",
            "wordings": [{"key": "msg", "value": "accident voyageur"}],
            "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "category-1"}
        },
        "tags": [
            {
                "created_at": "2014-07-30T07:11:08Z",
                "id": "ad9d80ce-17b8-11e4-a553-d4bed99855be",
                "name": "rer",
                "self": {
                    "href": "https://.../tags/ad9d80ce-17b8-11e4-a553-d4bed99855be"
                },
                "updated_at": null
            }
        ],
        "localization": [
            {
                "id": "stop_area:RTP:SA:3786125",
                "name": "HENRI THIRARD - LEON JOUHAUX",
                "type": "stop_area",
                "coord": {
                    "lat": "48.778867",
                    "lon": "2.340927"
                }
            },
            {
                "id": "stop_area:RTP:SA:3786123",
                "name": "DE GAULLE - GOUNOD - TABANOU",
                "type": "stop_area",
                "coord": {
                    "lat": "48.780179",
                    "lon": "2.340886"
                }
            }
        ],
        "publication_period" : {
            "begin": "2014-04-31T17:00:00Z",
            "end": null
        },
        "impacts": {
            "pagination": {
                "start_page": 1,
                "items_per_page": 20,
                "total_results": 3,
                "prev": null,
                "next": {"href": "https://.../disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts?start_page=1&item_per_page=20"},
                "first": {"href": "https://.../disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts?start_page=1&item_per_page=20"},
                "last": {"href": "https://.../disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts?start_page=1&item_per_page=20"}
            }
        }
    },
    "meta": {}
}
```

- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No disruption"
    }
}
```

## Update a disruption [PUT]

### Headers ([here](#headers))

### Parameters (see parameters for POST a disruption)

- Response 200 (application/json)
    * Body
```json
{
    "disruption":{
        "id": "3d1f32b2-e8df-11e3-8c3e-0008ca8657ea",
        "self": {"href": "https://.../disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea"},
        "reference": "foo",
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": "2014-04-31T16:55:18Z",
        "note": null,
        "status": "published",
        "publication_status": "ongoing",
        "contributor": "contrib.tn",
        "version": 2,
        "cause": {
            "id": "3d1f32b2-e8df-11e3-8c3e-0008ca8657ea",
            "wordings": [{"key": "msg", "value": "accident voyageur"}],
            "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "category-1"}
        },
        "tags": [
            {
                "created_at": "2014-07-30T07:11:08Z",
                "id": "ad9d80ce-17b8-11e4-a553-d4bed99855be",
                "name": "rer",
                "self": {
                    "href": "https://.../tags/ad9d80ce-17b8-11e4-a553-d4bed99855be"
                },
                "updated_at": null
            }
        ],
        "localization": [
            {
                "id": "stop_area:RTP:SA:3786125",
                "name": "HENRI THIRARD - LEON JOUHAUX",
                "type": "stop_area",
                "coord": {
                    "lat": "48.778867",
                    "lon": "2.340927"
                }
            },
            {
                "id": "stop_area:RTP:SA:3786123",
                "name": "DE GAULLE - GOUNOD - TABANOU",
                "type": "stop_area",
                "coord": {
                    "lat": "48.780179",
                    "lon": "2.340886"
                }
            }
        ],
        "publication_period" : {
            "begin": "2014-04-31T17:00:00Z",
            "end": null
        },
        "impacts": {
            "pagination": {
                "start_page": 1,
                "items_per_page": 20,
                "total_results": 2,
                "prev": null,
                "next": null,
                "first": {"href": "https://.../disruptions/1/impacts?start_page=1&item_per_page=20"},
                "last": {"href": "https://.../disruptions/1/impacts?start_page=1&item_per_page=20"}
            }
        },
        "properties": {
            "comment": [
                {
                    "property": {
                        "created_at": "2014-04-12T12:49:58Z",
                        "id": "10216aec-00ad-11e6-9f6d-0050568c8382",
                        "key": "special",
                        "self": {
                            "href": "https://.../properties/10216aec-00ad-11e6-9f6d-0050568c8382"
                        },
                        "type": "comment",
                        "updated_at": "2014-04-12T13:00:57Z"
                    },
                    "value": "This is a very nice comment !"
                }
            ]
        }
    },
    "meta": {}
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No disruption"
    }
}
```

- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'reference' is a required property"
    }
}
```
- Response 503 (application/json)
    * Body
```json
{
    "error": {
        "message": "An error occurred during transferring this disruption to Navitia. Please try again."
    }
}
```

- Response 500 (application/json)
    * Body
```json
{
    "error": {
        "message": "..."
    }
}
```

### You can pass the status in the request in order to update it

- Exemple of a request
```
    Method
            PUT
    Uri
            /disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea
    Headers
            X-Customer-Id: customer_id
            X-Coverage: coverage
            Authorization: token_navitia
            X-Contributors: contributor
    Body
        {
            "reference": "foo",
            "contributor": "contributor",
            "cause": {
                "id": "7ffab230-3d48-4eea-aa2c-22f8680230b6"
            },
            "status": "draft"
        }
```

### But you can't make a 'published' disruption going back to 'draft' status

- Response 409 CONFLICT (application/json)
    * Body
```json
{
    "error": {
        "message": "The current disruption is already published and cannot get back to the 'draft' status."
    }
}
```
## Delete a disruption [DELETE]

Archive one disruption.

### Headers ([here](#headers))

### Parameters

None

- Response 204 (__disruption archived__)

- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "..."
    }
}
```
# <a id="impacts" name="impacts"></a>List of Impacts [/disruptions/{disruption_id}/impacts]

## Retrieve impacts [GET]

Return all impacts of a disruption.

### Headers ([here](#headers))

### Parameters

| Name           | description                                      | required | default |
| -------------- | ------------------------------------------------ | -------- | ------- |
| start_page    | index of the first element returned (start at 1) | false    | 1       |
| items_per_page | number of items per page                         | false    | 20      |

- Response 200 (application/json)
    * Body
```json
{
    "impacts": [
        {
        "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ea",
        "self": {"href": "https://.../disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8657ea"},
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": "2014-04-31T16:55:18Z",
        "send_notifications": true,
        "notification_date": "2014-04-31T17:00:00Z",
        "severity": {
            "id": "3d1f42b2-e8df-11e3-8c3e-0008ca86c7ea",
            "wordings" : [{"key": "msg", "value": "Bonne nouvelle"}],
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z",
            "color": "#123456",
            "priority": null,
            "effect": null
        },
        "application_period_patterns": [],
        "application_periods": [
            {
                "begin": "2014-04-31T16:52:00Z",
                "end": "2014-05-22T02:15:00Z"
            }
        ],
        "messages":[
            {
                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ca",
                "created_at": "2014-04-31T16:52:18Z",
                "updated_at": "2014-04-31T16:55:18Z",
                "text": "ptit dej à la gare!!",
                "publication_date": ["2014-04-31T16:52:18Z"],
                "publication_period": null,
                "channel": {
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657da",
                    "name": "message court",
                    "content_type": "text/plain",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "max_size": 140,
                    "types": ["web", "mobile"]
                }
            },
            {
                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8257ea",
                "created_at": "2014-04-31T16:52:18Z",
                "updated_at": "2014-04-31T16:55:18Z",
                "text": "#Youpi\n**aujourd'hui c'est ptit dej en gare",
                "publication_period" : {
                    "begin":"2014-04-31T17:00:00Z",
                    "end":"2014-05-01T17:00:00Z"
                },
                "publication_date" : null,
                "channel": {
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008cb8657ea",
                    "name": "message long",
                    "content_type": "text/markdown",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "max_size": null,
                    "types": ["web", "mobile"]
                }
            }
        ],
        "objects": [
            {
                "id": "stop_area:RTP:SA:3786125",
                "name": "HENRI THIRARD - LEON JOUHAUX",
                "type": "stop_area",
                "coord": {
                    "lat": "48.778867",
                    "lon": "2.340927"
                }
            },
            {
                "id": "line:RTP:LI:378",
                "name": "DE GAULLE - GOUNOD - TABANOU",
                "type": "line",
                "code": 2,
                "color": "FFFFFF"
            }
        ],
        "disruption" : {"href": "https://.../disruptions/3d1f42b2-e8df-11e3-823e-0008ca8657ea"}
        }
    ],
    "meta": {
        "pagination": {
        "start_page": 1,
        "items_per_page": 3,
        "total_results": 6,
        "prev": null,
        "next": {"href": "https://.../disruptions/3d1f42b2-e8df-11e3-823e-0008ca8657ea/impacts?start_page=4&items_per_page=3"},
        "first": {"href": "https://.../disruptions/3d1f42b2-e8df-11e3-823e-0008ca8657ea/impacts?start_page=1&items_per_page=3"},
        "last": {"href": "https://.../disruptions/3d1f42b2-e8df-11e3-823e-0008ca8657ea/impacts?start_page=4&items_per_page=3"}
        }
    }
}
```

## Create an impact [POST]

Create a new impact on a disruption.

### Headers ([here](#headers))

### Request (application/json) -> __Delete comments before POST__

- Body
```javascript
{
    // REQUIRED.
    "severity": {
        // REQUIRED. regexp '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'.
        "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ea"
    },
    // OPTIONAL. array. uniqueItems.
    "application_periods": [
        {
            // REQUIRED. regexp '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$'.
            "begin": "2014-04-31T16:52:00Z",
            // REQUIRED. regexp '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$' | null.
            "end": "2014-05-22T02:15:00Z"
        }
    ],
    // OPTIONAL. array. uniqueItems.
    "messages": [
        {
            // REQUIRED. string.
            "text": "ptit dej à la gare!!",
            // REQUIRED. object.
            "channel": {
                // REQUIRED. regexp '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'.
                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca86c7ea"
            }
        },
        {
            // REQUIRED. string.
            "text": "#Youpi\n**aujourd'hui c'est ptit dej en gare",
            // REQUIRED. object.
            "channel": {
                // REQUIRED. regexp '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'.
                "id": "4d1f42b2-e8df-11e3-8c3e-0002ca8657ea"
            }
        }
    ],
    // OPTIONAL. array. uniqueItems.
    "objects": [
        {
            // REQUIRED. string. maxLength 250.
            "id": "stop_area:RTP:SA:3786125",
            // REQUIRED. enum ["network","stop_area","line","line_section","route","stop_point"].
            "type": "stop_area"
        },
        {
            // REQUIRED. string. maxLength 250.
            "id": "line_section:AME:3",
            // REQUIRED. enum ["network","stop_area","line","line_section","route","stop_point"].
            "type": "line_section"
            // REQUIRED if type "line_section". object.
            "line_section": {
                // REQUIRED. object.
                "line": {
                    // REQUIRED. string. maxLength 250.
                    "id":"line:AME:3",
                    // REQUIRED. enum ["line"].
                    "type":"line"
                },
                // REQUIRED. object.
                "start_point": {
                    // REQUIRED. string. maxLength 250.
                    "id":"stop_area:MTD:SA:154",
                    // REQUIRED. enum ["stop_area"].
                    "type":"stop_area"
                },
                // REQUIRED. object.
                "end_point": {
                    // REQUIRED. string. maxLength 250.
                    "id":"stop_area:MTD:SA:155",
                    // REQUIRED. enum ["stop_area"].
                    "type":"stop_area"
                },
                // OPTIONAL. array. uniqueItems.
                "routes":[
                    {
                        // REQUIRED. string. maxLength 250.
                        "id": "route:MTD:9",
                        // REQUIRED. enum ["route"].
                        "type": "route"
                    },
                    {
                        // REQUIRED. string. maxLength 250.
                        "id": "route:MTD:10",
                        // REQUIRED. enum ["route"].
                        "type": "route"
                    },
                    {
                        // REQUIRED. string. maxLength 250.
                        "id": "route:MTD:Nav24",
                        // REQUIRED. enum ["route"].
                        "type": "route"
                    }
                ],
                // OPTIONAL. array. uniqueItems.
                "via":[
                    {
                        // REQUIRED. string. maxLength 250.
                        "id":"stop_area:MTD:SA:154",
                        // REQUIRED. enum ["stop_area"].
                        "type":"stoparea"
                    }
                ]
            }
        }
    ],
    // OPTIONAL. boolean.
    "send_notifications": true,
    // OPTIONAL. regexp '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$' | null.
    "notification_date": "2014-04-31T17:00:00Z"
}
```
- Response 201 (application/json)
    * Body
```json
{
    "impact": {
        "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8617ea",
        "self": {"href": "https://.../disruptions/3d1f42b2-e8df-11e3-8c3e-0008ca8647ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8617ea"},
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": "2014-04-31T16:55:18Z",
        "send_notifications": true,
        "notification_date": "2014-04-31T17:00:00Z",
        "severity": {
            "id": "3d1f42b2-e8df-11e3-8c3e-0008ca861aea",
            "wordings" : [{"key": "msg", "value": "Bonne nouvelle"}],
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z",
            "color": "#123456",
            "priority": 1,
            "effect": null
        },
        "application_period_patterns": [],
        "application_periods": [
            {
                "begin": "2014-04-31T16:52:00Z",
                "end": "2014-05-22T02:15:00Z"
            }
        ],
        "messages": [
            {
                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8631ea",
                "created_at": "2014-04-31T16:52:18Z",
                "updated_at": "2014-04-31T16:55:18Z",
                "text": "ptit dej à la gare!!",
                "publication_date": ["2014-04-31T16:52:18Z"],
                "publication_period": null,
                "channel": {
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca86a7ea",
                    "name": "message court",
                    "content_type": "text/plain",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "max_size": 140,
                    "types": ["web", "mobile"]
                }
            },
            {
                "id": "3d1f42b2-e8df-11a3-8c3e-0008ca8617ea",
                "created_at": "2014-04-31T16:52:18Z",
                "updated_at": "2014-04-31T16:55:18Z",
                "text": "#Youpi\n**aujourd'hui c'est ptit dej en gare",
                "publication_period" : {
                    "begin":"2014-04-31T17:00:00Z",
                    "end":"2014-05-01T17:00:00Z"
                },
                "publication_date" : null,
                "channel": {
                    "id": "3d1f42b2-e8af-11e3-8c3e-0008ca8617ea",
                    "name": "message long",
                    "content_type": "text/markdown",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "max_size": null,
                    "types": ["web", "mobile"]
                }
            }
        ],
        "objects": [
            {
                "id": "stop_area:RTP:SA:3786125",
                "name": "HENRI THIRARD - LEON JOUHAUX",
                "type": "stop_area",
                "coord": {
                    "lat": "48.778867",
                    "lon": "2.340927"
                }
            },
            {
                "id": "line_section:AME:3",
                "type": "line_section",
                "line_section": {
                    "line": {
                        "id":"line:AME:3",
                        "type":"line"
                    },
                    "start_point": {
                        "id":"stop_area:MTD:SA:154",
                        "type":"stop_area"
                    },
                    "end_point": {
                        "id":"stop_area:MTD:SA:155",
                        "type":"stop_area"
                    },
                    "sens": null,
                    "routes":[
                       {
                           "id": "route:MTD:9",
                           "name": "corquilleroy",
                           "type": "route"
                       },
                       {
                           "id": "route:MTD:10",
                           "name": "corquilleroy",
                           "type": "route"
                       },
                       {
                           "id": "route:MTD:Nav24",
                           "name": "pannes",
                           "type": "route"
                       }
                    ],
                    "via":[
                        {
                        "id":"stop_area:MTD:SA:154",
                        "type":"stoparea"
                        }
                    ]
                }
            }
        ],
        "disruption" : {"href": "https://.../disruptions/3d1f42b2-e8df-11e3-1c3e-0008ca8617ea"}
    },
    "meta": {}
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'severity' is a required property"
    }
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "..."
    }
}
```
- Response 503 (application/json)
    * Body
```json
{
    "error": {
        "message": "An error occurred during transferring this disruption to Navitia. Please try again"
    }
}
```
- Response 500 (application/json)
    * Body
```json
{
    "error": {
        "message": "..."
    }
}
```

# Impact [/disruptions/{disruption_id}/impacts/{id}]

## Retrieve an impact [GET]

Get an impact by id.

### Headers ([here](#headers))

### Parameters
none

- Response 200 (application/json)
    * Body
```json
{
    "impact": {
        "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8617ea",
        "self": {"href": "https://.../disruptions/3d1f42b2-e8df-11e3-8c3e-0008ca8647ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8617ea"},
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": "2014-04-31T16:55:18Z",
        "send_notifications": true,
        "notification_date": "2014-04-31T17:00:00Z",
        "severity": {
            "id": "3d1f42b2-e8df-11e3-8c3e-0008ca861aea",
            "wordings" : [{"key": "msg", "value": "Bonne nouvelle"}],
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z",
            "color": "#123456",
            "priority": 1,
            "effect": null
        },
        "application_period_patterns": [],
        "application_periods": [
            {
                "begin": "2014-04-31T16:52:00Z",
                "end": "2014-05-22T02:15:00Z"
            }
        ],
        "messages": [
            {
                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8631ea",
                "created_at": "2014-04-31T16:52:18Z",
                "updated_at": "2014-04-31T16:55:18Z",
                "text": "ptit dej à la gare!!",
                "publication_date": ["2014-04-31T16:52:18Z"],
                "publication_period": null,
                "channel": {
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca86a7ea",
                    "name": "message court",
                    "content_type": "text/plain",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "max_size": 140,
                    "types": ["web", "mobile"]
                }
            },
            {
                "id": "3d1f42b2-e8df-11a3-8c3e-0008ca8617ea",
                "created_at": "2014-04-31T16:52:18Z",
                "updated_at": "2014-04-31T16:55:18Z",
                "text": "#Youpi\n**aujourd'hui c'est ptit dej en gare",
                "publication_period" : {
                    "begin":"2014-04-31T17:00:00Z",
                    "end":"2014-05-01T17:00:00Z"
                },
                "publication_date" : null,
                "channel": {
                    "id": "3d1f42b2-e8af-11e3-8c3e-0008ca8617ea",
                    "name": "message long",
                    "content_type": "text/markdown",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "max_size": null,
                    "types": ["web", "mobile"]
                }
            }
        ],
        "objects": [
            {
                "id": "stop_area:RTP:SA:3786125",
                "name": "HENRI THIRARD - LEON JOUHAUX",
                "type": "stop_area",
                "coord": {
                    "lat": "48.778867",
                    "lon": "2.340927"
                }
            },
            {
                "id": "line:RTP:LI:378",
                "name": "DE GAULLE - GOUNOD - TABANOU",
                "type": "line",
                "code": 2,
                "color": "FFFFFF"
            }
        ],
        "disruption" : {"href": "https://.../disruptions/3d1f42b2-e8df-11e3-1c3e-0008ca8617ea"}
    },
    "meta": {}
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No disruption or impact"
    }
}
```
## Update an impact [PUT]

### Headers ([here](#headers))

### Request (see POST part for required elements)

### Exemple of a request
```
    * Url
        /impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8617ea

    * Headers

            Content-Type: application/json
            Authorization: navitia_token
            X-Customer-Id: customer_id
            X-Contributors: contributor_id
            X-Coverage: navitia_coverage

    * Body
            {
                "send_notifications": false,
                "notification_date": "2014-04-31T17:00:00Z",
                "severity": {
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca861aea"
                },
                "messages": [
                        {
                            "channel": {
                            "id": "3d1f42b2-e8df-11e3-8c3e-0002ca8657ea",
                            },
                            "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ca",
                            "text": "Messsage modifié",
                        },
                        {
                            "channel": {
                                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca86c7ea",
                            },
                            "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8257ea",
                            "text": "Message 2",
                        }
                ],
            }
```

- Response 200 (application/json)
    * Body
```json
{
    "impact": {
        "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8617ea",
        "self": {"href": "https://.../disruptions/3d1f42b2-e8df-11e3-8c3e-0008ca8647ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8617ea"},
        "created_at": "2014-04-31T16:52:18Z",
        "updated_at": "2014-04-31T17:00:01Z",
        "send_notifications": true,
        "notification_date": "2014-04-31T17:00:00Z",
        "severity": {
            "id": "3d1f42b2-e8df-11e3-8c3e-0008ca861aea",
            "wordings" : [{"key": "msg", "value": "Bonne nouvelle"}],
            "created_at": "2014-04-31T16:52:18Z",
            "updated_at": "2014-04-31T16:55:18Z",
            "color": "#123456",
            "effect": null,
            "priority": 1
        },
        "messages": [
                {
                    "channel": {
                    "content_type": "text/plain",
                    "created_at": "2014-04-31T16:52:18Z",
                    "id": "3d1f42b2-e8df-11e3-8c3e-0002ca8657ea",
                    "max_size": 140,
                    "name": "message court",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "types": ["web", "mobile"]
                    },
                    "created_at": "2014-04-31T16:52:18Z",
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ca",
                    "text": "Messsage modifié",
                    "updated_at": "2014-04-31T17:00:00Z"
                },
                {
                    "channel": {
                        "content_type": "text/markdown",
                        "created_at": "2014-04-31T16:52:18Z",
                        "id": "3d1f42b2-e8df-11e3-8c3e-0008ca86c7ea",
                        "max_size": null,
                        "name": "message long",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "types": ["web", "mobile"]
                    },
                    "created_at": "2014-04-31T16:52:18Z",
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8257ea",
                    "text": "Message 2",
                    "updated_at": "2014-04-31T16:55:18Z"
                }
        ],
        "application_period_patterns": [
            {
                "end_date": "2015-02-06",
                "start_date": "2015-02-01",
                "time_slots": [
                    {
                        "begin": "07:45",
                        "end": "09:30"
                    },
                    {
                        "begin": "17:30",
                        "end": "20:30"
                    }
                    ],
                "weekly_pattern": "1111100"
            }
        ],
        "application_periods": [
            {
                "begin": "2015-02-05T17:30:00Z",
                "end": "2015-02-05T20:30:00Z"
            },
            {
                "begin": "2015-02-05T07:45:00Z",
                "end": "2015-02-05T09:30:00Z"
            },
            {
                "begin": "2015-02-04T17:30:00Z",
                "end": "2015-02-04T20:30:00Z"
            },
            {
                "begin": "2015-02-04T07:45:00Z",
                "end": "2015-02-04T09:30:00Z"
            },
            {
                "begin": "2015-02-03T17:30:00Z",
                "end": "2015-02-03T20:30:00Z"
            },
            {
                "begin": "2015-02-03T07:45:00Z",
                "end": "2015-02-03T09:30:00Z"
            },
            {
                "begin": "2015-02-02T17:30:00Z",
                "end": "2015-02-02T20:30:00Z"
            },
            {
                "begin": "2015-02-02T07:45:00Z",
                "end": "2015-02-02T09:30:00Z"
            }
        ],
        "objects": [
            {
                "id": "network:RTP:3786125",
                "name": "RER A",
                "type": "network",
            },
            {
                "id": "network:RTP:378",
                "name": "RER B",
                "type": "network",
            },
            {
                "id": "line:AME:3",
                "type": "line_section",
                "line_section": {
                    "line": {
                        "id":"line:AME:3",
                        "type":"line"
                    },
                    "start_point": {
                        "id":"stop_area:MTD:SA:154",
                        "type":"stop_area"
                    },
                    "end_point": {
                        "id":"stop_area:MTD:SA:155",
                        "type":"stop_area"
                    },
                    "sens": null,
                    "routes":[
                       {
                           "id": "route:MTD:9",
                           "name": "corquilleroy",
                           "type": "route"
                       },
                       {
                           "id": "route:MTD:10",
                           "name": "corquilleroy",
                           "type": "route"
                       },
                       {
                           "id": "route:MTD:Nav24",
                           "name": "pannes",
                           "type": "route"
                       }
                    ],
                    "via":[
                        {
                        "id":"stop_area:MTD:SA:154",
                        "type":"stoparea"
                        }
                    ]
                }
            }
        ],
        "disruption" : {"href": "https://.../disruptions/3d1f42b2-e8df-11e3-1c3e-0008ca8617ea"}
    },
    "meta": {}
}
```
- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No impact"
    }
}
```
- Response 400 (application/json)
    * Body
```json
{
    "error": {
        "message": "'severity' is a required property"
    }
}
```
- Response 503 (application/json)
    * Body
```json
{
    "error": {
        "message": "An error occurred during transferring this impact to Navitia. Please try again."
    }
}
```
- Response 500 (application/json)
    * Body
```json
{
    "error": {
        "message": "..."
    }
}
```
## Delete an impact [DELETE]

Archive one impact.

### Headers ([here](#headers))

### Parameters
None

- Response 204 (impact archived)

- Response 404 (application/json)
    * Body
```json
{
    "error": {
        "message": "No impact"
    }
}
```
- Response 503 (application/json)
    * Body
```json
{
    "error": {
        "message": "An error occurred during transferring this impact to Navitia. Please try again."
    }
}
```
- Response 500 (application/json)
    * Body
```json
{
    "error": {
        "message": "An error occurred during deletion. Please try again."
    }
}
```
# List of Impacts by object type [/impacts]

## Retrieve impacts [GET]

Return all impacts by ptobject (search purpose).

### Headers ([here](#headers))

### Parameters

| Name                 | description                                                                                | required | default                     |
| -------------------- | ------------------------------------------------------------------------------------------ | -------- | --------------------------- |
| pt_object_type       | filter by ptobject, possible value are: network, stop_area, line, line_section, stop_point  | false if uri[]   |                             |
| uri[]                | filtre by ptobject.uri                                                                     | false if pt_object_type    |                             |
| start_date           | filtre by application period :star date                                                    | false    | Now():00:00:00Z             |
| end_date             | filtre by application period :end date                                                     | false    | Now():23:59:59Z             |

- Response 200 (application/json)
    * Body
```json
{

    "meta": {
        "pagination": {
                "first": {
                    "href": "https://.../impacts?start_page=1&items_per_page=20"
                },
                "items_on_page": "1",
                "items_per_page": "20",
                "last": {
                    "href": "https://.../impacts?start_page=1&items_per_page=20"
                },
                "next": {
                    "href": null
                },
                "prev": {
                    "href": null
                },
                "start_page": "1",
                "total_result": "1"
        }
    },
    "objects": [
        {
            "id": "RER:A",
            "impacts": [
                {
                    "application_period_patterns": [],
                    "application_periods": [
                            {
                                "begin": "2014-03-29T16:52:00Z",
                                "end": "2014-05-22T02:15:00Z"
                            }
                    ],
                    "send_notifications": true,
                    "notification_date": "2014-04-31T17:00:00Z",
                    "created_at": "2014-04-31T16:52:18Z",
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ea",
                    "messages": [
                            {
                                "channel": {
                                "content_type": "text/plain",
                                "created_at": "2014-04-31T16:52:18Z",
                                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657da",
                                "max_size": 140,
                                "name": "message court",
                                "updated_at": "2014-04-31T16:55:18Z",
                                "types": ["web", "mobile"]
                                },
                                "created_at": "2014-04-31T16:52:18Z",
                                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ca",
                                "publication_date": [
                                    "2014-04-31T16:52:18Z"
                                    ],
                                "publication_period": null,
                                "text": "ptit dej la gare!!",
                                "updated_at": "2014-04-31T16:55:18Z"
                            },
                            {
                                "channel": {
                                    "content_type": "text/markdown",
                                    "created_at": "2014-04-31T16:52:18Z",
                                    "id": "3d1f42b2-e8df-11e3-8c3e-0008cb8657ea",
                                    "max_size": null,
                                    "name": "message long",
                                    "updated_at": "2014-04-31T16:55:18Z",
                                    "types": ["sms", "notification"]
                                },
                                "created_at": "2014-04-31T16:52:18Z",
                                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8257ea",
                                "publication_date": null,
                                "publication_period": {
                                    "begin": "2014-04-31T17:00:00Z",
                                    "end": "2014-05-01T17:00:00Z"
                                },
                                "text": "est ptit dej en gare",
                                "updated_at": "2014-04-31T16:55:18Z"
                            }
                    ],
                    "objects": [
                        {
                            "id": "RER:A",
                            "name": "RER:A",
                            "type": "network"
                        }
                    ],
                    "self": {
                        "href": "https://.../disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8657ea"
                    },
                    "severity": {
                        "color": "#123456",
                        "created_at": "2014-04-31T16:52:18Z",
                        "effect": "none",
                        "id": "3d1f42b2-e8df-11e3-8c3e-0008ca86c7ea",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "wordings" : [{"key": "msg", "value": "Bonne nouvelle"}]
                    },
                    "updated_at": "2014-04-31T16:55:18Z"
                    }
            ],
            "name": "RER:A",
            "type": "network"
        }
    ]
}
```
# <a id="traffic" name="traffic"></a>Traffic reports [/traffic_reports] [GET]

This service provides the state of public transport traffic.

## Objects

Disruptions is an array of some impact objects.

Traffic_reports is an array of some traffic_report objects. One traffic_report object is a complex object, made of a network, an array of lines and an array of stop_areas.

A typical traffic_report object will contain:

- 1 **network** which is the grouping object

    it can contain links to its disruptions. These disruptions are globals and might not be applied on lines or stop_areas.

- 0..n **lines**
    each line contains at least a link to its disruptions

- 0..n **line_sections**
    each line_section contains at least a link to its disruptions, start_point, stop_point, the line, routes, meta and via if exist

- 0..n **stop_areas**
    each stop_area contains at least a link to its disruptions

- 0..n **stop_points**
    each stop_point contains at least a link to its disruptions

It means that if a stop_area is used by many networks, it will appear many times.

## Headers ([here](#headers))

## Parameters

| Name                 | description                                                                    | required | default                 |
| -------------------- | ------------------------------------------------------------------------------ | -------- | ----------------------- |
| current_time         | parameter for settings the use by this request, mostly for debugging purpose   | false    | NOW                     |

- Response 200 (application/json)
    * Body
```json
{
    "disruptions": [
        {
            "application_periods": [
                {
                    "begin": "2015-12-08T00:00:00Z",
                    "end": "2015-12-11T22:00:00Z"
                }
            ],
            "cause": "Travaux",
            "disruption_id": "8cc6a5ec-9d90-11e5-b08a-ecf4bb4460c7",
            "id": "a3ca6a6e-9dca-11e5-b08a-ecf4bb4460c7",
            "messages": [
                {
                    "channel": {
                        "content_type": "text/html",
                        "id": "ffe4308f-7e4b-f211-8e74-4ed3e055a969",
                        "max_size": 1000,
                        "name": "email",
                        "types": [
                            "email"
                        ]
                    },
                    "text": "<p>C'est entièrement gainé de plomb il n'y a plus rien à craindre.</p> <a href=\"http://navitia.io\">Pour navitia, cliquez ici</a>"
                },
                {
                    "channel": {
                        "content_type": "text/plain",
                        "id": "7a831bc8-8c5f-11e5-b2c5-ecf4bb4460c7",
                        "max_size": 255,
                        "name": "Titre (OV1)",
                        "types": [
                            "web"
                        ]
                    },
                    "text": "Je suis pour toi OV1 "
                },
                {
                    "channel": {
                        "content_type": "text/plain",
                        "id": "90b61dbd-d5a0-3df4-c426-79f8893bbc60",
                        "max_size": 160,
                        "name": "sms",
                        "types": [
                            "sms"
                        ]
                    },
                    "text": "T'as de beaux yeux tu sais"
                }
            ],
            "severity": {
                "color": "#FF4455",
                "effect": "no_service",
                "id": "69fb2a67-4e61-ff72-7ed6-65529f2502fc",
                "name": "Blocking",
                "priority": 0
            },
            "status": "active"
        },
        {
            "application_periods": [
                {
                    "begin": "2015-12-08T00:00:00Z",
                    "end": "2015-12-10T02:00:00Z"
                }
            ],
            "cause": "Travaux",
            "disruption_id": "8cc6a5ec-9d90-11e5-b08a-ecf4bb4460c7",
            "id": "8cc97e3e-9d90-11e5-b08a-ecf4bb4460c7",
            "messages": [
                {
                    "channel": {
                        "content_type": "text/plain",
                        "id": "7a831bc8-8c5f-11e5-b2c5-ecf4bb4460c7",
                        "max_size": 255,
                        "name": "Titre (OV1)",
                        "types": [
                            "web"
                        ]
                    },
                    "text": "That's a message OV1"
                },
                {
                    "channel": {
                        "content_type": "text/plain",
                        "id": "90b61dbd-d5a0-3df4-c426-79f8893bbc60",
                        "max_size": 160,
                        "name": "sms",
                        "types": [
                            "sms"
                        ]
                    },
                    "text": "That's a message SMS"
                },
                {
                    "channel": {
                        "content_type": "text/html",
                        "id": "ffe4308f-7e4b-f211-8e74-4ed3e055a969",
                        "max_size": 1000,
                        "name": "email",
                        "types": [
                            "email"
                        ]
                    },
                    "text": "That's a message mail"
                }
            ],
            "severity": {
                "color": "#FF4455",
                "effect": "no_service",
                "id": "69fb2a67-4e61-ff72-7ed6-65529f2502fc",
                "name": "Blocking",
                "priority": 0
            },
            "status": "past"
        },
        {
            "application_periods": [
                {
                    "begin": "2015-09-28T23:30:00Z",
                    "end": "2016-01-01T02:00:00Z"
                }
            ],
            "cause": "Trafic",
            "disruption_id": "0614bf52-8c60-11e5-b2c5-ecf4bb4460c7",
            "id": "0615615a-8c60-11e5-b2c5-ecf4bb4460c7",
            "messages": [
                {
                    "channel": {
                        "content_type": "text/plain",
                        "id": "7a831bc8-8c5f-11e5-b2c5-ecf4bb4460c7",
                        "max_size": 255,
                        "name": "Titre (OV1)",
                        "types": [
                            "web"
                        ]
                    },
                    "text": "Des travaux sur les voies interrompent la circulation. <a href=\"http://navitia.io\">Pour navitia, cliquez ici</a>    Pendant les travaux, covoiturez !"
                }
            ],
            "severity": {
                "color": "#FF4455",
                "effect": "no_service",
                "id": "69fb2a67-4e61-ff72-7ed6-65529f2502fc",
                "name": "Blocking",
                "priority": 0
            },
            "status": "active"
        }
    ],
    "traffic_reports": [
        {
            "lines": [
                {
                    "code": "D",
                    "id": "line:DUA:123456789",
                    "links": [
                        {
                            "id": "0615615a-8c60-11e5-b2c5-ecf4bb4460c7",
                            "internal": true,
                            "rel": "disruptions",
                            "template": false,
                            "type": "disruption"
                        }
                    ],
                    "name": "Creil - Saturne / Mars / Pluton"
                }
            ],
            "line_sections": [
                        {
                            "id": "7ffab234-3d49-4eea-aa2c-22f8680230b6",
                            "line_section": {
                                "end_point": {
                                    "id": "stop_area:DUA:SA:8775810",
                                    "type": "stop_area"
                                },
                                "line": {
                                    "id": "line:DUA:810801041",
                                    "name": "Cergy Le Haut / Poissy / St-Germain-en-Laye - Marne-la-Vall\u00e9e Chessy Disneyland / Boissy-St-L\u00e9ger",
                                    "type": "line",
                                    "code": "A"
                                },
                                "start_point": {
                                    "id": "stop_area:DUA:SA:8738221",
                                    "type": "stop_area"
                                },
                                "routes":[
                                   {
                                       "id": "route:MTD:9",
                                       "type": "route"
                                   },
                                   {
                                       "id": "route:MTD:10",
                                       "type": "route"
                                   },
                                   {
                                       "id": "route:MTD:Nav24",
                                       "type": "route"
                                   }
                                ],
                                "via":[
                                    {
                                    "id":"stop_area:MTD:SA:154",
                                    "type":"stoparea"
                                    }
                                ],
                                "metas": [
                                    {
                                        "key": "direction",
                                        "value": "5"
                                    },
                                    {
                                        "key": "direction",
                                        "value": "4"
                                    }
                                ]
                            },
                            "links": [
                                {
                                    "id": "0615615a-8c60-11e5-b2c5-ecf4bb4460c7",
                                    "internal": true,
                                    "rel": "disruptions",
                                    "template": false,
                                    "type": "disruption"
                                }
                            ],
                            "type": "line_section"
                        }
                    ],
            "network": {
                "id": "network:DUA777",
                "name": "RESEAU D"
            }
        },
        {
            "network": {
                "id": "network:DUA999",
                "links": [
                    {
                        "id": "a3ca6a6e-9dca-11e5-b08a-ecf4bb4460c7",
                        "internal": true,
                        "rel": "disruptions",
                        "template": false,
                        "type": "disruption"
                    },
                    {
                        "id": "8cc97e3e-9d90-11e5-b08a-ecf4bb4460c7",
                        "internal": true,
                        "rel": "disruptions",
                        "template": false,
                        "type": "disruption"
                    }
                ],
                "name": "RESEAU A"
            }
        }
    ]
}
```
