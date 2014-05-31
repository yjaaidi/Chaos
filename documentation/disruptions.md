FORMAT: 1A
HOST: https://chaos.apiary-mock.com

#Chaos
It's an api for blabla


# Root [/]
##Retrieve Api [GET]

- response 200 (application/json)
    * Body

            {
                "disruptions": {"href": "https://chaos.apiary-mock.com/disruptions"},
                "disruption": {"href": "https://chaos.apiary-mock.com/disruptions/{id}", "templated": true},
                "severities": {"href": "https://chaos.apiary-mock.com/severities"},
                "causes": {"href": "https://chaos.apiary-mock.com/causes"}
            }


# List of disruptions [/disruptions]

##Retrieve disruptions [GET]
Return all visible disruptions.
##Parameters

| Name           | description                                      | required | default |
| -------------- | ------------------------------------------------ | -------- | ------- |
| start_index    | index of the first element returned (start at 1) | false    | 1       |
| items_per_page | number of items per page                         | false    | 20      |

@TODO: search and sort


- response 200 (application/json)

    * Body

            {
                "disruptions": [
                    {
                        "id": 1,
                        "self": {"href": "https://chaos.apiary-mock.com/disruptions/1"},
                        "reference": "RER B en panne",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "note": "blablbla",
                        "state": "published",
                        "contributor": "shortterm.tn",
                        "cause": {
                            "id": 23,
                            "wording": "Condition météo"
                        },
                        "tags": ["rer", "meteo", "probleme"],
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
                        "impacts": {
                            "pagination": {
                                "start_index": 0,
                                "items_per_page": 20,
                                "total_results": 3,
                                "prev": null,
                                "next": {"href": "https://chaos.apiary-mock.com/disruptions/1/impacts?start_index=1&item_per_page=20"},
                                "first": {"href": "https://chaos.apiary-mock.com/disruptions/1/impacts?start_index=1&item_per_page=20"},
                                "last": {"href": "https://chaos.apiary-mock.com/disruptions/1/impacts?start_index=1&item_per_page=20}"
                            }
                        }
                    },
                    {
                        "id": 4,
                        "self": {"href": "https://chaos.apiary-mock.com/disruptions/4"},
                        "reference": "RER A en panne",
                        "created_at": "2014-05-31T16:52:18Z",
                        "updated_at": null,
                        "note": null,
                        "state": "published",
                        "contributor": "shortterm.tn",
                        "cause": {
                            "id": 2,
                            "wording": "train cassé"
                        },
                        "tags": ["rer", "probleme"],
                        "localization": [],
                        "impacts": {
                            "pagination": {
                                "start_index": 0,
                                "items_per_page": 20,
                                "total_results": 5,
                                "prev": null,
                                "next": {"href": "https://chaos.apiary-mock.com/disruptions/4/impacts?start_index=1&item_per_page=20"},
                                "first": {"href": "https://chaos.apiary-mock.com/disruptions/4/impacts?start_index=1&item_per_page=20"},
                                "last": {"href": "https://chaos.apiary-mock.com/disruptions/4/impacts?start_index=1&item_per_page=20"}
                            }
                        }
                    },
                    {
                        "id": 2,
                        "self": {"href": "https://chaos.apiary-mock.com/disruptions/2"},
                        "reference": "Chatelet fermé",
                        "created_at": "2014-05-17T16:52:18Z",
                        "update_at": "2014-05-31T06:55:18Z",
                        "note": "retour probable d'ici 5H",
                        "state": "published",
                        "contributor": "shortterm.tn",
                        "cause": {
                            "id": 4,
                            "wording": "émeute"
                        },
                        "tags": ["rer", "metro", "probleme"],
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
                        "impacts": {
                            "pagination": {
                                "start_index": 0,
                                "items_per_page": 20,
                                "total_results": 25,
                                "prev": null,
                                "next": {"href": "https://chaos.apiary-mock.com/disruptions/2/impacts?start_index=1&item_per_page=20"},
                                "first": {"href": "https://chaos.apiary-mock.com/disruptions/2/impacts?start_index=1&item_per_page=20"},
                                "last": {"href": "https://chaos.apiary-mock.com/disruptions/2/impacts?start_index=21&item_per_page=20"}
                            }
                        }
                    }

                ],
                "meta": {
                    "pagination": {
                        "start_index": 1,
                        "items_per_page": 3,
                        "total_results": 6,
                        "prev": null,
                        "next": {"href": "https://chaos.apiary-mock.com/disruptions/?start_index=4&item_per_page=3"},
                        "first": {"href": "https://chaos.apiary-mock.com/disruptions/?start_index=1&item_per_page=3"},
                        "last": {"href": "https://chaos.apiary-mock.com/disruptions/?start_index=4&item_per_page=3"}
                    }
                }

            }

##Create a disruption [POST]

###Parameters

Create one valid disruption without impacts

**POST** /disruptions

- Request (application/json)

    * Body

            {
                "reference": "foo",
                "note": null,
                "state": "published",
                "contributor": "shortterm.tn",
                "cause": {
                       "id": 23
                }
                "tags": ["rer", "meteo", "probleme"],
                "localization": [
                    {
                        "id": "stop_area:RTP:SA:3786125",
                        "type": "stop_area"
                    },
                    {
                        "id": "stop_area:RTP:SA:3786123",
                        "type": "stop_area" //needed?
                    }
                ]
            }



- response 201 (application/json)

    * Body

            {
                "disruption":{
                    "id": 1,
                    "self": {"href": "https://chaos.apiary-mock.com/disruptions/1"},
                    "reference": "foo",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null,
                    "note": null,
                    "state": "published",
                    "contributor": "shortterm.tn",
                    "cause": {
                        "id": 23,
                        "wording": "Condition météo"
                    },
                    "tags": ["rer", "meteo", "probleme"],
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
                    "impacts": {
                        "pagination": {
                            "start_index": 0,
                            "items_per_page": 20,
                            "total_results": 0,
                            "prev": null,
                            "next": null,
                            "first": "null",
                            "last": "null"
                        }
                    }
                },
                "meta": {}
            }

# Disruptions [/disruptions/{id}]
##Retrieve one disruption [GET]

##Parameters

Retrieve one existing disruption:

- response 200 (application/json)

    * Body

            {
                "disruption": {
                    "id": 1,
                    "self": {"href": "https://chaos.apiary-mock.com/disruptions/1"},
                    "reference": "RER B en panne",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "note": "blablbla",
                    "state": "published",
                    "contributor": "shortterm.tn",
                    "cause": {
                        "id": 23,
                        "wording": "Condition météo"
                    },
                    "tags": ["rer", "meteo", "probleme"],
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
                    "impacts": {
                        "pagination": {
                            "start_index": 1,
                            "items_per_page": 20,
                            "total_results": 3,
                            "prev": null,
                            "next": {"href": "https://chaos.apiary-mock.com/disruptions/1/impacts?start_index=1&item_per_page=20"},
                            "first": {"href": "https://chaos.apiary-mock.com/disruptions/1/impacts?start_index=1&item_per_page=20"},
                            "last": {"href": "https://chaos.apiary-mock.com/disruptions/1/impacts?start_index=1&item_per_page=20"}
                        }
                    }
                },
                "meta": {}
            }


- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No disruption"
                },
                "meta": {}
            }


##Update a disruption [PUT]

###Parameters


- Request

    * Headers

            Content-Type: application/json

    * Body

            {
                "reference": "foo",
                "note": null,
                "state": "published",
                "contributor": "shortterm.tn",
                "cause": {
                    "id": 23
                }
                "tags": ["rer", "meteo", "probleme"],
                "localization": [
                    {
                        "id": "stop_area:RTP:SA:3786125",
                        "type": "stop_area"
                    },
                    {
                        "id": "stop_area:RTP:SA:3786123",
                        "type": "stop_area"
                    }
                ]
            }


- Response 200 (application/json)

    * Body

            {
                "disruption":{
                    "id": 4,
                    "self": {"href": "https://chaos.apiary-mock.com/disruptions/4"},
                    "reference": "foo",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "note": null,
                    "state": "published",
                    "contributor": "shortterm.tn",
                    "cause": {
                        "id": 23,
                        "wording": "Condition météo"
                    },
                    "tags": ["rer", "meteo", "probleme"],
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
                    "impacts": {
                        "pagination": {
                            "start_index": 0,
                            "items_per_page": 20,
                            "total_results": 0,
                            "prev": null,
                            "next": null,
                            "first": null,
                            "last": null
                        }
                    }
                },
                "meta": {}
            }

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No disruption"
                },
                "meta": {}
            }

##Delete a disruption [DELETE]
Delete one disruption.
###Parameters


- Response 204

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No disruption"
                },
                "meta": {}
            }


# List of Impacts [/disruptions/1/impacts]

##Retrieve impacts [GET]
Return all impacts of a disruption.
###Parameters

| Name           | description                                      | required | default |
| -------------- | ------------------------------------------------ | -------- | ------- |
| start_index    | index of the first element returned (start at 1) | false    | 1       |
| items_per_page | number of items per page                         | false    | 20      |

@TODO: search and sort


- response 200 (application/json)

    * Body

            {
                "impacts": [
                    {
                        "id": 1,
                        "self": {"href": "https://chaos.apiary-mock.com/disruptions/3/impacts/1"},
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "severity": {
                            "id": 2,
                            "wording": "Bonne nouvelle",
                            "is_blocking": false
                        },
                        "application_periods": [
                            {
                                "begin": "2014-04-31T16:52:00Z",
                                "end": "2014-05-22T02:15:00Z"
                            }
                        ],
                        "messages": [
                            {
                                "id": 1,
                                "created_at": "2014-04-31T16:52:18Z",
                                "updated_at": "2014-04-31T16:55:18Z",
                                "text": "ptit dej à la gare!!",
                                "publication_date": ["2014-04-31T16:52:18Z"],
                                "publication_period": null,
                                "channel": {
                                    "id": 3,
                                    "name": "message court",
                                    "content_type": "text/plain",
                                    "max_size": 140
                                }
                            },
                            {
                                "id": 2,
                                "created_at": "2014-04-31T16:52:18Z",
                                "updated_at": "2014-04-31T16:55:18Z",
                                "text": "#Youpi\n**aujourd'hui c'est ptit dej en gare",
                                "publication_period" : {
                                    "begin":"2014-04-31T17:00:00Z",
                                    "end":"2014-05-01T17:00:00Z"
                                },
                                "publication_date" : null,
                                "channel": {
                                    "id": 2,
                                    "name": "message long",
                                    "content_type": "text/markdown",
                                    "max_size": null
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
                        "disruption" : {"href": "https://chaos.apiary-mock.com/disruptions/3"}
                    }
                ],
                "meta": {
                    "pagination": {
                        "start_index": 1,
                        "items_per_page": 3,
                        "total_results": 6,
                        "prev": null,
                        "next": {"href": "https://chaos.apiary-mock.com/disruptions?start_index=4&items_per_page=3"},
                        "first": {"href": "https://chaos.apiary-mock.com/disruptions?start_index=1&items_per_page=3"},
                        "last": {"href": "https://chaos.apiary-mock.com/disruptions?start_index=4&items_per_page=3"}
                    }
                }
            }



##Create a impact [POST]
Create a new impact.
###Parameters

- request
    + headers

            Content-Type: application/json

    + body

            {
                "severity": {
                    "id": 2
                },
                "application_periods": [
                    {
                        "begin": "2014-04-31T16:52:00Z",
                        "end": "2014-05-22T02:15:00Z"
                    }
                ],
                "messages": [
                    {
                        "text": "ptit dej à la gare!!",
                        "publication_date": ["2014-04-31T16:52:18Z"],
                        "publication_period": null,
                        "channel": {
                            "id": 3
                        }
                    },
                    {
                        "text": "#Youpi\n**aujourd'hui c'est ptit dej en gare",
                        "publication_period" : {
                            "begin":"2014-04-31T17:00:00Z",
                            "end":"2014-05-01T17:00:00Z"
                        },
                        "publication_date" : null,
                        "channel": {
                            "id": 2
                        }
                    }
                ],
                "objects": [
                    {
                        "id": "stop_area:RTP:SA:3786125",
                        "type": "stop_area"
                    },
                    {
                        "id": "line:RTP:LI:378",
                        "type": "line"
                    }
                ]
            }

- response 200 (application/json)

    * Body

            {
                "impact": {
                    "id": 1,
                    "self": {"href": "https://chaos.apiary-mock.com/disruptions/3/impacts/1"},
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "severity": {
                        "id": 2,
                        "wording": "Bonne nouvelle",
                        "is_blocking": false
                    },
                    "application_periods": [
                        {
                            "begin": "2014-04-31T16:52:00Z",
                            "end": "2014-05-22T02:15:00Z"
                        }
                    ],
                    "messages": [
                        {
                            "id": 1,
                            "created_at": "2014-04-31T16:52:18Z",
                            "updated_at": "2014-04-31T16:55:18Z",
                            "text": "ptit dej à la gare!!",
                            "publication_date": ["2014-04-31T16:52:18Z"],
                            "publication_period": null,
                            "channel": {
                                "id": 3,
                                "name": "message court",
                                "content_type": "text/plain",
                                "max_size": 140
                            }
                        },
                        {
                            "id": 2,
                            "created_at": "2014-04-31T16:52:18Z",
                            "updated_at": "2014-04-31T16:55:18Z",
                            "text": "#Youpi\n**aujourd'hui c'est ptit dej en gare",
                            "publication_period" : {
                                "begin":"2014-04-31T17:00:00Z",
                                "end":"2014-05-01T17:00:00Z"
                            },
                            "publication_date" : null,
                            "channel": {
                                "id": 2,
                                "name": "message long",
                                "content_type": "text/markdown",
                                "max_size": null
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
                    "disruption" : {"href": "https://chaos.apiary-mock.com/disruptions/3"}
                }
            }



