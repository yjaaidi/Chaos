### disruptions

#Retrieve all Disruptions
GET /disruptions

- response 200
    * Headers
    * Body

            {
                "disruptions": [
                    {
                        "id": 1,
                        "reference": "RER B en panne",
                        "creation_date": "2014-04-31 16:52:18",
                        "update_date": "2014-04-31 16:55:18",
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
                    },
                    {
                        "id": 4,
                        "reference": "RER A en panne",
                        "creation_date": "2014-05-31 16:52:18",
                        "update_date": null,
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
                    },
                    {
                        "id": 2,
                        "reference": "Chatelet fermé",
                        "creation_date": "2014-05-17 16:52:18",
                        "update_date": "2014-05-31 06:55:18",
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
                    },

                ],
                "meta": {
                    "pagination": {
                        "items_per_page": 25,
                        "items_on_page": 25,
                        "start_page": 0,
                        "total_result": 8785
                    },
                }

            }

