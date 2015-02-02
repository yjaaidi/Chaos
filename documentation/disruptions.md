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
                "channels": {"href": "https://chaos.apiary-mock.com/channels"},
                "impactsbyobject": {"href": "https://chaos.apiary-mock.com/impactsbyobject"},
                "tags": {"href": "https://chaos.apiary-mock.com/tags"},
                "categories": {"href": "https://chaos.apiary-mock.com/categories"}
            }


##Headers

| Name                 | description                                                                    | required | default                 |
| -------------------- | ------------------------------------------------------------------------------ | -------- | ----------------------- |
| Content-Type         | input text type                                                                | true     | application/json        |
| Authorization        | token for navitia services                                                     | true     |                         |
| X-Customer-Id        | client code. A client is owner of cause, channel, severity and tag             | true     |                         |
| X-Contributors       | contributor code. A contributor is owner of a disruption                       | true     |                         |
| X-Coverage           | coverage of navitia services                                                   | true     |                         |

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
| tag[]                | filter by tag (id of tag)                                                      | false    |                         |
| uri                  | filter by uri of ptobject                                                      | false    |                         |

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
                        "version": 1,
                        "cause": {
                            "id": "3d1f34b2-e8df-11e3-8c3e-0008ca8657ea",
                            "wordings": [{"key": "msg", "value": "accident voyageur"}],
                            "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "category-1"}
                        },
                        tags": [
                            {
                                "created_at": "2014-07-30T07:11:08Z",
                                "id": "ad9d80ce-17b8-11e4-a553-d4bed99855be",
                                "name": "rer",
                                "self": {
                                    "href": "http://127.0.0.1:5000/tags/ad9d80ce-17b8-11e4-a553-d4bed99855be"
                                },
                                "updated_at": null
                            }
                        ]
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
                            "wordings": [{"key": "msg", "value": "accident voyageur"}],
                            "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "category-1"}
                        },
                        tags": [
                            {
                                "created_at": "2014-07-30T07:11:08Z",
                                "id": "ad9d80ce-17b8-11e4-a553-d4bed99855be",
                                "name": "rer",
                                "self": {
                                    "href": "http://127.0.0.1:5000/tags/ad9d80ce-17b8-11e4-a553-d4bed99855be"
                                },
                                "updated_at": null
                            }
                        ],
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
                            "wordings": [{"key": "msg", "value": "accident voyageur"}],
                            "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "category-1"}
                        },
                        tags": [
                            {
                                "created_at": "2014-07-30T07:11:08Z",
                                "id": "ad9d80ce-17b8-11e4-a553-d4bed99855be",
                                "name": "rer",
                                "self": {
                                    "href": "http://127.0.0.1:5000/tags/ad9d80ce-17b8-11e4-a553-d4bed99855be"
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
                },
                "tags":[{"id": "ad9d80ce-17b8-11e4-a553-d4bed99855be"}],
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
                    "version": 2,
                    "cause": {
                        "id": "3d1f34b2-e8df-1ae3-8c3e-0008ca8657ea",
                        "wordings": [{"key": "msg", "value": "accident voyageur"}],
                        "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "category-1"}
                    },
                    tags": [
                        {
                            "created_at": "2014-07-30T07:11:08Z",
                            "id": "ad9d80ce-17b8-11e4-a553-d4bed99855be",
                            "name": "rer",
                            "self": {
                                "href": "http://127.0.0.1:5000/tags/ad9d80ce-17b8-11e4-a553-d4bed99855be"
                            },
                            "updated_at": null
                        }
                    ]
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
                    "version": 2,
                    "cause": {
                        "id": "3d1e32b2-e8df-11e3-8c3e-0008ca8657ea",
                        "wordings": [{"key": "msg", "value": "accident voyageur"}],
                        "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "category-1"}
                    },
                    tags": [
                        {
                            "created_at": "2014-07-30T07:11:08Z",
                            "id": "ad9d80ce-17b8-11e4-a553-d4bed99855be",
                            "name": "rer",
                            "self": {
                                "href": "http://127.0.0.1:5000/tags/ad9d80ce-17b8-11e4-a553-d4bed99855be"
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
            Authorization: [navitia token]
            X-Customer-Id: [customer id]
            X-Contributors: [contributor id]
            X-Coverage: [navitia coverage]

    * Body

            {
                "reference": "foo",
                "note": null,
                "contributor": "shortterm.tn",
                "cause": {
                    "id": "3d1f32b2-e8df-11e3-8c3e-0008ca86c7ea"
                },
                "tags":[{"id": "ad9d80ce-17b8-11e4-a553-d4bed99855be"}],
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
                    "version": 2,
                    "cause": {
                        "id": "3d1f32b2-e8df-11e3-8c3e-0008ca8657ea",
                        "wordings": [{"key": "msg", "value": "accident voyageur"}],
                        "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "category-1"}
                    },
                    tags": [
                        {
                            "created_at": "2014-07-30T07:11:08Z",
                            "id": "ad9d80ce-17b8-11e4-a553-d4bed99855be",
                            "name": "rer",
                            "self": {
                                "href": "http://127.0.0.1:5000/tags/ad9d80ce-17b8-11e4-a553-d4bed99855be"
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

# List of Impacts by object type [/impacts]

##Retrieve impacts [GET]
Return all impacts by ptobject.
##Parameters

| Name                 | description                                                                    | required | default                     |
| -------------------- | ------------------------------------------------------------------------------ | -------- | --------------------------- |
| pt_object_type       | filter by ptobject, possible value are: network, stoparea, line, line_section  | false    |                             |
| uri[]                | filtre by ptobject.uri                                                         | false    |                             |
| start_date           | filtre by application period :star date                                        | false    | Now():00:00:00Z             |
| end_date             | filtre by application period :end date                                         | false    | Now():23:59:59Z             |

- response 200 (application/json)
    * Body

            {

			"meta": {
				"pagination": {
						"first": {
							"href": "http://127.0.0.1:5000/impacts?start_page=1&items_per_page=20"
						},
						"items_on_page": "1",
						"items_per_page": "20",
						"last": {
							"href": "http://127.0.0.1:5000/impacts?start_page=1&items_per_page=20"
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
							"application_periods": [
									{
										"begin": "2014-03-29T16:52:00Z",
										"end": "2014-05-22T02:15:00Z"
									}
							],
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
										"updated_at": "2014-04-31T16:55:18Z"
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
											"updated_at": "2014-04-31T16:55:18Z"
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
							"object": [
								{
									"id": "RER:A",
									"name": "RER:A",
									"type": "network"
								}
							],
							"self": {
								"href": "https://chaos.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8657ea"
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


# List of Impacts [/disruptions/{disruption_id}/impacts]

##Retrieve impacts [GET]
Return all impacts of a impact.
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
					"wordings" : [{"key": "msg", "value": "Bonne nouvelle"}],
					"created_at": "2014-04-31T16:52:18Z",
					"updated_at": "2014-04-31T16:55:18Z",
					"color": "#123456",
					"priority": null,
					"effect": null
				},
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
            Authorization: [navitia token]
            X-Customer-Id: [customer id]
            X-Contributors: [contributor id]
            X-Coverage: [navitia coverage]

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
                        "id": "line:AME:3",
                        "type": "line_section"
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
                            "sens":0,
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
                        "wordings" : [{"key": "msg", "value": "Bonne nouvelle"}],
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "color": "#123456",
                        "priority": 1,
                        "effect": null
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
                            "id": "line:AME:3",
                            "type": "line_section"
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
                                "sens":0,
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
                    "disruption" : {"href": "https://chaos.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-1c3e-0008ca8617ea"}
                },
                "meta": {}
            }

##Update a impact [PUT]

###Parameters


- Request

    * Headers

            Content-Type: application/json
            Authorization: [navitia token]
            X-Customer-Id: [customer id]
            X-Contributors: [contributor id]
            X-Coverage: [navitia coverage]

    * Body

            {
                "impact": {
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8617ea",
                    "self": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-8c3e-0008ca8647ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8617ea"},
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
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
                                "updated_at": "2014-04-31T16:55:18Z"
                                },
                                "created_at": "2014-04-31T16:52:18Z",
                                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ca",
                                "text": "Message 1",
                                "updated_at": "2014-04-31T16:55:18Z"
                            },
                            {
                                "channel": {
                                    "content_type": "text/markdown",
                                    "created_at": "2014-04-31T16:52:18Z",
                                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca86c7ea",
                                    "max_size": null,
                                    "name": "message long",
                                    "updated_at": "2014-04-31T16:55:18Z"
                                },
                                "created_at": "2014-04-31T16:52:18Z",
                                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8257ea",
                                "text": "Message 2",
                                "updated_at": "2014-04-31T16:55:18Z"
                            }
                    ],
                    "application_periods": [
                        {
                            "begin": "2014-04-31T16:52:00Z",
                            "end": "2014-05-22T02:15:00Z"
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
                            "type": "line_section"
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
                                "sens":0,
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
                    "disruption" : {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-1c3e-0008ca8617ea"}
                },
                "meta": {}
            }


- Response 200 (application/json)

    * Body

            {
                "impact": {
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8617ea",
                    "self": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-8c3e-0008ca8647ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8617ea"},
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
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
                                "updated_at": "2014-04-31T16:55:18Z"
                                },
                                "created_at": "2014-04-31T16:52:18Z",
                                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ca",
                                "text": "Message 1",
                                "updated_at": "2014-04-31T16:55:18Z"
                            },
                            {
                                "channel": {
                                    "content_type": "text/markdown",
                                    "created_at": "2014-04-31T16:52:18Z",
                                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca86c7ea",
                                    "max_size": null,
                                    "name": "message long",
                                    "updated_at": "2014-04-31T16:55:18Z"
                                },
                                "created_at": "2014-04-31T16:52:18Z",
                                "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8257ea",
                                "text": "Message 2",
                                "updated_at": "2014-04-31T16:55:18Z"
                            }
                    ],
                    "application_periods": [
                        {
                            "begin": "2014-04-31T16:52:00Z",
                            "end": "2014-05-22T02:15:00Z"
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
                            "type": "line_section"
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
                                "sens":0,
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
                    "disruption" : {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-1c3e-0008ca8617ea"}
                },
                "meta": {}
            }

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No impact"
                },
                "meta": {}
            }

##Delete a impact [DELETE]
Archive one impact.
###Parameters


- Response 204

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No impact"
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
                        "wordings" : [{"key": "msg", "value": "Bonne nouvelle"}],
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "color": "#123456",
                        "priority": 1,
                        "effect": null
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
Return all the severities ordered by priority.

- response 200 (application/json)

    * Body

            {
                "severities": [
                    {
                        "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                        "wordings" : [{"key": "msg", "value": "Normal"}],
                        "effect": null,
                        "priority": 1,
                        "color": "#123456",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b4-e8df-11e3-8c3e-0008ca8617ea",
                        "wordings" : [{"key": "msg", "value": "Majeur"}],
                        "effect": null,
                        "priority": 2,
                        "color": "#123456",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b5-e8df-11e3-8c3e-0008ca8617ea",
                        "wordings" : [{"key": "msg", "value": "Bloquant"}],
                        "effect": "blocking",
                        "priority": 3,
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
            X-Customer-Id: [customer id]

    * Body

                {
                    "wordings" : [{"key": "msg", "value": "Normal"}],
                    "color": "#123456",
                    "priority": 1,
                    "effect": null
                }

- response 200 (application/json)

    * Body

            {
                "severity": {
                    "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                    "wordings" : [{"key": "msg", "value": "Normal"}],
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null,
                    "color": "#123456",
                    "priority": 1,
                    "effect": null
                },
                "meta": {}
            }

#List of causes [/causes]

##Retrieve the list of all causes [GET]
##Paramètres

| Name                 | description                                                                               | required | default                 |
| -------------------- | ----------------------------------------------------------------------------------------- | -------- | ----------------------- |
| category             |  filter by category (id of category)                                                      | false    |                         |


- response 200 (application/json)

    * Body

            {
                "causes": [
                    {
                        "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                        "wordings": [{"key": "msg", "value": "accident voyageur"}],
                        "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "test"}
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b2-e8df-11e5-8c3e-0008ca8617ea",
                        "wordings": [{"key": "msg", "value": "accident voyageur"}],
                        "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "category-1"}
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b2-e8df-11e6-8c3e-0008ca8617ea",
                        "wordings": [{"key": "msg", "value": "accident voyageur"}],
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
            X-Customer-Id: [customer id]

    * Body

                {
                    "wordings": [{"msg": "météo"}],
                    "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be"}
                }

- response 200 (application/json)

    * Body

            {
                "cause": {
                    "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                    "wordings": [{"key": "msg", "value": "accident voyageur"}],
                    "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "test"}
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null
                },
                "meta": {}
            }

#List of tags [/tags]

##Retrieve the list of all tags [GET]

- response 200 (application/json)

    * Body

            {
                "tags": [
                    {
                        "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                        "name": "meteo",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b2-e8df-11e5-8c3e-0008ca8617ea",
                        "name": "probleme",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b2-e8df-11e6-8c3e-0008ca8617ea",
                        "name": "rer",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    }
                ],
                "meta": {}
            }

##Create a tag [POST]
- request
    + headers

            Content-Type: application/json
            X-Customer-Id: [customer id]

    * Body

                {
                    "name": "meteo"
                }

- response 200 (application/json)

    * Body

            {
                "tag": {
                    "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                    "name": "meteo",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null
                },
                "meta": {}
            }

# tags [/tags/{id}]
##Retrieve one tag [GET]

##Parameters

Retrieve one existing tag:

- response 200 (application/json)

    * Body

            {
                "tag": {
                    "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                    "self": {
                        "href": "https://ogv2ws.apiary-mock.com/tags/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
                    }
                    "name": "rer",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null
                },
                "meta": {}
            }


- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No tag"
                },
                "meta": {}
            }

##Update a tag [PUT]

###Parameters

- Request

    * Headers

            Content-Type: application/json
            X-Customer-Id: [customer id]

    * Body

            {
                "name": "rer"
            }

- Response 200 (application/json)

    * Body

            {
                "tag": {
                    "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                    "self": {
                        "href": "https://ogv2ws.apiary-mock.com/tags/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
                    }
                    "name": "rer",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z"
                },
                "meta": {}
            }

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No tag"
                },
                "meta": {}
            }

- response 400 (application/json)
    * Body

            {
                "error": {
                    "message": "'name' is a required property"
                }
                "meta": {}
            }

##Delete a tag [DELETE]
Archive a tag.
###Parameters


- Response 204

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No tag"
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
            X-Customer-Id: [customer id]

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
                    "wordings" : [{"key": "msg", "value": "Normal"}],
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null,
                    "color": "#123456",
                    "priority": 1,
                    "effect": null
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
            X-Customer-Id: [customer id]

    * Body

            {
                "wordings" : [{"key": "msg", "value": "Bonne nouvelle"}],
                "color": "#123456",
                "effect": null
            }


- Response 200 (application/json)

    * Body

            {
                "severity": {
                    "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                    "wordings" : [{"key": "msg", "value": "Bonne nouvelle"}],
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "color": "#123456",
                    "priority": 1,
                    "effect": null
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
                    "wordings": [{"key": "msg", "value": "accident voyageur"}],
                    "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "test"}
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
            X-Customer-Id: [customer id]

    * Body

            {
                    "wordings": [{"msg": "accident voyageur"}],
                    "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be"}
            }

- Response 200 (application/json)

    * Body

            {
                "cause": {
                    "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                    "wordings": [{"key": "msg", "value": "accident voyageur"}],
                    "category": {"id": "32b07ff8-10e0-11e4-ae39-d4bed99855be", "name": "cat-1"}
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

#List of categories [/categories]

##Retrieve the list of all categories [GET]

- response 200 (application/json)

    * Body

            {
                "categories": [
                    {
                        "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                        "name": "meteo",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b2-e8df-11e5-8c3e-0008ca8617ea",
                        "name": "probleme",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b2-e8df-11e6-8c3e-0008ca8617ea",
                        "name": "rer",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    }
                ],
                "meta": {}
            }

##Create a category [POST]
- request
    + headers

            Content-Type: application/json
            X-Customer-Id: [customer id]

    * Body

                {
                    "name": "meteo"
                }

- response 200 (application/json)

    * Body

            {
                "category": {
                    "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                    "name": "meteo",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null
                },
                "meta": {}
            }

# categories [/categories/{id}]
##Retrieve one category [GET]

##Parameters

Retrieve one existing category:

- response 200 (application/json)

    * Body

            {
                "category": {
                    "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                    "self": {
                        "href": "https://ogv2ws.apiary-mock.com/categories/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
                    }
                    "name": "rer",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null
                },
                "meta": {}
            }


- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No category"
                },
                "meta": {}
            }

##Update a category [PUT]

###Parameters

- Request

    * Headers

            Content-Type: application/json
            X-Customer-Id: [customer id]

    * Body

            {
                "name": "rer"
            }

- Response 200 (application/json)

    * Body

            {
                "category": {
                    "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                    "self": {
                        "href": "https://ogv2ws.apiary-mock.com/categories/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
                    }
                    "name": "rer",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z"
                },
                "meta": {}
            }

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No category"
                },
                "meta": {}
            }

- response 400 (application/json)
    * Body

            {
                "error": {
                    "message": "'name' is a required property"
                }
                "meta": {}
            }

##Delete a category [DELETE]
Archive a category.
###Parameters


- Response 204

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No category"
                },
                "meta": {}
            }
