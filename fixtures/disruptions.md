# disruptions

###Retrieve disruptions

####Parameters

Name | description | required | default
--- | --- | ---
limit | max numbers of disruptions on a response | false | 20
page | index of the page | false | 1

####Examples

GET /disruptions
- response 200
    * Headers
    * Body
                "disruptions": [],
                "meta": {
                    "pagination": {
                        "limit": 20,
                        "page": 1,
                        "pages": 1,
                    },
                }

            }


GET /disruptions?limit=3
- response 200
    * Headers
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
                        "limit": 3,
                        "page": 1,
                        "pages": 2,
                    },
                }

            }
