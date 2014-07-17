FORMAT: 1A
HOST: https://ogv2ws.apiary-mock.com

#Web Services Ogesper v2
Les web Services Ogesper v2 permettent la gestion des perturbations sur un référentiel de transport.
Les entités manipulées par le web service sont:

   - les perturbations (disruptions), qui représentent toutes situations affectant positivement ou négativement le réseau de transport.
   - les impacts (impacts), qui représentent toute application d'une perturbation sur une entité du référentiel de transport (ligne, zone d'arrêt, ...).
   - les sévérités, ou conséquences (severities), qui représentent les conséquences d'un impact sur l'entité du référentiel affectée (bloquant, information, ...)
   - les causes, ou motif (causes), qui représentent les origine de la perturbation (obstacle sur les voies, accident de voyageur, ...)
   - les canaux de diffusion (channels), qui représentent les medias vers lesquels les informations seront transmises.

Pour chacune des entités présentées, les web services proposent les fonctions de création, suppression, édition, liste, et recherche unitaire. Sauf mention contraire, seules les fonctions de liste et de recherche sont proposées à l'implémentation.

L'ensemble des services retournent les URLs nécessaires à une séquence d'appel. Par exemple, l'API disruptions retourne une URL permettant d'accéder au détail de chaque perturbation retournée (attribut "self"), des liens vers la liste des impacts de la perturbation ("impacts"); il est donc inutile de retravailler les paramètres d'appels côté media entre deux interrogations.
Dans ce document, toutes les sections décrivent les différents points d'entrée.

Dans chacune des APIs il est décrit les méthodes http qui sont implémentées

En général les APIs implémentent sur les méthodes GET la pagination.
On peut alors préciser le numéro de la page demandé avec le paramètre start_page, puis préciser le
nombre d'items que l'on veut par page à l'aide du paramètre items_per_page.

Certaines des urls contiennent des places holders, ils sont contenus entre ```{ }```,
il faudra remplacer, ```{}```, par une valeur.
Exemple : ```/disruptions/{disruption_id}/impacts```
Cette url n'est pas valide, il faut remplacer ```{disruption_id}``` par un id de
disruption valide.


Les différents concepts manipulés sont présentés dans la diagramme suivant:

![schema conceptuel](https://raw.githubusercontent.com/CanalTP/Chaos/master/documentation/Conceptuel.jpg?token=448185__eyJzY29wZSI6IlJhd0Jsb2I6Q2FuYWxUUC9DaGFvcy9tYXN0ZXIvZG9jdW1lbnRhdGlvbi9Db25jZXB0dWVsLmpwZyIsImV4cGlyZXMiOjE0MDYwNDA1MDN9--b3e9f38f53f9b6a80d21d45ad545144fa69f5521)


La gestion des erreurs est embryonaire, en cas d'erreur technique une réponse de type 500 est retourné sans plus d'information.
Si il est fait référence à une resources qui n'existe pas (ou plus), que ce soit dans les URL, ou dans le json de création/modfication une réponse de type 404 est retournée.
Enfin, en cas de paramétre non valide, y compris un json ne respestant pas les contraintes définies, une réponse de type 400 est retourné, celle ci contient un message textuel précisant l'erreur.

# Racine [/]
##Récupérer la liste des API [GET]

- response 200 (application/json)
    * Body

            {
                "disruptions": {"href": "https://ogv2ws.apiary-mock.com/disruptions"},
                "disruption": {"href": "https://ogv2ws.apiary-mock.com/disruptions/{id}", "templated": true},
                "severities": {"href": "https://ogv2ws.apiary-mock.com/severities"},
                "causes": {"href": "https://ogv2ws.apiary-mock.com/causes"},
                "channels": {"href": "https://ogv2ws.apiary-mock.com/channels"}
            }


# Liste des perturbations [/disruptions]

##Récupérer les disruptions [GET]
Retourne la liste de toutes les perturbations visibles.
##Paramètres

| Name                 | description                                                                               | required | default                 |
| -------------------- | ----------------------------------------------------------------------------------------- | -------- | ----------------------- |
| start_page           | Numéro de la page (commence par 1)                                                        | false    | 1                       |
| items_per_page       | Nombre d'items par page                                                                   | false    | 20                      |
| publication_status[] | Filtre sur publication_status,  les valeurs possibles sont : past, ongoing, coming        | false    | [past, ongoing, coming] |
| current_time         | Permet de changer l'heure d'appel, sert surtout pour le debug                             | false    | NOW                     |


Le paramétre ```publication_status``` permet, par rapport à l'heure de référence passée en paramètre, de retourner les perturbations en cours (c'est à dire ayant des dates/heures de publications encadrant la date/heure de référence), à venir (qui ont des dates/heures de publications postérieures à la date/heure de référence) ou passées (ayant des dates/heures de publications antérieures à la date/heure de référence).

L'attribut ```status``` des disruptions ne peut actuellement prendre qu'une seule valeurs: ```published```.

L'attribut ```publication_status``` des disruptions correspond à l'énumération ```DisruptionStatus``` du schéma ci dessus.

Le champs ```impacts``` contient un objet de pagination contenant les liens vers la liste des impacts.

##Example
- response 200 (application/json)

    * Body

            {
                "disruptions": [
                    {
                        "id": "d30502d2-e8de-11e3-8c3e-0008ca8657ea",
                        "self": {"href": "https://ogv2ws.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ea"},
                        "reference": "RER B en panne",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "note": "blablbla",
                        "status": "published",
                        "publication_status": "ongoing",
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
                                "next": {"href": "https://ogv2ws.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ea/impacts?start_page=1&item_per_page=20"},
                                "first": {"href": "https://ogv2ws.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ea/impacts?start_page=1&item_per_page=20"},
                                "last": {"href": "https://ogv2ws.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ea/impacts?start_page=1&item_per_page=20"}
                            }
                        }
                    },
                    {
                        "id": "d30502d2-e8de-11e3-8c3e-0008ca8657eb",
                        "self": {"href": "https://ogv2ws.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657eb"},
                        "reference": "RER A en panne",
                        "created_at": "2014-05-31T16:52:18Z",
                        "updated_at": null,
                        "note": null,
                        "status": "published",
                        "publication_status": "coming",
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
                                "next": {"href": "https://ogv2ws.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657eb/impacts?start_page=1&item_per_page=20"},
                                "first": {"href": "https://ogv2ws.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657eb/impacts?start_page=1&item_per_page=20"},
                                "last": {"href": "https://ogv2ws.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657eb/impacts?start_page=1&item_per_page=20"}
                            }
                        }
                    },
                    {
                        "id": "d30502d2-e8de-11e3-8c3e-0008ca8657ec",
                        "self": {"href": "https://ogv2ws.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ec"},
                        "reference": "Chatelet fermé",
                        "created_at": "2014-05-17T16:52:18Z",
                        "update_at": "2014-05-31T06:55:18Z",
                        "note": "retour probable d'ici 5H",
                        "status": "published",
                        "publication_status": "past",
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
                                "next": {"href": "https://ogv2ws.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ec/impacts?start_page=1&item_per_page=20"},
                                "first": {"href": "https://ogv2ws.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ec/impacts?start_page=1&item_per_page=20"},
                                "last": {"href": "https://ogv2ws.apiary-mock.com/disruptions/d30502d2-e8de-11e3-8c3e-0008ca8657ec/impacts?start_page=2&item_per_page=20"}
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
                        "next": {"href": "https://ogv2ws.apiary-mock.com/disruptions/?start_page=2&item_per_page=3"},
                        "first": {"href": "https://ogv2ws.apiary-mock.com/disruptions/?start_page=1&item_per_page=3"},
                        "last": {"href": "https://ogv2ws.apiary-mock.com/disruptions/?start_page=2&item_per_page=3"}
                    }
                }
            }

##Créer une perturbation [POST]

La création d'une perturbation est réalisé via une requéte ```POST``` à sur la resource ```disruptions```.
Le content-type de la requete doit etre json et le corps de celle ci doit contenir un json correspondant au format d'une perturbation.

Les champs suivant peuvent etre défini:

  - reference (obligatoire)
  - note
  - publication_period

Lors d'un succés une réponse 201 est retourné, celle ci contient la perturbation créée.

###Exemple
- Request (application/json)

    * Body

            {
                "reference": "foo",
                "note": null,
                "publication_period" : {
                    "begin": "2014-04-31T17:00:00Z",
                    "end": null
                }
            }



- response 201 (application/json)

    * Body

            {
                "disruption":{
                    "id": "3d1f32b2-e8df-11e3-8c3e-0008ca8657ea",
                    "self": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea"},
                    "reference": "foo",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null,
                    "note": null,
                    "status": "published",
                    "publication_status": "ongoing",
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
                            "first": {"href": "https://ogv2ws.apiary-mock.com/disruptions/1/impacts?start_page=1&item_per_page=20"},
                            "last": null
                        }
                    }
                },
                "meta": {}
            }

- response 400 (application/json)

    * Body

            {
                "error": {
                    "message": "'reference' is a required property"
                }
                "meta": {}
            }


# Disruptions [/disruptions/{id}]
##Récupérer une perturbation [GET]

Retourne une perturbation (si elle existe):

###Exemple
- response 200 (application/json)

    * Body

            {
                "disruption": {
                    "id": "3d1f32b2-e8df-11e3-8c3e-0008ca8657ea",
                    "self": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea"},
                    "reference": "RER B en panne",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "note": "blablbla",
                    "status": "published",
                    "publication_status": "ongoing",
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
                            "next": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts?start_page=1&item_per_page=20"},
                            "first": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts?start_page=1&item_per_page=20"},
                            "last": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts?start_page=1&item_per_page=20"}
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


##Mise à jour d'une perturbation [PUT]

La mise à jour d'une perturbation est réalisé via une requéte ```PUT``` à sur la resource ```disruptions```.
Le content-type de la requete doit etre json et le corps de celle ci doit contenir un json correspondant au format d'une perturbation.

Les champs suivant peuvent etre mis à jour:

  - reference
  - note
  - publication_period

Si un champs n'est pas présent dans le json la valeur est considéré null.

Lors d'un succés une réponse 200 est retourné, celle ci contient la perturbation modifiée.

###Exemple
- Request

    * Headers

            Content-Type: application/json

    * Body

            {
                "reference": "foo",
                "note": null,
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
                    "self": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea"},
                    "reference": "foo",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "note": null,
                    "status": "published",
                    "publication_status": "ongoing",
                    "publication_period" : {
                        "begin": "2014-04-31T17:00:00Z",
                        "end": null
                    },
                    "impacts": {
                        "pagination": {
                            "start_page": 0,
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


- response 400 (application/json)

    * Body

            {
                "error": {
                    "message": "'reference' is a required property"
                }
                "meta": {}
            }

##Effacer une perturbation [DELETE]
Cette fonction archive une perturbation, elle pourra eventuellement être restaurée par la suite.

L'archivage est réalisé via un une requete ```DELETE``` sur une pertubation.

Une réponse de type 204 est retournée en cas de succés.
###Exemple

- Response 204

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No disruption"
                },
                "meta": {}
            }


# Liste des Impacts [/disruptions/{disruption_id}/impacts]
Un impact représente une relation entre une liste d'objet TC, une sévérité, des périodes d'application et des messages (pas encore implémenté).

Seul les objet TC de type network et stop area sont actuellement géré.

##Retourne les impacts [GET]
Retourne tous les impacts d'une perturbation. Ils sont triés par la priorité de leurs sévérité.
###Paramètres

| Name                 | description                                        | required | default                 |
| -------------------- | -------------------------------------------------- | -------- | ----------------------- |
| start_page           | Numéro de la page (commence par 1)                 | false    | 1                       |
| items_per_page       | Nombre d'items par page                            | false    | 20                      |

Aucun filtre actuellement sur la récupération de liste des impacts: l'interrogation se fait seulement avec un identifiant de perturbation, afin de récupérer l'ensemble des impacts déclarés pour la perturbation demandée.

###Exemple
- response 200 (application/json)

    * Body

            {
                "impacts": [
                    {
                        "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ea",
                        "self": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8657ea"},
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "severity": {
                            "id": "3d1f42b2-e8df-11e3-8c3e-0008ca86c7ea",
                            "wording": "Bonne nouvelle",
                            "created_at": "2014-04-31T16:52:18Z",
                            "updated_at": "2014-04-31T16:55:18Z",
                            "color": "#123456",
                            "effect": null,
                            "priority": 1,
                        },
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
                            }
                        ],
                        "disruption" : {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-823e-0008ca8657ea"}
                    }
                ],
                "meta": {
                    "pagination": {
                        "start_page": 1,
                        "items_per_page": 3,
                        "total_results": 6,
                        "prev": null,
                        "next": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-823e-0008ca8657ea/impacts?start_page=2&items_per_page=3"},
                        "first": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-823e-0008ca8657ea/impacts?start_page=1&items_per_page=3"},
                        "last": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-823e-0008ca8657ea/impacts?start_page=2&items_per_page=3"}
                    }
                }
            }



##Créer un impact [POST]
Création d'un nouvel impact.

La création d'un impact est réalisé via une requéte ```POST``` à sur la resource ```impacts```.
Le content-type de la requete doit etre json et le corps de celle ci doit contenir un json correspondant au format d'un impact.


Lors d'un succés une réponse 201 est retourné, celle ci contient l'impact créé.
###Exemple

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
                "objects": [
                    {
                        "id": "network:RTP:3786125",
                        "type": "network"
                    },
                    {
                        "id": "network:RTP:378",
                        "type": "network"
                    }
                ]
            }

- response 200 (application/json)

    * Body

            {
                "impact": {
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8617ea",
                    "self": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-8c3e-0008ca8647ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8617ea"},
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "severity": {
                        "id": "3d1f42b2-e8df-11e3-8c3e-0008ca861aea",
                        "wording": "Bonne nouvelle",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "color": "#123456",
                        "effect": null,
                        "priority": 0
                    },
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
                        }
                    ],
                    "disruption" : {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-1c3e-0008ca8617ea"}
                },
                "meta": {}
            }

- response 400 (application/json)

    * Body

            {
                "error": {
                    "message": "'severity' is a required property"
                }
                "meta": {}
            }



#Impact [/disruptions/{disruption_id}/impacts/{id}]
##Retourne un impact [GET]
###Exemple

- response 200 (application/json)

    * Body

            {
                "impact": {
                    "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8617ea",
                    "self": {"href": "https://ogv2ws.apiary-mock.com/disruptions/3d1f42b2-e8df-11e3-8c3e-0008ca8647ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8617ea"},
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "severity": {
                        "id": "3d1f42b2-e8df-11e3-8c3e-0008ca861aea",
                        "wording": "Bonne nouvelle",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "color": "#123456",
                        "effect": null,
                        "priority": 1
                    },
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
                    "message": "No disruption or impact"
                },
                "meta": {}
            }

#Liste des sévérités [/severities]

Une sévérité est composé des champs suivants:

  - ```wording``` correspond au libellé qui sera affiché pour cette sévérité.
  - ```color``` correspond à la couleur, en hexadécimale, associé à cette sévérité.
  - ```priority``` correspond à l'ordre d'affichage de la sévérité, et donc des impacts qui lui sont rattachés.
  - ```effect``` correspond à l'énumération ```SeverityEffect``` et détermine l'effet dans le calculateur d'itinéraire.

##Retourne la liste de toutes les sévérités [GET]
Permet de récupérer l'ensemble des sévérités (ou conséquences) déclarées.

- response 200 (application/json)

    * Body

            {
                "severities": [
                    {
                        "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                        "self": {
                            "href": "https://ogv2ws.apiary-mock.com/severities/3d1f42b3-e8df-11e3-8c3e-0008ca8617ea"
                        }
                        "wording": "normal",
                        "effect": null,
                        "priority": 1,
                        "color": "#123456",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b4-e8df-11e3-8c3e-0008ca8617ea",
                        "self": {
                            "href": "https://ogv2ws.apiary-mock.com/severities/3d1f42b4-e8df-11e3-8c3e-0008ca8617ea"
                        }
                        "wording": "majeur",
                        "effect": null,
                        "priority": 2,
                        "color": "#123456",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b5-e8df-11e3-8c3e-0008ca8617ea",
                        "self": {
                            "href": "https://ogv2ws.apiary-mock.com/severities/3d1f42b5-e8df-11e3-8c3e-0008ca8617ea"
                        }
                        "wording": "bloquant",
                        "effect": "blocking",
                        "priority": 3,
                        "color": "#123456",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    }
                ],
                "meta": {}
            }

##Créer une sévérité [POST]


La création d'une sévérité est réalisée via une requête ```POST``` sur la resource ```severities```.
Le content-type de la requete doit etre json et le corps de celle ci doit contenir un json correspondant au format d'une sévéritié.

Les champs suivant peuvent etre défini:

  - wording (obligatoire)
  - color
  - priority
  - effect


Lors d'un succés une réponse 201 est retourné, celle ci contient la sévérité créée.

- request
    + headers

            Content-Type: application/json
    * Body

                {
                    "wording": "normal",
                    "color": "#123456",
                    "effect": null,
                    "priority": 1
                }

- response 200 (application/json)

    * Body

            {
                "severity": {
                    "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                    "self": {
                        "href": "https://ogv2ws.apiary-mock.com/severities/3d1f42b3-e8df-11e3-8c3e-0008ca8617ea"
                    }
                    "wording": "normal",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null,
                    "color": "#123456",
                    "priority": 1,
                    "effect": null
                },
                "meta": {}
            }

- response 400 (application/json)

    * Body

            {
                "error": {
                    "message": "'wording' is a required property"
                }
                "meta": {}
            }


# Severities [/severities/{id}]
##Retourne une sévérité [GET]

##Exemple

Retourne une sévérité existante.

- response 200 (application/json)

    * Body

            {
                "severity": {
                    "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                    "self": {
                        "href": "https://ogv2ws.apiary-mock.com/severities/3d1f42b3-e8df-11e3-8c3e-0008ca8617ea"
                    }
                    "wording": "normal",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null,
                    "color": "#123456",
                    "effect": null,
                    "priority": 1
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

##Mise à jour d'une sévérité [PUT]
La mise à jour d'une sévérité est réalisé via une requéte ```PUT``` sur la resource ```severities```.
Le content-type de la requete doit etre json et le corps de celle ci doit contenir un json correspondant au format d'une sévérité.

Les contraintes sont les meme que pour la création.

Lors d'un succés une réponse 200 est retourné, celle ci contient la sévérité modifiée.

###Exemple

- Request

    * Headers

            Content-Type: application/json

    * Body

            {
                "wording": "Bonne nouvelle",
                "color": "#123456",
                "effect": null,
                "priority": 1
            }


- Response 200 (application/json)

    * Body

            {
                "severity": {
                    "id": "3d1f42b3-e8df-11e3-8c3e-0008ca8617ea",
                    "self": {
                        "href": "https://ogv2ws.apiary-mock.com/severities/3d1f42b3-e8df-11e3-8c3e-0008ca8617ea"
                    }
                    "wording": "Bonne nouvelle",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z",
                    "color": "#123456",
                    "effect": null,
                    "priority": 1
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


- response 400 (application/json)

    * Body

            {
                "error": {
                    "message": "'wording' is a required property"
                }
                "meta": {}
            }

##supprimer une sévérité [DELETE]
supprime une sévérité.
###Exemple


- Response 204

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No severity"
                },
                "meta": {}
            }

#Liste des causes [/causes]

##Retourne la liste de toutes les causes [GET]

- response 200 (application/json)

    * Body

            {
                "causes": [
                    {
                        "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                        "self": {
                            "href": "https://ogv2ws.apiary-mock.com/causes/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
                        }
                        "wording": "météo",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b2-e8df-11e5-8c3e-0008ca8617ea",
                        "self": {
                            "href": "https://ogv2ws.apiary-mock.com/causes/3d1f42b2-e8df-11e5-8c3e-0008ca8617ea"
                        }
                        "wording": "gréve",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b2-e8df-11e6-8c3e-0008ca8617ea",
                        "self": {
                            "href": "https://ogv2ws.apiary-mock.com/causes/3d1f42b2-e8df-11e6-8c3e-0008ca8617ea"
                        }
                        "wording": "accident voyageur",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    }
                ],
                "meta": {}
            }

##Créer une cause [POST]

La création d'une cause est réalisée via une requête ```POST``` sur la resource ```cause```.
Le content-type de la requete doit etre json et le corps de celle ci doit contenir un json correspondant au format d'une cause.

Les champs suivant peuvent etre défini:

  - wording (obligatoire)

Le champs ```wording``` correspond au libellé qui sera affiché pour cette cause.

Lors d'un succés une réponse 201 est retourné, celle ci contient la cause créée.

###Exemple
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
                    "self": {
                        "href": "https://ogv2ws.apiary-mock.com/causes/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
                    }
                    "wording": "météo",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": null
                },
                "meta": {}
            }

- response 400 (application/json)

    * Body

            {
                "error": {
                    "message": "'wording' is a required property"
                }
                "meta": {}
            }

# Causes [/causes/{id}]
##Retourne une cause. [GET]

##Paramètres

Retourne une cause existante.

- response 200 (application/json)

    * Body

            {
                "cause": {
                    "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                    "self": {
                        "href": "https://ogv2ws.apiary-mock.com/causes/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
                    }
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

##Mise à jour d'une cause [PUT]
La mise à jour d'une cause est réalisé via une requéte ```PUT``` sur la resource ```causes```.
Le content-type de la requete doit etre json et le corps de celle ci doit contenir un json correspondant au format d'une cause.

Les contraintes sont les meme que pour la création.

Lors d'un succés une réponse 200 est retourné, celle ci contient la cause modifiée.
###Exemple


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
                    "self": {
                        "href": "https://ogv2ws.apiary-mock.com/causes/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
                    }
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

- response 400 (application/json)
    * Body

            {
                "error": {
                    "message": "'wording' is a required property"
                }
                "meta": {}
            }

##Archive une cause [DELETE]
Archive une cause.
###Paramètres


- Response 204

- response 404 (application/json)
    * Body

            {
                "error": {
                    "message": "No cause"
                },
                "meta": {}
            }

#Liste des canaux de diffusions [/channels]

##Retourne la liste de tous les canaux de diffusion [GET]

- response 200 (application/json)

    * Body

            {
                "channels": [
                    {
                        "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                        "self": {
                            "href": "https://ogv2ws.apiary-mock.com/channels/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
                        }
                        "name": "court",
                        "max_size": 140,
                        "content_type": "text/plain",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1a42b7-e8df-11e4-8c3e-0008ca8617ea",
                        "self": {
                            "href": "https://ogv2ws.apiary-mock.com/channels/3d1f42b7-e8df-11e4-8c3e-0008ca8617ea"
                        }
                        "name": "long",
                        "max_size": 512,
                        "content_type": "text/plain",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    },
                    {
                        "id": "3d1f42b2-e8df-11e4-8c3e-0008ca8617ea",
                        "self": {
                            "href": "https://ogv2ws.apiary-mock.com/channels/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
                        }
                        "name": "long riche",
                        "max_size": null,
                        "content_type": "text/markdown",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z"
                    }
                ],
                "meta": {}
            }

##Créer un canal [POST]
La création d'un canal est réalisée via une requête ```POST``` sur la resource ```channel```.
Le content-type de la requete doit etre json et le corps de celle ci doit contenir un json correspondant au format d'un canal.

Les champs suivant peuvent etre défini:

  - name (obligatoire)
  - max_size (obligatoire mais peut etre null pour signifier qu'il n'y a pas de taille max)
  - content_type (obligatoire)

Lors d'un succés une réponse 201 est retourné, celle ci contient la canal créé.

###Exemple

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
                    "self": {
                        "href": "https://ogv2ws.apiary-mock.com/channels/3d1f42b2-e8df-11e4-8c3e-0008ca8617ea"
                    }
                    "name": "court",
                    "max_size": 140,
                    "content_type": "text/plain",
                    "created_at": "2014-04-31T16:52:18Z",
                    "updated_at": "2014-04-31T16:55:18Z"
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
