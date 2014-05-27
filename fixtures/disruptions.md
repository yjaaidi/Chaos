# disruptions

##Retrieve disruptions [GET /disruptions]
Return all visible disruptions.
###Parameters

| Name           | description                                      | required | default |
| -------------- | ------------------------------------------------ | -------- | ------- |
| start_index    | index of the first element returned (start at 1) | false    | 1       |
| items_per_page | number of items per page                         | false    | 20      |

@TODO: search and sort

###Examples

**GET** /disruptions

- response 200
    * Headers

            Content-Type: application/json

    * Body

            {
                "disruptions": [],
                "meta": {
                    "pagination": {
                        "start_index": 1,
                        "items_per_page": 20,
                        "total_results": 0,
                    },
                }

            }


**GET** /disruptions?items_per_page=3

- response 200
    * Headers

            Content-Type: application/json

    * Body

            {
                "disruptions": [
                    {
                        "id": 1,
                        "url": "https://chaos.example.com/disruptions/1",
                        "reference": "RER B en panne",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "note": "blablbla",
                        "state": "published",
                        "contributor": "shortterm.tn",
                        "cause": {
                            id": 23,
                            wording": "Condition météo"
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
                                },
                            },
                            {
                                "id": "stop_area:RTP:SA:3786123",
                                "name": "DE GAULLE - GOUNOD - TABANOU",
                                "type": "stop_area",
                                "coord": {
                                    "lat": "48.780179",
                                    "lon": "2.340886"
                                },
                            }
                        ],
                        "nb_impacts": 3,
                        "impact_url" : "https://chaos.example.com/disruptions/1/impacts",
                    },
                    {
                        "id": 4,
                        "url": "https://chaos.example.com/disruptions/4",
                        "reference": "RER A en panne",
                        "created_at": "2014-05-31T16:52:18Z",
                        "updated_at": null,
                        "note": null,
                        "state": "published",
                        "contributor": "shortterm.tn",
                        "cause": {
                            id": 2,
                            wording": "train cassé"
                        },
                        "tags": ["rer", "probleme"],
                        "localization": [],
                        "nb_impacts": 5,
                        "impact_url" : "chaos.example.com/disruptions/4/impacts",
                    },
                    {
                        "id": 2,
                        "url": "https://chaos.example.com/disruptions/2",
                        "reference": "Chatelet fermé",
                        "created_at": "2014-05-17T16:52:18Z",
                        "update_at": "2014-05-31T06:55:18Z",
                        "note": "retour probable d'ici 5H",
                        "state": "published",
                        "contributor": "shortterm.tn",
                        "cause": {
                            id": 4,
                            wording": "émeute"
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
                                },
                            },
                        ],
                        "nb_impacts": 15,
                        "impact_url" : "chaos.example.com/disruptions/2/impacts",
                    },

                ],
                "meta": {
                    "pagination": {
                        "start_index": 1,
                        "items_per_page": 3,
                        "total_results": 6,
                    },
                }

            }



##Retrieve one disruption [GET /disruptions/{id}]

###Parameters

###Examples

Retrieve one existing disruption:

**GET** /disruptions/1

- response 200
    * Headers

            Content-Type: application/json

    * Body

            {
                "disruption": {
                    "id": 1,
                    "url": "https://chaos.example.com/disruptions/1",
                    "reference": "RER B en panne",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "note": "blablbla",
                    "state": "published",
                    "contributor": "shortterm.tn",
                    "cause": {
                        id": 23,
                        wording": "Condition météo"
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
                            },
                        },
                        {
                            "id": "stop_area:RTP:SA:3786123",
                            "name": "DE GAULLE - GOUNOD - TABANOU",
                            "type": "stop_area",
                            "coord": {
                                "lat": "48.780179",
                                "lon": "2.340886"
                            },
                        }
                    ],
                    "nb_impacts": 3,
                    "impact_url" : "https://chaos.example.com/disruptions/1/impacts",
                },
                "meta": {}
            }


Retrieve a non existing (or deleted) disruption:

**GET** /disruptions/25

- response 404
    * Headers
    * Body

            {
                "error": {
                    "message": "No disruption"
                },
                "meta": {}
            }


##Create a disruption [POST /disruptions]

###Parameters

###Examples


Create one valid disruption without impacts

**POST** /disruptions

- Request

    * Headers

            Content-Type: application/json

    * Body

            {
                "reference": "foo",
                "note": null,
                "state": "published",
                "contributor": "shortterm.tn",
                "cause": 23, //child?
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



- response 201
    * Headers

            Content-Type: application/json

    * Body

            {
                "disruption":{
                    "id": 1,
                    "url": "https://chaos.example.com/disruptions/1",
                    "reference": "foo",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null,
                    "note": null,
                    "state": "published",
                    "contributor": "shortterm.tn",
                    "cause": {
                        id": 23,
                        wording": "Condition météo"
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
                            },
                        },
                        {
                            "id": "stop_area:RTP:SA:3786123",
                            "name": "DE GAULLE - GOUNOD - TABANOU",
                            "type": "stop_area",
                            "coord": {
                                "lat": "48.780179",
                                "lon": "2.340886"
                            },
                        }
                    ],
                    "nb_impacts": 0,
                    "impact_url" : "https://chaos.example.com/disruptions/1/impacts",
                },
                "meta": {}
            }

##Update a disruption [PUT /disruptions/{id}]

###Parameters

###Examples


Update one disruption without impacts

**PUT** /disruptions/4

- Request

    * Headers

            Content-Type: application/json

    * Body

            {
                "reference": "foo",
                "note": null,
                "state": "published",
                "contributor": "shortterm.tn",
                "cause": 23, //child?
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



- Response 200
    * Headers

            Content-Type: application/json

    * Body

            {
                "disruption":{
                    "id": 4,
                    "url": "https://chaos.example.com/disruptions/4",
                    "reference": "foo",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "note": null,
                    "state": "published",
                    "contributor": "shortterm.tn",
                    "cause": {
                        id": 23,
                        wording": "Condition météo"
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
                            },
                        },
                        {
                            "id": "stop_area:RTP:SA:3786123",
                            "name": "DE GAULLE - GOUNOD - TABANOU",
                            "type": "stop_area",
                            "coord": {
                                "lat": "48.780179",
                                "lon": "2.340886"
                            },
                        }
                    ],
                    "nb_impacts": 0,
                    "impact_url" : "https://chaos.example.com/disruptions/4/impacts",
                },
                "meta": {}
            }


##Delete a disruption [DELETE /disruptions/{id}]

###Parameters

###Examples

delete one disruption.

**DELETE** /disruptions/4

- Response 204

