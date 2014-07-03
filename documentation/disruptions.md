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
                "causes": {"href": "https://chaos.apiary-mock.com/causes"},
                "channels": {"href": "https://chaos.apiary-mock.com/channels"}
            }


# List of disruptions [/disruptions]

##Retrieve disruptions [GET]
Return all visible disruptions.
##Parameters

| Name                 | description                                                                    | required | default                 |
| -------------------- | ------------------------------------------------------------------------------ | -------- | ----------------------- |
| start_index          | index of the first element returned (start at 1)                               | false    | 1                       |
| items_per_page       | number of items per page                                                       | false    | 20                      |
| publication_status[] | filter by publication_status, possible value are: past, ongoing, coming        | false    | [past, ongoing, coming] |
| current_time         | parameter for settings the use by this request, mostly for debugging purpose   | false    | NOW                     |

@TODO: search and sort


- response 200 (application/json)

    * Body

            {
                "disruptions": [
                    {
                        "id": "d30502d2-e8de-11e3-8c3e-0008ca8657ea",
                        "self": {"href": "https://chaos.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ea"},
                        "reference": "RER B en panne",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "note": "blablbla",
                        "status": "published",
                        "publication_status": "ongoing",
                        "contributor": "shortterm.tn",
                        "cause": {
                            "id": "3d1f34b2-e8df-11e3-8c3e-0008ca8657ea",
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
                        "publication_period" : {
                            "begin":"2014-04-31T17:00:00Z",
                            "end":"2014-05-01T17:00:00Z"
                        },
                        "impacts": {
                            "pagination": {
                                "start_index": 0,
                                "items_per_page": 20,
                                "total_results": 3,
                                "prev": null,
                                "next": {"href": "https://chaos.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ea/impacts?start_index=1&item_per_page=20"},
                                "first": {"href": "https://chaos.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ea/impacts?start_index=1&item_per_page=20"},
                                "last": {"href": "https://chaos.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ea/impacts?start_index=1&item_per_page=20"}
                            }
                        }
                    },
                    {
                        "id": "d30502d2-e8de-11e3-8c3e-0008ca8657eb",
                        "self": {"href": "https://chaos.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657eb"},
                        "reference": "RER A en panne",
                        "created_at": "2014-05-31T16:52:18Z",
                        "updated_at": null,
                        "note": null,
                        "status": "published",
                        "publication_status": "coming",
                        "contributor": "shortterm.tn",
                        "cause": {
                            "id": "3d1f34b2-e8ef-11e3-8c3e-0008ca8657ea",
                            "wording": "train cassé"
                        },
                        "tags": ["rer", "probleme"],
                        "localization": [],
                        "publication_period" : {
                            "begin": "2014-04-31T17:00:00Z",
                            "end": null
                        },
                        "impacts": {
                            "pagination": {
                                "start_index": 0,
                                "items_per_page": 20,
                                "total_results": 5,
                                "prev": null,
                                "next": {"href": "https://chaos.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657eb/impacts?start_index=1&item_per_page=20"},
                                "first": {"href": "https://chaos.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657eb/impacts?start_index=1&item_per_page=20"},
                                "last": {"href": "https://chaos.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657eb/impacts?start_index=1&item_per_page=20"}
                            }
                        }
                    },
                    {
                        "id": "d30502d2-e8de-11e3-8c3e-0008ca8657ec",
                        "self": {"href": "https://chaos.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ec"},
                        "reference": "Chatelet fermé",
                        "created_at": "2014-05-17T16:52:18Z",
                        "update_at": "2014-05-31T06:55:18Z",
                        "note": "retour probable d'ici 5H",
                        "status": "published",
                        "publication_status": "past",
                        "contributor": "shortterm.tn",
                        "cause": {
                            "id": "3d1f34b2-e2df-11e3-8c3e-0008ca8657ea",
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
                        "publication_period" : {
                            "begin": "2014-04-31T17:00:00Z",
                            "end": null
                        },
                        "impacts": {
                            "pagination": {
                                "start_index": 0,
                                "items_per_page": 20,
                                "total_results": 25,
                                "prev": null,
                                "next": {"href": "https://chaos.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ec/impacts?start_index=1&item_per_page=20"},
                                "first": {"href": "https://chaos.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ec/impacts?start_index=1&item_per_page=20"},
                                "last": {"href": "https://chaos.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ec/impacts?start_index=21&item_per_page=20"}
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

Create one valid disruption with impacts

- Request (application/json)

    * Body

            {
                "reference": "foo",
                "note": null,
                "contributor": "shortterm.tn",
                "cause": {
                       "id": "3d1f34b2-e8df-1ae3-8c3e-0008ca8657ea"
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
                ],
                "publication_period" : {
                    "begin": "2014-04-31T17:00:00Z",
                    "end": null
                },
                "impacts": [
                    {
                        "severity": {
                            "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ea"
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
                                    "id": "3d1f42b6-e8df-11e3-8c3e-0008ca8657ea"
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
                                    "id": "3d1f42b6-e8df-11e3-8c3e-0008ca8657ea"
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
                ]
            }



- response 201 (application/json)

    * Body

            {
                "disruption":{
                    "id": "3d1f32b2-e8df-11e3-8c3e-0008ca8657ea",
                    "self": {"href": "https://chaos.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea"},
                    "reference": "foo",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null,
                    "note": null,
                    "status": "published",
                    "publication_status": "ongoing",
                    "contributor": "shortterm.tn",
                    "cause": {
                        "id": "3d1f34b2-e8df-1ae3-8c3e-0008ca8657ea",
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
                    "publication_period" : {
                        "begin": "2014-04-31T17:00:00Z",
                        "end": null
                    },
                    "impacts": {
                        "pagination": {
                            "start_index": 0,
                            "items_per_page": 20,
                            "total_results": 1,
                            "prev": null,
                            "next": null,
                            "first": {"href": "https://chaos.apiary-mock.com/disruptions/1/impacts?start_index=1&item_per_page=20"},
                            "last": null
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
                    "id": "3d1f32b2-e8df-11e3-8c3e-0008ca8657ea",
                    "self": {"href": "https://chaos.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea"},
                    "reference": "RER B en panne",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "note": "blablbla",
                    "status": "published",
                    "publication_status": "ongoing",
                    "contributor": "shortterm.tn",
                    "cause": {
                        "id": "3d1e32b2-e8df-11e3-8c3e-0008ca8657ea",
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
                    "publication_period" : {
                        "begin": "2014-04-31T17:00:00Z",
                        "end": null
                    },
                    "impacts": {
                        "pagination": {
                            "start_index": 1,
                            "items_per_page": 20,
                            "total_results": 3,
                            "prev": null,
                            "next": {"href": "https://chaos.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts?start_index=1&item_per_page=20"},
                            "first": {"href": "https://chaos.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts?start_index=1&item_per_page=20"},
                            "last": {"href": "https://chaos.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts?start_index=1&item_per_page=20"}
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
                "contributor": "shortterm.tn",
                "cause": {
                    "id": "3d1f32b2-e8df-11e3-8c3e-0008ca86c7ea"
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
                ],
                "publication_period" : {
                    "begin": "2014-04-31T17:00:00Z",
                    "end": null
                }
            }


- Response 200 (application/json)

    * Body

            {
                "disruption":{
                    "id": "3d1f32b2-e8df-11e3-8c3e-0008ca8657ea",
                    "self": {"href": "https://chaos.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea"},
                    "reference": "foo",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "note": null,
                    "status": "published",
                    "publication_status": "ongoing",
                    "contributor": "shortterm.tn",
                    "cause": {
                        "id": "3d1f32b2-e8df-11e3-8c3e-0008ca8657ea",
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
                    "publication_period" : {
                        "begin": "2014-04-31T17:00:00Z",
                        "end": null
                    },
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
Archive one disruption.
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


# List of Impacts [/disruptions/{disruption_id}/impacts]

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
                        "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ea",
                        "self": {"href": "https://chaos.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8657ea"},
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "severity": {
                            "id": "3d1f42b2-e8df-11e3-8c3e-0008ca86c7ea",
                            "wording": "Bonne nouvelle",
                            "created_at": "2014-04-31T16:52:18Z",
                            "updated_at": "2014-04-31T16:55:18Z",
                            "color": "#123456",
                            "priority": null,
                            "effect": "none"
                        },
                        "application_periods": [
                            {
                                "begin": "2014-04-31T16:52:00Z",
                                "end": "2014-05-22T02:15:00Z"
                            }
                        ],
                        "messages": [
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
                                    "max_size": 140
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
                        "disruption" : {"href": "https://chaos.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-823e-0008ca8657ea"}
                    }
                ],
                "meta": {
                    "pagination": {
                        "start_index": 1,
                        "items_per_page": 3,
                        "total_results": 6,
                        "prev": null,
                        "next": {"href": "https://chaos.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-823e-0008ca8657ea/impacts?start_index=4&items_per_page=3"},
                        "first": {"href": "https://chaos.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-823e-0008ca8657ea/impacts?start_index=1&items_per_page=3"},
                        "last": {"href": "https://chaos.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-823e-0008ca8657ea/impacts?start_index=4&items_per_page=3"}
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
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ea"
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
                            "id": "3d1f42b2-e8df-11e3-8c3e-0008ca86c7ea"
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
                            "id": "3d1f42b2-e8df-11e3-8c3e-0002ca8657ea"
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
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8617ea",
                    "self": {"href": "https://chaos.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-8c3e-0008ca8647ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8617ea"},
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "severity": {
                        "id": "3d1f42b2-e8df-11e3-8c3e-0008ca861aea",
                        "wording": "Bonne nouvelle",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "color": "#123456",
                        "priority": 1,
                        "effect": "none"
                    },
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
                                "max_size": 140
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
                    "disruption" : {"href": "https://chaos.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-1c3e-0008ca8617ea"}
                },
                "meta": {}
            }


#Impact [/disruptions/{disruption_id}/impacts/{id}]
##Retrieve a impact [GET]
###Parameters

- response 200 (application/json)

    * Body

            {
                "impact": {
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8617ea",
                    "self": {"href": "https://chaos.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-8c3e-0008ca8647ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8617ea"},
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "severity": {
                        "id": "3d1f42b2-e8df-11e3-8c3e-0008ca861aea",
                        "wording": "Bonne nouvelle",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "color": "#123456",
                        "priority": 1,
                        "effect": "none"
                    },
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
                                "max_size": 140
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
                    "disruption" : {"href": "https://chaos.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-1c3e-0008ca8617ea"}
                },
                "meta": {}
            }

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No disruption or impact"
                },
                "meta": {}
            }

#List of severities [/severities]

##Retrieve the list of all severities [GET]

- response 200 (application/json)

    * Body

            {
                "severities": [
                    {
                        "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                        "wording": "normal",
                        "effect": "none",
                        "color": "#123456",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b4-e8df-11e3-8c3e-0008ca8617ea",
                        "wording": "majeur",
                        "effect": "none",
                        "color": "#123456",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b5-e8df-11e3-8c3e-0008ca8617ea",
                        "wording": "bloquant",
                        "effect": "blocking",
                        "color": "#123456",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    }
                ],
                "meta": {}
            }

##Create a severity [POST]
- request
    + headers

            Content-Type: application/json
    * Body

                {
                    "wording": "normal",
                    "color": "#123456",
                    "priority": 1,
                    "effect": "none"
                }

- response 200 (application/json)

    * Body

            {
                "severity": {
                    "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                    "wording": "normal",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null,
                    "color": "#123456",
                    "priority": 1,
                    "effect": "none"
                },
                "meta": {}
            }

#List of causes [/causes]

##Retrieve the list of all causes [GET]

- response 200 (application/json)

    * Body

            {
                "causes": [
                    {
                        "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                        "wording": "météo",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b2-e8df-11e5-8c3e-0008ca8617ea",
                        "wording": "gréve",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b2-e8df-11e6-8c3e-0008ca8617ea",
                        "wording": "accident voyageur",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    }
                ],
                "meta": {}
            }

##Create a cause [POST]
- request
    + headers

            Content-Type: application/json
    * Body

                {
                    "wording": "météo"
                }

- response 200 (application/json)

    * Body

            {
                "cause": {
                    "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                    "wording": "météo",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null
                },
                "meta": {}
            }

#List of channels [/channels]

##Retrieve the list of all channels [GET]

- response 200 (application/json)

    * Body

            {
                "channels": [
                    {
                        "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                        "name": "court",
                        "max_size": 140,
                        "content_type": "text/plain",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1a42b7-e8df-11e4-8c3e-0008ca8617ea",
                        "name": "long",
                        "max_size": 512,
                        "content_type": "text/plain",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                        "name": "long riche",
                        "max_size": null,
                        "content_type": "text/markdown",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    }
                ],
                "meta": {}
            }

##Create a channels [POST]
- request
    + headers

            Content-Type: application/json
    * Body

                {
                    "name": "court",
                    "max_size": 140,
                    "content_type": "text/plain"
                }

- response 200 (application/json)

    * Body

            {
                "channel": {
                    "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                    "name": "court",
                    "max_size": 140,
                    "content_type": "text/plain",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z"
                },
                "meta": {}
            }

# Severities [/severities/{id}]
##Retrieve one severity [GET]

##Parameters

Retrieve one existing severity:

- response 200 (application/json)

    * Body

            {
                "severity": {
                    "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                    "wording": "normal",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null,
                    "color": "#123456",
                    "priority": 1,
                    "effect": "none"
                },
                "meta": {}
            }


- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No severity"
                },
                "meta": {}
            }

##Update a severity [PUT]

###Parameters

- Request

    * Headers

            Content-Type: application/json

    * Body

            {
                "wording": "Bonne nouvelle",
                "color": "#123456",
                "effect": "none"
            }


- Response 200 (application/json)

    * Body

            {
                "severity": {
                    "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                    "wording": "Bonne nouvelle",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "color": "#123456",
                    "priority": 1,
                    "effect": "none"
                },
                "meta": {}
            }

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No severity"
                },
                "meta": {}
            }

##Delete a severity [DELETE]
Archive one severity.
###Parameters


- Response 204

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No severity"
                },
                "meta": {}
            }

# Causes [/causes/{id}]
##Retrieve one cause [GET]

##Parameters

Retrieve one existing cause:

- response 200 (application/json)

    * Body

            {
                "cause": {
                    "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                    "wording": "météo",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null
                },
                "meta": {}
            }


- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No cause"
                },
                "meta": {}
            }

##Update a cause [PUT]
###Parameters


- Request

    * Headers

            Content-Type: application/json

    * Body

            {
                "wording": "accident voyageur"
            }

- Response 200 (application/json)

    * Body

            {
                "cause": {
                    "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                    "wording": "accident voyageur",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z"
                },
                "meta": {}
            }

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No cause"
                },
                "meta": {}
            }

##Delete a cause [DELETE]
Archive a cause.
###Parameters


- Response 204

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No cause"
                },
                "meta": {}
            }
